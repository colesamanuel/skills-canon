---
name: card-reconciler
description: >
  Reconciliación 4 vías Colé S.A.: cruza facturas Odoo (JSON-RPC), cuentas bancarias
  Promerica CRC/USD y BNCR CRC/USD, tarjeta Black por tarjetahabiente (Marco *9582,
  Manuel *6931, Zulkary *2225), y hojas contables internas. Categoriza gastos negocio
  vs personal, genera CxC aging, detecta discrepancias y produce XLSX con semáforo.
  Activar con: reconciliación, conciliación, tarjetas, quincena, estado de cuenta,
  gastos tarjeta, cruzar, verificar gastos, Promerica, BNCR, cierre quincenal, banco
  vs Cole, facturas Odoo, CxC, aging, flujo de caja, reconciliación bancaria, o
  cualquier análisis financiero de Colé S.A. Activar incluso si la solicitud parece simple.
---

# Reconciliador Financiero 4 Vías — Colé S.A.

**v1.7 (2026-06-12)** — Fórmulas de la hoja 15na descifradas y verificadas:
- 🔴 **Reglas de Negocio 4-5 CORREGIDAS**. La fórmula real (verificada celda por celda
  contra el libro maestro, quincena 15-05-2026 y 108/158 quincenas con verificación
  completa) es:
  `Bruto = Σ facturas` · `45% = 0.45 × Bruto` ·
  `Salario Marco = 45%·Bruto − Total(columna 45% de gastos)` ·
  `Transferir = NETO = Salario Marco + extras (Cholo/Rosie/Agencia)`.
  La versión anterior ("Neto = bruto − 45%") era una aproximación incorrecta.
- **Fuente 4 identificada**: las hojas Colé viven en el libro maestro
  `Pendientes desde Nov 2019.xlsx` (carpeta Hojas contables Cole) — 161 pestañas, una
  por quincena desde 15_11_19 (158 con fecha + 3 auxiliares). Layout 2026:
  A=Proyecto B=USD C=CRC D=45%USD E=45%CRC con fila Total; bloque facturas
  G=Factura H=USD I=CRC; resumen Bruto/0.45/NETO/Salario Marco/Transferir en col G;
  extras a transferir bajo Transferir. Layout legado 2019: facturas con USD a la
  IZQUIERDA del nombre (F=USD G=Factura H=CRC) y porcentaje 35%.
  Las PNG de la carpeta son capturas de este libro: usar SIEMPRE el .xlsx, nunca OCR.
- El Reconciliador HTML v1.1 parsea el libro completo con selector de quincena,
  verificación automática de fórmulas por hoja y Concil Marco por quincena.

**v1.6 (2026-06-12)** — Formato 2026, reparación de archivo y validación de integridad:
- 🔴 **REPARACIÓN**: el SKILL.md v1.5 distribuido estaba **truncado** a mitad de la Regla
  de Negocio 12 ("COBRO POR TERMINAL") y **no incluía** la carpeta `references/`
  obligatoria. Las reglas 12+ se reconstruyeron (12 con evidencia bancaria; ver marca
  [RECONSTRUIDA]) y los references se regeneraron desde el propio SKILL.md y los datos
  reales. El titular debe revisar y completar lo marcado como parcial.
- **Formato 2026 de exports Promerica** (validado contra 9 archivos dic-2025→may-2026):
  - Cuentas: header `Fecha | Documento | Descripción | Débitos | Créditos | Saldo`
    (sustituye Concepto/Lugar/Monto). Ver §2a-2026.
  - BMC: header `Fecha | Número de Tarjeta | Descripción | Débitos | Créditos | Moneda`
    con tarjetahabiente POR FILA y monedas mezcladas (sustituye bloques por tarjeta).
    Ver §2b-2026. Los parsers v1.2 NO procesan este formato.
- **Validación de integridad obligatoria** por estado de cuenta:
  `saldo_inicial + Σcréditos − Σdébitos = saldo_final` y Σ calculadas vs filas
  "Total de Débitos/Créditos" del archivo (tolerancia 0.02). En 6/6 cuentas reales cuadró
  exacto; si no cuadra, el parseo perdió filas — DETENER y revisar antes de cruzar.
- **Cruce pagos TEF↔BMC — regla empírica**: los montos NO coinciden 1:1
  (abr-may 2026: TEF ₡4,000,000 del 04/05 vs abono BMC ₡3,970,852.42 del mismo día).
  Emparejar por proximidad de fecha (≤3 días, misma moneda, menor Δ) y REPORTAR el Δ
  como discrepancia. Abonos BMC sin TEF Promerica correspondiente suelen estar fondeados
  desde BNCR u otra cuenta no incluida en el set — señalarlo, no marcarlo como error.
- **Herramienta local complementaria**: `Reconciliador Cole 15na.html` (carpeta
  *Auditoria Contable Card Reconcilier*) — app HTML 100% local con estos mismos parsers
  (suite de tests node contra los 11 archivos reales), categorización con histórico
  Money Manager, Concil Marco, calculadora 45% y export XLSX. Money Manager CSV se usa
  SOLO como histórico de categorías, no como vía de cruce (decisión del titular 2026-06-12).

**v1.5 (2026-05-19)** — Hoja Conciliación Marco:
- Nueva hoja obligatoria **"Concil Marco"** en el XLSX técnico (posición 2, después de
  "Cruce 4 vias"). Cruza el gasto real de Marco *9582 en BMC contra las líneas de la
  hoja Cole atribuibles a Marco, identifica el Δ no reportado y agrupa hallazgos por
  categoría.
- Razón: Marco *9582 = todo negocio por regla global, pero la hoja Cole solo registra
  un subset de sus gastos (Aerocasillas, Aero Marco, K&S, ODOO, Klarity ajuste, IA).
  Sin vista dedicada, gastos materiales como Klarity Medical compra completa
  ($7,502.93 en Q1 ene 2026) quedan invisibles en el cruce general.
- Estructura: 6 bloques — (1) BMC Marco detallado, (2) Hoja Cole atribuible a Marco,
  (3) Análisis Δ USD agregado, (4) Detalle Δ línea por línea por categoría, (5) Marco
  CRC BMC vs Hoja, (6) Conclusión accionable con recomendación de cierre.
- Algoritmo de atribución hoja Cole → Marco: matchear concepto contra
  `['marco','aero','k&s','odoo','klarity','chat gpt','cholo','rosie','jiras']`.
- Total hojas XLSX técnico sin Odoo: 10 (era 9). Con Odoo: 13.

