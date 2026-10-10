---
name: loop-designer
description: >-
  Diseñador de bucles iterativos (patrón generador-evaluador / self-refine) para
  tareas de la IA. NO ejecuta el bucle: decide si conviene y emite sus parámetros
  (tarea atómica, criterio de parada verificable, freno). Activar SOLO cuando el
  usuario pida explícitamente diseñar, evaluar o parametrizar un bucle iterativo
  con frases como: "diseña el bucle/loop para…", "¿conviene iterar aquí?",
  "¿vale la pena un bucle/loop?", "parametriza el loop", "evalúa si usar un loop",
  "convierte esto en un bucle iterativo", "patrón generador-evaluador",
  "self-refine", "loop iterativo", "¿debería iterar esta tarea?", o cuando pida
  el gate de decisión sobre iteración. Activar aunque la solicitud parezca simple
  — el gate de tres condiciones y la verificabilidad del criterio requieren
  disciplina activa. NO activar para peticiones genéricas de "hazlo exhaustivo"
  o "revisa todo" que no pidan diseñar el bucle; NO activar como motor de
  ejecución de un bucle ya diseñado.
---

# loop-designer

## Qué es y qué NO es

Diseña bucles iterativos para tareas de la IA bajo el patrón **generador–evaluador**
(literatura: Self-Refine, Madaan et al. 2023; Reflexion, Shinn et al. 2023). El
bucle vence un límite concreto —la degradación de atención sobre contexto largo
(*Lost in the Middle*, Liu et al. 2023)— mediante troceo + cobertura repetida, no
por "magia iterativa".

**Límite duro:** este skill es un **parametrizador en tiempo de diseño**, no un
motor de iteración. Un skill es referencia cargada en contexto, no una estructura
de control. El loop real lo ejecuta un `while` (API/Claude Code) o un iterador
(Make.com). En chat solo se *simula* — declararlo siempre (ver Fase 2).

**Principio rector:** el criterio de parada lo verifica algo **distinto** del mismo
juicio generativo. Un modelo que no detecta un error al generar tampoco lo detecta
al evaluar (punto ciego correlacionado). El bucle amplifica lo verificable, no lo
que el modelo no puede ver. Por eso el GATE exige criterio externo medible — nunca
"que quede bien".

## Flujo obligatorio (3 fases, en orden)

### FASE 0 — GATE de decisión (tres condiciones en AND)

El bucle conviene **solo si se cumplen las TRES**. Falla cualquiera → prompt
estructurado de una pasada; abortar el diseño del loop y decirlo.

1. **Cobertura sub-óptima en una pasada.** Fuente larga o espacio de búsqueda
   amplio donde un solo recorrido deja huecos (extracción normativa extensa,
   libro/informe completo, lote grande de registros, barrido multi-criterio).
   Si la tarea cabe holgada en una pasada → falla.

2. **Criterio de parada externamente verificable.** Conteo, regex, suma que
   cuadra, contraste contra norma, validación de esquema. Algo que un script o
   una comprobación objetiva pueda evaluar sin re-emitir un juicio subjetivo.
   Si el único criterio posible es "calidad", "que esté bien redactado",
   "que se vea profesional" → falla. Estos son juicios subjetivos: el loop no
   los mejora de forma fiable.

3. **Valor marginal > costo marginal.** La exhaustividad extra justifica los
   tokens/tiempo/iteraciones. Si el cuello de botella es otra cosa (p. ej.
   frescura de un dato en vivo, no profundidad de análisis) → falla; iterar no
   vuelve fresco un dato obsoleto.

**Salida de la Fase 0:** veredicto explícito `LOOP` o `NO-LOOP`, con la condición
que falla si aplica. No avanzar a Fase 1 sin `LOOP`.

### FASE 1 — Parámetros (la tripleta)

Solo si Fase 0 = `LOOP`. Emitir los tres elementos:

- **Tarea atómica:** la unidad mínima que se repite por iteración, anclada a la
  unidad de troceo real (capítulo, artículo del decreto, factura, barrera de
  blindaje, registro, tema del temario). Una iteración = una unidad. Si no hay
  unidad natural de troceo, replantear el troceo antes de seguir.

- **Criterio de parada (booleano comprobable):** expresar como condición que
  evalúa Verdadero/Falso de forma objetiva. Ejemplos válidos:
  `len(lista) == N`, `cada barrera tiene D_sem numérico vs límite P`,
  `dos pasadas consecutivas no añaden elementos`, `toda transacción cruzada o
  marcada`, `cada tema tiene ≥ N preguntas`. Prohibido criterio no medible.

