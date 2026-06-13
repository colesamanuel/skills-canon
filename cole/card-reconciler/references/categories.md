# Categorías de gasto tarjeta — reglas de clasificación
**[RECONSTRUIDO v1.6 desde las reglas confirmadas del SKILL.md + histórico Money Manager
(7,871 movimientos 2009-2026, 203 beneficiarios). Validar contra el original perdido.]**

## Prioridad de aplicación
1. Pagos/créditos → **EXCLUIR**: `PAGO ELECTRONICO`, `CREDITO CARGOS CORRIENTES`,
   `CREDITO O REVERSO`, `REVERSO DE COMPRA`, `Traslados de puntos`
2. `IMPUESTO VALOR AGREGADO TRANSFRONTERIZO` → **IVA** (informativo)
3. Cargos bancarios → **BANCARIO**: interés, comisión, membresía, seguro saldo, multa
4. Marco *9582 → **NEGOCIO** (regla global confirmada, sin excepciones)
5. Reglas por comercio: MARRIOTT → PERSONAL · UBER → PERSONAL · DROPBOX → NEGOCIO
6. Keywords NEGOCIO: OpenAI/ChatGPT, Anthropic/Claude.AI, Google Workspace, Zoom,
   Odoo/WFS*Odoo, K&S Associates, Klarity, Aeropost/DLC*AEROPOST, DHL, FedEx, Ludlum,
   Radcal, SendinBlue/Brevo, GoDaddy, Hostinger, LinkedIn
7. Servicios fijos → **FIJO**: Quick Pass, CNFL, Kolbi/ICE, AyA, `Cobro de terminales`
8. Default: *2225 (Zulkary) → PERSONAL (hogar/super/farmacia/niños) · resto → AMBIGUO

## Categorías Money Manager más frecuentes (histórico real)
- Ingresos: `INgresos`, `Ingresos provenientes de CCSS`, `Ingresos provenientes de Bionet`,
  subcategorías CURSOS, Solurad, clientes nombrados
- Egresos: `Inversiones de la Empresa / En Proyectos`, `Pagos de cuentas / CCSS`,
  `Pagos de cuentas / Agua, electricidad, telefonos`, `Salario`
- Estos nombres alimentan el matching histórico beneficiario→categoría del Reconciliador.
