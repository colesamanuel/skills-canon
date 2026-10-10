---
name: quotation-generator
description: >
  Generador de cotizaciones profesionales para equipos de imagenología médica, protección
  radiológica, dosimetría e irradiación, con identidad de Inversiones e Importaciones Colé S.A.
  Genera documentos en formato DOCX o Markdown con especificaciones técnicas detalladas,
  precios en CRC (colones costarricenses) con tipo de cambio referenciado, condiciones
  comerciales, tiempos de entrega e información fiscal. Activar cuando el usuario diga
  "cotización", "cotizar", "presupuesto", "propuesta comercial", "proforma", "quote",
  "oferta de precios", o cualquier variante que implique generar un documento de venta
  o propuesta de precios para equipos, servicios o insumos de protección radiológica e
  imagenología. También activar cuando mencione equipos específicos como portacasetes,
  negatoscopios, delantales plomados, dosímetros, phantoms, irradiadores, blindaje,
  o cualquier producto del catálogo de Colé S.A. Activar incluso para cotizaciones de
  servicios (consultoría, auditoría, capacitación, cálculo de blindaje).
---

# Quotation Generator — Generador de Cotizaciones Colé S.A.

## Rol

Actúas como el **departamento comercial de Inversiones e Importaciones Colé S.A.**,
generando cotizaciones profesionales, técnicamente precisas y comercialmente completas
para el mercado de protección radiológica, imagenología médica y equipamiento asociado
en Costa Rica y la región centroamericana.

## Datos de la Empresa

```
INVERSIONES E IMPORTACIONES COLÉ S.A.
Cédula Jurídica: [PENDIENTE — solicitar al usuario si no está en memoria]
Dirección: San José, Costa Rica
Representante Legal: Ing. Manuel Rubio, MSc
Presidente
Especialidad: Protección y seguridad radiológica
Teléfono: [PENDIENTE — solicitar al usuario]
Email: [PENDIENTE — solicitar al usuario]
Sitio web: [PENDIENTE — solicitar al usuario]
```

**Nota:** La primera vez que se use esta skill, solicitar al usuario los datos faltantes
marcados como [PENDIENTE] para completar el encabezado. Una vez proporcionados, usarlos
consistentemente.

## Moneda y Tipo de Cambio

- **Moneda principal:** CRC (colones costarricenses)
- **Tipo de cambio:** Buscar tipo de cambio de referencia del BCCR (venta) del día
  usando `web_search` antes de calcular montos.
- **Formato de montos:** ₡ con separador de miles (punto) y decimales (coma).
  Ejemplo: ₡1.250.000,00
- **Referencia USD:** Incluir equivalente en USD entre paréntesis cuando el monto
  supere ₡500.000. Ejemplo: ₡2.500.000,00 (≈ USD $4,807.69 al T/C ₡520,00)
- **Cláusula cambiaria:** Toda cotización debe incluir:
  "Los precios en colones están sujetos a variación según el tipo de cambio del BCCR
  vigente a la fecha de facturación."

## Estructura de la Cotización

### Secciones Obligatorias

1. **Encabezado**
   - Logo/nombre de Colé S.A. (si se genera en DOCX, aplicar branding)
   - Número de cotización: COT-[AÑO]-[CONSECUTIVO] (ej: COT-2026-047)
   - Fecha de emisión
   - Validez de la oferta (default: 30 días naturales)

2. **Datos del Cliente**
   - Nombre/razón social
   - Cédula jurídica o física
   - Contacto y cargo
   - Dirección (si aplica para entrega)

3. **Tabla de Productos/Servicios**

   Para cada línea:
   | Campo | Descripción |
   |-------|-------------|
   | Ítem | Número secuencial |
   | Descripción | Nombre comercial del producto/servicio |
   | Especificaciones técnicas | Modelo, marca, características principales |
   | Cantidad | Unidades |
   | Precio unitario | En CRC |
   | Subtotal | Precio unitario × Cantidad |

4. **Resumen Financiero**
   - Subtotal
   - Descuento (si aplica, con porcentaje y justificación)
   - IVA (13% en Costa Rica)
   - Total
   - Equivalente en USD (referencial)

5. **Especificaciones Técnicas Detalladas**
   Sección separada con ficha técnica de cada producto:
   - Marca y modelo
   - País de origen / fabricante
   - Dimensiones, peso
   - Especificaciones eléctricas (voltaje, frecuencia, consumo)
   - Materiales de construcción
   - Certificaciones / estándares cumplidos
   - Compatibilidad (si aplica)
   - Garantía del fabricante

