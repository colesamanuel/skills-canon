---
name: wikiforge
description: >
  Convierte cualquier colección de documentos en una wiki de conocimiento
  interconectada en Obsidian, siguiendo el patrón LLM Wiki de Karpathy.
  Ingesta transcripciones de YouTube, cursos, reuniones Meet/Zoom, informes,
  PDFs, artículos web, podcasts, hilos de Slack y notas sueltas — y los
  transforma en páginas markdown con wikilinks, frontmatter YAML e índice
  navegable. Activar siempre que el usuario mencione "wiki", "segundo cerebro",
  "base de conocimiento", "knowledge base", "obsidian", "ingestar", "organizar
  notas", "organizar transcripciones", "crear wiki", "LLM wiki", "wiki
  Karpathy", "wikiforge", o quiera estructurar cualquier corpus de documentos
  en un sistema de conocimiento. También activar cuando pida consultar,
  mantener, hacer lint, o ampliar una wiki existente, o conectar varias wikis
  entre sí. Si el usuario tiene documentos desordenados y quiere orden, esta
  es la skill.
---

# WikiForge

Transforma documentos en bruto en wikis de conocimiento vivas.

La idea central es simple: en lugar de que el LLM redescubra el conocimiento
cada vez que le preguntas algo (como hace RAG), aquí el LLM lee las fuentes
una vez, extrae el conocimiento, y lo organiza en páginas markdown
interconectadas que se enriquecen con cada fuente nueva. El conocimiento
se compila y se acumula — no se re-deriva en cada consulta.

Obsidian es el IDE. El LLM es el programador. La wiki es el código.

---

## Cómo funciona — Las 5 operaciones

WikiForge tiene 5 operaciones. Cada una se puede invocar individualmente,
pero el flujo típico es: SETUP → INGEST (batch) → QUERY → LINT → repetir.

### SETUP — Crear un vault nuevo

Antes de crear nada, entender el proyecto. Si el usuario da material sin
explicar nada, inferir todo del contenido — es mejor actuar que preguntar.
Si hay ambigüedad real, preguntar solo lo imprescindible:

- **Dominio** (¿de qué trata?)
- **Tipos de fuente** (¿qué material va a entrar?)
- **Objetivo** (¿consulta personal, agentes, contenido, estudio?)

Con eso, decidir las categorías de la wiki (subcarpetas bajo `wiki/`) y
los tipos de entidad a extraer. Después:

1. Crear la estructura de carpetas (ver Arquitectura abajo)
2. Mover las fuentes del usuario a `raw/`
3. Generar `CLAUDE.md` en la raíz — leer `references/claude-md-template.md`
   de esta skill y adaptarlo al dominio concreto sustituyendo los placeholders
4. Crear `wiki/index.md` y `wiki/log.md` vacíos

#### Detectar estructura interna de las fuentes

Antes de ingestar, analizar cómo están organizadas las fuentes. Los corpus
no son todos iguales — un curso tiene módulos y lecciones, una serie de
reuniones tiene fechas y participantes, un canal de Slack tiene hilos y
autores. Detectar esta estructura es clave para decidir la granularidad
de las páginas `fuentes/` y cómo vincular los archivos originales.

Patrones comunes y cómo mapearlos:

| Estructura del corpus | Granularidad de `fuentes/` | Vinculación a raw |
|---|---|---|
| Curso con módulos y lecciones | Una página fuente por módulo, con wikilinks a cada lección individual | `## Transcripciones del módulo` con [[nombre-leccion]] |
| Reuniones periódicas de un equipo | Una página fuente por reunión (o por sprint/semana si hay muchas) | `## Actas originales` con [[nombre-acta]] |
| Canal de Slack / Discord | Una página fuente por hilo relevante o por tema recurrente | `## Hilos originales` con [[nombre-hilo]] |
| Colección de artículos / PDFs | Una página fuente por documento | `## Documento original` con [[nombre-documento]] |
| Vídeos de YouTube sueltos | Una página fuente por vídeo | `## Transcripción original` con [[nombre-transcripcion]] |
| Notas sueltas del usuario | Agrupar por tema si hay patrón, o una página por nota si no | `## Notas originales` con [[nombre-nota]] |

