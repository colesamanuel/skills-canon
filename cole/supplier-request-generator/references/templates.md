# Plantillas de Solicitud — Colé S.A. a Proveedores

Cada plantilla define asunto, estructura de cuerpo y fórmulas clave para cada tipo
de solicitud. Completar los campos `[ENTRE_CORCHETES]` con los datos extraídos.

---

## CAL — Solicitud de Calibración

**Asunto:**
```
Solicitud de Servicio de Calibración — [MARCA] [MODELO] — Colé S.A. / [FECHA]
```
Si urgente (CalDue vencida):
```
[URGENTE] Solicitud de Calibración — Equipo(s) con Trazabilidad Vencida — Colé S.A.
```

**Cuerpo:**
```
Estimado(a) [NOMBRE_CONTACTO / equipo de servicio técnico]:

Por medio de la presente, Inversiones e Importaciones Colé S.A. solicita formalmente
el servicio de calibración para los equipos indicados en la tabla adjunta, los cuales
forman parte de nuestro inventario activo de dosimetría en [país/región: Costa Rica].

[TABLA_EQUIPOS]

Solicitamos que la calibración se realice bajo trazabilidad a patrones nacionales o
internacionales (NIST o equivalente), con emisión del certificado de calibración
correspondiente que indique: fecha de calibración, fecha de vencimiento, factores
de corrección aplicados y número de reporte.

[SI APLICA: "El equipo con S/N [XX] presenta calibración vencida desde [FECHA], 
por lo que la atención tiene carácter prioritario."]

Favor confirmar: (1) disponibilidad de agenda, (2) tiempo estimado de turnaround,
(3) costo del servicio, y (4) instrucciones para envío o visita técnica.

[FIRMA]
```

---

## MNT — Solicitud de Mantenimiento Preventivo / Correctivo

**Asunto:**
```
Solicitud de Mantenimiento [Preventivo / Correctivo] — [MARCA] [MODELO] — Colé S.A.
```

**Cuerpo:**
```
Estimado(a) [NOMBRE_CONTACTO]:

Colé S.A. solicita el servicio de mantenimiento [preventivo / correctivo] para los
equipos detallados a continuación:

[TABLA_EQUIPOS]

[SI CORRECTIVO: "Los equipos presentan las siguientes anomalías operativas: [DESCRIPCIÓN]."]

Solicitamos cotización del servicio, incluyendo mano de obra, repuestos (si aplica)
y tiempo estimado de intervención. Indicar si el servicio requiere traslado del equipo
o puede realizarse en sitio (San José, Costa Rica).

[FIRMA]
```

---

## COT — Solicitud de Cotización

**Asunto:**
```
Solicitud de Cotización — [PRODUCTO/SERVICIO] — Colé S.A. / [FECHA]
```

**Cuerpo:**
```
Estimado(a) [NOMBRE_CONTACTO]:

Inversiones e Importaciones Colé S.A., con cédula jurídica 3-101-392010, solicita
cotización formal para los siguientes productos / servicios:

[TABLA_EQUIPOS o LISTA_DE_ÍTEMS]

Requerimos que la cotización incluya: precio unitario, descuento por volumen (si aplica),
tiempo de entrega, condiciones de garantía y términos de pago (CIF San José, Costa Rica).

Somos distribuidores autorizados en Centroamérica. Favor indicar precio de lista y
precio de distribuidor por separado.

[FIRMA]
```

---

## RMA — Reporte de Falla / Return Merchandise Authorization

**Asunto:**
```
Reporte de Falla y Solicitud de RMA — [MARCA] [MODELO] S/N [SERIAL] — Colé S.A.
```

**Cuerpo:**
```
Estimado(a) equipo de soporte técnico / [NOMBRE_CONTACTO]:

Colé S.A. reporta la siguiente falla en equipo bajo nuestra custodia y solicita
autorización de devolución (RMA) para diagnóstico y reparación:

[TABLA_EQUIPOS]

Descripción de la falla:
[DESCRIPCIÓN_SÍNTOMA — fecha de inicio, condiciones en que se manifiesta, impacto operativo]

Solicitamos: (1) número de RMA, (2) instrucciones de empaque y envío, (3) dirección
de destino, y (4) tiempo estimado de diagnóstico / reparación.

[FIRMA]
```

---

## RCS — Renovación de Contrato de Servicio

**Asunto:**
```
Solicitud de Renovación de Contrato de Servicio — [MARCA] — Colé S.A. / [AÑO]
```

**Cuerpo:**
```
Estimado(a) [NOMBRE_CONTACTO]:

Colé S.A. solicita la renovación del contrato de servicio técnico y/o calibración
para los equipos indicados a continuación, correspondiente al período [AÑO / PERÍODO]:

[TABLA_EQUIPOS]

Favor remitir propuesta actualizada que incluya: alcance del servicio, frecuencia de
intervenciones, cobertura de repuestos, condiciones de respuesta ante falla, y costo
anual del contrato.

Quedamos atentos a su propuesta para proceder con la aprobación interna.

[FIRMA]
```

---

---

## Dirección de Envío Estándar — Proveedores USA

Usar para todos los envíos a proveedores con sede en Estados Unidos.

**Ship To:**
```
Inversiones Colé
506 Aeropost Way, SJO-3354-01
Miami, FL 33206-3206
USA
Tel: +1 (786) 322-2032
Attn: Manuel Rubio
```

⚠️ **NOTA CRÍTICA — Sin factura comercial en el paquete:**
Todo envío desde USA hacia Costa Rica vía Aeropost debe ir **SIN FACTURA COMERCIAL**
dentro del paquete físico. La factura se gestiona por separado en el proceso de importación.
Incluir esta instrucción explícita en toda solicitud de envío a proveedores USA:

> "Please do **NOT** include a commercial invoice inside the package.
> Shipping documents should be sent separately via email to colesa.manuel@gmail.com.
> This is required for our import clearance process through our freight forwarder."

---

## Plantilla Bilingüe (ES + EN) — Para Proveedores Extranjeros sin Distribuidor Local

Usar cuando el proveedor es extranjero y no hay intermediario regional identificado.
Incluir ambos bloques en el mismo email, separados por línea divisoria.

```
[BLOQUE EN ESPAÑOL — usar plantilla correspondiente arriba]

---

[ENGLISH VERSION]

Dear [CONTACT NAME / Technical Support Team]:

[Traducción al inglés del bloque español, manteniendo misma estructura y tabla de equipos]

[ENGLISH SIGNATURE BLOCK]
Manuel Rubio, MSc — President / Radiation Protection Officer
Inversiones e Importaciones Colé S.A. | www.colecr.com
Tel: +506 2285-3211 | WhatsApp: +506 8395-7547
Email: colesa.manuel@gmail.com | San José, Costa Rica
```