**v1.4 (2026-05-19)** — Odoo opt-in:
- Paso 1 (Odoo JSON-RPC) y Paso 5a (cruce facturas↔banco) y Paso 6 (CxC aging) marcados
  como **opt-in explícito**. NO ejecutar a menos que el usuario lo pida con palabras
  como "incluye Odoo", "trae las facturas", "cruzá con CxC", "aging clientes",
  "morosos", "facturación". Por defecto la reconciliación es banco + tarjeta + hoja
  Cole sin facturación.
- Razón: muchas reconciliaciones son de alcance personal/operativo y no requieren
  contexto de facturación; jalar Odoo agrega ruido y consume tiempo innecesariamente.
- Entregables: sin facturación, omitir hojas "Cruce Odoo↔Banco↔Colé", "CxC Aging" y
  "CxC Top Deudores". El XLSX técnico queda con 10 hojas en vez de 13 (incluye 'Concil Marco' — siempre).

**v1.3 (2026-05-19)** — Adaptación claude.ai:
- Memorias `hoja_cole_tipos_renglon.md` y `clientes_cole_aliases.md` embebidas en
  `references/`. Leerlas SIEMPRE antes de interpretar la hoja Cole o hacer match
  cliente banco↔Odoo.
- Paso 4b (SINPE Móvil desde Gmail) marcado como **opcional**: ejecutar solo si hay
  conector Gmail disponible. Si no, pedirle al usuario que adjunte el listado.
- Presentación final agnóstica: archivos van a `/mnt/user-data/outputs/` (claude.ai)
  o `outputs/` configurado por el cliente; la UI los muestra automáticamente como
  links de descarga. No depender de `present_files` ni helpers de Cowork.

**v1.2 (2026-05-18)** — Cambios desde v1.1:
- XLS HTML disfrazado promovido a **fuente primaria** sobre PDF (parser BeautifulSoup
  determinístico, 30-60× más rápido que OCR, sin pérdida de decimales CRC).
- Soporte para formato **MHTML frameset** (subcarpeta `_archivos/sheet001.htm`).
- BNCR CRC y USD agregados como cuentas bancarias nativas.
- Convención de nomenclatura BMC documentada: corte 01-mes_M cubre transacciones M-1.
- Bug guards: Saldo Inicial primera ocurrencia, Línea de Financiamiento +12, header
  secundario "Límite de Pago" rompe procesamiento de transacciones.
- Proveedor RADI TEKNOLOJI MEDIKAL (Turquía) agregado al catálogo internacional.

## Propósito

Automatizar la reconciliación mensual/quincenal cruzando **4 fuentes de datos**:

1. **Odoo** — Facturas emitidas (`account.move`), clientes (`res.partner`), CxC
2. **Bancos Colé** — Cuentas Promerica CRC/USD y BNCR CRC/USD
3. **Tarjeta Black** — Estado de cuenta tarjeta de crédito Promerica (*6931) con extensiones
4. **Hojas Colé** — Hojas Excel internas de gastos e ingresos por quincena

Genera XLSX profesional con discrepancias, clasificación por responsable, CxC aging, y flujo consolidado.

## Inputs Esperados

**Fuente primaria (v1.2):** archivos `.xls` HTML disfrazado exportados desde portal Promerica.
PDF solo como fallback cuando el XLS no esté disponible.

El usuario típicamente proporciona combinaciones de:

1. **Tarjeta Black BMC** — `.xls` HTML disfrazado del portal Promerica (preferido) o PDF "Transacciones por corte"
2. **Estados Promerica CRC/USD** — `.xls` HTML disfrazado (preferido) o PDF
3. **Estados BNCR CRC/USD** — PDF generado web (tiene texto extraíble, NO necesita OCR)
4. **Hojas contables Colé** — Imágenes/screenshots de las hojas Excel internas
5. **Período** — Si no se indica, inferir del rango de fechas en los archivos

No todos los inputs son obligatorios. Ejecutar el cruce con lo disponible y señalar qué falta.

### Referencias obligatorias (leer SIEMPRE antes de cruzar)

Antes de interpretar la hoja Cole o hacer match cliente banco↔Odoo, leer:

- `references/hoja_cole_tipos_renglon.md` — tres tipos de renglón en la hoja Cole (flujo real, pago Marco de su bolsillo, asignación contable pura). Sin esto se atribuyen gastos a movimientos bancarios fantasma.
- `references/clientes_cole_aliases.md` — alias de clientes en banco vs hoja Cole vs Odoo (CICC↔EGAUGE, Papel Serv Fix↔SERVICIOS RADIOLOGIC, Eleinmsa↔ELECTRONICA INDUSTRI). Sin esto se marcan cobros como pendientes cuando solo cambia el nombre.

### Convención de nomenclatura BMC (importante)

Los archivos BMC se nombran por el **mes del corte**, NO por el mes de las transacciones.
La regla es: **corte 01-mes_M cubre transacciones del mes M-1**.

| Archivo | Fecha de corte | Período cubierto |
|---------|----------------|------------------|
| `1 bmc enero 2026.xls` | 01 ENE 2026 | diciembre 2025 |
| `2 bmc feb 2026.xls` | 01 FEB 2026 | enero 2026 |
| `3 bmc mar 2026.xls` | 01 MAR 2026 | febrero 2026 |
| `4 bmc abr 2026.xls` | 01 MAY 2026 | abril 2026 (¡no marzo!) |

**SIEMPRE** leer la "Fecha de Corte" del archivo para confirmar período cubierto antes de procesar.

## Conexión Odoo (JSON-RPC)

**SIEMPRE** jalar facturas de Odoo para el período analizado. No esperar a que el usuario lo pida.

```python
import subprocess, json

URL = "https://colesamarco2020-colesa.odoo.com/jsonrpc"
DB  = "colesamarco2020-colesa-colesa-27146045"
UID = 7
KEY = "c05ae3a29733ef6f21933c7a4c7d1b5ed091a2b4"

def call(model, method, args, kwargs=None):
    payload = {
        "jsonrpc": "2.0", "method": "call", "id": 1,
        "params": {
            "service": "object", "method": "execute_kw",
            "args": [DB, UID, KEY, model, method, args, kwargs or {}]
        }
    }
    r = subprocess.run(
        ["curl", "-sk", "-X", "POST", URL,
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload)],
        capture_output=True, text=True, timeout=60
    )
    data = json.loads(r.stdout)
    if "error" in data:
        msg = data["error"].get("data", {}).get("message", str(data["error"]))
        raise Exception(f"Odoo [{model}.{method}]: {msg}")
    return data.get("result")
```

**SSL:** Siempre `curl -sk`. Nunca `requests` ni `xmlrpc.client`.

### Queries obligatorias por reconciliación

