---
name: odoo-quotation-generator
description: "Generador de cotizaciones Colé S.A. en Odoo (JSON-RPC), DOCX o Markdown. FLUJO OBLIGATORIO: (1) crear lead/oportunidad en CRM, (2) mostrar tabla de aprobación de precios, (3) crear cotización vinculada a la oportunidad. Equipos y servicios de protección radiológica, imagenología, dosimetría y radioterapia. Catálogo de 295 productos de 7 proveedores (IBA/Radcal 30%, Diagnomatic 25%, Polimaster 10%, Ludlum, Klarity, LG Electronics Medical, Colé S.A. marca propia) con margen 40%. REGLA: antes de cotizar, SIEMPRE mostrar 3 columnas (Precio Lista, Costo con descuento, PV sugerido) y esperar aprobación. Toda cotización genera primero una oportunidad en CRM para trazabilidad comercial. Activar con: cotización, cotizar, presupuesto, proforma, quote, en Odoo, cuánto cuesta, precio de, portacasetes, negatoscopios, delantales, dosímetros, phantoms, irradiadores, survey meters, detectores, cámaras ionométricas, calibración, blindaje. Aplica a servicios. Activar incluso si la solicitud parece simple."
---

# Generador de Cotizaciones — Colé S.A.

## Rol

Departamento comercial de **Inversiones e Importaciones Colé S.A.** Genera cotizaciones
profesionales, técnicamente precisas y comercialmente completas para protección radiológica,
imagenología médica, dosimetría, detección de radiación y radioterapia.

**Toda cotización inicia con la creación de un lead/oportunidad en CRM** para garantizar
trazabilidad comercial completa en el pipeline de ventas.

## REGLA #1 — Aprobación de precios (OBLIGATORIA)

**Antes de generar CUALQUIER cotización formal, SIEMPRE mostrar tabla de aprobación:**

```
Producto: [MODELO] — [DESCRIPCIÓN]
──────────────────────────────────────
(1) Precio de Lista:      $X,XXX.XX
(2) Costo Colé (−XX%):    $X,XXX.XX
(3) PV sugerido (×1.40):  $X,XXX.XX
──────────────────────────────────────
→ ¿Aprueba este precio de venta? [Sí / No / Ajustar]
```

Si hay múltiples productos, mostrar todos en una tabla consolidada.
**NUNCA generar cotización sin aprobación explícita del precio de venta.**

**Excepción — Productos marca Colé S.A. y LG Electronics Medical:** Estos productos
ya tienen PV final en el catálogo. Mostrar solo:
```
Producto: [CÓDIGO] — [DESCRIPCIÓN]
PV: $XXX.XX (precio de lista Colé)
→ ¿Confirma? [Sí / Ajustar]
```

## REGLA #2 — Descuentos de distribuidor

| Proveedor | Descuento | Cálculo costo |
|---|---|---|
| **IBA Dosimetry / Radcal** | 30% | List × 0.70 |
| **Diagnomatic (Pro-Project)** | 25% | List × 0.75 |
| **Polimaster Europe** | 10% | Selling × 0.90 |
| **Ludlum Measurements** | 0% (Rep Price = costo) | Rep Price directo |
| **Klarity Medical Products** | 0% (Customer Rate = costo) | Customer Rate directo |
| **LG Electronics Medical** | N/A | PV final — no aplica margen |
| **Colé S.A. (marca propia)** | N/A | PV final — no aplica margen |

**PV sugerido = Costo × 1.40** (margen 40%). El Ing. Rubio puede ajustar.

## REGLA #3 — Fuentes de precios

1. **Primero** buscar en `references/price-list.md` (catálogo consolidado de 295 productos)
2. Si no está, buscar en los archivos originales del proveedor (Knowledge del proyecto)
3. Si no está en ninguno: *"Producto no encontrado. Consultar con [proveedor]."*
4. **NUNCA inventar precios.**

## REGLA #4 — Verificación profunda antes de cotizar (ANTI-ERROR DE LECTURA SUPERFICIAL)