La regla general: cada página `fuentes/` debe incluir wikilinks a todos
los archivos raw que cubre. Esto es lo que hace que aparezcan conectados
en el grafo de Obsidian — sin estos enlaces, los archivos originales
flotan desconectados y la wiki pierde navegabilidad.

#### Arquitectura del vault

```
vault-nombre/
├── CLAUDE.md              ← Schema: cómo opera el LLM sobre este vault
├── raw/                   ← Fuentes originales — INMUTABLES
│   └── [estructura libre del usuario]
├── wiki/
│   ├── index.md           ← Catálogo maestro (enlace + resumen de cada página)
│   ├── log.md             ← Historial cronológico de operaciones
│   ├── hot.md             ← (opcional) Cache de contexto reciente
│   ├── fuentes/           ← Un resumen por cada fuente ingestada (SIEMPRE)
│   └── [categorias]/      ← Subcarpetas adaptadas al dominio
└── .obsidian/
```

La carpeta `fuentes/` es obligatoria. Las demás subcarpetas dependen del
dominio. Algunos ejemplos:

| Dominio | Subcarpetas típicas |
|---|---|
| Curso / educación | `tecnicas/`, `conceptos/`, `herramientas/`, `ejemplos/` |
| Negocio / equipo | `decisiones/`, `proyectos/`, `personas/`, `metricas/` |
| Investigación | `hallazgos/`, `metodologias/`, `autores/`, `hipotesis/` |
| YouTube / contenido | `temas/`, `herramientas/`, `frameworks/`, `personas/` |
| Personal | `objetivos/`, `ideas/`, `contactos/`, `reflexiones/` |

---

### INGEST — Procesar fuentes

Esta es la operación central. Por cada fuente:

1. **Leer** la fuente completa
2. **Clasificar** el tipo (transcripción, informe, artículo, reunión, notas...)
3. **Extraer entidades** del dominio — el contenido real dicta qué extraer,
   no una lista fija. Buscar: conceptos, técnicas, herramientas, personas,
   decisiones, datos, ejemplos, relaciones causales.
4. **Crear o actualizar** páginas wiki:
   - Siempre una página en `fuentes/` con el resumen de la fuente
   - Incluir en cada página `fuentes/` los wikilinks a cada archivo raw
     individual que cubre (ver "Detectar estructura interna" arriba)
   - Páginas temáticas en las categorías correspondientes
   - Si una página ya existe → **ampliar con el contenido nuevo**, no duplicar

   Esto es fundamental: cada fuente nueva puede tocar 5-15 páginas
   existentes. La wiki crece en profundidad, no solo en cantidad.

5. **Enlazar densamente** con `[[wikilinks]]` — el grafo de Obsidian es
   tan útil como la densidad de sus conexiones. Reglas de enlazado:
   - Mínimo 8 wikilinks por página, distribuidos en el cuerpo del texto
     (no solo agrupados en una sección "Relaciones" al final)
   - Cada mención de un concepto, herramienta, técnica o caso que tenga
     página propia debe ser un `[[wikilink]]`
   - Usar `[[nombre-pagina|Texto visible]]` cuando el nombre de la página
     difiera del texto en la frase
   - Buscar equilibrio: no solo enlazar a las 3-4 páginas principales,
     sino también a páginas menos centrales que sean relevantes

6. **Actualizar** `wiki/index.md` con las nuevas entradas
7. **Registrar** en `wiki/log.md` con formato:
   ```
   ## [YYYY-MM-DD] ingest | Nombre de la fuente
   - Páginas creadas: X
   - Páginas actualizadas: Y
   - Entidades extraídas: lista breve
   ```

#### Reglas según tipo de fuente

