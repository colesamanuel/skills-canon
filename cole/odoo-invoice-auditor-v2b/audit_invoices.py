#!/usr/bin/env python3
"""
audit_invoices.py — Auditor de facturas Odoo multi-empresa (Colé / Kermatec) v2b.

VARIANTE "KEY EMBEBIDA" — DECISIÓN CONSCIENTE DEL USUARIO
=========================================================
La API key de Odoo está hardcodeada en la constante API_KEY (abajo).
El Ing. Manuel Rubio solicitó explícitamente esta variante el 2026-04-23,
sobreescribiendo la recomendación de seguridad del asistente, a cambio
de cero fricción operativa.

IMPLICACIONES:
- NO subir este archivo a repositorios públicos.
- NO compartir con terceros sin remover la key primero.
- Rotar la key periódicamente y tras cualquier sospecha de filtración.
- Backups del directorio deben estar en destinos cifrados.

Para rotar: editar API_KEY abajo, revocar la anterior en Odoo.
Para override temporal sin editar: exportar ODOO_API_KEY o usar --api-key.

Precedencia: --api-key CLI > $ODOO_API_KEY env > constante API_KEY embebida.

Uso típico:
    python3 audit_invoices.py --company-id 2                    # Kermatec
    python3 audit_invoices.py --company-id 1                    # Colé
    python3 audit_invoices.py --company-id 2 \\
        --date-from 2026-01-01 --date-to 2026-04-23 \\
        --output ~/kermatek_audit.xlsx

Niveles: AB (default), ABC, ABCD, ABCDE. C/D/E son stubs.
"""

import argparse
import json
import os
import sys
import urllib.request
from collections import defaultdict
from datetime import date, datetime
from typing import Any

import pandas as pd


# ============================================================
# API KEY EMBEBIDA — ROTAR AQUÍ SI ES NECESARIO
# ============================================================
API_KEY = "c05ae3a29733ef6f21933c7a4c7d1b5ed091a2b4"


# ============================================================
# Configuración por defecto (tenant Manuel Rubio)
# ============================================================
DEFAULT_URL = "https://colesamarco2020-colesa.odoo.com"
DEFAULT_DB = "colesamarco2020-colesa-colesa-27146045"
DEFAULT_UID = 7

COMPANY_NAMES = {
    1: "Colé S.A.",
    2: "Kermatec Dosimetric S.A.",
}

# Catálogo de hallazgos (sincronizado con references/hallazgos-catalogo.md)
HALLAZGO_SEVERIDAD = {
    "H0": "🟢",  "H1": "🟡",  "H2": "🟡",  "H3": "🔴",
    "H4": "🟠",  "H5": "🟡",  "H6": "🟡",  "H7": "🔴",
    "H8": "🟠",  "H9": "🟠",  "H10": "🟡", "H11": "🔴",
    "H12": "🟠", "H13": "🟡", "H14": "🟡", "H15": "🟠",
}


# ============================================================
# Resolución de API key (precedencia: CLI > env > constante embebida)
# ============================================================
def resolve_api_key(cli_key: str | None) -> str:
    """
    Precedencia explícita:
        1. --api-key CLI argument
        2. $ODOO_API_KEY variable de entorno
        3. Constante API_KEY embebida en este archivo
    """
    if cli_key:
        return cli_key
    env_key = os.environ.get("ODOO_API_KEY")
    if env_key:
        return env_key
    if not API_KEY or API_KEY.startswith("REPLACE_"):
        sys.exit(
            "ERROR: constante API_KEY vacía o placeholder en audit_invoices.py. "
            "Editar el archivo o pasar --api-key / exportar ODOO_API_KEY."
        )
    return API_KEY