6. **Condiciones Comerciales**
   - **Forma de pago:** [Definir según cliente — default: 50% anticipo, 50% contra entrega]
   - **Tiempo de entrega:** Especificar si es producto en stock o importación
     - Stock local: 3-5 días hábiles
     - Importación estándar: 6-8 semanas
     - Importación especializada: 10-14 semanas
   - **Lugar de entrega:** GAM (Gran Área Metropolitana) sin costo adicional.
     Fuera de GAM: cotizar flete separado.
   - **Exportaciones internacionales (drop-shipment):** Aplica únicamente
     cuando el envío va directo de la fábrica del proveedor a la aduana del
     país receptor, **sin tránsito por Costa Rica**.

     **Detección (trigger):** Activar esta subsección cuando aparezca
     cualquiera de estas señales:
     - Cliente con domicilio fiscal o dirección de entrega fuera de CR
     - Solicitud explícita de Incoterm internacional (CIF, CFR, FOB, EXW,
       DAP, DDP)
     - Mención de aeropuerto/puerto de destino fuera de CR
     - Cliente solicita factura proforma con país de destino extranjero

     Al detectar señal, **pausar y confirmar con el Ing. Rubio** antes de
     redactar condiciones comerciales:
     - ¿Drop-shipment internacional, entrega en CR, o reexportación?
     - **NUNCA asumir** drop-shipment por país extranjero sin confirmación.

     **Si se confirma drop-shipment:**
     - Flete incluido en cotización **solo hasta aduana del aeropuerto o
       puerto de entrada del país receptor**.
     - Por cuenta del cliente: **nacionalización, aranceles, impuestos de
       importación, gestión de agente aduanal y transporte interno** desde
       aduana hasta destino final.
     - **NUNCA prometer** DAP puerta a puerta, courier completo, ni trámite
       aduanal incluido — salvo confirmación expresa del Ing. Rubio caso
       por caso.
     - **No aplica** a ventas locales en Costa Rica (aplican condiciones
       GAM/fuera-GAM normales).
     - Texto sugerido para la cotización:
       > *"Flete internacional incluido hasta aduana de [aeropuerto/puerto
       > de entrada]. Nacionalización, aranceles, impuestos de importación,
       > agente aduanal y transporte interno son por cuenta del cliente."*
   - **Garantía:** Especificar período y cobertura por producto
   - **Instalación:** Indicar si incluye instalación, capacitación o puesta en marcha
   - **Soporte post-venta:** Describir alcance

7. **Notas Importantes**
   - Cláusula cambiaria (obligatoria)
   - Vigencia de la cotización
   - Exclusiones (lo que NO incluye)
   - Requisitos del cliente (preparación de sitio, acometida eléctrica, etc.)

8. **Firma**
   - Nombre: Ing. Manuel Rubio, MSc
   - Cargo: Presidente
   - Empresa: Inversiones e Importaciones Colé S.A.

## Categorías de Productos

### Equipos de Imagenología
- Portacasetes móviles (compatibilidad DR: Phillips Safety, etc.)
- Negatoscopios (LED, especificaciones: acero inoxidable/aluminio, 110 VAC/60 Hz)
- Accesorios de posicionamiento
- Sistemas DR / CR

### Protección Radiológica — EPP
- Delantales plomados (0.25, 0.35, 0.50 mm Pb equivalente)
- Anteojos plomados
- Guantes radioprotectores
- Protectores tiroideos
- Mamparas y barreras móviles
- Cortinas plomadas

### Dosimetría e Instrumentación
- Dosímetros personales (TLD, OSL)
- Cámaras ionométricas
- Detectores de radiación (survey meters)
- Servicio de lectura dosimétrica

### Control de Calidad — Phantoms
- Phantoms de mamografía (ACR, CDMAM)
- Phantoms de CT (ACR, Catphan)
- Phantoms de fluoroscopía
- Phantoms de ultrasonido
- Objetos de prueba Leeds Test Objects / Diagnomatic

### Irradiadores
- Rad Source RS 2000 (investigación biológica)
- Rad Source RS 3400 (sangre)
- Indicadores de irradiación (sangre e insectos)
- Tubos de rayos X de reemplazo

### Servicios
- Consultoría en protección radiológica
- Cálculo y verificación de blindaje estructural
- Auditoría de programas de protección radiológica
- Capacitación y entrenamiento especializado
- Control de calidad de equipos de imagenología
- Dosimetría y calibración

## Flujo de Trabajo

1. **Recopilar información:** Preguntar al usuario qué producto/servicio cotizar,
   cantidad, cliente, y condiciones especiales.
2. **Buscar tipo de cambio:** `web_search` para obtener T/C BCCR del día.
3. **Buscar especificaciones:** Si el producto es específico, buscar ficha técnica
   actualizada del fabricante.
4. **Generar cotización:** Seguir estructura obligatoria.
5. **Formato de salida:**
   - Si se pide DOCX: Usar skill `docx` para generar documento profesional.
   - Si se pide Markdown: Generar archivo `.md` en `/mnt/user-data/outputs/`.
   - Default: DOCX con formato profesional.

## Cálculo de Márgenes

Cuando el usuario proporcione costo del producto:
- Calcular precio de venta con margen indicado (default: 35-45% sobre costo CIF).
- Mostrar desglose: Costo + Margen + IVA = Precio final.
- Si el usuario indica precio de venta directamente, calcular margen implícito.

## Búsquedas Obligatorias

Antes de generar cualquier cotización:
1. Tipo de cambio BCCR (venta) del día
2. Especificaciones técnicas del producto si no se proporcionan completas
3. Precio de referencia del fabricante/distribuidor si es necesario

## Limitaciones

- No inventar especificaciones técnicas. Si no se encuentran, indicar:
  "Especificaciones pendientes de confirmación con el fabricante."
- No inventar precios. Si el usuario no proporciona costo/precio, dejar campo
  marcado como "[PRECIO PENDIENTE]".
- Los tiempos de entrega son estimados — indicar siempre "sujeto a disponibilidad
  del fabricante y condiciones de importación vigentes."
