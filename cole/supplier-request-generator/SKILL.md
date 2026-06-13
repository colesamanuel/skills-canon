---
name: supplier-request-generator
description: >
  Genera emails formales y cartas DOCX de Colé S.A. hacia proveedores de equipos
  dosimétricos y de protección radiológica. Cubre: calibración, mantenimiento
  preventivo/correctivo, cotización, reporte de falla/RMA y renovación de contrato.
  Parsea listas de equipos en texto libre (marca, modelo, S/N, observaciones) y
  genera tabla estructurada dentro del mensaje. Detecta automáticamente calibraciones
  vencidas y marca urgencia. Firma con datos completos de Ing. Manuel Rubio MSc.
  Genera versión bilingüe ES/EN para proveedores extranjeros sin distribuidor local.
  Activar con: "solicitar calibración", "pedir mantenimiento", "reportar falla",
  "RMA", "renovar contrato", "email a Radcal", "email a IBA", "carta a proveedor",
  "solicitud de servicio", "solicitud de cotización a proveedor", "enviar a
  distribuidor", calibración vencida, o cualquier comunicación formal saliente
  hacia proveedor o distribuidor de equipos médicos o dosimétricos.
---

# Supplier Request Generator — Solicitudes Formales a Proveedores

Skill para redactar comunicaciones formales de Colé S.A. hacia proveedores de equipos
médicos, dosimétricos y de protección radiológica.

---

## Paso 1 — Extracción de Datos

Antes de redactar, extraer los siguientes datos del mensaje del usuario (o solicitarlos
si están ausentes):

### Datos del destinatario (proveedor)
- **Nombre del proveedor / empresa**
- **Contacto** (nombre, cargo, email) — si no se provee, omitir o dejar placeholder `[CONTACTO]`
- **País / región** del proveedor (infiere si es obvio: Radcal → USA, etc.)

### Tipo de solicitud
Identificar cuál de los cinco tipos aplica (puede ser más de uno):

| Código | Tipo |
|--------|------|
| `CAL` | Calibración de equipos |
| `MNT` | Mantenimiento preventivo o correctivo |
| `COT` | Cotización de producto o servicio |
| `RMA` | Reporte de falla / Return Merchandise Authorization |
| `RCS` | Renovación de contrato de servicio |

### Lista de equipos
Parsear desde texto libre. Buscar patrones:
- Marca / fabricante (ej: Radcal, IBA, Ludlum, Unfors, RTI, Polimaster, Fluke)
- Modelo (ej: AGMS-D+, 10X6-0.6CT, 9010, Piranha)
- Número de serie (S/N) — buscar patrones numéricos o alfanuméricos junto a "S/N", "serie", "serial"
- Observaciones relevantes: fecha de última calibración, fecha de vencimiento, número de reporte,
  condición del equipo, lugar de uso

**Tabla de salida normalizada:**

| # | Marca | Modelo | S/N | Observaciones |
|---|-------|--------|-----|---------------|

Si hay datos ambiguos, asumir lo más razonable e indicar `[VERIFICAR]` en la celda dudosa.
No bloquear la generación por datos faltantes menores — continuar con lo disponible.

---

## Paso 2 — Selección de Plantilla

Leer el archivo de plantillas correspondiente según el tipo de solicitud:
→ `references/templates.md`

Cada plantilla define:
- Asunto del email
- Estructura del cuerpo
- Tono y fórmulas de cortesía
- Campos de datos que deben insertarse

---

## Paso 3 — Generación del Email

### Estructura del email

```
De: colesa.manuel@gmail.com
Para: [EMAIL_PROVEEDOR]
Asunto: [ASUNTO_SEGÚN_PLANTILLA] — Colé S.A. / [FECHA_HOY]

[SALUDO]

[CUERPO_PRINCIPAL con tabla de equipos incrustada]

[PÁRRAFO DE CIERRE + instrucciones de respuesta]

[FIRMA]
```

### Firma estándar Colé S.A.