**REGLA CRÍTICA:** No limitar consultas Odoo al mes de análisis. Ejecutar DOS queries separadas:
1. **CxC completa** — TODAS las facturas pendientes sin filtro de fecha (para aging real).
2. **Contexto de período** — Facturas emitidas desde el inicio del mes analizado en adelante (para cruce banco y visibilidad de facturación reciente).

```python
# 1. CxC COMPLETA: Todas las facturas pendientes (sin filtro de fecha)
all_unpaid = call('account.move', 'search_read',
    [[['move_type', '=', 'out_invoice'],
      ['state', '=', 'posted'],
      ['payment_state', 'in', ['not_paid', 'partial']]]],
    {'fields': ['id','name','partner_id','invoice_date','invoice_date_due',
                'amount_total','amount_residual','amount_total_signed',
                'currency_id','payment_state'],
     'order': 'invoice_date asc', 'limit': 200})

# 2. CONTEXTO PERÍODO: Facturas emitidas desde inicio del mes analizado en adelante
#    (incluye in_payment, paid, reversed para cruce completo contra banco)
period_invoices = call('account.move', 'search_read',
    [[['move_type', 'in', ['out_invoice','out_refund']],
      ['state', '=', 'posted'],
      ['invoice_date', '>=', 'YYYY-MM-01']]],  # Sin fecha fin — captura todo hacia adelante
    {'fields': ['id','name','partner_id','invoice_date','invoice_date_due',
                'amount_total','amount_residual','amount_total_signed',
                'currency_id','payment_state','ref','move_type'],
     'order': 'invoice_date asc', 'limit': 200})

# 3. Líneas de factura (unir IDs de ambas queries, deduplicar)
all_inv_ids = list(set([i['id'] for i in all_unpaid] + [i['id'] for i in period_invoices]))
lines = call('account.move.line', 'search_read',
    [[['move_id', 'in', all_inv_ids],
      ['display_type', '=', 'product']]],
    {'fields': ['move_id','product_id','name','quantity','price_unit',
                'price_subtotal','price_total'],
     'order': 'move_id asc'})

# 4. Clientes (solo si no se tiene cache reciente)
clients = call('res.partner', 'search_read',
    [[['customer_rank', '>', 0]]],
    {'fields': ['id','name','vat','email','phone','city','country_id',
                'customer_rank','is_company'],
     'order': 'name asc', 'limit': 300})
```

**Nota:** `total_invoiced` es campo computed no almacenado — NO se puede usar en `order` ni `search`. Calcular agregando `amount_total_signed` de facturas.

**Nota timeout:** Si la query de `all_unpaid` es grande (>100 registros), usar `limit`+`offset` en batches de 100. Timeout de `curl` debe ser 60s mínimo para queries amplias.

## Tarjetahabientes

| Tarjeta | Persona | Rol | Notas |
|---------|---------|-----|-------|
| `*9582` | Marco | Extensión de Manuel | **TODO = Negocio Colé** (regla global confirmada) |
| `*6931` | Manuel (Ing. Rubio) | Titular principal | Mezcla gastos personales y de negocio |
| `*2225` | Zulkary | Extensión | Compras hogar, supermercado, farmacia, niños |
| `*3838` | Otra extensión | — | Baja frecuencia (Google One, Adobe) |
| `*0206` | Manuel Rubio G. | Extensión | Baja frecuencia |
| `0` | Sin tarjeta | Cargos automáticos | Intereses, cuotas, seguros, Quick Pass, CNFL |

## Cuentas Bancarias Colé S.A.

| Banco | Moneda | Número | IBAN | Producto |
|-------|--------|--------|------|----------|
| Promerica | CRC | 30000000416863 | CR70011600103004168637 | Cuenta Óptima Preferencial Empresarial |
| Promerica | USD | 40000000416863 | CR09011600104004168634 | Cuenta Corriente Corporativa |
| BNCR | CRC | 087-001869-2 | CR76 0151 0871 0010 0186 95 | Cuenta Corriente Colones |
| BNCR | USD | 087-601368-0 | CR23 0151 0871 0026 0136 88 | Cuenta Corriente Dólares |

### Proveedores internacionales conocidos (pagos wire desde cuenta USD)

| Beneficiario banco | Proveedor real | Tipo | País |
|---|---|---|---|
| RPP INC BANK DETAILS | RPP Inc. | Plomo y vidrio plomado para blindaje | USA |
| K & S ASSOCIATES | K&S Associates | Proveedor negocio Colé | USA (Nashville) |
| RADI TEKNOLOJI MEDIKAL | Radi Teknoloji Medikal SA | Equipos radiológicos (NUEVO 2026-04) | Turquía |

## Flujo de Ejecución

### Paso 1: Jalar facturas Odoo (OPT-IN — solo si el usuario lo pide)

**NO ejecutar por defecto.** Solo activar si la solicitud del usuario menciona explícitamente:
"incluye Odoo", "con facturas", "cruzá con CxC", "aging clientes", "morosos",
"facturación", "trae facturas", "estado de cobro", o similar.

Si el usuario NO mencionó facturación, omitir este Paso completo, omitir Paso 5a y
Paso 6, y omitir las hojas de Odoo/CxC en los entregables.

**Si se activa**, ejecutar las DOS queries JSON-RPC obligatorias:
- **`all_unpaid`**: CxC completa sin filtro de fecha. Indexar por `partner_id` y por `invoice_date_due` para aging.
- **`period_invoices`**: Facturas desde inicio del mes analizado en adelante. Clasificar por `payment_state`: paid, not_paid, partial, in_payment, reversed. Usar para cruce contra banco.

Deduplicar IDs entre ambos conjuntos antes de buscar líneas de factura.

### Paso 2: Parsear estados de cuenta bancarios

#### 2a. XLS HTML disfrazado de Promerica (FUENTE PRIMARIA)

Los archivos `.xls` exportados desde el portal Promerica son **HTML disfrazado** (no Excel binario).
Existen DOS variantes:

**Variante A: HTML directo** — archivo `.xls` contiene HTML completo, todas las tablas accesibles.

**Variante B: MHTML Frameset** — archivo `.xls` es un frameset stub con `<meta name="Excel Workbook Frameset">`.
Los datos reales están en subcarpeta `<base>_archivos/sheet001.htm`.

Parser robusto que maneja ambas variantes:

