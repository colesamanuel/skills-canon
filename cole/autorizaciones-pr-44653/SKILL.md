---
name: autorizaciones-pr-44653
description: >-
  Requisitos de cumplimiento para autorizaciones y licencias de protección radiológica en Costa Rica bajo el Decreto 44653-S, SEGÚN TIPO DE INSTALACIÓN (Tipos I-V, Anexo III): autorización de operación (nueva, renovación, modificación), puesta en servicio (Tipo I clases 1,3-10,16), RPR, licencia de operador, cierre, y requisitos constructivos del art. 42 (planos CFIA/APC, memorias de blindaje, levantamientos radiométricos). Activar con: requisitos de autorización, licencia de operación, licencia institucional, autorización de operación, puesta en servicio, renovación, qué necesita una clínica/hospital/industria para operar rayos X, requisitos MINSA, F01, F02-A, F02-B, F03, F11, Anexo III, tipo de instalación, RPR, trámite UPR, checklist de cumplimiento radiológico, o cualquier consulta sobre qué exige el Ministerio de Salud para operar fuentes de radiación. Activar aunque parezca simple — el régimen difiere por tipo y clase. Complementa a manuales-pr-44653 (Anexo VI).
---

# Autorizaciones y Licencias PR — Decreto 44653-S (Costa Rica)

Skill de cumplimiento regulatorio para determinar y documentar los requisitos de autorización/licenciamiento de instalaciones con fuentes de radiación ante el Ministerio de Salud de Costa Rica, según el tipo y clase de instalación.

## 0. Corrección terminológica obligatoria

El Decreto 44653-S NO usa las figuras "licencia de operación" ni "licencia institucional". Si el usuario o el cliente las usa, normalizar SIEMPRE a la terminología legal correcta y explicar el mapeo una sola vez al inicio del entregable:

| Término coloquial | Figura legal correcta (44653-S) | Sujeto |
|---|---|---|
| "Licencia institucional" / "licencia de operación" | **Autorización de operación** de instalaciones con fuentes de radiación | Persona física o jurídica titular de la instalación |
| "Permiso de arranque" | **Autorización de puesta en servicio** (solo Tipo I, clases 1, 3, 4, 5, 6, 7, 8, 9, 10 y 16) | Titular de la instalación |
| "Licencia del encargado" | **Autorización de Responsable de la Protección Radiológica (RPR)** y RPR sustituto (art. 167, Anexo XIII) | Persona física |
| "Carné de operador" | **Licencia de operador** (arts. 21 y 168, Anexo XIII) | Persona física |
| "Baja / desmantelamiento" | **Autorización de cierre** | Titular de la instalación |

## 1. Flujo obligatorio (no saltar pasos)

**Paso 1 — Clasificar la instalación.** Leer `references/anexo3_clasificacion.md` (Anexo III verbatim). Identificar Tipo (I–V) y Clase exacta a partir de la práctica descrita por el usuario. Si la práctica es ambigua entre dos clases (p. ej., fluoroscopía diagnóstica Tipo II-7 vs. intervencionismo Tipo I-11; tomógrafo médico Tipo II-5 vs. haz cónico odontológico Tipo III-1), PREGUNTAR — nunca asumir. La clase determina requisitos diferenciales (puesta en servicio, plan de cierre, levantamiento radiométrico, certificado de conformidad).

**Paso 2 — Identificar el trámite.** ¿Nueva autorización, renovación, modificación, puesta en servicio, cierre, RPR o licencia de operador? Cada uno tiene lista propia dentro del documento del tipo correspondiente.

**Paso 3 — Cargar SOLO la referencia del tipo aplicable** (texto oficial verbatim, con secciones 2.1 nuevas / 2.2 renovaciones / 2.3 modificaciones):