```
Ing. Manuel Rubio, MSc
Presidente | Oficial de Protección Radiológica (OPR)
Inversiones e Importaciones Colé S.A.
Cédula Jurídica: 3-101-392010
Servicios de Protección Radiológica · Equipos de Imagen Médica

Tel: (506) 2285-3211 / 2285-9561
Cel/WhatsApp: (506) 8395-7547 / 6050-0161
Email: colesa.manuel@gmail.com
Web: www.colecr.com
Dirección: Del BCR 125m Este, Calle de Piedra, Zapote, San José, Costa Rica
```

### Reglas de redacción

1. **Idioma:** Español formal por defecto. Si el proveedor es extranjero (USA, Europa)
   y no tiene distribuidor local identificado, generar email bilingüe (español + inglés),
   con el cuerpo en ambos idiomas separados por línea divisoria.
2. **Tono:** Técnico-profesional. Sin exceso de fórmulas de cortesía. Directo al punto.
3. **Fecha:** Usar la fecha del día actual en el asunto y cuerpo cuando aplique.
4. **Números de reporte / certificados:** Si están en las observaciones, citarlos
   explícitamente (ej: "Calibration Report No. 134184").
5. **Fechas de vencimiento:** Si un equipo tiene `CalDue` vencida o próxima a vencer
   (≤ 60 días), indicarlo explícitamente como urgencia en el mensaje.

---

## Paso 4 — Presentación al Usuario

Mostrar el email generado en bloque de código o formato limpio para revisión.

Luego preguntar:
- ¿Requiere ajustes?
- ¿Generar también versión DOCX con membrete Colé S.A.?

Si solicita DOCX: usar el skill `docx` combinado con `cole-brand-identity` para generar
carta formal con encabezado corporativo, logo, línea azul decorativa y pie de página.

---

### Dirección de envío — Proveedores USA

Dirección estándar para todos los envíos desde proveedores en EE. UU.:

```
Inversiones Colé
506 Aeropost Way, SJO-3354-01
Miami, FL 33206-3206 · USA
Tel: +1 (786) 322-2032 · Attn: Manuel Rubio
```

⚠️ **Regla fija — Sin factura en el paquete:**
Siempre incluir la siguiente instrucción en solicitudes de envío a proveedores USA:
> "Please do NOT include a commercial invoice inside the package.
> Send shipping documents separately via email to colesa.manuel@gmail.com."

---

## Proveedores Conocidos — Referencia Rápida

| Proveedor | País | Tipo principal | Contacto por defecto |
|-----------|------|----------------|----------------------|
| Radcal Corporation | USA | Calibración / dosimetría | info@radcal.com |
| IBA Dosimetry | Alemania / USA | Calibración ADCL / dosimetría | [consultar web] |
| Ludlum Measurements | USA | Survey meters / detectores | service@ludlum.com |
| Unfors RaySafe / Fluke Biomedical | USA / Suecia | Dosimetría diagnóstica | [consultar web] |
| Polimaster | Bielorrusia / USA | Dosimetría personal | info@polimaster.us |
| Diagnomatic | Distribuidor regional | Imagen médica / QC | [referencia interna] |
| Leeds Test Objects | UK | Phantoms de QC | info@leedstestobjects.com |
| CIRS | USA | Phantoms / dosimetría | info@cirsinc.com |

Si el proveedor no está en esta lista, continuar con los datos que el usuario provea.

---

## Casos Especiales

### Equipos con calibración vencida
Si `CalDue` < fecha actual: agregar en el asunto `[URGENTE]` y en el cuerpo indicar
explícitamente los días de vencimiento. Ejemplo:
> "El equipo presenta calibración vencida desde el [FECHA], por lo que la solicitud
> tiene carácter prioritario para mantener la trazabilidad metrológica."

### RMA — Reporte de falla
Solicitar al usuario (si no lo provee):
- Descripción del síntoma o falla
- Fecha de inicio del problema
- Condiciones de envío preferidas (prepaid / collect)

### Calibración con múltiples equipos de la misma marca
Consolidar en un solo email con tabla completa. No generar emails separados por equipo.

### Idioma del proveedor extranjero sin distribuidor local
Generar cuerpo bilingüe con bloque en español primero, separador `---`, luego traducción
al inglés. Firma en ambos idiomas (o firma única bilingüe).
