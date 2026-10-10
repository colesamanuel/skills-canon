---
name: odoo-invoice-auditor-v2b
description: Auditor de facturas de venta en Odoo 18 multi-empresa Colé S.A. (company_id=1) y Kermatec Dosimetric S.A. (company_id=2) vía JSON-RPC, con credencial externa mediante ODOO_API_KEY. Niveles A (inventario), B (aging/CxC), C (fiscal CR), D (precios), E (contable). Genera reporte de morosos consolidado por cliente+moneda y detallado por factura. Detecta hallazgos H1-H15. Genera XLSX multi-hoja con inventario, aging, top clientes, morosos y hallazgos. Activar con "audita facturas", "revisa facturas Kermatek", "revisa facturas Colé", "CxC Odoo", "aging clientes", "cuentas por cobrar", "morosos", "lista de morosos", "quién me debe", "clientes morosos", "deuda por cliente", "estado de cuenta clientes", "in_payment sin conciliar", "facturas sin IVA", o cualquier análisis crítico de account.move. Activar incluso si la solicitud parece simple.
---

# Odoo Invoice Auditor v2b

Auditor multi-empresa con 15 detectores y salida XLSX. La API key no forma parte
del skill ni del repositorio: se obtiene de `ODOO_API_KEY` o, de forma temporal,
del argumento `--api-key`.

## Seguridad de la credencial

- Nunca escribir la API key en `SKILL.md`, scripts, ejemplos, logs o commits.
- Comprobar `ODOO_API_KEY` antes de consultar Odoo.
- Si falta, detenerse y pedir al titular que la configure fuera del repositorio.
- Revocar y sustituir inmediatamente cualquier key que haya sido publicada.

## Precedencia de la API key

```
1. --api-key CLI argument  (override temporal)
2. $ODOO_API_KEY env var   (configuración normal)
```

## Contexto operativo

| Parámetro | Valor |
|---|---|
| URL | `https://colesamarco2020-colesa.odoo.com` |
| DB | `colesamarco2020-colesa-colesa-27146045` |
| UID | 7 |
| `company_id=1` | Inversiones E Importaciones Colé S.A. (cédula 3-101-392010) |
| `company_id=2` | Kermatec Dosimetric S.A. (cédula 3-101-857015) |

## Uso

Tras descomprimir en el directorio de skills:

```bash
# Colé S.A.
python3 scripts/audit_invoices.py --company-id 1

# Kermatec
python3 scripts/audit_invoices.py --company-id 2

# Ventana específica
python3 scripts/audit_invoices.py --company-id 2 \
    --date-from 2026-01-01 --date-to 2026-04-23 \
    --output ~/kermatek_audit.xlsx

# Configuración segura por entorno
export ODOO_API_KEY="nueva_key_rotada"
python3 audit_invoices.py --company-id 2

# Override temporal
python3 audit_invoices.py --api-key OTRA_KEY --company-id 2
```

## Rotación de la key

Cuando sea necesario rotar (por política interna, sospecha de filtración, cambio de personal con acceso):

1. Generar nueva API key en Odoo: **Mi perfil → Cuenta → Claves API**.
2. **Revocar la anterior** en la misma pantalla.
3. Actualizar `ODOO_API_KEY` en el entorno del usuario o sistema autorizado.
4. Reiniciar las aplicaciones que deban heredar la variable.
5. Verificar con `python3 audit_invoices.py --company-id 2`.

## Flujo obligatorio

### Paso 1 — Parametrización inicial

Antes de consultar Odoo, confirmar con el usuario:

1. **Compañía objetivo:** `1` (Colé), `2` (Kermatec), o `ambas`.
2. **Ventana temporal:** rango de fechas o "todo el histórico".
3. **Nivel de auditoría:** `AB` (default), `ABC`, `ABCD`, o `ABCDE`.
4. **Output:** XLSX + resumen en chat.

Si el usuario dice "audita las facturas de X" sin más contexto, asumir **A+B, histórico completo de la compañía mencionada, XLSX + resumen**. Confirmar en una línea y proceder.

No pedir que la API key se pegue en el chat. Si la variable no existe, indicar el
nombre `ODOO_API_KEY` y detener la consulta hasta que el titular la configure.

### Paso 2 — Descubrimiento de compañías

Verificar el tenant antes de filtrar. Si el VAT no coincide con lo esperado (Colé: 3-101-392010, Kermatec: 3-101-857015), detener y consultar al usuario.

### Paso 3 — Ejecutar auditoría

El script:

1. Usa la API key embebida (a menos que se override por CLI o env).
2. Descarga `account.move` filtradas por `company_id` y `move_type in ('out_invoice','out_refund')`.
3. Normaliza en DataFrame.
4. Calcula aging con fecha de hoy como ancla.
5. Genera reporte de morosos.
6. Corre los 15 detectores de hallazgos.
7. Genera XLSX multi-hoja.
8. Imprime resumen estructurado a stdout.

### Paso 4 — Presentar resumen en chat

Estructura obligatoria:

```markdown
## Resumen ejecutivo
[Tabla: compañía | facturas | total | pendiente | % cobrado por moneda]

## Aging CxC
[Tabla de buckets: Vigente | 1-30 | 31-60 | 61-90 | 91-180 | >180]

## Hallazgos (ordenados por criticidad: 🔴 → 🟠 → 🟡 → 🟢)

## Siguiente paso recomendado
```

Adjuntar XLSX con `present_files`.

### Paso 5 — Ofrecer profundización

Preguntar si quiere profundizar en algún hallazgo o escalar a nivel C/D/E. **No ejecutar niveles adicionales sin confirmación.**

## Catálogo de hallazgos

Ver `references/hallazgos-catalogo.md` — códigos H0–H15, severidades 🔴🟠🟡🟢.

## Validación fiscal (nivel C)

Ver `references/fiscal-cr.md` — tarifas IVA, clave numérica Hacienda, consecutivo fiscal, exenciones.

## Regla de cambios quirúrgicos (Karpathy)

Este skill **detecta y reporta. No modifica data de Odoo.** No ejecuta `write`, `unlink` ni `create`. Si el usuario pide corregir, responder: "Este skill es de solo lectura. Para corregir [X] usa UI Odoo o un skill separado de escritura."

## ⚠️ Checklist de seguridad operativa

Antes de cada acción que toque el directorio del skill, preguntar:

- [ ] ¿Voy a subir esto a un repositorio? → **Verificar .gitignore y hacer `git diff` antes de commit.**
- [ ] ¿Voy a compartir con un colaborador? → **NO. Compartir solo una versión sin la key.**
- [ ] ¿Voy a hacer backup a servicio externo? → **Verificar que el destino esté cifrado.**
- [ ] ¿El backup automático de mi sistema incluye esta carpeta? → **Verificar destino del backup.**
- [ ] ¿Hay otra persona con acceso físico o SSH a esta máquina? → **Considerar rotación periódica de la key.**

Si cualquiera de los anteriores representa duda, **considerar migrar a v2** (key fuera del skill en `~/.config/`).