- **Freno (triple, todos obligatorios):**
  1. `max_iter` duro (tope numérico de seguridad de costo).
  2. Condición de meta lograda (el criterio booleano anterior se cumple).
  3. **Detector de no-progreso:** dos iteraciones que producen salida idéntica
     o sin novedades → salir. Evita oscilación y consumo infinito.

### FASE 2 — Substrato de ejecución

Mapear el diseño al contenedor donde corre de verdad. Declarar siempre cuál
aplica y su grado de control:

| Substrato | Control real | Cómo se implementa |
|---|---|---|
| **Chat (claude.ai)** | Simulado, sin control de flujo | Troceo explícito en un turno (recorrer unidades dentro de la respuesta). Degradado: vuelve a chocar con el límite de atención si el troceo no es estricto. **Declarar la limitación.** |
| **Claude Code / API** | Real | `while` con `max_iterations` + verificación programática del criterio (script que cuenta/valida) entre iteraciones. Substrato preferido cuando importa la automatización. |
| **Make.com** | Real | Iterador + módulo de verificación + flag/contador de salida. Para flujos ya orquestados (iGMS, Gmail, Odoo). |

Regla: si el usuario pide "automático" de verdad, **no proponer chat**; dirigir a
Claude Code/API o Make. Si solo hay chat disponible, degradar elegantemente y
declarar que es simulación, no bucle controlado.

## Plantilla de salida OBLIGATORIA

Toda invocación cierra con esta estructura (alineada con el cierre operativo del
Perfil Estratégico del titular):

```
## Veredicto del GATE
LOOP / NO-LOOP — [condición que falla si NO-LOOP]

## Parámetros del bucle   (solo si LOOP)
- Tarea atómica: …
- Unidad de troceo: …
- Criterio de parada (booleano): …
- Freno: max_iter=N · meta=[criterio] · no-progreso=[regla]

## Substrato
[Chat simulado | Claude Code/API | Make.com] — [grado de control + limitación]

## Esqueleto ejecutable   (solo si LOOP y substrato = Code/Make)
[pseudocódigo while/iterador con la verificación del criterio explícita]

## Cierre
1. Recomendación  2. Pasos concretos  3. Riesgos y mitigación
4. Confianza (🟢🟡🟠🔴)
```

## Mapeo a skills del canon (envolver, no duplicar)

Cuando la tarea iterativa corresponde a un dominio que ya tiene skill, este
diseñador **envuelve** ese skill en el bucle; no reescribe su lógica. Casos
típicos del titular:

- Extracción/auditoría normativa extensa → `manuales-pr-44653`,
  `autorizaciones-pr-44653` (recorrer artículo por artículo del Decreto 44653-S).
- Auditoría de facturas, hallazgos H1–H15 → `odoo-invoice-auditor-v2b`
  (recorrer cada categoría hasta sin coincidencias).
- Banco de preguntas Anexo XIII → `exam-bank-converter` / `minsa-course-format`
  (iterar hasta ≥ N preguntas por tema).
- Verificación de blindaje barrera por barrera → `shielding-verification`
  (cada barrera con D_sem vs límite P, contraste NCRP 147).
- Reconciliación 4 vías → `card-reconciler` (iterar hasta toda transacción
  cruzada o marcada).

Si el dominio NO tiene skill, el diseñador opera autónomo igual.

## Antipatrones (rechazar o corregir)

- **Loop sin criterio verificable** ("itera hasta que quede bien"): el GATE lo
  bloquea en la condición 2. Reconvertir a prompt estructurado o pedir un
  criterio medible.
- **Loop por moda en tarea simple:** briefing bursátil, copy corto, respuesta de
  una pasada. El valor está en otra parte; el GATE falla en condición 1 o 3.
- **"Automático" en chat:** prometer control de flujo que el chat no tiene.
  Siempre declarar simulación.
- **Sin freno:** multiplica tokens y puede oscilar. Freno triple no negociable.
- **Confiar en autoevaluación pura:** sin verificación externa el loop arrastra
  el punto ciego del generador. El criterio externo es el corazón del patrón.

## Nivel de confianza del propio skill

🟢 Alta en la mecánica generador-evaluador y sus límites (peer-reviewed).
🟡 Media en cuándo el substrato "chat" basta vs. exige Code/Make — depende del
grado de automatización que el titular requiera en cada caso, que él decide.