# ============================================================
# JSON-RPC helper
# ============================================================
def rpc_call(url: str, db: str, uid: int, api_key: str,
             model: str, method: str, args: list, kwargs: dict | None = None) -> Any:
    """Ejecuta una llamada JSON-RPC a Odoo. Retorna el campo result o lanza excepción."""
    kwargs = kwargs or {}
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [db, uid, api_key, model, method, args, kwargs],
        },
    }
    req = urllib.request.Request(
        f"{url}/jsonrpc",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (OdooInvoiceAuditor/2b)",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if "error" in data:
        raise RuntimeError(f"Odoo RPC error: {json.dumps(data['error'], indent=2)}")
    return data["result"]


# ============================================================
# Descubrimiento
# ============================================================
def discover_companies(url, db, uid, api_key):
    return rpc_call(url, db, uid, api_key, "res.company", "search_read",
                    [[]], {"fields": ["id", "name", "currency_id", "vat", "country_id"]})


# ============================================================
# Carga de facturas
# ============================================================
def fetch_invoices(url, db, uid, api_key, company_id, date_from=None, date_to=None):
    domain = [
        ["company_id", "=", company_id],
        ["move_type", "in", ["out_invoice", "out_refund"]],
    ]
    if date_from:
        domain.append(["invoice_date", ">=", date_from])
    if date_to:
        domain.append(["invoice_date", "<=", date_to])

    fields = [
        "id", "name", "invoice_date", "invoice_date_due",
        "partner_id", "move_type", "state", "payment_state",
        "currency_id", "amount_untaxed", "amount_tax", "amount_total",
        "amount_residual", "ref", "invoice_origin",
    ]
    return rpc_call(url, db, uid, api_key, "account.move", "search_read",
                    [domain], {"fields": fields, "order": "invoice_date desc"})


# ============================================================
# Normalización
# ============================================================
def to_dataframe(invoices, today: date) -> pd.DataFrame:
    rows = []
    for inv in invoices:
        partner = inv.get("partner_id")
        currency = inv.get("currency_id")
        inv_date = inv.get("invoice_date") or None
        due_date = inv.get("invoice_date_due") or None

        dias_atraso = None
        if (inv_date and due_date
                and inv["state"] == "posted"
                and inv["payment_state"] in ("not_paid", "partial")):
            try:
                due = datetime.strptime(due_date, "%Y-%m-%d").date()
                dias_atraso = max(0, (today - due).days) if today > due else 0
            except ValueError:
                dias_atraso = None

        rows.append({
            "ID": inv["id"],
            "Número": inv.get("name") or "(sin número)",
            "Tipo": "Factura" if inv["move_type"] == "out_invoice" else "Nota Crédito",
            "Fecha emisión": inv_date,
            "Fecha vencimiento": due_date,
            "Cliente": partner[1] if partner else "(sin cliente)",
            "Partner ID": partner[0] if partner else None,
            "Estado": inv["state"],
            "Estado pago": inv.get("payment_state") or "n/a",
            "Moneda": currency[1] if currency else "n/a",
            "Subtotal": inv.get("amount_untaxed", 0.0),
            "Impuesto": inv.get("amount_tax", 0.0),
            "Total": inv.get("amount_total", 0.0),
            "Saldo pendiente": inv.get("amount_residual", 0.0),
            "Días atraso": dias_atraso,
            "Origen (SO)": inv.get("invoice_origin") or "",
            "Ref externa": inv.get("ref") or "",
        })
    return pd.DataFrame(rows)


# ============================================================
# Aging
# ============================================================
def bucket_aging(dias: float | None) -> str:
    if dias is None:
        return "Sin fecha vto"
    if dias <= 0:
        return "00. Vigente"
    if dias <= 30:
        return "01. 1-30 días"
    if dias <= 60:
        return "02. 31-60 días"
    if dias <= 90:
        return "03. 61-90 días"
    if dias <= 180:
        return "04. 91-180 días"
    return "05. >180 días"


# ============================================================
# Detectores de hallazgos
# ============================================================
def detectar_hallazgos(df: pd.DataFrame, today: date) -> list[dict]:
    detectados = []

    # H1 — Sin fecha emisión
    m = df["Fecha emisión"].isna()
    if m.any():
        detectados.append({
            "codigo": "H1",
            "descripcion": "Facturas sin fecha de emisión",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H2 — Número placeholder
    m = df["Número"].isin(["(sin número)", "/", ""]) | df["Número"].str.startswith("/", na=False)
    m = m & (df["Estado"] != "cancel")
    if m.any():
        detectados.append({
            "codigo": "H2",
            "descripcion": "Documentos no cancelados con número placeholder o vacío",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H3 — Aritmética inconsistente
    df_chk = df.copy()
    df_chk["Delta"] = (df_chk["Subtotal"] + df_chk["Impuesto"] - df_chk["Total"]).abs()
    m = df_chk["Delta"] > 0.01
    if m.any():
        detectados.append({
            "codigo": "H3",
            "descripcion": "Subtotal + impuesto ≠ total (tolerancia 0.01)",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H4 — IVA=0 en facturas posted
    m = (df["Estado"] == "posted") & (df["Tipo"] == "Factura") & (df["Impuesto"] == 0)
    if m.any():
        total_fact = ((df["Estado"] == "posted") & (df["Tipo"] == "Factura")).sum()
        pct = 100 * m.sum() / total_fact if total_fact else 0
        detectados.append({
            "codigo": "H4",
            "descripcion": f"Facturas posted con impuesto=0 ({pct:.0f}% del total posted) — validar exención fiscal",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H5 — Borradores olvidados
    m = df["Estado"] == "draft"
    if m.any():
        detectados.append({
            "codigo": "H5",
            "descripcion": "Borradores pendientes de postear o descartar",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H6 — Canceladas con número asignado
    m = (df["Estado"] == "cancel") & (~df["Número"].isin(["(sin número)", "/", ""])) & (~df["Número"].str.startswith("/", na=False))
    if m.any():
        detectados.append({
            "codigo": "H6",
            "descripcion": "Facturas canceladas con número asignado — revisar continuidad de consecutivo",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H7 — in_payment sin conciliar
    m = (df["Estado"] == "posted") & (df["Estado pago"] == "in_payment") & (df["Saldo pendiente"] > 0)
    if m.any():
        detectados.append({
            "codigo": "H7",
            "descripcion": "Facturas en in_payment con residual > 0 — conciliación bancaria pendiente",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H8 — Partner duplicado
    def normalizar(nombre):
        if not isinstance(nombre, str):
            return ""
        return (nombre.upper()
                .replace(".", "").replace(",", "").replace("  ", " ")
                .replace("SOCIEDAD ANONIMA", "SA").replace("S.A.", "SA")
                .replace("SOCIEDAD DE RESPONSABILIDAD LIMITADA", "SRL")
                .strip())
    df_p = df[["Cliente", "Partner ID"]].drop_duplicates()
    df_p["Norm"] = df_p["Cliente"].apply(normalizar)
    dup_groups = df_p.groupby("Norm").filter(lambda g: g["Partner ID"].nunique() > 1)
    if not dup_groups.empty:
        grupos = dup_groups.groupby("Norm")["Partner ID"].nunique()
        detectados.append({
            "codigo": "H8",
            "descripcion": f"Clientes con múltiples partner_id (probable duplicado): {len(grupos)} grupo(s)",
            "casos": int(len(dup_groups)),
            "ids": dup_groups["Partner ID"].tolist(),
            "detalle": dup_groups.to_dict("records"),
        })

    # H9 — Saldo > total
    m = df["Saldo pendiente"] > df["Total"] + 0.01
    if m.any():
        detectados.append({
            "codigo": "H9",
            "descripcion": "Saldo pendiente supera total facturado — anomalía contable",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H10 — Posted sin referencia a SO
    m = (df["Estado"] == "posted") & (df["Tipo"] == "Factura") & (df["Origen (SO)"] == "")
    if m.any():
        detectados.append({
            "codigo": "H10",
            "descripcion": "Facturas posted sin referencia a sale.order (trazabilidad comercial ausente)",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H11 — Vencimiento anterior a emisión
    def check_vto(row):
        try:
            if row["Fecha emisión"] and row["Fecha vencimiento"]:
                e = datetime.strptime(row["Fecha emisión"], "%Y-%m-%d").date()
                v = datetime.strptime(row["Fecha vencimiento"], "%Y-%m-%d").date()
                return v < e
        except (ValueError, TypeError):
            pass
        return False
    m = df.apply(check_vto, axis=1)
    if m.any():
        detectados.append({
            "codigo": "H11",
            "descripcion": "Fecha de vencimiento anterior a fecha de emisión",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H12 — Aging profundo (>90 días)
    cxc = df[(df["Estado"] == "posted") & (df["Tipo"] == "Factura")
             & (df["Estado pago"].isin(["not_paid", "partial"]))
             & (df["Días atraso"] > 90)]
    if not cxc.empty:
        detectados.append({
            "codigo": "H12",
            "descripcion": f"Clientes con facturas >90 días de atraso: {cxc['Cliente'].nunique()} cliente(s)",
            "casos": int(len(cxc)),
            "ids": cxc["ID"].tolist(),
        })

    # H13 — Moneda fuera de CRC/USD
    m = ~df["Moneda"].isin(["CRC", "USD", "n/a"])
    if m.any():
        detectados.append({
            "codigo": "H13",
            "descripcion": f"Facturas en moneda distinta a CRC/USD: {df.loc[m, 'Moneda'].unique().tolist()}",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H14 — Fecha emisión futura
    def check_futuro(row):
        try:
            if row["Fecha emisión"]:
                e = datetime.strptime(row["Fecha emisión"], "%Y-%m-%d").date()
                return e > today
        except (ValueError, TypeError):
            pass
        return False
    m = df.apply(check_futuro, axis=1)
    if m.any():
        detectados.append({
            "codigo": "H14",
            "descripcion": "Facturas con fecha de emisión futura",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    # H15 — Total ≤ 1
    m = (df["Estado"] == "posted") & (df["Tipo"] == "Factura") & (df["Total"] <= 1) & (df["Total"] > 0)
    if m.any():
        detectados.append({
            "codigo": "H15",
            "descripcion": "Facturas posted con total ≤ 1 (posible error de captura)",
            "casos": int(m.sum()),
            "ids": df.loc[m, "ID"].tolist(),
        })

    return detectados


# ============================================================
# Morosos
# ============================================================
def generar_morosos(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    morosos = df[
        (df["Estado"] == "posted")
        & (df["Tipo"] == "Factura")
        & (df["Estado pago"].isin(["not_paid", "partial"]))
        & (df["Días atraso"].notna())
        & (df["Días atraso"] > 0)
    ].copy()

    if morosos.empty:
        return pd.DataFrame(), pd.DataFrame()

    consolidado = (
        morosos.groupby(["Cliente", "Moneda"])
        .agg(
            Facturas_morosas=("ID", "count"),
            Saldo_total_adeudado=("Saldo pendiente", "sum"),
            Dias_atraso_max=("Días atraso", "max"),
            Dias_atraso_min=("Días atraso", "min"),
            Factura_mas_antigua=("Fecha emisión", "min"),
        )
        .reset_index()
        .sort_values("Saldo_total_adeudado", ascending=False)
    )

    detalle = (
        morosos[[
            "Cliente", "Moneda", "Número", "Fecha emisión", "Fecha vencimiento",
            "Días atraso", "Total", "Saldo pendiente", "Estado pago", "ID",
        ]]
        .sort_values(["Cliente", "Moneda", "Días atraso"], ascending=[True, True, False])
        .reset_index(drop=True)
    )

    return consolidado, detalle


def imprimir_morosos(consolidado: pd.DataFrame, detalle: pd.DataFrame):
    print(f"\n--- Morosos (facturas vencidas y no pagadas) ---")
    if consolidado.empty:
        print("Sin morosos. Toda la CxC vencida está al día o no hay facturas vencidas.")
        return

    print(f"Total clientes morosos: {consolidado['Cliente'].nunique()}")
    print(f"Total facturas vencidas: {len(detalle)}")

    print(f"\nDeuda total por moneda:")
    for moneda, grupo in consolidado.groupby("Moneda"):
        print(f"  {moneda}: {grupo['Saldo_total_adeudado'].sum():,.2f} "
              f"en {grupo['Facturas_morosas'].sum()} facturas "
              f"de {len(grupo)} cliente(s)")

    print(f"\nTop 10 morosos (consolidado por cliente + moneda):")
    top = consolidado.head(10)
    for _, r in top.iterrows():
        print(f"  [{r['Moneda']}] {r['Saldo_total_adeudado']:>10,.2f}  "
              f"({r['Facturas_morosas']} fact, máx {r['Dias_atraso_max']:.0f}d)  "
              f"{r['Cliente']}")


# ============================================================
# Reporte
# ============================================================
def imprimir_resumen(df: pd.DataFrame, hallazgos: list, company_id: int, today: date):
    sep = "=" * 70
    print(sep)
    print(f"AUDITORÍA — {COMPANY_NAMES.get(company_id, f'company_id={company_id}')} ({today})")
    print(sep)
    print(f"\nTotal documentos: {len(df)}")
    print(f"\nPor estado:\n{df['Estado'].value_counts().to_string()}")
    print(f"\nPor estado de pago (solo posted):")
    print(df[df['Estado']=='posted']['Estado pago'].value_counts().to_string())

    posted_inv = df[(df['Estado']=='posted') & (df['Tipo']=='Factura')]
    print(f"\nFacturación posted por moneda:")
    for moneda, grupo in posted_inv.groupby("Moneda"):
        print(f"  {moneda}: {len(grupo)} facturas  |  "
              f"Total: {grupo['Total'].sum():,.2f}  |  "
              f"Saldo pendiente: {grupo['Saldo pendiente'].sum():,.2f}")

    cxc = df[(df["Estado"]=="posted") & (df["Tipo"]=="Factura")
             & (df["Estado pago"].isin(["not_paid","partial"]))].copy()
    cxc["Bucket"] = cxc["Días atraso"].apply(bucket_aging)

    print(f"\n--- Aging CxC (posted no pagadas) ---")
    print(f"Total CxC: {len(cxc)} facturas")
    for moneda, grupo in cxc.groupby("Moneda"):
        print(f"\n  {moneda}:")
        ag = grupo.groupby("Bucket").agg(
            Facturas=("ID", "count"),
            Saldo=("Saldo pendiente", "sum"),
        ).sort_index()
        print(ag.to_string())

    consolidado_mor, detalle_mor = generar_morosos(df)
    imprimir_morosos(consolidado_mor, detalle_mor)

    print(f"\n--- Hallazgos detectados ---")
    for h in sorted(hallazgos, key=lambda x: HALLAZGO_SEVERIDAD.get(x["codigo"], "🟢")):
        sev = HALLAZGO_SEVERIDAD.get(h["codigo"], "🟢")
        print(f"  {sev} {h['codigo']} — {h['descripcion']} ({h['casos']} caso(s))")


def exportar_xlsx(df: pd.DataFrame, hallazgos: list, output_path: str, today: date):
    cxc = df[(df["Estado"]=="posted") & (df["Tipo"]=="Factura")
             & (df["Estado pago"].isin(["not_paid","partial"]))].copy()
    cxc["Bucket"] = cxc["Días atraso"].apply(bucket_aging)

    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.drop(columns=["Partner ID"]).to_excel(writer, sheet_name="Inventario completo", index=False)
        cxc.drop(columns=["Partner ID"]).sort_values(["Bucket","Saldo pendiente"], ascending=[True,False])\
           .to_excel(writer, sheet_name="CxC Aging", index=False)

        aging_resumen = cxc.groupby("Bucket").agg(
            Facturas=("ID","count"),
            Saldo=("Saldo pendiente","sum"),
        ).reset_index()
        aging_resumen.to_excel(writer, sheet_name="Aging resumen", index=False)

        top = cxc.groupby("Cliente").agg(
            Facturas=("ID","count"),
            Saldo_total=("Saldo pendiente","sum"),
            Max_atraso=("Días atraso","max"),
        ).sort_values("Saldo_total", ascending=False).reset_index()
        top.to_excel(writer, sheet_name="Top clientes CxC", index=False)

        consolidado_mor, detalle_mor = generar_morosos(df)
        if not consolidado_mor.empty:
            consolidado_mor.to_excel(writer, sheet_name="Morosos consolidado", index=False)
            detalle_mor.to_excel(writer, sheet_name="Morosos detalle", index=False)

        filas_h = []
        for h in hallazgos:
            sev = HALLAZGO_SEVERIDAD.get(h["codigo"], "🟢")
            for _id in h.get("ids", []):
                row = df[df["ID"]==_id]
                if not row.empty:
                    r = row.iloc[0]
                    filas_h.append({
                        "Severidad": sev,
                        "Hallazgo": h["codigo"],
                        "Descripción": h["descripcion"],
                        "ID": _id,
                        "Número": r["Número"],
                        "Cliente": r["Cliente"],
                        "Estado": r["Estado"],
                        "Total": r["Total"],
                        "Saldo": r["Saldo pendiente"],
                    })
        if filas_h:
            pd.DataFrame(filas_h).to_excel(writer, sheet_name="Hallazgos detalle", index=False)

    print(f"\nXLSX generado: {output_path}")


# ============================================================
# Main
# ============================================================
def main():
    parser = argparse.ArgumentParser(
        description="Auditor de facturas Odoo multi-empresa v2b (API key embebida)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Precedencia de API key: --api-key > $ODOO_API_KEY > constante API_KEY embebida.\n"
            "Para rotar la key: editar API_KEY en este archivo y revocar la anterior en Odoo."
        ),
    )
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--uid", type=int, default=DEFAULT_UID)
    parser.add_argument(
        "--api-key",
        default=None,
        help="API key de Odoo. Si se omite, usa $ODOO_API_KEY o la constante embebida.",
    )
    parser.add_argument("--company-id", type=int, required=True,
                        help="1=Colé, 2=Kermatec. Usar --company-id 0 para ambas en corridas separadas.")
    parser.add_argument("--date-from", default=None, help="YYYY-MM-DD, opcional")
    parser.add_argument("--date-to", default=None, help="YYYY-MM-DD, opcional")
    parser.add_argument("--level", default="AB", choices=["AB", "ABC", "ABCD", "ABCDE"],
                        help="Nivel de auditoría. AB=inventario+aging (default).")
    parser.add_argument("--output", default="/mnt/user-data/outputs/odoo_audit.xlsx")
    parser.add_argument("--today", default=None, help="Override fecha de hoy (YYYY-MM-DD) para testing")
    args = parser.parse_args()

    api_key = resolve_api_key(args.api_key)

    today = (datetime.strptime(args.today, "%Y-%m-%d").date()
             if args.today else date.today())

    print("Descubriendo compañías del tenant...")
    companies = discover_companies(args.url, args.db, args.uid, api_key)
    print("\nCompañías disponibles:")
    for c in companies:
        print(f"  id={c['id']:>3} | VAT={c['vat']:>15} | {c['name']}")

    if not any(c["id"] == args.company_id for c in companies):
        print(f"\nERROR: company_id={args.company_id} no existe en el tenant.", file=sys.stderr)
        sys.exit(2)

    print(f"\nDescargando facturas company_id={args.company_id}...")
    invoices = fetch_invoices(args.url, args.db, args.uid, api_key,
                              args.company_id, args.date_from, args.date_to)
    print(f"  {len(invoices)} documentos recuperados")

    df = to_dataframe(invoices, today)
    hallazgos = detectar_hallazgos(df, today)

    imprimir_resumen(df, hallazgos, args.company_id, today)
    exportar_xlsx(df, hallazgos, args.output, today)

    if args.level != "AB":
        print(f"\n[INFO] Niveles {args.level[2:]} solicitados pero no implementados todavía.")
        print("Ver references/fiscal-cr.md para roadmap del nivel C.")


if __name__ == "__main__":
    main()