| Situación | Referencia |
|---|---|
| Operación Tipo I | `references/tipo1_operacion.md` |
| Operación Tipo II | `references/tipo2_operacion.md` |
| Operación Tipo III | `references/tipo3_operacion.md` |
| Operación Tipo IV | `references/tipo4_operacion.md` |
| Operación Tipo V | `references/tipo5_operacion.md` |
| Puesta en servicio (Tipo I, clases 1,3,4,5,6,7,8,9,10,16) | `references/puesta_servicio_tipo1.md` |
| Licencia de operador | `references/licencia_operador.md` |
| Cierre de instalación | `references/cierre.md` |
| Clasificación / dudas de tipo-clase | `references/anexo3_clasificacion.md` |

**Paso 4 — Generar el entregable** (ver §4) transcribiendo los requisitos del documento oficial, marcando los condicionales que aplican o no según la clase y la práctica concreta.

**Paso 5 — Cierre operativo estándar**: recomendación, pasos concretos (incluido dónde presentar, ver §3), riesgos (causas típicas de archivo del trámite) y nivel de confianza explícito.

## 2. Reglas duras de régimen (memorizar)

1. **Formularios**: F01 = puesta en servicio · F02-A = operación Tipos I y II (revisión documental completa por la UPR) · F02-B = operación Tipos III, IV y V (régimen de **declaración jurada**) · F03 = cierre · F11 = licencia de operador.
2. **Declaración jurada ≠ menos requisitos**: en Tipos III, IV y V la autorización se otorga por declaración jurada del representante legal, PERO el interesado debe cumplir y poder demostrar la totalidad de los requisitos; el incumplimiento comprobado faculta al Ministerio a cancelar la autorización y clausurar. Advertirlo SIEMPRE en el entregable.
3. **Puesta en servicio previa**: solo Tipo I, clases 1, 3, 4, 5, 6, 7, 8, 9, 10 y 16. La autorización de operación de esas clases exige además el informe de resultados de las pruebas de puesta en servicio.
4. **Artículo 42 (construcción/ampliación/remodelación)**: instalaciones Tipo I, II y III requieren planos constructivos y memoria de cálculo de blindaje tramitados y sellados ante la plataforma APC del CFIA, conforme al Decreto 36550-MP-MIVAH-S-MEIC. Las secciones 3.2 y 3.3 de cada referencia detallan el contenido exigido de planos y memorias.
5. **RPR y RPR sustituto** (art. 167, Anexo XIII): título de Licenciatura (prácticas médicas humanas y veterinarias) o Bachillerato/Licenciatura (industriales e investigación) + certificado de curso avanzado de 80 h en la práctica específica, emitido por prestador autorizado, con no más de 2 años de emitido.
6. **Licencia de operador** (Anexo XIII): curso básico de 16 h en la práctica específica (≤2 años de emitido) + título académico según tabla por práctica (ver referencia) + dictamen médico de aptitud para exposición ocupacional.
7. **Dosimetría personal externa**: contrato con entidad con ensayos acreditados ISO/IEC 17025, especificando tipo, cantidad de dosímetros y vigencia.
8. **Fuentes radiactivas selladas**: documento de origen (compra-venta), certificado de fuente y de hermeticidad/prueba de fuga del fabricante, y compromiso del fabricante de recibir la fuente al fin de vida útil. Plan de cierre aplica a las clases listadas en `references/cierre.md`.
9. **Levantamiento radiométrico y mantenimiento**: deben provenir de prestadores de servicios técnicos autorizados por el Ministerio de Salud (lista oficial en línea — verificar vigencia, no citar de memoria).
10. **Curso A 80 h ↔ RPR; Curso B 16 h ↔ operador.** Vínculo directo con la oferta MINSA-autorizada de Colé S.A. (skill `minsa-course-format`): cuando el checklist revele que al cliente le falta el curso, señalarlo como oportunidad comercial legítima de Colé, sin distorsionar el contenido regulatorio.

## 3. Ventanilla de presentación

Regla general: trámites ante la **Unidad de Protección Radiológica (UPR)** de la Dirección de Protección Radiológica y Salud Ambiental. Excepciones que se tramitan ante las **Direcciones de Área Rectora de Salud**: licencias de operador y autorización de operación de instalaciones con equipos de rayos X de uso odontológico (y sus modificaciones/renovaciones). Ante duda sobre la ventanilla de una clase concreta, verificar en línea en la página de trámites del Ministerio — no asumir.