```python
import os, re
from bs4 import BeautifulSoup

def to_float(s):
    if s is None: return 0.0
    s = str(s).strip().replace(',', '').replace('\xa0','')
    if not s or s == '-': return 0.0
    try: return float(s)
    except: return 0.0

def parse_promerica(path, currency):
    """Parsea estado de cuenta Promerica (CRC o USD). Soporta HTML directo y MHTML frameset."""
    if not os.path.exists(path):
        return None
    # Si existe sheet001.htm en subcarpeta _archivos, usarlo (MHTML)
    base, _ = os.path.splitext(path)
    sheet = f"{base}_archivos/sheet001.htm"
    actual = sheet if os.path.exists(sheet) else path

    with open(actual, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Frameset sin subcarpeta → archivo corrupto
    if 'Excel Workbook Frameset' in content[:500] and not os.path.exists(sheet):
        return {'currency': currency, 'movements': [], 'parse_error': 'Frameset sin subcarpeta'}
    soup = BeautifulSoup(content, 'html.parser')

    HEADER = ['Fecha','Documento','Concepto','Lugar','Descripción','Monto','Saldo']
    movements_tbl = None
    saldos_tbl = None
    for tbl in soup.find_all('table'):
        rows = tbl.find_all('tr')
        if not rows: continue
        for ri, row in enumerate(rows):
            cells = [c.get_text(strip=True) for c in row.find_all(['th','td'])]
            if len(cells) >= 7 and cells[:7] == HEADER:
                if movements_tbl is None or len(rows) > len(movements_tbl[0].find_all('tr')):
                    movements_tbl = (tbl, ri)
                break
            if len(cells) >= 2 and cells[0] == 'Saldo anterior':
                if saldos_tbl is None or len(rows) < len(saldos_tbl.find_all('tr')):
                    saldos_tbl = tbl
                break
    if movements_tbl is None:
        return {'currency': currency, 'movements': [], 'parse_error': 'No header found'}

    mov_tbl, hi = movements_tbl
    bal_start = bal_end = total_creds = total_debs = None
    movs = []
    for row in mov_tbl.find_all('tr')[hi+1:]:
        cells = [c.get_text(strip=True).replace('\n  ','').replace('\n',' ') for c in row.find_all(['th','td'])]
        if len(cells) < 7: continue
        # BUG GUARD: Saldo Inicial solo en PRIMERA ocurrencia (no sobrescribir)
        if bal_start is None and cells[0].replace(' ','').lower() in ('saldoinicial','saldoinicial:'):
            bal_start = to_float(cells[6])
            continue
        # Saldos al corte dentro de la misma tabla (formato MHTML)
        if cells[0].lower().startswith('saldo') or cells[0].lower().startswith('total'):
            continue
        if not re.match(r'\d{1,2}/\d{1,2}/\d{4}', cells[0]):
            continue
        movs.append({
            'date': cells[0], 'doc': cells[1], 'concept': cells[2], 'place': cells[3],
            'description': cells[4], 'amount': to_float(cells[5]), 'balance': to_float(cells[6])
        })
    # Tabla de saldos al corte (cuando existe separada)
    if saldos_tbl:
        for row in saldos_tbl.find_all('tr'):
            cells = [c.get_text(strip=True) for c in row.find_all(['th','td'])]
            if len(cells) >= 2:
                k = cells[0]; v = to_float(cells[1])
                if k == 'Saldo anterior': bal_start = v
                elif k == 'Total Créditos': total_creds = v
                elif k == 'Total Débitos y Cargos': total_debs = v
                elif k == 'Saldo Parcial Actual': bal_end = v
    # Fallback: inferir bal_start del primer movimiento
    if bal_start is None and movs:
        bal_start = movs[0]['balance'] - movs[0]['amount']
    if bal_end is None and movs:
        bal_end = movs[-1]['balance']
    return {'currency': currency, 'balance_start': bal_start, 'balance_end': bal_end,
            'total_credits': total_creds, 'total_debits': total_debs,
            'movements': movs, 'mov_count': len(movs), 'source_path': actual}
```

#### 2b. BMC Black Master Card (XLS HTML disfrazado)

Estructura similar a Promerica pero header diferente:
`['Fecha','Concepto','Lugar','Transacción Colones','Interés Colones','Transacción Dolares','Interés Dolares']`

**BUG GUARDS críticos:**

1. **Sección "Línea de Financiamiento"** — al detectar header secundario o "Línea de Financiamiento",
   romper el procesamiento de transacciones. Las filas de cuotas NO son transacciones.

2. **Filas tipo `"# 12 Cuota # 6/12"`** — son del rubro Línea de Financiamiento +12 cuotas.
   Filtrar con `re.search(r'#\s*\d+\s*Cuota\s*#', joined)`.

3. **Sección "Línea de Financiamiento"** se identifica por header secundario:
   `['Límite de Pago', 'Concepto', 'Monto total de la Cuota', 'Pagos de Intereses', ...]`

```python
def parse_bmc(path):
    base, _ = os.path.splitext(path)
    sheet = f"{base}_archivos/sheet001.htm"
    actual = sheet if os.path.exists(sheet) else path
    with open(actual, 'r', encoding='utf-8', errors='replace') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    HEADER = ['Fecha','Concepto','Lugar','Transacción Colones','Interés Colones',
              'Transacción Dolares','Interés Dolares']
    txns = []
    current_card = None
    meta = {}

    # Fecha de corte: indica QUÉ MES cubren las transacciones (mes anterior al corte)
    for row in soup.find_all('tr'):
        cells = [c.get_text(strip=True).replace('\n',' ').replace('  ',' ') for c in row.find_all(['th','td'])]
        if any('Fecha de Corte' in c or 'Fecha deCorte' in c for c in cells):
            for ci, c in enumerate(cells):
                if ('Fecha' in c and 'Corte' in c) and ci+1 < len(cells) and cells[ci+1]:
                    meta['cycle_end'] = cells[ci+1]
                    break
            break

    # Buscar la tabla con HEADER y procesar
    main_tbl = None
    for tbl in soup.find_all('table'):
        for ri, row in enumerate(tbl.find_all('tr')):
            cells = [c.get_text(strip=True) for c in row.find_all(['th','td'])]
            if len(cells) >= 7 and cells[:7] == HEADER:
                if main_tbl is None or len(tbl.find_all('tr')) > len(main_tbl[0].find_all('tr')):
                    main_tbl = (tbl, ri)
                break
    if main_tbl is None: return {'meta': meta, 'transactions': [], 'count': 0}

    saw_credit_section = False
    for row in main_tbl[0].find_all('tr')[main_tbl[1]+1:]:
        cells = [c.get_text(strip=True).replace('\n  ','').replace('\n',' ').replace('\xa0','')
                 for c in row.find_all(['th','td'])]
        if not cells or all(not c for c in cells): continue
        joined = ' '.join(cells)
        # BUG GUARD: detectar sección Línea de Financiamiento → romper
        if 'Línea de Financiamiento' in joined or 'Monto total de la Cuota' in joined:
            saw_credit_section = True
            continue
        if saw_credit_section: continue
        # BUG GUARD: filtrar filas de cuotas (línea +12)
        if re.search(r'#\s*\d+\s*Cuota\s*#', joined): continue
        # Detectar tarjetahabiente
        m = re.search(r'\*+-?\*+-?\*+-?\*+-?(\d{4})', joined)
        if m and len(cells) <= 3:
            current_card = m.group(1); continue
        m = re.search(r'5\d{12,15}', joined)
        if m and len(cells) <= 4:
            current_card = m.group(0)[-4:]; continue
        # Transacción estándar
        if len(cells) >= 7 and re.match(r'^\d{1,2}/\d{1,2}/\d{4}$', cells[0]):
            crc = to_float(cells[3]); usd = to_float(cells[5]) if len(cells) > 5 else 0
            if crc != 0:
                txns.append({'date': cells[0], 'description': cells[1], 'place': cells[2],
                            'amount': crc, 'currency': 'CRC', 'card': current_card or '6931'})
            if usd != 0:
                txns.append({'date': cells[0], 'description': cells[1], 'place': cells[2],
                            'amount': usd, 'currency': 'USD', 'card': current_card or '6931'})
    return {'meta': meta, 'transactions': txns, 'count': len(txns)}
```

