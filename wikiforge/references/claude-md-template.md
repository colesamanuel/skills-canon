# CLAUDE.md — {{NOMBRE_WIKI}}

{{DESCRIPCION_PROYECTO}}

Patrón LLM Wiki (Karpathy): el LLM construye y mantiene una wiki de
markdown interconectada a partir de fuentes en bruto. Las fuentes son
inmutables. La wiki es propiedad del LLM.

## Estructura del vault

```
raw/              → Fuentes originales. NUNCA modificar.
wiki/             → Páginas generadas y mantenidas por el LLM.
  index.md        → Catálogo maestro: enlace + resumen de cada página.
  log.md          → Historial cronológico de operaciones.
  hot.md          → (opcional) Contexto reciente para agentes externos.
  fuentes/        → Un resumen por cada fuente ingestada (SIEMPRE).
  {{CATEGORIAS}}
```

## Idioma

Todas las páginas de esta wiki se escriben en **{{IDIOMA}}**.
Esto incluye títulos, secciones, cuerpo de texto — todo.
Los nombres técnicos de productos se mantienen como están.
Los wikilinks nunca se traducen.

Si delegas trabajo a subagentes, incluye siempre esta instrucción
explícita: "Escribe todo en {{IDIOMA}}".

## Navegación

1. Empieza siempre por `wiki/index.md` — es el mapa de todo.
2. Sigue los `[[wikilinks]]` para profundizar.
3. Solo lee `raw/` si necesitas la fuente original textual.

## Estructura de las fuentes

{{ESTRUCTURA_FUENTES}}

Cada página en `fuentes/` debe incluir wikilinks a los archivos raw
individuales que cubre. Esto es lo que conecta los archivos originales
en el grafo de Obsidian — sin estos enlaces, las fuentes flotan
desconectadas y la wiki pierde navegabilidad.

## Ingest — Añadir una fuente nueva

1. Lee la fuente completa de `raw/`.
2. Clasifica el tipo: {{TIPOS_FUENTE}}.
3. Extrae entidades del dominio: {{TIPOS_ENTIDAD}}.
4. Crea una página en `fuentes/` con el resumen. Incluye wikilinks
   a cada archivo raw individual que cubra la fuente.
5. Crea o amplía páginas temáticas en las subcarpetas. Si la página ya
   existe, amplía — no dupliques.
6. Enlaza con `[[wikilinks]]` — mínimo 8 por página, distribuidos
   en el cuerpo del texto (no solo agrupados al final).
7. Actualiza `wiki/index.md`.
8. Registra en `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | Nombre de la fuente
   - Páginas creadas: X
   - Páginas actualizadas: Y
   - Entidades extraídas: lista breve
   ```

## Query — Responder preguntas

1. Lee `wiki/index.md` para localizar páginas relevantes.
2. Lee las páginas necesarias.
3. Sintetiza con citas a las páginas wiki.
4. Si la respuesta es valiosa, ofrece guardarla como página nueva.

## Lint — Mantenimiento obligatorio post-batch

Ejecutar todos estos checks y reportar números concretos:

1. **Frontmatter**: 100% de páginas con exactamente estos 5 campos:
   `tags`, `tipo`, `fuentes`, `fecha_creacion`, `fecha_actualizacion`.
   No usar alternativas como `title`, `description`, `slug`, `created`.
2. **Idioma**: 100% de páginas en {{IDIOMA}}.
3. **Fantasmas**: 0 wikilinks rotos (que apunten a páginas inexistentes).
4. **Densidad de links**: Todas las páginas temáticas con al menos
   8 wikilinks, distribuidos en el cuerpo del texto.
5. **Equilibrio de entrantes**: Todas las páginas temáticas con al
   menos 5 enlaces entrantes. Si alguna tiene menos, añadir enlaces
   desde páginas relacionadas.
6. **Raw vinculados**: Todos los archivos en `raw/` referenciados como
   `[[wikilink]]` desde al menos una página en `fuentes/`.
7. **Huérfanas**: Páginas wiki sin enlaces entrantes — conectarlas.
8. **Gaps**: Conceptos mencionados repetidamente sin página propia —
   crearlas.

Registrar resultados en `wiki/log.md`.

## Delegación a subagentes

Cuando delegues trabajo a subagentes, cada prompt debe incluir:

1. **Idioma**: "Escribe todo en {{IDIOMA}}"
2. **Frontmatter**: Copiar la plantilla exacta (ver Convenciones)
3. **Lista de páginas existentes**: Para que los wikilinks apunten
   a páginas reales
4. **Mínimo de wikilinks**: "Mínimo 8 wikilinks por página,
   distribuidos en el cuerpo del texto"

## Convenciones

- Idioma: {{IDIOMA}}.
- Archivos: kebab-case sin tildes (`cadena-de-pensamiento.md`).
- Frontmatter YAML obligatorio — usar exactamente estos 5 campos:
  ```yaml
  tags: [categoria, subcategoria]
  tipo: tecnica | concepto | persona | herramienta | decision | fuente
  fuentes: ["nombre-fuente-original"]
  fecha_creacion: YYYY-MM-DD
  fecha_actualizacion: YYYY-MM-DD
  ```
  No usar `title`, `description`, `slug`, `created`, `category` u otros.
- Wikilinks: `[[nombre-archivo]]` sin extensión. Mínimo 8 por página.
  Usar `[[nombre|Texto visible]]` cuando el nombre del archivo no
  coincida con el texto natural de la frase.
- Páginas: 200-500 palabras. Si crece más, dividir.
- Evidencia concreta en cada página (ejemplos, datos, citas).
- No duplicar: si ya existe, enlazar.