## 4. Formatos de entregable

- **Lista enviable por WhatsApp y/o email** (DEFAULT): texto plano en viñetas/numeración simple, copiable sin pérdida de formato en ambos canales. Reglas estrictas: SIN tablas Markdown, SIN encabezados `#`, negrita solo con *asteriscos simples* (formato nativo WhatsApp, legible también en email). Estructura fija: (1) saludo breve y objeto; (2) línea de *Clasificación* (Tipo-Clase Anexo III, formulario aplicable, ventanilla); (3) *Requisitos de la solicitud:* lista numerada, un requisito por línea, texto fiel al documento oficial condensado a una oración; (4) advertencia de régimen (declaración jurada / causas típicas de archivo); (5) cierre comercial Colé con servicios aplicables; (6) firma con datos canónicos de Colé S.A. (Ing. Manuel Rubio, MSc · Tel (506) 2285-3211 · WhatsApp (506) 8395-7547 · www.colecr.com). Extensión objetivo: legible en una sola pantalla de WhatsApp por sección, máx. ~350 palabras. Entregar mediante la herramienta de composición de mensajes si está disponible; si no, como bloque de texto plano listo para copiar. Omitir salvedades técnicas internas (criterios administrativos no confirmados): esas se reportan al titular por separado, nunca al cliente.
- **Checklist de cumplimiento en tabla** (solo bajo solicitud explícita de "tabla", "checklist detallado" o "auditoría"): Markdown, columnas Nº / Requisito (texto fiel al documento oficial) / ¿Aplica? (sí/no según clase, con justificación) / Estado (pendiente/cumplido/por verificar) / Evidencia esperada. Encabezado con: instalación, Tipo-Clase (Anexo III), trámite, formulario aplicable, ventanilla.
- **Informe DOCX para cliente** (solo bajo solicitud explícita): usar skill `cole-brand-identity` (es operación corporativa Colé S.A.) y skill `docx`. Incluir mapeo terminológico (§0), checklist, sección de brechas y plan de subsanación.
- Las cotizaciones derivadas (cursos, levantamientos, manuales, cálculo de blindaje) NO se generan con este skill: derivar a `odoo-quotation-generator`.
- Exclusión dura heredada del perfil del titular: cartas regulatorias y auditorías con trazabilidad normativa son SIEMPRE textuales (Markdown/DOCX), nunca dashboards HTML.

## 5. División de trabajo con skills hermanos

- `manuales-pr-44653` → contenido y estructura del Manual de Procedimientos (Anexo VI) y respuesta a prevenciones UPR. Este skill solo indica QUE el manual es requisito y QUÉ secciones exige el documento oficial de requisitos (sección "Manual de Procedimientos" de cada referencia); la redacción del manual se delega.
- `minsa-course-format` → programas de curso (Anexo XIII) cuando el cliente necesita formar RPR u operadores.
- `shielding-verification` → levantamientos radiométricos y verificación de blindaje cuando el requisito 3.2/3.3/4 lo exige.

## 6. Anti-desinformación y trazabilidad

- Las referencias son texto verbatim de los documentos oficiales UPR (serie 2025), extraído el 2026-06-10. Antes de emitir un entregable formal a cliente o regulador, verificar en ministeriodesalud.go.cr que la versión siga vigente (la UPR actualiza la serie; en 2025 reemplazó la serie anterior).
- Toda afirmación de requisito en el entregable debe poder rastrearse a un numeral del documento oficial o a un artículo/anexo del Decreto 44653-S. Si un requisito no aparece en la fuente, NO inventarlo: declarar "no verificado en fuente oficial" y proponer consulta a la UPR.
- Listas dinámicas (prestadores de servicios técnicos autorizados, prestadores de capacitación, inventario de RPR) se consultan en línea SIEMPRE; nunca citarlas de memoria.