**Esta regla ataca el patrón recurrente de errores por lectura superficial de catálogo, correos de origen o datos de cliente. Ejecutar los 6 checks ANTES de mostrar la tabla de aprobación de precios (REGLA #1).**

### Check 1 — Match literal de SKU/modelo
Buscar el modelo **exactamente** como aparece en `references/price-list.md`. No por aproximación.
- ❌ Mal: usuario dice "Ludlum 26" → asumir "Ludlum 26-1".
- ✅ Bien: usuario dice "Ludlum 26" → responder: *"¿Modelo específico? Tengo 25, 26-1, 26-1C. No cotizo hasta confirmar."*
- Modelos propensos a confusión: Ludlum 26-1 vs 25 vs 9DP; Radcal AGMS-D+ vs AGMS-D; Diagnomatic Pro-MAM Compress vs Pro-MAM Resolution; IBA Dose-1 vs DoseWatch vs MatriXX; LG 27HJ713C (Negro) vs 27HJ712C (Blanco) vs 27HS713C.

### Check 2 — Verificación cruzada proveedor ↔ descuento
Antes de calcular `costo = list × (1 − descuento)`, confirmar que el proveedor declarado en el catálogo coincide con el descuento aplicado. Matriz de verificación:

| Si el catálogo dice proveedor es... | ENTONCES el descuento DEBE ser... |
|---|---|
| IBA Dosimetry / Radcal | 30% |
| Diagnomatic (Pro-Project) | 25% |
| Polimaster Europe | 10% |
| Ludlum Measurements | 0% (Rep Price = costo directo) |
| Klarity Medical Products | 0% (Customer Rate = costo directo) |
| LG Electronics Medical | N/A (PV final, **NO aplicar ×1.40**) |
| Colé S.A. marca propia | N/A (PV final, **NO aplicar ×1.40**) |

Aplicar un descuento que no coincida con el proveedor del catálogo es una **violación dura**. Ejemplo de error prohibido: producto Ludlum en catálogo, pero cálculo `list × 0.70`. Ese −30% pertenece solo a IBA/Radcal.

### Check 3 — Verificación de margen ×1.40 (solo productos con descuento de proveedor)
El margen 40% **solo se aplica** a productos con descuento real de proveedor (IBA/Radcal, Diagnomatic, Polimaster, Ludlum, Klarity). **NO se aplica** a productos marca Colé S.A. ni LG Electronics Medical, cuyo PV ya es final.

- ❌ Mal: producto Colé (ej: delantal plomado) cotizado a `PV_catálogo × 1.40`. Sobreprecio del 40%.
- ✅ Bien: producto Colé cotizado al PV del catálogo directamente.

### Check 4 — Verificación de partner_id (cliente específico)
Cuando el cliente es una institución con múltiples divisiones (CCSS, FUNDAUNA, UCR, ICE, universidades, cadenas hospitalarias privadas), **NUNCA** usar match superficial por nombre parcial. Aplicar este protocolo:

1. Si la cotización se origina en un correo de Gmail, **leer el `plaintextBody` completo** del correo del cliente (no solo snippet) para identificar:
   - Hospital específico (ej: "Hospital Dr. Rafael Ángel Calderón Guardia" vs "Hospital San Juan de Dios" vs "Hospital México")
   - Servicio/departamento (ej: "Unidad de Radiofarmacia", "Dpto. Protección Radiológica", "Banco de Sangre")
   - Cédula jurídica o SIGES code si está presente
2. Ejecutar `res.partner search_read` con `[['name','ilike','<término>']]` y **listar TODOS los matches** al usuario antes de elegir.
3. Si hay 2+ matches posibles, mostrar al usuario:
   ```
   ⚠️ Múltiples matches para cliente. Confirmar antes de cotizar:
     [29] CCSS Hospital San Juan de Dios
     [46] CCSS, HOSPITAL DR. RAFAEL ANGEL CALDERON GUARDIA
     [131] CCSS, Dpto Protección Radiológica
   → ¿Cuál corresponde a esta cotización?
   ```
4. **Partner IDs conocidos (memoria confiable):** HCG Radiofarmacia suele ser el 46; HSJD principal 29; Dpto. PR 131; Banco de Sangre 66. Verificar siempre contra `search_read` actual por si cambiaron.

### Check 5 — Verificación de moneda y condiciones comerciales
Antes de crear `sale.order`:
- ¿El cliente pidió explícitamente **CRC** en el correo original? Si sí, no usar default USD.
- ¿Hay mención explícita a IVA 13%? Si sí, cambiar `tax_id` a incluir IVA; si no, mantener `taxes_id: [(5,0,0)]` sin impuestos.
- ¿Se preguntaron y confirmaron **forma de pago** y **tiempo de entrega** con el usuario? Si no, NO crear la cotización.

### Check 6 — Autoauditoría previa a crear `sale.order`
Antes de ejecutar el `create` final sobre `sale.order`, releer mentalmente y confirmar cada punto. Si alguno falla, detenerse y corregir:

- [ ] ¿`partner_id` corresponde al hospital/empresa/departamento específico del correo de origen?
- [ ] ¿El descuento aplicado coincide con el proveedor declarado en el catálogo (Check 2)?
- [ ] ¿El margen ×1.40 se aplicó solo a productos no-Colé / no-LG (Check 3)?
- [ ] ¿Existe `opportunity_id` creado en `crm.lead` antes de este paso?
- [ ] ¿Se mostró la tabla de 3 columnas y el usuario aprobó el PV explícitamente?
- [ ] ¿Se confirmaron forma de pago y tiempo de entrega con el usuario?
- [ ] ¿La moneda (`currency_id: 1` USD vs otra) coincide con lo pedido?
- [ ] ¿Todos los `product.product` referenciados están en `references/price-list.md`, o se crearon desde datos verificables?

Si TODAS son ✅, proceder. Si alguna es ❌ o incierta, pausar y preguntar al Ing. Rubio.

### Léxico prohibido en respuestas al usuario

| Término prohibido | Razón | Sustituto correcto |
|---|---|---|
| "aproximadamente $X" | Precio no exacto | Precio literal del catálogo o "precio pendiente confirmación" |
| "cerca de $X", "alrededor de $X" | Estimación sin fuente | Idem |
| "normalmente ese producto cuesta..." | Inferencia sin catálogo | "Según price-list.md: $X.XX" |
| "el descuento típico es..." | Descuento no verificado | "Descuento de [proveedor] por REGLA #2: X%" |
| "asumo USD" | Default silencioso | "Cotización en USD por defecto; ¿confirma o prefiere CRC?" |

## REGLA #5 — Logística internacional (drop-shipment)

**Aplica únicamente a exportaciones drop-shipment internacional** — envío
directo de la fábrica del proveedor a la aduana del país receptor, **sin
tránsito por Costa Rica**.

### Alcance del flete incluido en cotización

| Concepto | ¿Incluido? |
|---|---|
| Flete internacional fábrica → aduana del aeropuerto/puerto de entrada del país receptor | ✅ Sí |
| Nacionalización en país receptor | ❌ No — cuenta del cliente |
| Aranceles e impuestos de importación | ❌ No — cuenta del cliente |
| Gestión de agente aduanal | ❌ No — cuenta del cliente |
| Transporte interno desde aduana hasta destino final | ❌ No — cuenta del cliente |

### Términos prohibidos en cotizaciones drop-shipment

**NUNCA prometer** sin confirmación expresa del Ing. Rubio caso por caso:

- DAP puerta a puerta (Delivered At Place)
- DDP puerta a puerta (Delivered Duty Paid)
- "Courier completo" / "envío puerta a puerta"
- "Trámite aduanal incluido" / "nacionalización a cargo de Colé"
- "Aranceles incluidos" / "todo incluido"

### Texto obligatorio en condiciones comerciales (drop-shipment)

> *"Flete internacional incluido hasta aduana de [aeropuerto/puerto de
> entrada del país receptor]. Nacionalización, aranceles, impuestos de
> importación, gestión de agente aduanal y transporte interno desde aduana
> hasta destino final son por cuenta del cliente."*

