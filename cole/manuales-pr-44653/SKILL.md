---
name: manuales-pr-44653
description: Elabora y audita Manuales de Procedimientos de Protección y Seguridad Radiológica conforme al Decreto 44653-S de Costa Rica (Anexo VI), para instalaciones médicas, odontológicas, veterinarias, industriales y de investigación (Tipos I a V). Genera el manual con la estructura y numeración exacta exigida por la UPR del Ministerio de Salud, audita manuales contra prevenciones (CARTA-MS-DSS-UPR) y lista los documentos a anexar al trámite. Activar con "manual de procedimientos", "manual de operación", "manual de protección radiológica", "Decreto 44653", "Anexo VI", "prevención MINSA", "prevención UPR", "autorización de operación", "trámite UPR", "F02-A", "revisar manual", "auditar manual", "elaborar manual para clínica/industria/laboratorio", o cualquier documentación regulatoria de protección radiológica para autorización de instalaciones en Costa Rica. Activar incluso si la solicitud parece simple — la UPR archiva trámites por detalles.
---

# Manuales de Procedimientos PR — Decreto 44653-S

Elabora Manuales de Procedimientos de Protección y Seguridad Radiológica que superen la revisión de la Unidad de Protección Radiológica (UPR) del Ministerio de Salud de Costa Rica en el primer intento. La UPR revisa contra la letra exacta del Anexo VI: una sola omisión de contenido, una inconsistencia de fechas o una "nota técnica" olvidada provoca prevención y, si no se subsana, el archivo del trámite (Ley 8220, art. 6).

## Principio rector

El manual NO es un documento creativo: es una respuesta punto por punto a una lista de verificación reglamentaria. La estructura, la numeración y los encabezados deben replicar exactamente la sección VI.1 o VI.2 del Anexo VI. Todo numeral que no aplique a la instalación se conserva en el documento con la leyenda "No aplica" más una justificación técnica de una oración (por qué no aplica para ese tipo/clase). Nunca eliminar ni renumerar numerales.

## Flujo de trabajo

### Paso 1 — Clasificar la instalación
Determinar Tipo y Clase según el Anexo III. Leer `references/clasificacion-anexo-iii.md`. La clasificación define qué estructura usar:
- **Tipo I y II** → estructura VI.1 (`references/estructura-vi1.md`)
- **Tipo III, IV y V** → estructura VI.2 (`references/estructura-vi2.md`)

La clasificación también determina qué numerales aplican (p. ej., 5.1.10 detectores solo aplica a Tipo I excepto clase 11 y Tipo II clases 3, 9-14; la sección 5.6 Emergencias no aplica a Tipo II clases 1, 2, 4, 5, 6, 7, 8).

### Paso 2 — Recolectar insumos antes de redactar
No redactar con huecos ni con datos "por ejemplo". Solicitar al usuario, como mínimo:
1. Razón social, nombre comercial, cédula jurídica, dirección exacta.
2. Representante legal / titular, RPR y RPR sustituto (el sustituto es obligatorio; verificar que su licencia o trámite sea coherente).
3. Operadores: nombre EXACTO como aparece en la licencia, número de licencia, fecha de emisión y vencimiento. Transcribir de la licencia, no de memoria.
4. Fuentes de radiación: para rayos X — tipo, marca, modelo, serie, imagen (analógico/digital), modalidad (fijo/móvil), número de tubos, kVp y mA máximos, ubicación y uso. Para fuentes radiactivas, ver requisitos en la estructura de referencia.
5. Prestadores externos (control de calidad, mantenimiento, dosimetría, calibración): razón social Y cédula jurídica de cada uno. El Decreto lo exige textualmente; omitir la cédula jurídica es causal de prevención.
   - PREGUNTAR SIEMPRE: ¿el certificado anual de conformidad de parámetros del generador lo emitió Inversiones e Importaciones Colé S.A. (cédula 3-101-392010) u otra empresa? Si es otra, solicitar su razón social, cédula jurídica y número de autorización como prestador, y nombrarla en 5.1.7/5.3.3 en lugar de Colé. No asumir Colé por defecto.
6. Entidad de dosimetría real (acreditada ISO/IEC 17025) y contrato firmado por ambas partes — el contrato se anexa al trámite.
7. Planos: número de contrato/código APC del CFIA de los planos constructivos y de la memoria de cálculo de blindaje. Sin código APC verificable no hay cumplimiento del art. 42 (aplica también a edificaciones existentes adaptadas al nuevo uso).
8. Datos de blindaje (espesores, equivalencias en Pb) y resultados del levantamiento radiométrico, para fundamentar cuantitativamente la restricción de dosis.