- **Transcripciones** (YouTube, cursos, podcasts): Limpiar muletillas y
  repeticiones del habla. Extraer la estructura lógica, no la temporal.
  Preservar ejemplos prácticos textuales.
- **Reuniones**: Preservar quién dijo qué si es relevante. Extraer
  decisiones, acciones pendientes y contexto de las discusiones.
- **Informes / PDFs**: Respetar estructura del documento. Extraer datos
  cuantitativos, conclusiones y recomendaciones.
- **Artículos web**: Distinguir hechos de opiniones. Registrar autor,
  fecha y URL en el frontmatter.
- **Notas del usuario**: Fuente primaria de alta prioridad. Integrar
  respetando la intención original.

#### Idioma

Todas las páginas wiki se escriben en el mismo idioma que las fuentes.
Detectar el idioma al inicio del proceso y mantenerlo de forma estricta
en todas las páginas — títulos, secciones, cuerpo de texto, todo.

Esto es especialmente importante cuando se delega trabajo a subagentes:
el idioma debe ser una instrucción explícita en cada prompt de delegación.
Los subagentes tienden a escribir en inglés por defecto si no se les indica
lo contrario, y esto produce wikis con mezcla de idiomas que confunden.

Los nombres técnicos de productos (Canvas, Deep Research, Gems) se
mantienen como están. Los wikilinks nunca se traducen.

#### Formato de página wiki

Copiar este bloque exacto como plantilla. Los cinco campos de frontmatter
son obligatorios — no usar otros nombres de campo como `title`,
`description`, `slug` o `created`:

```markdown
---
tags: [categoria, subcategoria]
tipo: tecnica | concepto | persona | herramienta | decision | fuente
fuentes: ["nombre-fuente-original"]
fecha_creacion: YYYY-MM-DD
fecha_actualizacion: YYYY-MM-DD
---

# Título

Descripción clara y concisa en 2-3 párrafos. Incluir [[wikilinks]]
a las páginas relacionadas directamente en el texto.

## Detalle

Desarrollo del contenido con [[wikilinks]] entretejidos en cada
párrafo donde se mencionen entidades con página propia.

## Ejemplo / Evidencia

> Cita o ejemplo concreto extraído de las fuentes.

## Relaciones

- Véase también: [[pagina-relacionada]]
- Depende de: [[concepto-previo]]
- Se conecta con: [[otra-pagina]]

## Fuentes

- [[fuente-original]]
```

#### Batch ingest

Cuando hay muchas fuentes de golpe:

1. Listar todo lo que hay en `raw/`
2. Decidir un orden lógico (cronológico, por complejidad, o por
   dependencias conceptuales — lo básico primero para que los conceptos
   fundamentales existan antes de que lleguen los avanzados)
3. Procesar una a una, actualizando index y log tras cada una
4. Al terminar, ejecutar un LINT obligatorio (ver checklist abajo)

#### Delegación a subagentes

Cuando el volumen de fuentes requiere paralelizar el trabajo con
subagentes, cada prompt de delegación debe incluir:

1. **El idioma obligatorio** — "Escribe todo en [idioma detectado]"
2. **El bloque exacto de frontmatter** — copiar la plantilla literal
   para que no inventen campos propios
3. **La lista completa de páginas wiki existentes** — para que los
   wikilinks apunten a páginas reales y no fantasmas
4. **El mínimo de wikilinks** — "Mínimo 8 wikilinks por página,
   distribuidos en el cuerpo del texto"

Sin estas 4 instrucciones explícitas, los subagentes producen páginas
en inglés, con frontmatter inconsistente, con pocos links, o con links
a páginas que no existen. Esto se ha verificado en la práctica.

---

### QUERY — Consultar la wiki

1. Leer `wiki/index.md` para localizar páginas relevantes
2. Leer las páginas identificadas
3. Sintetizar respuesta con citas a las páginas wiki
4. Si la respuesta genera contenido nuevo valioso → ofrecerlo como
   nueva página wiki (las exploraciones también componen conocimiento)