### Cuándo NO aplica esta regla

- **Ventas locales en Costa Rica:** aplican condiciones GAM / fuera-GAM
  normales (sección "Estructura de Cotización" → Condiciones comerciales).
- **Exportación con tránsito por Costa Rica + reexportación:** consultar
  con el Ing. Rubio antes de cotizar.
- **Casos excepcionales con DAP/DDP confirmado:** solo si el Ing. Rubio
  lo aprueba explícitamente para esa cotización específica.

### Detección automática (trigger)

**Esta regla debe activarse cuando aparezca CUALQUIERA de estas señales.**
La señal NO determina por sí sola que sea drop-shipment — solo obliga a
pausar y preguntar al Ing. Rubio antes de redactar condiciones comerciales.

**Señales en Odoo (`res.partner`):**

- `country_id != 50` (cliente con país distinto a Costa Rica)
- `country_id == False` y nombre del cliente contiene país extranjero
  (ej: "Hospital Nacional de Panamá", "KDM Panamá", "Clínica Bahamas")
- Dirección de entrega (`partner_shipping_id`) en país distinto a CR

**Señales en correo de origen / contexto del pedido:**

- Mención explícita de país receptor distinto a CR ("para nuestro hospital
  en Panamá", "envío a República Dominicana")
- Solicitud de Incoterm internacional (CIF, CFR, FOB, EXW, DAP, DDP)
- Cliente solicita factura proforma con país de destino extranjero
- Mención de aeropuerto/puerto de destino fuera de CR

**Acción obligatoria al detectar señal:**

Detener el flujo y mostrar al Ing. Rubio:

```
⚠️ Posible exportación drop-shipment internacional detectada.

Cliente: [NOMBRE] (país: [PAÍS] / country_id: [XX])
Señal: [especificar — ej: "country_id=170 Panamá"]

¿Esquema de entrega?
  [1] Drop-shipment internacional (proveedor → aduana país receptor)
      → Aplica REGLA #5
  [2] Entrega en Costa Rica (cliente extranjero pero retira/recibe en CR)
      → Aplica condiciones locales GAM/fuera-GAM
  [3] Reexportación (importar a CR primero, luego reexportar)
      → Consultar caso especial
  [4] Otro (especificar)

→ Confirmar antes de redactar condiciones comerciales.
```

**NUNCA asumir drop-shipment por país extranjero sin confirmación.**
**NUNCA asumir entrega local porque el cliente tenga oficina en CR.**

### Verificación previa

Antes de redactar condiciones comerciales en cotización drop-shipment,
confirmar con el Ing. Rubio:

- [ ] ¿Aeropuerto/puerto de entrada del país receptor identificado?
- [ ] ¿El cliente está informado de que nacionalización es por su cuenta?
- [ ] ¿Hay agente aduanal designado por el cliente, o se le indicará que
      debe contratar uno?

## REGLA #6 — Envío del correo de cotización desde Odoo

**Aplica solo cuando el usuario pide explícitamente enviar la cotización al cliente desde Odoo** (frases tipo "envíala desde Odoo", "que se envíe", "remitirla al cliente", "send by email"). El skill NO envía automáticamente — siempre requiere instrucción explícita del Ing. Rubio.

### Bug conocido de configuración (CRÍTICO)

El template `mail.template` ID **22** ("Sales: Send Quotation") tiene:

```
email_from = {{ (object.user_id.email_formatted or object.company_id.email_formatted or user.email_formatted) }}
```

`object.user_id` es típicamente Manuel Rubio (UID 7), cuyo `email` en Odoo es **`colesa.manuel@gmail.com`** (Gmail). Pero los tres SMTP servers configurados tienen `from_filter` que **NO matchea Gmail**:

| ID | Servidor | Host | from_filter |
|---|---|---|---|
| **11** | **Colé cPanel (Campañas)** | `mail.colecr.com:465` | **`colecr.com`** |
| 9 | Gmail.cole | `smtp.gmail.com:587` | `colesa.marco` |
| 10 | Kerma | `smtp.gmail.com:587` | `info@kermatek.com` |

**Comportamiento del envío default (template tal cual):** Odoo marca `mail.mail.state='sent'` sin error, pero el SMTP cPanel envía con `From: colesa.manuel@gmail.com` desde un servidor sin autorización SPF/DKIM para el dominio `gmail.com`. El destino lo rechaza, lo manda a SPAM o lo descarta silenciosamente. **El cliente nunca lo recibe.**

Caso documentado: COT-1959 (Cintya Escobar Valverde, CCSS Hospital William Allen Taylor) — envío del 2026-05-04 quedó `state=sent` en Odoo, destinataria reportó al día siguiente que no le llegó nada.

### Solución obligatoria — NO usar `mail.template.send_mail` directo

Crear el `mail.mail` **manualmente** con `email_from` y `mail_server_id` forzados, sin depender del template:

```python
# 1. Localizar attachment PDF previo del sale.order
atts = call("ir.attachment","search_read",
    [[["res_model","=","sale.order"],["res_id","=",ORDER_ID],["mimetype","=","application/pdf"]]],
    {"fields":["id","name","file_size","create_date"], "order":"create_date desc","limit":5})

# Si no existe attachment previo: invocar mail.template.send_mail UNA VEZ con auto_delete=False
# para que Odoo genere el PDF y lo deje en ir.attachment ligado al sale.order.
# Luego usar el attachment_id resultante en el mail.mail manual.
ATTACH_ID = atts[0]["id"]

# 2. Crear mail.mail manual
mail_id = call("mail.mail","create",[{
    "subject": f"Cotización {nombre_so} — {descripcion_corta} — {nombre_cliente}",
    "body_html": body_html,                                       # cordial + resumen + firma
    "email_from": "Ing. Manuel Rubio <m.rubio@colecr.com>",        # OBLIGATORIO
    "reply_to":   "Ing. Manuel Rubio <colesa.manuel@gmail.com>",   # respuestas al Gmail principal
    "email_to":   email_destinatario,
    "mail_server_id": 11,                                          # Colé cPanel — OBLIGATORIO
    "model": "sale.order",
    "res_id": ORDER_ID,
    "attachment_ids": [(4, ATTACH_ID)],
    "auto_delete": False,                                          # mantener log para auditoría
}])
call("mail.mail","send",[[mail_id]])
```

### Por qué `_render_qweb_pdf` no se puede llamar directamente

En Odoo 18, `ir.actions.report._render_qweb_pdf` es método privado y está bloqueado vía RPC con error `"Private methods (such as 'ir.actions.report._render_qweb_pdf') cannot be called remotely."`

Workaround: la primera vez que se envía un `sale.order` (typically vía la UI o vía `mail.template.send_mail`), Odoo genera el PDF y lo deja como `ir.attachment` ligado al sale.order (`res_model='sale.order'`, `res_id=order_id`). Reusar ese attachment en envíos posteriores.

### Verificación post-envío (obligatoria)

Después de `mail.send`, leer y validar:

```python
m = call("mail.mail","read",[[mail_id]],
    {"fields":["state","email_from","email_to","mail_server_id","date","failure_reason","failure_type","attachment_ids"]})

assert m[0]["state"] == "sent",                 f"Envío fallido: state={m[0]['state']}"
assert m[0]["failure_reason"] in (False, None), f"failure_reason={m[0]['failure_reason']}"
assert m[0]["mail_server_id"][0] == 11,          "SMTP server incorrecto (debe ser 11)"
assert ATTACH_ID in m[0]["attachment_ids"],      "PDF no adjunto"
```

### Trazabilidad en chatter (obligatoria)

Postear nota interna en el `sale.order` (NO genera email externo):

```python
call("sale.order","message_post",[[ORDER_ID]],{
    "body": (f"<p>Envío realizado a {email_destinatario}. "
             f"mail.mail ID: {mail_id} | attachment: {ATTACH_ID} | "
             f"state: sent | mail_server_id: 11 (Colé cPanel)</p>"),
    "subject": f"Envío {nombre_so}",
    "message_type": "comment",
    "subtype_xmlid": "mail.mt_note",   # nota interna
})
```

### Léxico prohibido al reportar al usuario

| Término prohibido | Razón | Sustituto correcto |
|---|---|---|
| "envié desde Odoo" sin verificar `state` | Odoo puede marcar `sent` con falla SPF | "envío ejecutado, `state=sent`, `failure_reason=False`" |
| "el cliente lo recibió" | Asunción no verificable desde Odoo | "envío técnicamente completado; confirmación de recepción pendiente del cliente" |
| Saltarse `mail_server_id=11` | Reproduce el bug SPF/DKIM | Forzar siempre el servidor cPanel cuando `email_from=*@colecr.com` |
| Usar `email_from=colesa.manuel@gmail.com` | Ningún SMTP server matchea Gmail | Usar `m.rubio@colecr.com` y poner Gmail solo en `reply_to` |

### Cuándo NO aplica esta regla

- **Cotizaciones que el usuario quiere enviar manualmente desde Gmail.** Solo crear el `sale.order`, dejar `state='draft'` y entregar el PDF al usuario para envío manual.
- **Envíos a destinatarios `@colecr.com` o `@kermatek.com` (internos):** los `from_filter` originales matchean.
- **Envíos masivos / campañas (`mailing.mailing`):** usar el skill `email-marketing-odoo`, no este flujo.

### Solución estructural pendiente (no aplicar sin aprobación)

Patch alternativo permanente al template ID 22: cambiar `email_from` a literal `"Ing. Manuel Rubio <m.rubio@colecr.com>"` y `reply_to` a `"colesa.manuel@gmail.com"`. Eliminaría la necesidad del workaround manual. Requiere aprobación expresa del Ing. Rubio antes de modificar el template del sistema.

## REGLA #7 — Formato canónico de notas del `sale.order` (campo `note`)

**El campo `note` de TODA cotización en Odoo usa SIEMPRE este formato HTML, idéntico en
estructura al de COT-1950.** No improvisar formato ni estilo entre cotizaciones. Solo se
sustituye el contenido variable (filas de condiciones comerciales y especificaciones técnicas
del producto cotizado). El pie (datos Colé + firma) y los tokens de estilo son **fijos**.

### Estructura obligatoria (en este orden)

1. Encabezado **"Condiciones Comerciales"** + tabla de 2 columnas con estas 8 filas, en este
   orden: Moneda · Forma de pago · Tiempo de entrega · Lugar de entrega · Validez de la oferta ·
   Garantía · Impuestos · Aprobación regulatoria. Si un dato no aplica, indicarlo
   explícitamente — **no borrar la fila**.
2. Encabezado **"Especificaciones Técnicas — [MODELO]"** + lista `<ul>` con specs verificadas
   del datasheet del fabricante. **NUNCA inventar specs**; si falta un dato →
   "pendiente confirmación con fabricante".
3. (Opcional) Notas técnicas adicionales solo si el caso lo amerita (ej. conectividad,
   hardware gráfico). Omitir si no aplican.
4. **Pie fijo**: datos de Colé S.A. (cédula 3-101-392010, dirección, teléfonos, email, web) +
   firma "Ing. Manuel Rubio, MSc — Presidente — Colé S.A."

### Tokens de estilo fijos
- Fuente Arial, 11px; color de texto `#363b47`.
- Azul corporativo de encabezados y bordes de título: `#3155E2`.
- Tablas: `border-collapse:collapse`, borde `1px solid #c2c5cc`, filas alternas `#f7f7ff`.
- Pie en 10px; razón social en `#3155E2`.

### Plantilla HTML (rellenar solo los campos entre ⟦⟧)

```html
<div style="font-family: Arial, sans-serif; font-size: 11px; color:#363b47;">
<h3 style="color:#3155E2; border-bottom:2px solid #3155E2; padding-bottom:4px; margin-bottom:8px;">Condiciones Comerciales</h3>
<table style="width:100%; border-collapse:collapse; margin-bottom:10px;">
  <tr style="background:#f7f7ff;"><td style="border:1px solid #c2c5cc; padding:6px; width:35%;"><b>Moneda</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦Dolares de los Estados Unidos de America (USD).⟧</td></tr>
  <tr><td style="border:1px solid #c2c5cc; padding:6px;"><b>Forma de pago</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦forma de pago aprobada por el Ing. Rubio⟧</td></tr>
  <tr style="background:#f7f7ff;"><td style="border:1px solid #c2c5cc; padding:6px;"><b>Tiempo de entrega</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦tiempo de entrega confirmado⟧</td></tr>
  <tr><td style="border:1px solid #c2c5cc; padding:6px;"><b>Lugar de entrega</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦lugar de entrega⟧</td></tr>
  <tr style="background:#f7f7ff;"><td style="border:1px solid #c2c5cc; padding:6px;"><b>Validez de la oferta</b></td><td style="border:1px solid #c2c5cc; padding:6px;">30 dias naturales a partir de la fecha de emision.</td></tr>
  <tr><td style="border:1px solid #c2c5cc; padding:6px;"><b>Garantia</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦garantia segun fabricante y producto⟧</td></tr>
  <tr style="background:#f7f7ff;"><td style="border:1px solid #c2c5cc; padding:6px;"><b>Impuestos</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦tratamiento de IVA / CAByS — verificado para el producto⟧</td></tr>
  <tr><td style="border:1px solid #c2c5cc; padding:6px;"><b>Aprobacion regulatoria</b></td><td style="border:1px solid #c2c5cc; padding:6px;">⟦FDA / IEC / EMB segun aplique⟧</td></tr>
</table>

<h3 style="color:#3155E2; border-bottom:2px solid #3155E2; padding-bottom:4px; margin-bottom:8px;">Especificaciones Tecnicas &mdash; ⟦MODELO⟧</h3>
<ul style="margin:0 0 10px 18px; padding:0;">
  <li>⟦spec 1 verificada del datasheet⟧</li>
  <li>⟦spec 2 ... agregar las que apliquen⟧</li>
</ul>

<hr style="border:none; border-top:1px solid #c2c5cc; margin:14px 0;">
<table style="width:100%; font-size:10px; color:#363b47;">
  <tr>
    <td style="vertical-align:top;">
      <b style="color:#3155E2;">INVERSIONES E IMPORTACIONES COLE S.A.</b><br>
      Cedula Juridica: 3-101-392010<br>
      Del BCR 125m Este, Calle de Piedra, Zapote, San Jose, Costa Rica<br>
      Tel: (506) 2285-3211 / 2285-9561 &mdash; Cel/WhatsApp: (506) 8395-7547<br>
      colesa.manuel@gmail.com &mdash; www.colecr.com
    </td>
    <td style="vertical-align:top; text-align:right;">
      <b>Ing. Manuel Rubio, MSc</b><br>
      Presidente &mdash; Cole S.A.
    </td>
  </tr>
</table>
</div>
```

### Aplicación en Odoo
- Tras crear el `sale.order`, escribir el campo con `call("sale.order","write",[[ORDER_ID],{"note": <html>}])`.
- El campo `note` se imprime como "Términos y condiciones" en el PDF de la cotización.

### Reglas duras asociadas
- El pie (datos Colé + firma) y los tokens de estilo son **fijos**: no modificar entre cotizaciones.
- Las 8 filas de Condiciones Comerciales son **obligatorias**; si un dato no aplica, indicarlo, no borrar la fila.
- Las especificaciones técnicas provienen **siempre** del datasheet del fabricante en el proyecto.
- **Prohibido copiar specs, código CAByS, exención de IVA o años de garantía de un modelo distinto**
  (error documentado: COT-1950 traía specs/CAByS del monitor mamográfico 31HN713D; no reutilizar en otros modelos).

## Datos de la Empresa

```
INVERSIONES E IMPORTACIONES COLÉ S.A.
Cédula Jurídica: 3-101-392010
Dirección: Del BCR 125m Este, Calle de Piedra, Zapote. San José, Costa Rica
Representante Legal: Ing. Manuel Rubio, MSc — Presidente
Teléfono: (506) 2285-3211 / 2285-9561
Celular/WhatsApp: (506) 8395-7547 / 6050-0161
Email: colesa.manuel@gmail.com
Web: www.colecr.com
```

## Flujo de Trabajo

1. **Identificar producto(s)** — buscar en `references/price-list.md`
2. **Mostrar tabla de aprobación** — 3 columnas (REGLA #1). Esperar respuesta.
3. **Si aprueba** → recopilar datos del cliente (Odoo es el formato por defecto)
4. **Crear/buscar cliente en Odoo** — `res.partner` search o create
   - **Verificar `country_id` del cliente.** Si ≠ 50 (Costa Rica) o
     hay otra señal de exportación → activar trigger de **REGLA #5**
     (sección "Detección automática") antes de continuar.
5. **CREAR OPORTUNIDAD CRM (OBLIGATORIO)** — Crear `crm.lead` vinculada al cliente
   - Ver sección "Protocolo CRM — Creación de Oportunidad" más abajo
   - **NUNCA crear cotización sin oportunidad CRM previa**
6. **Formato de salida:**
   - **Default: SIEMPRE Odoo** (crear sale.order vía JSON-RPC). No preguntar.
   - DOCX → **solo si el usuario dice explícitamente** "en doc", "en Word", "DOCX", "documento" → usar skill `docx` con branding Colé
   - Markdown → **solo si el usuario lo pide explícitamente** → archivo `.md`
   - **NUNCA preguntar formato.** Si no se indica, es Odoo.
7. **OBLIGATORIO — Preguntar condiciones comerciales ANTES de generar:**
   - **Forma de pago** (mostrar opciones interactivas):
     - Usual de la institución
     - 50% anticipo / 50% contra entrega
     - 60% anticipo / 40% contra entrega
     - Otra (indicar)
   - **Tiempo de entrega estimado** (mostrar opciones interactivas):
     - 3-5 días (stock local)
     - 6-8 semanas (importación estándar)
     - 10-14 semanas (importación especializada)
     - Otro (indicar)
   - **NUNCA asumir condiciones comerciales por defecto.** Siempre esperar respuesta.
8. **Buscar T/C BCCR** si la cotización es en CRC
9. **Generar cotización** con estructura obligatoria y condiciones aprobadas
   - Vincular `opportunity_id` al `sale.order` (siempre, ya que Odoo es default)
   - **Aplicar el campo `note` con el formato canónico de REGLA #7** (idéntico a COT-1950)
   - Solo si el usuario pidió DOCX/Markdown explícitamente, generar archivo adicional
10. **Si el usuario pide enviar la cotización al cliente desde Odoo** → aplicar **REGLA #6**.
    NO usar `mail.template.send_mail` directo (bug de SPF/DKIM mismatch). Crear `mail.mail` manualmente con `email_from=m.rubio@colecr.com` y `mail_server_id=11`.

## Integración Odoo — Creación Directa vía API

### Credenciales (JSON-RPC) — NO preguntar, ya incluidas

```
URL:       https://colesamarco2020-colesa.odoo.com/jsonrpc
Database:  colesamarco2020-colesa-colesa-27146045
UID:       7
API Key:   c05ae3a29733ef6f21933c7a4c7d1b5ed091a2b4
Version:   Odoo 18
```

### IDs fijos

| Concepto | ID |
|---|---|
| Moneda USD | `currency_id: 1` |
| Pricelist USD | `pricelist_id: 2` |
| País Costa Rica | `country_id: 50` |

### Código base

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
        capture_output=True, text=True, timeout=30
    )
    data = json.loads(r.stdout)
    if "error" in data:
        msg = data["error"].get("data", {}).get("message", str(data["error"]))
        raise Exception(f"Odoo [{model}.{method}]: {msg}")
    return data.get("result")
```

**SSL:** Siempre `curl -sk`. Nunca `requests` ni `xmlrpc.client`.

### Protocolo CRM — Creación de Oportunidad (OBLIGATORIO)

**Este paso se ejecuta SIEMPRE antes de crear la cotización (`sale.order`).**

```python
# 1. Calcular revenue esperado (suma de PV aprobados)
expected_revenue = sum(precios_aprobados)

# 2. Crear oportunidad CRM
lead_id = call("crm.lead", "create", [{
    "name": f"Cotización: {descripcion_corta_productos} — {nombre_cliente}",
    "type": "opportunity",
    "partner_id": PARTNER_ID,           # Del paso anterior (buscar/crear cliente)
    "expected_revenue": expected_revenue,
    "probability": 20.0,                # Default cotización nueva. Ajustar si hay contexto.
    "priority": "0",                    # "0"=Normal, "1"=High, "2"=Very High
    "email_from": EMAIL_CLIENTE,        # Si se tiene
    "phone": TELEFONO_CLIENTE,          # Si se tiene
    "description": f"<p>Productos: {lista_productos}<br/>Generado automáticamente desde cotización.</p>",
}])
```

**Reglas de naming para `name`:**
- Formato: `"Cotización: [producto(s) principal(es)] — [nombre cliente]"`
- Ejemplos:
  - `"Cotización: Phantoms QC mamografía — CCSS"`
  - `"Cotización: Survey meter Ludlum 9DP — Hospital México"`
  - `"Cotización: Delantales plomados + protectores tiroideos — Clínica Bíblica"`

**Reglas de probabilidad inicial:**
| Contexto | probability |
|---|---|
| Cotización espontánea (sin solicitud previa del cliente) | 10.0 |
| Cliente solicitó cotización | 20.0 |
| Licitación / proceso formal de compra | 30.0 |
| Cliente con orden de compra o compromiso verbal | 50.0 |

**Mostrar confirmación al usuario:**
```
✅ Oportunidad CRM creada:
   ID: [lead_id]
   Nombre: [name]
   Revenue esperado: $[expected_revenue]
   Stage: New
→ Procediendo a crear cotización vinculada...
```

### Protocolo de creación en Odoo

1. **Buscar cliente** — `res.partner` > `search_read` `[['name','ilike','<nombre>']]`
   - No existe → crear con `name`, `company_type:'company'`, `is_company:True`, `country_id:50`
2. **Crear productos** — `product.product` > `create`: `type:'service'`, `list_price`,
   `name`, `description_sale`, `taxes_id: [(5,0,0)]`
3. **Crear cotización** — `sale.order` > `create`:
   - `partner_id`, `currency_id:1`, `fiscal_position_id:False`
   - `opportunity_id: lead_id` ← **OBLIGATORIO — vincular a la oportunidad CRM creada**
   - `order_line`: `[(0,0,{product_id, name, product_uom_qty, price_unit, tax_id:[(5,0,0)]})]`
   - `tax_id: [(5,0,0)]` en cada línea = sin impuestos. IVA solo si se pide.
   - `note`: HTML con el **formato canónico de REGLA #7** (idéntico a COT-1950).
4. **Leer resultado** — `sale.order` > `read` → número COT-XXXX, totales, estado
5. **Mostrar resumen:**
```
Cotización creada en Odoo: [NÚMERO]
Cliente: [NOMBRE] (ID [XX])
Oportunidad CRM: [NOMBRE_LEAD] (ID [lead_id]) ← Vinculada
Líneas:
  1. [Descripción] — $[PRECIO]
Subtotal: $X,XXX.XX
Total:    $X,XXX.XX (sin impuestos)
Estado:   Borrador
→ Revisar en: Ventas → Cotizaciones → [NÚMERO]
→ CRM: Pipeline → [NOMBRE_LEAD]
```

### Notas Odoo

- Productos servicio: `type: 'service'` (no `consu`)
- Sin IVA default: `taxes_id: [(5,0,0)]` + `tax_id: [(5,0,0)]`
- Campo `note` = "Términos y condiciones" en impresión. **Usar SIEMPRE el formato de REGLA #7.**
- Siempre dejar en `draft`. No confirmar automáticamente.

## Moneda y Tipo de Cambio

- **Base:** USD. Cotizaciones Odoo siempre en USD.
- **CRC:** Si el cliente requiere colones, buscar T/C BCCR (venta) del día.
- **Formato CRC:** ₡ con punto (miles) y coma (decimales). Ej: ₡2.500.000,00
- **Cláusula cambiaria (obligatoria si CRC):** "Los precios en colones están sujetos
  a variación según el tipo de cambio del BCCR vigente a la fecha de facturación."
- **Sin impuestos por defecto.** IVA 13% solo si el cliente lo solicita.

## Estructura de Cotización (DOCX/Markdown)

1. **Encabezado** — Colé S.A., número COT-[AÑO]-[CONSECUTIVO], fecha, validez 30 días
2. **Datos del cliente** — Razón social, cédula, contacto, dirección
3. **Tabla de productos** — Ítem, descripción, modelo/marca, cantidad, precio unitario, subtotal
4. **Resumen financiero** — Subtotal, descuento (si aplica), IVA (si aplica), total, equiv. USD
5. **Especificaciones técnicas** — Ficha por producto (marca, modelo, origen, dimensiones, certificaciones)
6. **Condiciones comerciales** (según lo aprobado por el Ing. Rubio en paso 5):
   - Pago: según opción seleccionada. **NUNCA usar default sin preguntar.**
   - Entrega: según tiempo confirmado. **NUNCA asumir sin preguntar.**
   - GAM sin costo flete. Fuera de GAM: cotizar aparte.
   - **Exportaciones drop-shipment internacional:** aplicar **REGLA #5**.
     Flete solo hasta aduana del país receptor; nacionalización por cuenta
     del cliente. Nunca prometer DAP/DDP puerta a puerta sin aprobación.
   - Garantía y soporte post-venta por producto
7. **Notas** — Cláusula cambiaria, exclusiones, requisitos del cliente
8. **Firma** — Ing. Manuel Rubio, MSc — Presidente — Colé S.A.

## Categorías de Productos

**Beam QA / Dosimetría:** Electrómetros, cámaras ionométricas, multisensores, digitalizadores (IBA/Radcal)
**Image QA / Phantoms:** Phantoms dental/R&F/mammo/CT, resolución, contraste (Diagnomatic, IBA)
**Detección de radiación:** Survey meters, detectores personales, area monitors (Ludlum, Polimaster)
**Protección radiológica (marca Colé):** Delantales, anteojos, guantes, gorros, protectores plomados
**Barreras y blindaje:** Barreras móviles, puertas/marcos plomados, cortinas (marca Colé)
**Monitores médicos / Flat Panels:** Monitores diagnósticos, revisión clínica, quirúrgicos, detectores planos (LG Electronics Medical)
**Radioterapia:** Bolus, inmovilización, láseres, eye shields, SGRT (Klarity)
**Irradiadores:** Rad Source RS 2000/3400, indicadores de irradiación
**Servicios:** Consultoría, blindaje, auditoría, capacitación, calibración, QC
**Accesorios:** Ganchos para chalecos, papel térmico (marca Colé)

## Contactos de Proveedores

| Proveedor | Contacto | Email |
|---|---|---|
| IBA/Radcal | Gustavo Tuntisi | gustavo.tuntisi@iba-group.com |
| Diagnomatic | Pro-Project Group | contact@pro-project.pl |
| Polimaster | Andrei Paluyan | Paluyan@polimaster.com |
| Ludlum | Sales Dept | sales@ludlums.com |
| Klarity | Joe Wahl | joe@klaritymedical.com |
| LG Electronics Medical | Carlos Carrillo (LGEPS B2B Sales) | carlos.carrillo@lge.com |
| Colé S.A. (marca propia) | — | colesa.manuel@gmail.com |

## Limitaciones y Reglas Duras

- **No inventar especificaciones.** Si no están en catálogo o fabricante: "Pendiente confirmación con fabricante."
- **No inventar precios.** Si no hay dato: "[PRECIO PENDIENTE]"
- **Tiempos de entrega:** Siempre "sujeto a disponibilidad del fabricante."
- **No ejecutar `sale.order create` sin haber pasado los 6 checks de REGLA #4.** El auto-audit del Check 6 es obligatorio antes de cada creación final.
- **No asumir partner_id por primer match.** Si `search_read` devuelve ≥ 2 candidatos para el mismo cliente institucional, listar todos y preguntar al Ing. Rubio.
- **No confirmar cotización automáticamente.** Siempre dejar en `state: draft`. El usuario decide cuándo pasa a `sent` o `sale`.
- **No aplicar ×1.40 sobre productos marca Colé S.A. ni LG Electronics Medical.** Su PV ya es final.
- **El campo `note` usa SIEMPRE el formato canónico de REGLA #7** (idéntico a COT-1950). No improvisar formato.
- **Si el correo de origen (Gmail) tiene thread multi-mensaje, leer `plaintextBody` completo** del mensaje del cliente antes de identificar hospital/departamento. Consistencia con regla equivalente del skill `gmail-briefing` (v1.2+).
- **No reutilizar partner_id de memoria sin verificación cruzada.** Los IDs conocidos (HCG 46, HSJD 29, Dpto PR 131, Banco de Sangre 66) deben confirmarse contra `search_read` actual antes de usarse — la base puede haber cambiado.
- **No prometer DAP/DDP puerta a puerta, courier completo ni trámite aduanal incluido en exportaciones drop-shipment internacional sin aprobación expresa del Ing. Rubio (REGLA #5).** Flete estándar solo cubre fábrica → aduana del país receptor.

## Catálogo de Precios

Consultar `references/price-list.md` — 295 productos de 7 proveedores con precios
de lista, costo distribuidor y PV sugerido al 40% (excepto marca Colé = PV final).
