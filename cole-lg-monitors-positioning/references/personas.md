# Personas-Decisor — Monitores LG Medical (venta privada)

6 personas-decisor priorizadas para v1 del skill. Cada una con: **dolor primario**,
**modelo LG asociado**, **dato técnico ancla**, **CTA correcto**.

> En monitores médicos, la persona que **influye** la compra (radiólogo, físico médico)
> es a menudo distinta de quien **firma** (jefe de servicio, gerente, comprador).
> El skill debe identificar cuál es la audiencia del copy antes de redactar — la voz
> y los argumentos cambian materialmente.

Si la solicitud no especifica persona, **preguntar antes de redactar**.

---

## 1. Radiólogo / Médico de imagen (usuario técnico)

**Quién es**: lector primario que pasa 6-10 horas diarias frente al monitor. Es el
**influencer técnico** de la compra, generalmente no firma directamente.

**Dolor primario verificable**:
- Fatiga visual y disminución de detección de lesiones de bajo contraste con monitores
  fuera de calibración GSDF.
- Variabilidad entre estaciones de lectura cuando los monitores no están calibrados
  uniformemente.
- Falta de consistencia entre lectura primaria y revisión clínica.

**Cifra dura**: el cumplimiento DICOM Part 14 GSDF asegura percepción uniforme entre
estaciones. Sin GSDF calibrado, la misma imagen luce distinta en cada monitor.

**Modelo LG asociado**:
- Diagnóstico general: **21HQ513D** (3MP) o **21HQ613D** (5MP).
- Diagnóstico alta exigencia: **32HQ713D** (8MP).
- Mamografía: **31HN713D** (12MP).

**Dato técnico ancla**:
- Resolución exacta del modelo (3MP / 5MP / 8MP / 12MP).
- Brillo declarado por LG (cd/m², no nits) — `[VALIDAR-LG]`.
- Cumplimiento DICOM GSDF Part 14.
- AAPM TG-270 para QA continuo.

**Argumento TCO ancla**: el costo del monitor distribuido en 5-7 años de vida útil
es marginal frente al tiempo de lectura ahorrado por consistencia visual.

**CTA correcto**: solicitud de demo en sala de lectura.
- Email: "Solicito demo del 32HQ713D en mi estación de lectura para evaluar uniformidad."
- LinkedIn: link a landing /diagnostico-lg.
- WhatsApp: "Quiero ver el monitor en mi consultorio antes de cotizar."

**Tono**: técnico-clínico. Asume conocimiento de DICOM, AAPM, lectura primaria,
revisión secundaria, ALARA. Cero condescendencia. **No mencionar costos directamente**
— este perfil influye, no firma.

---

## 2. Físico médico (calibración, QA, AAPM)

**Quién es**: responsable de QA de equipos. Tiene autoridad técnica sobre aceptación
y calibración periódica. Influye decisión y a menudo redacta especificaciones técnicas.

**Dolor primario verificable**:
- QA periódico AAPM TG-270 requiere phantom + software calibrado + tiempo del físico.
- Monitores de marca múltiple en una misma institución duplican esfuerzo de calibración.
- Trazabilidad documentada de QA para auditoría regulatoria.

**Cifra dura**: AAPM TG-270 es el estándar vigente para QA de displays médicos.
Reemplaza al TG-18 para QA periódico. Sin TG-270 documentado, la institución es
vulnerable en auditoría.

**Modelo LG asociado**: depende de la institución. Argumento aplica a línea diagnóstica
completa (21HQ513D, 21HQ613D, 31HN713D, 32HQ713D, 32HL512D).

**Dato técnico ancla**:
- Calibración GSDF de fábrica con certificado individual.
- Compatibilidad con phantoms estándar (Diagnomatic, ACR).
- Logs de calibración accesibles para QA periódico.
- IEC 62563-1 como referencia de método.

**Argumento TCO ancla**: estandarizar la flota en LG reduce horas de físico médico
en QA periódico (mismo software, mismo procedimiento). El servicio Colé puede
absorber el QA periódico bajo contrato (mencionar como ventaja).

**CTA correcto**: especificación técnica para licitación o documento de aceptación.
- Email: "Necesito hoja técnica AAPM TG-270 del modelo X para incluir en spec."
- Reunión técnica con Manuel sobre integración de QA.

**Tono**: técnico-físico. Cifras, normas, métodos. Esta persona detecta inconsistencia
en 30 segundos. Honestidad explícita en limitaciones del producto.