#### 2a-2026. Cuentas Promerica — FORMATO 2026 (fuente primaria actual)

Desde 2026 el portal Promerica exporta con header nuevo:
`['Fecha','Documento','Descripción','Débitos','Créditos','Saldo']` (débito y crédito en
columnas separadas; ya no existe columna única "Monto" ni "Concepto/Lugar").
Metadatos por texto plano: `Número de cuenta:` (40000…=USD, 30000…=CRC, o sufijo
DOLARES/COLONES) y `Rango de Fechas: d/m/yyyy - d/m/yyyy`.

```python
HEADER_2026 = ['Fecha','Documento','Descripción','Débitos','Créditos','Saldo']
# Recorrer TODAS las filas <tr> del documento (no confiar en límites de <table>:
# los exports anidan tablas). Activar captura al encontrar HEADER_2026; cada fila
# con fecha d/m/yyyy y ≥6 celdas es un movimiento:
#   {fecha, doc, descripcion, debito, credito, saldo}
# Filas 'Total de Débitos'/'Total de Créditos' → guardar para validación.
```

**Validación de integridad (OBLIGATORIA, v1.6):**

```python
saldo_inicial = movs[0]['saldo'] + movs[0]['debito'] - movs[0]['credito']
esperado = saldo_inicial + sum(m['credito'] for m in movs) - sum(m['debito'] for m in movs)
assert abs(esperado - movs[-1]['saldo']) < 0.02       # cuadre de saldos
assert abs(sum_debitos_calc - total_debitos_archivo) < 0.02  # vs fila Total del archivo
```

Si falla, el parseo perdió o duplicó filas: DETENER, no cruzar con datos incompletos.

#### 2b-2026. BMC Black — FORMATO 2026 (tarjetahabiente por fila)

Header nuevo: `['Fecha','Número de Tarjeta','Descripción','Débitos','Créditos','Moneda']`.
Diferencias vs formato legado:

- El tarjetahabiente viene POR FILA en columna 2 (`537*********6931`) — ya NO hay bloques.
  Extraer últimos 4 dígitos; valor literal `0` = cargos automáticos sin tarjeta.
- `Moneda` por fila: `DOLARES` | `COLONES` (mezcladas en el mismo archivo).
- Los archivos se exportan por RANGO de fechas (`Rango de Fechas:`), no por corte; la
  convención "corte 01-mes_M cubre M-1" aplica solo a archivos legado nombrados por corte.
- Archivos de rangos contiguos pueden SOLAPARSE: deduplicar por
  fecha+descripción+monto+tarjeta+moneda antes de cruzar.
- Mantener BUG GUARDS v1.2: cortar en 'Línea de Financiamiento'/'Monto total de la Cuota'
  y filtrar filas `# 12 Cuota # M/N` (cuota típica ₡91,316 — verificada también en 2026).

#### 2c. PDF fallback (BMC, Promerica, BNCR)

Si el usuario solo proporciona PDFs:

**Tarjeta Black (PDF "Transacciones por corte")** — Leer transacciones individuales de la tabla. **IGNORAR** las líneas resumen de intereses (Interés del Periodo, Intereses Corrientes, Pago de Interés, Interés diario moratorio) — son informativos, NO contabilizar como gastos.

**Cuentas Promerica CRC/USD (PDF)** — Escaneados, requieren OCR (pytesseract con `lang='spa'`). OCR pierde decimales en montos CRC grandes — usar XLS si disponible.

**Cuentas BNCR CRC/USD (PDF)** — Generados desde portal web con texto extraíble. Usar `pdfplumber` directamente (sin OCR). Header esperado: `['FECHA','NÚMERO','DESCRIPCIÓN','MONTO','SALDO DIARIO']`.

### Paso 3: Separar tarjeta por tarjetahabiente

Filtrar por número de tarjeta parcial: `9582`→Marco, `6931`→Manuel, `2225`→Zulkary, `3838`→Otra, `0206`→Manuel alt, `0`→Bancarios.

### Paso 4: Categorizar gastos tarjeta

Leer `references/categories.md` para la tabla completa. Categorías: NEGOCIO, PERSONAL, AMBIGUO, EXCLUIR (pagos/créditos), IVA (transfronterizo).

**Reglas de clasificación confirmadas (aplicar siempre):**

| Regla | Clasificación | Alcance |
|-------|--------------|---------|
| Marco *9582 | **TODO Negocio** | Regla global — cualquier cargo en esta tarjeta es negocio Colé |
| Marriott | **Personal** | Todos los cargos Marriott, sin importar tarjetahabiente |
| Dropbox | **Negocio Colé** | Plan de negocio |
| Uber | **Personal** | Todos los viajes Uber, sin importar tarjetahabiente |

**Prioridad de reglas:** (1) Pagos/créditos → EXCLUIR, (2) Cargos bancarios → BANCARIO, (3) Servicios fijos → FIJO, (4) Marco *9582 → NEGOCIO, (5) Reglas por comercio (Marriott, Dropbox, Uber), (6) Keywords de negocio (Claude.AI, SendinBlue, OpenAI, etc.), (7) Default → PERSONAL.

### Paso 4b: Leer SINPE Móvil desde Gmail (opcional — requiere conector Gmail)

