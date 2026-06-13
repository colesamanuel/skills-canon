---
name: wiki-query
description: >
  Busca y responde preguntas consultando la wiki de conocimiento del vault
  activo (patrón LLM Wiki / Karpathy). Activar siempre que el usuario diga
  "busca en la wiki", "consulta la wiki", "qué dice la wiki sobre",
  "encuentra en la wiki", "wiki search", "buscar en mis notas", "qué tengo
  sobre", "en qué fuente se habla de", "qué páginas cubren", o cualquier
  pregunta cuya respuesta esté en la wiki del vault actual. También activar
  cuando el usuario haga preguntas sobre temas que claramente están cubiertos
  por el vault — incluso sin mencionar "wiki". Si existe una carpeta wiki/
  con un index.md en la carpeta seleccionada, este skill es el camino
  más rápido para responder.
---

# Wiki Query — Búsqueda inteligente en cualquier wiki LLM

Este skill implementa el flujo QUERY del patrón LLM Wiki: buscar información
en la wiki de forma rápida y estructurada, sin dar vueltas innecesarias.

Funciona con cualquier vault que siga la estructura estándar de wiki LLM,
independientemente del tema (un curso, un proyecto, notas personales, etc.).

## Paso 0 — Descubrir la wiki

Antes de buscar, localiza la wiki en la carpeta seleccionada por el usuario.
Busca una carpeta `wiki/` que contenga un archivo `index.md`. Este archivo
es el catálogo maestro y el punto de entrada obligatorio.

Si no encuentras `wiki/index.md`, comprueba si existe un `CLAUDE.md` en la
raíz — puede indicar dónde está la wiki o cómo se llama la carpeta principal.

Si no hay wiki, díselo al usuario: "No encuentro una wiki en esta carpeta.
¿Quieres que la cree?" (y en ese caso, usa el skill wikiforge).

## Paso 1 — Escanear el índice

Lee `wiki/index.md`. Este archivo lista todas las páginas de la wiki con un
resumen de una línea cada una. Está organizado por categorías (las subcarpetas
de la wiki).

Con el índice puedes identificar qué 1-3 páginas son relevantes para la
pregunta del usuario. La clave: el índice ya te dice de qué va cada página.
No necesitas abrir todas — solo las que encajen.

## Paso 2 — Leer las páginas relevantes

Abre solo las páginas identificadas en el paso anterior. Cada página tiene:

- **Frontmatter YAML**: tags, tipo, fuentes, fechas — útil para filtrar
- **Contenido**: el texto con la información
- **Wikilinks** `[[nombre-pagina]]`: enlaces a páginas relacionadas

Si una página referencia otra vía wikilink y esa referencia parece importante
para completar la respuesta, ábrela también. Pero no hagas cadenas largas
de lecturas — 2-3 páginas suelen bastar.

## Paso 3 — Sintetizar y responder

Responde la pregunta del usuario citando las páginas wiki consultadas.
Formato natural y directo. Al final, incluye las fuentes como referencias:

> Fuentes: [[nombre-pagina-1]], [[nombre-pagina-2]]

## Cuándo ir a las fuentes originales

Muchas wikis tienen una carpeta `raw/` con los materiales en bruto
(transcripciones, artículos, documentos originales). Son inmutables.

Solo ve a `raw/` si:

- El usuario pide la cita textual exacta
- La wiki no tiene suficiente detalle para responder
- Necesitas verificar algo específico

Las páginas en la subcarpeta `fuentes/` de la wiki suelen ser resúmenes de
cada fuente original — funcionan como puente entre la wiki procesada y el
material en bruto. Consúltalas primero antes de ir directo a `raw/`.

## Lo que NO debes hacer

- **No busques con grep ni lances agentes**. El índice existe precisamente
  para evitar búsquedas brutas. Úsalo.
- **No leas todas las páginas "por si acaso"**. Lee el índice, identifica
  las relevantes, y ve directo.
- **No respondas sin consultar la wiki**. La gracia de este skill es que
  la respuesta viene de las páginas, no de conocimiento general.
- **No inventes información**. Si no está en la wiki, dilo con claridad.
  Puedes sugerir al usuario ingestar nueva información con wikiforge.