---

## 3. Jefe de Servicio Radiología

**Quién es**: decisor técnico institucional. Aprueba compra dentro del servicio,
escala a gerencia para presupuesto. Combina criterio clínico + administrativo.

**Dolor primario verificable**:
- Estandarización de la flota de monitores para reducir variabilidad diagnóstica.
- Justificación de inversión ante gerencia administrativa.
- Cumplimiento normativo de todo el servicio bajo su responsabilidad.
- Rotación de personal que requiere monitores intuitivos y estandarizados.

**Cifra dura**: una flota mixta de monitores no calibrados uniformemente genera
variabilidad diagnóstica documentada en literatura. Estandarizar reduce riesgo.

**Modelo LG asociado**:
- Lectura primaria: 21HQ613D (5MP) en serie de 4-8 unidades.
- Revisión clínica: 24HR513C (2MP) o 27HJ712C (8MP) según presupuesto.
- Mamografía: 31HN713D (par calibrado).

**Dato técnico ancla**:
- Cumplimiento DICOM GSDF y AAPM TG-270.
- Vida útil esperada 5-7 años con calibración periódica.
- Servicio Colé local (mencionado como ventaja).

**Argumento TCO ancla**: un programa institucional de monitores LG con calibración
anual TG-270 contratada es predecible y auditable. Versus compra reactiva de
monitores variados que generan no-cumplimiento intermitente.

**CTA correcto**: propuesta institucional con plan de QA.
- Email: "Solicito propuesta de programa de monitores diagnósticos para el servicio
  + plan de QA anual."
- Reunión técnica presencial en el servicio.

**Tono**: gerencial-técnico. Tablas, costos predecibles, KPIs de cumplimiento,
trazabilidad documentada.

---

## 4. Gerente Hospitalario / Director Médico privado

**Quién es**: decisor administrativo. Firma compras grandes. NO entra en tecnicismo
radiológico — eso lo lleva el jefe de servicio. El gerente compra **previsibilidad**
y **mitigación de riesgo**.

**Dolor primario verificable**:
- Riesgo regulatorio (multas, suspensión de servicios, mala praxis).
- Riesgo competitivo (hospital que no tiene equipo a la altura pierde médicos).
- Costo predecible vs gasto reactivo.
- Diferenciación competitiva del hospital privado.

**Cifra dura**: una demanda por error diagnóstico relacionado a calidad de imagen
es un costo de varios órdenes de magnitud sobre el costo del monitor. La inversión
en línea diagnóstica certificada es seguro de operación.

**Modelo LG asociado**: paquete institucional completo. No entrar en código de modelo
— hablar de "línea diagnóstica certificada FDA 510(k)" y "línea de revisión clínica".

**Dato técnico ancla**:
- Cumplimiento normativo verificable.
- Garantía LG + extensión Colé.
- Plan de QA anual contractual (servicio Colé).
- Trazabilidad para auditoría y aseguradora.

**Argumento TCO ancla**: el ROI del programa institucional se mide en evitar **un solo
evento adverso** (multa, demanda, mala praxis). Es seguro operacional, no gasto.
Costo/año predecible vs gasto reactivo no presupuestable.

**CTA correcto**: reunión ejecutiva con dossier de cumplimiento.
- Email: "Solicito reunión para evaluar programa de monitores diagnósticos para
  el servicio de imagenología."
- LinkedIn (perfil corporativo): casos de implementación documentados.

**Tono**: ejecutivo. Riesgo, costo predecible, diferenciación competitiva.
NO entrar en tecnicismo radiológico.

---

## 5. IT Hospitalario (integración PACS, infraestructura)

**Quién es**: responsable de infraestructura tecnológica. Decisor o influencer en
compra de displays porque debe integrarlos al PACS, RIS, HIS, red.

**Dolor primario verificable**:
- Compatibilidad con PACS instalado (típicamente Carestream, Sectra, Siemens,
  Agfa, Philips).
- Compatibilidad con tarjetas gráficas médicas (NVIDIA Quadro Medical, Barco MXRT).
- Soporte de drivers a largo plazo y actualizaciones.
- Integración con sistema de calibración remota o centralizada.

**Cifra dura**: monitor médico DisplayPort + DVI dual-link con resolución nativa
soportada por la tarjeta gráfica. Sin compatibilidad GPU, el monitor no entrega
su resolución certificada.