**Si hay conector Gmail disponible**, buscar transferencias SINPE del período automáticamente. **Si no hay Gmail** (típico en claude.ai sin MCP), pedirle al usuario explícitamente: *"No tengo acceso a Gmail en este entorno. Para incluir los SINPE Móvil del período, adjuntá un listado (CSV/texto/captura) con fecha, beneficiario, monto y descripción. Si no aplica, puedo continuar sin la hoja SINPE."* Continuar la reconciliación sin la hoja SINPE si el usuario no provee el dato.

```python
# 1. Buscar emails SINPE del mes analizado
# Gmail tool: gmail_search_messages
# q = 'subject:"tu transferencia SINPE Móvil" after:YYYY/MM/01 before:YYYY/MM+1/01'
# maxResults = 30

# 2. Leer cada email con gmail_read_message(messageId)

# 3. Parsear HTML del body con regex:
import re
body = message['body']
# Beneficiario + ID
m = re.search(r'realizada con éxito a\s*</span>\s*<span[^>]*>\s*(.+?)\s*Identificación\s+(\S+)', body)
beneficiario = m.group(1).strip() if m else ''
# Monto
m = re.search(r'por un monto de\s*</span><span[^>]*>\s*CRC\s+([\d,]+\.\d{2})', body)
monto = float(m.group(1).replace(',','')) if m else 0
# Descripción
m = re.search(r'Descripción:\s*</span><span[^>]*>\s*(.+?)\s*<', body)
desc = m.group(1).strip() if m else ''
# Fecha
m = re.search(r'Fecha de ejecución:\s*</span><span[^>]*>\s*(\d{2}/\d{2}/\d{4})', body)
fecha = m.group(1) if m else ''
```

**Clasificación SINPE:** La mayoría son personales (jardinero, guarda, huevos, terapeuta, equitación, niños). Marcar como negocio solo si la descripción contiene "COLESA", "COLE", "mensajería" u otra referencia explícita a la empresa.

**Incluir en entregables:** Los SINPE van en la hoja "Gastos Personales Consolidados" (junto con gastos personales de tarjeta) y en "SINPE Marzo" (hoja dedicada en XLSX técnico).

### Paso 5: Cruce 4 vías

#### 5a. Facturas Odoo ↔ Ingresos Banco (OPT-IN — solo si Paso 1 se ejecutó)

Si el Paso 1 NO se ejecutó (caso default), saltar este sub-paso completo.

Si sí se ejecutó: usar `period_invoices` (desde inicio del mes analizado en adelante). Para cada factura posted, buscar ingreso correspondiente en cuentas CRC/USD (Promerica + BNCR):
- Match por nombre de cliente (fuzzy) + monto (±5% tolerancia por comisiones/IVA)
- Marcar: `✅ Cobrada` | `🔄 En pago sin ingreso` | `❌ Pendiente`

#### 5b. Ingresos Banco ↔ Hojas Colé
Para cada crédito en cuentas bancarias, buscar registro en hojas Colé:
- Match por concepto/nombre + monto
- Detectar ingresos banco sin factura Odoo (posibles facturas de otro período)

#### 5c. Pagos Banco → Tarjeta Black
Cruzar débitos "TEF. ELEC black" en cuentas CRC/USD contra créditos "PAGO ELECTRONICO" en tarjeta:
- Verificar montos coincidan
- Detectar diferencias (pagos parciales, créditos cargos corrientes)

#### 5d. Gastos Tarjeta ↔ Hojas Colé
Para cada gasto de negocio en tarjeta, buscar en hojas Colé:
- `✅ OK` — Match exacto
- `⚠️ Δ` — Existe con diferencia de monto
- `⚠️ Agrupado` — Múltiples cargos consolidados en Colé
- `❌ Falta` — No aparece en Colé
- `❓ Ambiguo` — No determinable

### Paso 6: CxC Aging (OPT-IN — solo si Paso 1 se ejecutó)

Si el Paso 1 NO se ejecutó (caso default), saltar este Paso completo y omitir las hojas "CxC Aging" y "CxC Top Deudores" en los entregables.

Si sí se ejecutó: usar `all_unpaid` (TODAS las facturas pendientes en Odoo, sin filtro de fecha):
- Calcular días vencidos = hoy - `invoice_date_due`
- Clasificar: 🟢 Vigente | 🟠 1-15 días | 🟡 16-30 días | 🔴 >30 días
- Agrupar por cliente para detectar concentración de riesgo
- Incluir resumen de buckets (totales por rango de antigüedad)
- Identificar top 5 deudores por monto residual

### Paso 7: Generar Entregables

**SIEMPRE generar DOS archivos.** Leer `/mnt/skills/public/xlsx/SKILL.md` y `/mnt/skills/public/frontend-design/SKILL.md` antes de generar.

#### Entregable A: XLSX Técnico (`reconciliacion_[mes]_[año].xlsx`)

Archivo de trabajo con datos crudos y cruces detallados. Hasta 13 hojas:

1. **"Cruce Odoo↔Banco↔Colé"** — Hoja maestra (solo si Odoo opt-in): facturas Odoo desde inicio del mes analizado en adelante, cruzadas contra ingreso banco y registro Colé. Créditos banco sin match de factura al final.
   - Columnas: Factura | Fecha | Cliente | Monto USD | Estado Pago | Tipo | Ingreso Banco | Nota

2. **"Concil Marco"** — Hoja dedicada de conciliación Marco (SIEMPRE — v1.5). Cruza gasto real Marco *9582 en BMC vs líneas hoja Cole atribuibles a Marco. Ver §7.5 para algoritmo y estructura de 6 bloques.

3. **"Q1 [Mes] Tarjeta"** — Transacciones tarjeta 1era quincena categorizadas
   - Columnas: Fecha | Tarjetahabiente | Descripción | Débito | Crédito | Moneda | Tipo | Categoría

4. **"Q2 [Mes] Tarjeta"** — Transacciones tarjeta 2da quincena (deduplicadas vs Q1)

5. **"SINPE [Mes]"** — Todas las transferencias SINPE Móvil del período, leídas de Gmail
   - Columnas: Fecha | Beneficiario | Monto CRC | Descripción | Tipo (Negocio/Personal)

6. **"Promerica CRC"** — Movimientos cuenta colones con categorización y cruce

7. **"Promerica USD"** — Movimientos cuenta dólares con categorización y cruce

8. **"BNCR CRC"** — Movimientos cuenta BNCR colones (si hay)

9. **"BNCR USD"** — Movimientos cuenta BNCR dólares (si hay)

10. **"CxC Aging"** — (solo si Odoo opt-in) TODAS las facturas pendientes en Odoo (sin filtro de fecha), con días vencidos, semáforo de riesgo, buckets de antigüedad y top deudores