### Paso 3 — Redactar
Seguir la estructura de referencia numeral por numeral. Reglas duras aprendidas de prevenciones reales de la UPR (detalle y casuística en `references/checklist-prevenciones.md`):
- Incluir tabla de contenidos que refleje la estructura del Anexo VI.
- Cero "notas técnicas", "sugerencias", comentarios al lector o referencias metodológicas a documentos de terceros. El manual es un documento final del cliente, emitido bajo la identidad del cliente (sin marca del consultor).
- Sección 1.1: fecha, versión, nombre, FIRMA y cargo de quien elaboró, revisó y aprobó.
- 5.1.1: incluir organigrama gráfico (no solo lista) con titular, RPR, POE operador y no operador.
- 5.1.6: el programa de capacitación debe incluir las 6 partes: objetivos, contenidos, metodología, duración, evaluaciones y plan de trabajo (cronograma anual).
- 5.1.15 (VI.1) / 5.1.8 (VI.2): TODOS los registros aplicables deben tener formato definido (tabla modelo en anexos del manual), incluidos inventario de fuentes, verificación de sistemas de seguridad, vigilancia de áreas, expediente del POE y revisión del programa.
- 5.2.9 (VI.1) / 5.2.6 (VI.2): la restricción de dosis exige fundamento, criterios, CÁLCULOS y evidencia (datos de blindaje o radiometría); una justificación cualitativa no cumple.
- 5.3.3: especificar límites de tolerancia numéricos y acciones correctivas, no solo "según fabricante".
- Punto 6 del Anexo VI: todo documento externo referenciado en el manual DEBE anexarse (planos, contratos, certificados, licencias).
- Identificar los prestadores de servicios externos UNA SOLA VEZ en el manual (en 5.1.1, junto a la estructura organizativa), con razón social, cédula jurídica y autorización de cada uno. En el resto del documento referirlos únicamente como "Proveedor de Servicios" del área correspondiente (control de calidad, mantenimiento, dosimetría), remitiendo al punto 5.1.1. Evita inconsistencias y facilita actualizar el dato en un solo lugar.
- Resaltar en amarillo, en los borradores de trabajo, los datos de los prestadores de servicios y todo campo pendiente de completar ([COMPLETAR ANTES DE SOMETER]); advertir al titular que los resaltados se retiran antes de imprimir la versión final para firma.
- NO detallar marcas, modelos ni números de serie de los instrumentos detectores o medidores del prestador externo dentro del manual del cliente: referirlos de forma genérica ("instrumentos de medición del prestador, con certificados de calibración vigentes y trazabilidad metrológica, identificados en cada informe"). La identificación específica viaja en los informes del prestador; detallarla en el manual lo desactualiza cada vez que el prestador renueva equipo. Sí se detallan los equipos detectores PROPIOS de la instalación cuando el numeral 5.1.10 aplica a su tipo/clase.
- Consistencia interna absoluta: nombres, cédulas, fechas y vigencias idénticos en todo el documento y coincidentes con los documentos adjuntos al trámite. Una discrepancia de fecha de vencimiento de licencia genera prevención.

### Paso 4 — Verificación cruzada (obligatoria antes de entregar)
Ejecutar la lista de `references/checklist-prevenciones.md` sección "Checklist de salida". Verificar contra los documentos fuente (licencias, planos, contratos), no contra el propio texto. Reportar al usuario cualquier dato que no se pudo verificar.

### Paso 5 — Entregable
Generar DOCX (usar el skill `docx`) con: portada, tabla de control documental (versión, fecha, elaboró/revisó/aprobó con espacios de firma), tabla de contenidos, cuerpo numerado según el Anexo VI, y anexos con los formatos de registro. Idioma: español formal-técnico. El documento se firma por el representante legal (requisito del trámite de autorización).

## Auditoría de manuales existentes
Cuando el usuario pida revisar un manual o responder una prevención: extraer el texto del manual, leer la prevención (CARTA-MS-DSS-UPR), y comparar numeral por numeral contra la estructura de referencia aplicable. Producir un dictamen con semáforo (cumple / parcial / no cumple) por numeral, las correcciones exactas y la lista de documentos faltantes del trámite. Recordar: si el trámite fue archivado, se reinicia con TODOS los requisitos del Anexo IV, no solo los prevenidos.
                                                                                                                      