5. Si no hay respuesta → señalar gaps y buscar con web search si hay acceso

---

### LINT — Mantenimiento

Ejecutar después de cada batch ingest y periódicamente. No es opcional
después de un batch — los problemas se acumulan rápido.

#### Checklist obligatoria post-batch

Ejecutar todos estos checks y reportar resultados con números concretos:

1. **Frontmatter**: 100% de páginas deben tener los 5 campos exactos
   (`tags`, `tipo`, `fuentes`, `fecha_creacion`, `fecha_actualizacion`).
   Contar cuántas cumplen y cuántas no. Corregir las que fallen.

2. **Idioma**: Verificar que el 100% de las páginas están en el idioma
   de las fuentes. Forma rápida: contar palabras comunes del idioma
   esperado vs palabras en otros idiomas en cada archivo. Corregir
   las que estén en idioma incorrecto.

3. **Fantasmas**: 0 wikilinks rotos (que apunten a páginas inexistentes).
   Listar todos los targets de `[[wikilinks]]` y verificar que existen
   como archivos `.md`. Crear las páginas faltantes o corregir los links.

4. **Densidad de links**: Todas las páginas temáticas deben tener al
   menos 8 wikilinks. Contar por archivo y corregir las que estén por
   debajo.

5. **Equilibrio de enlaces entrantes**: Contar cuántas páginas enlazan
   a cada página (enlaces entrantes). Si alguna página temática tiene
   menos de 5 entrantes, añadir enlaces desde páginas relacionadas.
   El objetivo es que no haya clusters sobre-conectados junto a páginas
   casi aisladas.

6. **Archivos raw vinculados**: Verificar que todos los archivos en
   `raw/` aparecen referenciados como `[[wikilink]]` desde al menos
   una página en `fuentes/`. Los que no estén conectados, conectarlos.

7. **Huérfanas**: Páginas wiki sin enlaces entrantes. Conectarlas o
   evaluar si deben eliminarse.

8. **Gaps**: Conceptos mencionados repetidamente sin página propia.
   Crear las páginas faltantes.

Registrar todo en `wiki/log.md` con los números del check.

---

### MERGE — Conectar wikis (opcional)

Si hay múltiples vaults:

1. Listar las wikis y sus dominios
2. Identificar entidades compartidas
3. Crear enlaces inter-vault o proponer consolidación
4. No mezclar las carpetas `raw/` de proyectos distintos

---

## Convenciones de estilo

Estas reglas existen para que la wiki sea navegable y consistente a medida
que crece. Sin convenciones, las wikis grandes se vuelven un caos:

- **Idioma**: El del material fuente (detectar al inicio, mantener
  estrictamente en toda la wiki — ver sección "Idioma" arriba)
- **Nombres de archivo**: kebab-case sin tildes ni caracteres especiales
  (`cadena-de-pensamiento.md`, no `Cadena de Pensamiento.md`)
- **Frontmatter YAML**: Usar exactamente estos 5 campos en todas las
  páginas: `tags`, `tipo`, `fuentes`, `fecha_creacion`,
  `fecha_actualizacion`. No usar alternativas como `title`, `description`,
  `slug`, `created`, `category` u otros.
- **Wikilinks**: `[[nombre-archivo]]` sin extensión `.md`. Mínimo 8 por
  página, distribuidos en el cuerpo del texto. Usar
  `[[nombre|Texto visible]]` cuando el nombre del archivo no coincida
  con el texto natural de la frase.
- **Brevedad**: 200-500 palabras por página. Si crece más, dividir.
  Las páginas cortas se leen, las largas se ignoran.
- **Sin duplicación**: Si el contenido ya existe, enlazar. No copiar.
- **Evidencia**: Incluir siempre al menos un ejemplo concreto o dato
  específico por página. Las páginas abstractas sin evidencia no aportan.

---

## Referencia

- `references/claude-md-template.md` — Plantilla adaptable del CLAUDE.md
  que se genera en cada vault nuevo. Leer antes de ejecutar SETUP.