**Modelo LG asociado**: depende de configuración GPU del cliente. Toda la línea
diagnóstica LG soporta tarjetas Quadro Medical y MXRT estándar — `[VALIDAR-LG]`.

**Dato técnico ancla**:
- Conectividad: DisplayPort 1.4, DVI dual-link, HDMI según modelo.
- Compatibilidad con tarjetas gráficas certificadas médicas.
- Resolución nativa por modelo.
- Soporte de drivers Windows / Linux.

**Argumento TCO ancla**: estandarizar en LG reduce esfuerzo de integración cuando
se rotan equipos. Mismo perfil de driver, mismo procedimiento de calibración.

**CTA correcto**: especificación técnica de integración.
- Email: "Necesito spec de compatibilidad GPU + conectividad para integrar al PACS X."
- Reunión técnica con departamento IT.

**Tono**: técnico-IT. Sin lirismo. Cifras de conectividad, resoluciones soportadas,
compatibilidad de drivers.

---

## 6. Comprador técnico / Gestión de licitaciones privadas

**Quién es**: responsable de procurement. En hospitales privados grandes maneja
licitaciones formales con criterios técnicos y económicos. NO toma decisión clínica
— ejecuta proceso.

**Dolor primario verificable**:
- Cumplimiento técnico de cada oferta vs especificación.
- Comparabilidad de ofertas (precio, garantía, soporte, plazo).
- Trazabilidad documental para auditoría interna.
- Manejo de proveedores con histórico de incumplimiento.

**Cifra dura**: la oferta más barata pierde si no cumple especificación.
La oferta de mejor TCO instalado a igual cumplimiento gana cuando el comprador
está bien orientado.

**Modelo LG asociado**: depende de la especificación. El skill genera copy que
**facilita la elaboración de la especificación técnica** (no que la viole).

**Dato técnico ancla**:
- Modelo LG con especificación completa por línea.
- Garantía LG + extensión Colé (años exactos).
- Plazo de entrega + plazo de instalación.
- Soporte técnico local con SLA.

**Argumento TCO ancla**: hoja de cálculo TCO por años incluyendo precio inicial +
instalación + calibración + garantía + soporte. La transparencia ayuda al comprador
a defender la elección ante auditoría interna.

**CTA correcto**: paquete de cumplimiento técnico-comercial.
- Email: "Solicito propuesta técnica completa con TCO instalado a 5 años para
  línea diagnóstica."
- Tabla comparativa interna (entregable Colé).

**Tono**: documental, completo, sin opiniones. Cumplimiento punto por punto contra
la especificación.

---

## Cross-references entre personas

| Si la solicitud menciona... | Persona principal | Considerar también |
|---|---|---|
| "radiólogo", "lectura primaria", "diagnóstico" | Radiólogo | Físico médico, Jefe de Servicio |
| "calibración", "QA", "AAPM TG-270" | Físico médico | Jefe de Servicio |
| "compra para mi servicio" | Jefe de Servicio | Gerente Hospitalario, Físico médico |
| "hospital privado", "clínica grande" | Gerente Hospitalario | + Jefe de Servicio relevante |
| "PACS", "integración", "infraestructura" | IT Hospitalario | Físico médico |
| "licitación privada", "RFP", "spec técnica" | Comprador técnico | + Jefe de Servicio |
| "mamografía" | Radiólogo (mamógrafo) + Físico médico + Jefe Mamografía | (caso especial — exige cumplimiento ACR) |

## Cuándo el copy va al influencer vs al firmante

- **Influencer (radiólogo, físico, IT)**: copy **técnico**. Cifras, normas, demos.
  No precios. CTA es "agendar evaluación técnica".
- **Firmante (jefe servicio, gerente, comprador)**: copy **gerencial**. TCO,
  riesgo, predictibilidad, garantía, soporte. Precios SÍ aparecen, pero como TCO/año.

Misma persona en una venta puede recibir **dos copys distintos** en dos canales
distintos. El skill debe respetar esa segregación.

## Personas NO incluidas (escalar antes de proceder)

- Pacientes finales (no aplica — los monitores médicos son B2B).
- Sector público (CCSS, MINSA, hospitales públicos) — fuera de scope del skill.
- Investigación / academia — generalmente requiere argumentación distinta (research-grade).
- Veterinaria (LG no tiene línea veterinaria certificada — no recomendar).