11. **"Gastos Personales Consolidados"** — Todos los gastos personales de TODAS las fuentes unificados: tarjeta Manuel+Zulkary+Marco (personales) + SINPE personales. Columnas: Fecha | Fuente | Titular/Beneficiario | Descripción | Monto | Moneda | Categoría. Incluir totales por fuente y moneda al final.

12. **"Flujo Consolidado"** — Ingresos, egresos, variación neta del período por moneda. Incluir resumen CxC con buckets.

13. **"Discrepancias"** — Lista priorizada por severidad (🔴 Alta, 🟡 Media, 🟠 Baja)

**Codificación de color:**
- Verde (#C6EFCE): OK / match confirmado
- Amarillo (#FFEB9C): Discrepancia / ambiguo / en pago
- Rojo (#FFC7CE): Faltante / sin cobro / alerta
- Azul (#D6E4F0): Negocio Colé
- Gris (#F2F2F2): IVA / informativo

#### Entregable B: Resumen Ejecutivo — Doble formato

Pensado para audiencia no contable. Lenguaje claro, iconos, semáforos, sin jerga.

**B.1: XLSX Ejecutivo (`resumen_[mes]_[año].xlsx`)**

5 hojas con formato visual, categorías con iconos, explicaciones en lenguaje simple:

1. **"Resumen Ejecutivo"** — KPIs principales (CxC total, facturado, cobrado, saldo consolidado), distribución de gastos (negocio/personal/ambiguo/bancario con porcentajes y explicaciones), aging CxC con semáforo, saldos bancarios con variación.

2. **"Gastos Negocio"** — Detalle de gastos deducibles Colé agrupados por categoría (Software/SaaS, Equipos, Courier, Viajes, Servicios fijos, Intereses). Columnas: Categoría | Descripción | USD | CRC | Tarjetahabiente. Resaltar sobregiros en rojo.

3. **"Gastos Personales"** — Detalle de gastos no deducibles agrupados por categoría con iconos (🛒🍽️💊🦷🧸📺⛽🔧). Incluir sección aparte de suscripciones digitales con costo mensual, servicio y titular.

4. **"CxC Top Deudores"** — Lista de todos los clientes con CxC pendiente, ordenados por monto. Columnas: Cliente | # Facturas | Monto USD | Fecha más antigua | Días vencido | Semáforo | Acción sugerida. Nota de concentración de riesgo (ej: "CCSS concentra X% del CxC").

5. **"Roadmap y Alertas"** — Tres secciones:
   - Alertas por severidad (🔴 Alta, 🟡 Media, 🟠 Baja) con monto y acción requerida
   - Decisiones pendientes de clasificación (gastos ambiguos con pregunta y tarjetahabiente)
   - Roadmap de cobro semana por semana (4 semanas) con acciones concretas, clientes y montos
   - Próximos pasos numerados al final

**B.2: Dashboard React (`dashboard_[mes]_[año].jsx`)**

Componente React con recharts, tema dark, 5 tabs interactivos:

1. **📊 Resumen** — KPI cards (CxC, facturado, cobrado, saldo), barras de progreso aging, pie charts CRC/USD por tipo de gasto, gráfico de área flujo de caja con proyección 2 meses.

2. **💳 Gastos Tarjeta** — Bar chart horizontal gasto por tarjetahabiente, listas detalladas negocio (con iconos) y personal (con iconos), grid de suscripciones digitales, badge de gastos ambiguos.

3. **📋 Cuentas por Cobrar** — Bar chart aging por bucket (coloreado por severidad), lista de top deudores con días vencidos y semáforo, roadmap visual de cobro 4 semanas con timeline.

4. **🏦 Bancos** — Cards de variación de saldo por cuenta (inicio → delta → cierre, Promerica + BNCR), listas de principales egresos e ingresos con clasificación.

5. **🚨 Alertas** — AlertBoxes por severidad, tarjetas de decisiones pendientes con contexto, sección de próximos pasos.

**Librerías React permitidas:** recharts, lucide-react, Tailwind core utilities. Tema dark con CSS variables. No localStorage.


### Paso 7.5: Conciliación Marco (SIEMPRE — v1.5)

Marco *9582 = todo negocio por regla global, pero la hoja Cole solo registra un subset
de sus gastos. Sin vista dedicada, gastos materiales como Klarity Medical
(compra completa $7,502.93 en Q1 ene 2026) quedan invisibles. Esta sección genera la
hoja **"Concil Marco"** en posición 2 del XLSX técnico.

**Estructura de 6 bloques:**

1. **BMC Marco detallado** — todos los cargos *9582 del período, ordenados por moneda
   y día. Columnas: Fecha, Descripción, Moneda, Monto, Sub-categoría, Nota. Totales
   USD y CRC al final.

2. **Hoja Cole atribuible a Marco** — líneas de la hoja Cole que se cargan a Marco.
   Algoritmo de atribución: matchear `concepto.lower()` contra keywords:
   `['marco','aero','k&s','odoo','klarity','chat gpt','cholo','rosie','jiras']`.
   Columnas: Concepto, Tipo (1/2/3), USD, CRC, Tratamiento, Nota.

3. **Análisis Δ USD agregado** — tres filas:
   - BMC Marco *9582 total USD
   - Hoja Cole atribuible Tipo 1 USD (solo flujos reales — Tipo 2 son reembolsos,
     Tipo 3 son asignaciones contables sin flujo)
   - Δ NO reportado = BMC − Hoja Tipo 1

4. **Detalle Δ línea por línea** — agrupar BMC Marco USD por categoría/proveedor y
   comparar contra concepto correspondiente en hoja Cole:
   - Aeropost (suma DLC*AEROPOST) vs aerocasillas + Aero Marco
   - K&S Associates vs K&S Fito pino SFE
   - WFS*Odoo vs ODOO server
   - Klarity Medical vs Ajuste Klarity HSJD (típicamente compra completa fuera de
     hoja — hipótesis principal: facturada al cliente, debe estar en facturas
     emitidas no en gastos)
   - Google Workspace, Zoom, eBay, Amazon, ChatGPT/OpenAI Marco — verificar
     individualmente, marcar 🔴 si no aparece en hoja
   - Google Play (Crunchyroll/Rakuten/Viber) — ambiguo personal/negocio Marco
   - IVA transfronterizo — informativo

5. **Marco CRC BMC vs Hoja** — incluir Mitigo seguro auto, viáticos alimentación
   (McDonald, Plaza Toros, BMBoston, restaurantes), parqueo, DHL, Naviera, PriceSmart,
   etc. vs líneas hoja Cholo/Limpieza Rosie/Jiras/Viáticos Marco con sus tipos. Notar
   cargos fuera del período (caen en Q2).

6. **Conclusión accionable** — 5-6 líneas con tags:
   - ✅ Lo que cuadra
   - 🟡 Δ por refinar (<$50)
   - 🔴 Δ material (Klarity típicamente el más grande)
   - 🔴 No reportados en hoja
   - ℹ️ Fuera de Q1/Q2
   - 🎯 Recomendación final con totales BMC vs Hoja Tipo 1 y Δ.

**Codificación de color por fila Δ:** verde si Δ < $1 USD, amarillo si $1 ≤ Δ < $50,
rojo si Δ ≥ $50 o concepto no aparece en hoja.

### Paso 8: Presentar resultados

1. Generar los 3 archivos (XLSX técnico + XLSX ejecutivo + JSX dashboard) en el directorio de salida del entorno:
   - **claude.ai**: `/mnt/user-data/outputs/`
   - **Cowork / desktop**: carpeta del proyecto del usuario (ej: `C:\Users\<user>\.claude\projects\Card Reconcilier\`)
   - **Otros entornos**: directorio que el cliente exponga como outputs
2. Listar los 3 archivos al usuario por nombre y ruta. Si el entorno provee un helper de presentación (ej. `mcp__cowork__present_files`), usarlo con orden: dashboard → resumen XLSX → técnico. Si no lo hay, basta con mencionar los paths en la respuesta — la UI del cliente los renderiza como descargas.
3. Resumen ejecutivo breve en texto del chat:
   - Total facturado Odoo vs cobrado en banco
   - CxC total y top clientes morosos
   - Distribución negocio/personal/ambiguo
   - Alertas críticas (máximo 3)
   - Decisiones pendientes (listar)
   - Variación de saldo bancario

## Reglas de Negocio

1. **Pagos no son gastos** — `PAGO ELECTRONICO`, `CREDITO CARGOS CORRIENTES`, `CREDITO O REVERSO` son pagos/créditos. Excluir de gastos.
2. **Cargos del 01 del mes siguiente** — Los cargos bancarios (intereses, cuotas, seguros) del día 01 del mes siguiente pertenecen al cierre de la 2da quincena.
3. **Rezagos de fecha** — Deduplicar por fecha+descripción+monto entre quincenas.
4. **45% regla [CORREGIDA v1.7]** — `45% = 0.45 × Bruto` donde `Bruto = Σ facturas` de la
   quincena (por moneda). Cada gasto/proyecto lleva su propia columna 45%; la fila Total
   acumula `Total(45%·gastos)`. Verificada contra libro maestro 15-05-2026:
   0.45×23,973.62 = 10,788.13 ✓.
5. **Salario Marco [CORREGIDA v1.7]** — `Salario Marco = 45%·Bruto − Total(columna 45% de
   gastos)` por moneda. `Transferir = NETO = Salario Marco + extras a transferir`
   (Cholo/Limpieza Rosie/Agencia). Verificada: 10,788.13 − 5,557.29 = 5,230.84 ✓ y
   1,923,563.01 + 696,573 = 2,620,136.01 ✓. Puede ser negativo.
6. **Intereses en "Transacciones por corte" son informativos** — Los PDFs de estado de cuenta Promerica incluyen líneas de intereses en tablas resumen. Son **solo informativos** y NO se contabilizan como transacciones. Solo procesar intereses que aparecen como transacciones individuales en los XLS de movimientos (ej: `CARGOS CORRIENTES POR DEUDA`, `CARGOS CORRIENTES POR FLOTANTES`).
7. **Capitalización de intereses en cuentas bancarias** — Las líneas `CAPITALIZACION NORMAL DE INTERESES` en cuentas CRC/USD son intereses ganados. Registrar como ingreso menor, no como operación comercial.
8. **Comisiones SINPE** — Los `DEBITO COMISION CM TFT SINPE IB` son cargos bancarios por transferencia. Agrupar en gastos bancarios, no asignar a la operación que acompañan.
9. **Facturas revertidas** — Facturas Odoo con `payment_state: reversed` o `move_type: out_refund` no se procesan como ingreso pendiente. Verificar que tengan nota crédito correspondiente.
10. **Wire transfers internacionales** — Pagos `DOL P/TRAN.DOL A BANCOS` o `WT:` desde cuenta USD son pagos a proveedores internacionales. Clasificar como gasto de negocio. RPP INC = plomo/vidrio plomado; RADI TEKNOLOJI = equipos radiológicos Turquía.
11. **Línea de Financiamiento +12 BMC** — Saldo de la línea +12 cuotas NO es una transacción del mes. Aparece como fila `# 12 Cuota # M/N` con valor en columna de "Monto total de la Cuota". Filtrar antes de categorizar. Cuota mensual típica: ₡91,316.
12. **COBRO POR TERMINAL (Promerica)** — [RECONSTRUIDA v1.6 — confirmar con el titular]
    Cargo fijo mensual de ₡14,000 en cuenta CRC con descripción `Cobro de terminales [Mes]`
    (servicio de datáfono/POS). Evidencia: nov-2025→abr-2026, siempre ₡14,000, fin de mes.
    Clasificar como **gasto bancario fijo**, no como operación comercial ni gasto de proyecto.
13. **Integridad de saldos antes de cruzar (v1.6)** — Por cada estado de cuenta parseado,
    verificar `saldo_inicial + Σcréditos − Σdébitos = saldo_final` y las sumas calculadas
    contra las filas "Total de Débitos/Créditos" del archivo (tolerancia 0.02). Si no
    cuadra, NO ejecutar el cruce: el parseo perdió filas y todo cruce posterior miente.
14. **TEF↔BMC no cuadra 1:1 (v1.6)** — Los TEF de pago de tarjeta y los abonos
    `PAGO ELECTRONICO` del BMC difieren en monto de forma normal. Emparejar por proximidad
    de fecha (≤3 días, misma moneda, menor Δ) y reportar el Δ como discrepancia 🟡.
    Abono BMC sin TEF Promerica = probable fondeo desde BNCR u otra cuenta fuera del set
    cargado: reportar como 🟠 informativo, no como error.
15. **Solapamiento de archivos por rango (v1.6)** — Los exports 2026 por rango de fechas
    pueden solaparse entre sí. Deduplicar SIEMPRE por fecha+descripción+monto+tarjeta+moneda
    antes de totalizar o cruzar; reportar cuántas filas se descartaron.

> **NOTA DE REPARACIÓN v1.6:** el archivo v1.5 terminaba abruptamente en la Regla 12.
> Si existían reglas o secciones posteriores en el original, se perdieron y deben
> re-dictarse por el titular. La Regla 12 actual se reconstruyó con evidencia bancaria
> real; las Reglas 13-15 son nuevas de v1.6.
