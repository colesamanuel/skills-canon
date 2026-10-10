---
name: gmail-briefing
description: >
  Genera un reporte consolidado ejecutando 3 tareas automáticas: (A) revisión de correos Gmail últimos 7 días
  con identificación de urgentes y estado de respuesta, (B) creación de eventos en Google Calendar
  con recordatorios para correos que requieran acción, (C) listado de eventos ±7 días con detección
  de conflictos. Opcionalmente, (D) creación de borrador de correo-resumen ejecutivo solo cuando el usuario lo solicite. Activar con: "revisa mi correo", "qué hay en Gmail", "briefing", "briefing diario",
  "reporte de correo y calendario", "qué llegó", "correos nuevos", "qué hay hoy", "reporte diario",
  "novedades de correo", "hay correos de [remitente]", o cualquier consulta que implique leer,
  clasificar o resumir correos y/o revisar la agenda. Activar incluso si la solicitud parece simple
  — el contexto de negocio requiere priorización activa, creación de eventos y detección de conflictos.
---

# Gmail + Calendar Briefing — Colé S.A.

> **Versión 2.1** (28-may-2026). Changelog: (1) Paso A1 — añadido barrido amplio obligatorio del INBOX como red de seguridad contra falsos negativos de cobertura (dominios/keywords no listados). (2) Regla dura #15 — verificación de threads largos (N≥5) cuya fecha visible en `search_threads` puede estar truncada. (3) Nombres de herramientas MCP actualizados a la nomenclatura real (`Gmail:*`, `Google Calendar:*`). Edición quirúrgica bajo Perfil Operativo §4.3.

## Herramientas MCP requeridas

- **Gmail MCP** — `Gmail:search_threads`, `Gmail:get_thread`
- **Google Calendar MCP** — `Google Calendar:list_events`, `Google Calendar:create_event`

Si algún MCP no está disponible, declararlo explícitamente. No simular resultados.

---

## Flujo de ejecución — 4 tareas obligatorias

### TAREA A — Correos (últimos 7 días)

**Paso A1: Búsqueda segmentada**

Ejecutar estas queries en Gmail (`newer_than:7d` en todas):

| Segmento | Query |
|---|---|
| Institucional / regulatorio | `from:(ccss.sa.cr OR misalud.go.cr OR msj.go.cr OR fundauna.org OR oiea.org OR iaea.org OR sugef.fi.cr OR minsa.go.cr) newer_than:7d` |
| Cotizaciones / clientes / licitaciones | `(cotización OR quote OR proforma OR factura OR "purchase order" OR licitación OR adjudicación OR SICOP) newer_than:7d` |
| Reservas Airbnb / Vrbo / iGMS | `from:(airbnb.com OR vrbo.com OR automated@airbnb.com OR igms.com) newer_than:7d` |
| Proveedores activos | `from:(ups.com OR radiationgroup.com OR connexisint.com OR iba-dosimetry.com OR radcal.com OR polimaster.com OR ludlums.com OR standardimaging.com OR leedstestobjects.com OR diagnomatic.com OR klaritymedical.com OR ezag.com OR radixray.com OR lge.com OR xstrahl.com) newer_than:7d` |
| No leídos importantes | `is:unread is:important newer_than:7d` |
| Automatizaciones / Make | `(igms OR make.com OR webhook OR automatización) newer_than:7d` |
| Google Forms — exámenes de cursos | `from:forms-receipts-noreply@google.com newer_than:7d` |
| **Barrido amplio INBOX (red de seguridad)** | `in:inbox newer_than:7d -category:promotions` |

**REGLA DURA — Barrido amplio obligatorio (anti-falso-negativo de cobertura):** Las queries segmentadas anteriores son listas blancas (dominios y keywords fijos) y por diseño NO capturan clientes/proveedores cuyo dominio no esté listado (ej: `insuma.co.cr`, `sonda.com`, `promed-sa.com`, gmails genéricos de contactos comerciales) ni asuntos fuera del vocabulario comercial cargado (ej: "curso", "certificado", "demo", "préstamo", "memoria de cálculo", "revisión", "contrato"). El barrido amplio del INBOX es la red de captura que garantiza cobertura completa. Ejecutarlo SIEMPRE, además de las segmentadas, y fusionar resultados deduplicando por `threadId`. El ruido conocido (notificaciones bancarias, adjudicaciones Connexis/SICOP diarias, agendas automáticas de Calendar, newsletters) se descarta SOLO después de confirmar que el thread no contiene acción comercial u operativa pendiente — nunca se filtra a ciegas por remitente antes de revisar.

Ver `references/query-templates.md` para queries adicionales.

**Instrucciones especiales — Google Forms (notificaciones de examen):**

Cada correo de `forms-receipts-noreply@google.com` indica que un participante completó un examen de curso de Protección Radiológica. Esto **activa el flujo de generación de certificado**. Clasificar siempre como 🔴 **Urgente**.

Para cada notificación de Google Forms, reportar en el briefing:
- **Nombre del formulario** (= nombre del curso/módulo)
- **Email del respondente** (visible en el snippet del correo)
- **Empresa inferida** del dominio del correo (ej: `@novapark.net` → Novapark, `@insuma.co.cr` → INSUMA)
- **Acción requerida:** "Revisar calificación en Google Forms → generar certificado Curso [X] PR para [empresa]"

⚠️ El cuerpo del correo de Google Forms **no incluye los datos completos** del participante (nombre completo, cédula, calificación). Esos datos están solo en Google Forms. Indicar al usuario que debe ingresar a Forms para obtenerlos antes de generar el certificado.

**Paso A2: Clasificación de urgencia**

Para cada correo identificado, determinar:

- 🔴 **Urgente** — respuesta/acción requerida en <24h
  - _Ejemplos: solicitud de cotización con plazo, check-in Airbnb <48h, alerta regulatoria, PO activo, fallo de automatización_
- 🟡 **Accionable** — esta semana, sin urgencia inmediata
  - _Ejemplos: seguimiento de cotización, consulta técnica, propuesta de proveedor, reunión a confirmar_
- ⚪ **Informativo** — sin acción requerida
  - _Ejemplos: newsletters, confirmaciones automáticas, recibos, notificaciones bancarias_

**Paso A2.5: Lectura profunda OBLIGATORIA antes de clasificar estado (anti-error)**

**REGLA DURA ANTI-ERROR DE CLASIFICACIÓN:** Los snippets de Gmail (primeros ~100 caracteres) son insuficientes para juzgar estado comercial, intención o resultado de una acción. Antes de emitir cualquier clasificación cargada en la tabla final, ejecutar `Gmail:get_thread` con `messageFormat=FULL_CONTENT` sobre los siguientes threads:

1. **Todos los threads candidatos a 🔴 Urgente o 🟡 Accionable** con ≥ 2 mensajes.
2. **Todos los threads que contengan al menos un mensaje saliente** de `colesa.manuel@gmail.com`, `colesa.marco@gmail.com` o `colesa.admi@gmail.com` — el estado actual del thread lo define ese mensaje saliente, no el snippet del entrante.
3. **Todos los threads donde la clasificación preliminar use vocabulario cargado** (ver léxico prohibido abajo).

Del body completo, extraer:
- **Último mensaje saliente Colé**: texto literal de la acción tomada (cotización enviada, aceptación, rechazo, solicitud de información, etc.).
- **Último mensaje entrante del cliente**: texto literal de la solicitud o respuesta pendiente.
- **Referencias explícitas a COT-XXXX, números de PO, guías DHL, tracking**: extraer tal cual aparecen.

**Léxico prohibido sin evidencia textual literal en el body:**

Los siguientes términos NO pueden aparecer en el briefing a menos que el `plaintextBody` del mensaje saliente contenga frase explícita equivalente:

| Término prohibido | Requiere en el body |
|---|---|
| "declinación", "declinado", "rechazado" | "no podemos cotizar", "declinamos participar", "lamentamos informar que no", "no ofrecemos este producto" |
| "cerrado", "perdido", "ganado" | confirmación explícita de adjudicación o pérdida por parte del cliente |
| "contraoferta", "negociación" | propuesta numérica alternativa emitida por Colé o el cliente |
| "cancelado", "suspendido" | mención explícita de cancelación/suspensión |
| "urgente" | plazo explícito en el body, palabra "URGE/URGENTE" del cliente, o fecha límite < 48h |

Si el body no contiene evidencia equivalente, usar términos neutros:
- "cotización enviada, pendiente respuesta del cliente"
- "en curso"
- "seguimiento pendiente"
- "pendiente confirmación"

**Regla de match bidireccional Gmail ↔ Odoo:** Antes de reportar "❌ No emitida" o "❌ No encontrada" en la columna Cotización Odoo, aplicar estos tres filtros en orden:
1. Buscar COT con `partner_id` que coincida con el cliente del correo.
2. Buscar COT con `date_order` dentro de ±3 días de la fecha del correo saliente Colé.
3. Si en el Paso A2.5 se encontró una referencia literal "COT-XXXX" en el body del mensaje saliente, ese es el match directo — buscar ese número en Odoo y usarlo.

Solo si los tres filtros devuelven vacío, reportar "❌ No emitida".

**Paso A3: Verificar si ya tiene respuesta**

Para cada correo 🔴 o 🟡, verificar si existe mensaje enviado en el mismo thread:
- Buscar `in:sent thread:[threadId]` o revisar si el thread tiene mensajes propios.
- Reportar **Sí** (respondido) o **No** (pendiente).

**IMPORTANTE — No basta con detectar "hay respuesta":** además hay que leer el body del mensaje saliente (ejecutado en Paso A2.5) y resumir textualmente la acción tomada. Ejemplos correctos:
- "Sí — COT-1938 enviada 11/04" (no solo "Sí")
- "Sí — declinación formal: 'no ofrecemos este producto' (body literal)" (solo si el body lo dice)
- "Sí — acuse de recibo, pendiente respuesta sustantiva"

Ejemplos incorrectos (no usar):
- "Sí (declinación)" sin verificar que el body diga declinación.
- "Sí (cerrado favorable)" sin confirmación del cliente.

**Paso A4: Verificar cotizaciones en Odoo (OBLIGATORIO antes de presentar Sección A)**

**REGLA DURA:** Este paso es OBLIGATORIO y debe ejecutarse ANTES de presentar el briefing al usuario. Nunca presentar la tabla de correos sin haber consultado Odoo primero. Si Odoo no responde, reportar `⚠️ Odoo no disponible` en la columna, pero el intento debe haberse hecho.

Para cada correo que sea solicitud de cotización de clientes (CCSS, FUNDAUNA, hospitales, empresas, sector privado), verificar si ya existe una cotización emitida en Odoo.

**Credenciales (NO preguntar al usuario — usar directamente):**
Obtener API key y credenciales del skill `odoo-quotation-generator` (sección "Credenciales de conexión").

**Consulta via JSON-RPC (ejecutar con bash_tool + curl -sk):**

```python
import subprocess, json

url = "https://colesamarco2020-colesa.odoo.com/jsonrpc"
db = "colesamarco2020-colesa-colesa-27146045"
uid = 7
# API key: obtener del skill odoo-quotation-generator

def call(model, method, args, kwargs=None):
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [db, uid, api_key, model, method, args, kwargs or {}]
        },
        "id": 2
    }
    result = subprocess.run(
        ["curl", "-sk", "-X", "POST", url,
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload)],
        capture_output=True, text=True, timeout=30
    )
    data = json.loads(result.stdout)
    return data.get("result")
```

**Estrategia de búsqueda (ejecutar DOS consultas):**

1. **Búsqueda amplia reciente:** Todas las cotizaciones `state in [draft, sent, sale]` con `date_order >= <7 días antes>`, limit 25, order `date_order desc`. Esto captura cotizaciones que podrían estar bajo nombres de cliente diferentes.
2. **Búsqueda por cliente específico:** Para cada solicitud de cotización en los correos, buscar `partner_id.name ilike <término>`. Usar múltiples términos si es necesario:
   - CCSS genérico → `"CCSS"` o `"CAJA COSTARRICENSE"`
   - Hospital específico → nombre del hospital (ej: `"San Juan"`, `"México"`, `"Calderón"`)
   - Área de Salud → nombre del área (ej: `"Matina"`)
   - FUNDAUNA → `"FUNDAUNA"`
   - Empresa privada → nombre de la empresa (ej: `"Teradyne"`, `"Panduit"`)
   - Empresas con acrónimo distinto a razón social → buscar por palabra clave del nombre completo, NO por siglas:
     - `ECISA` (`logistica@equiposcorp.com`) → buscar `"Equipos"` → razón social en Odoo: **Equipos y Componentes Industriales S.A.**
     - Regla general: si la búsqueda por sigla devuelve vacío, intentar con la primera palabra significativa del dominio del remitente o del nombre comercial conocido.

**⚠️ Regla anti-falso-negativo:** Si la búsqueda por sigla/acrónimo devuelve vacío, NO reportar `❌ No encontrada` de inmediato. Ejecutar una segunda búsqueda con término derivado del dominio del remitente (ej: `equiposcorp.com` → buscar `"Equipos"`). Solo reportar `❌` tras haber agotado al menos 2 variantes del nombre del cliente.

**Matching:** Cruzar resultados de Odoo con los correos por: nombre de cliente + fecha cercana (±5 días) + monto si es conocido. Si hay duda, listar la cotización candidata con "?" para revisión del usuario.

**Columna "Cotización Odoo" — valores posibles:**
- ✅ `COT-XXXX — [estado] — $X,XXX` si hay match claro
- ❓ `COT-XXXX — posible match` si hay cotización del mismo cliente pero sin certeza de que corresponda al correo específico
- ❌ No encontrada
- ⚠️ Odoo no disponible (si la consulta falla)
- `—` (guión) si el correo NO es una solicitud de cotización (ej: embarque, convocatoria, notificación)

**Formato sección A:**

```
## SECCIÓN A — Correos últimos 7 días

### 🔴 Urgentes (N)
| # | Remitente | Asunto | Fecha | Respondido | Cotización Odoo |
|---|---|---|---|---|---|
| 1 | [nombre] <email> | [asunto] | [DD/MM] | Sí / No | ✅ COT-XXXX / ❌ No / — |

### 🟡 Accionables (N)
| # | Remitente | Asunto | Fecha | Respondido | Cotización Odoo |
|---|---|---|---|---|---|

### ⚪ Informativos (N) — solo conteo y lista compacta
- [Remitente] | [Asunto]
```

---

### TAREA B — Propuesta de eventos para calendarizar

**REGLA CRÍTICA: NUNCA crear eventos en Google Calendar sin confirmación explícita del usuario.**

El flujo obligatorio es:

1. **Proponer** — presentar tabla con los eventos sugeridos
2. **Esperar** — el usuario aprueba, modifica o descarta cada uno
3. **Crear** — solo los que el usuario confirme, con los parámetros que indique

**Paso B1: Propuesta (siempre)**

Para cada correo 🔴 y 🟡 no respondido, proponer un evento con:
- **Título sugerido:** `[Acción] — [Remitente/Empresa]`
- **Fecha/hora sugerida:**
  - Urgente: mañana en horario laboral (8:00–17:00 GMT-6)
  - Accionable: dentro de los próximos 3 días hábiles
- **Recordatorios estándar:** 1 día antes + 2 horas antes

**Formato sección B — Propuesta:**

```
## SECCIÓN B — Eventos propuestos para Calendar

| # | Título sugerido | Fecha/hora sugerida | Vinculado a |
|---|---|---|---|
| 1 | [título] | [DD/MM HH:MM] | [correo referencia] |

¿Confirma la creación de estos eventos? Puede:
- Aprobar todos: "Sí, créalos todos"
- Aprobar selectivos: "Crea el 1 y el 3"
- Modificar fecha/hora: "El 2 ponlo el martes a las 10"
- Descartar: "No, ninguno"
```

**Paso B2: Creación (solo tras confirmación EXPLÍCITA e ÍTEM-POR-ÍTEM)**

**REGLA DURA — APROBACIÓN EXPLÍCITA POR EVENTO:** Antes de crear cualquier evento en Google Calendar, el usuario debe indicar de forma explícita CUÁLES eventos aprueba y CUÁLES no. Un "sí" genérico, "hazlo", "ok", "procede", "dale", "créalos" o similar NO constituye aprobación suficiente porque no discrimina entre los ítems propuestos.

**Formas de aprobación válidas (solo estas):**

| Tipo | Ejemplo | Acción |
|---|---|---|
| Selección explícita por números | "Crea el 1, 3 y 5" | Crear solo 1, 3 y 5 |
| Aprobación total explícita | "Sí, créalos TODOS los 6", "apruebo todos" | Crear los 6 |
| Selección por nombre | "Crea solo el de KraftHeinz y el de DHL" | Crear esos 2 |
| Modificación + selección | "El 1 ponlo jueves 7/may, y crea 2 y 4" | Ajustar y crear los indicados |

**Formas de "aprobación" que NO son válidas (pedir clarificación):**

| Entrada del usuario | Respuesta correcta del skill |
|---|---|
| "Sí" (solo) | "¿Apruebo los 6 o algunos? Indique números o 'todos'." |
| "Dale", "hazlo", "ok", "procede" | Idem |
| "Perfecto" | Idem |
| Silencio o cambio de tema | No crear nada hasta que el usuario vuelva al tema |

**Regla adicional:** incluso cuando el usuario diga "todos", el skill debe repetir la lista final una vez más antes de ejecutar, y esperar un "confirmado" explícito, a menos que la instrucción inicial haya sido "crea todos sin confirmar de nuevo".

**Orden estricto de ejecución para la Tarea B:**

1. Presentar tabla numerada de eventos propuestos (Paso B1).
2. Esperar respuesta del usuario.
3. Si la respuesta es ambigua → pedir clarificación. **NO crear nada.**
4. Si la respuesta es explícita por números/nombres → crear SOLO esos eventos.
5. Reportar cuáles se crearon y cuáles quedaron sin crear.

**Calendario obligatorio:** Crear eventos en el calendario **Cole S.A.** usando:
```
calendarId = "a6bitvljhejddblgg1dqglmrq4@group.calendar.google.com"
```
No usar `primary`. Reportar resultado:

```
## SECCIÓN B — Eventos creados

| # | Evento | Fecha/Hora | Estado |
|---|---|---|---|
| 1 | [título] | [DD/MM HH:MM] | ✅ Creado |

Recordatorios activos en todos: 1 día antes + 2 horas antes.
```

Si no hay correos no respondidos que requieran acción → declarar: `"No se requieren eventos nuevos."`.

---

### TAREA C — Calendario ±7 días (solo Cole S.A.)

**REGLA:** Consultar ÚNICAMENTE el calendario empresarial **"Cole S.A."** usando el `calendarId` específico:

```
calendarId = "a6bitvljhejddblgg1dqglmrq4@group.calendar.google.com"
```

**NO consultar** el calendario `primary` (personal), ni otros calendarios como "Cumpleaños", "Radioterapia Superficial", "Desembolsos de Crece", "Ordenes de compra", "Fechas Conmemorativas", etc. Solo eventos del calendario empresarial Cole S.A. son relevantes para el briefing.

**Consultar Google Calendar (Cole S.A.):**
- Semana pasada (contexto): desde hace 7 días hasta hoy
- Próxima semana (preparación): desde hoy hasta en 7 días
- **Parámetro obligatorio:** `calendarId = "a6bitvljhejddblgg1dqglmrq4@group.calendar.google.com"`
- **Timezone:** `America/Costa_Rica`

**Análisis de conflictos:** Si dos eventos del calendario Cole S.A. se solapan en horario, marcarlos con ⚠️.

**Formato sección C:**

```
## SECCIÓN C — Agenda Cole S.A. ±7 días

### Semana pasada (contexto)
| Fecha | Hora | Evento | Notas |
|---|---|---|---|

### Próxima semana (preparación)
| Fecha | Hora | Evento | Notas |
|---|---|---|---|

### ⚠️ Conflictos detectados
[Lista de solapamientos, o "Sin conflictos."]
```

---

## Reglas duras

1. **No inventar datos** — solo reportar lo que devuelvan los MCPs.
2. **Ejecutar las 3 tareas automáticas siempre** — A, B y C son obligatorias en cada ejecución del briefing. D solo se ejecuta cuando el usuario lo solicite explícitamente (ej: "crea el borrador", "envía el resumen", "correo resumen").
3. **Confirmar antes de calendarizar — APROBACIÓN EXPLÍCITA ÍTEM-POR-ÍTEM** — NUNCA crear eventos en Google Calendar sin aprobación explícita del usuario. La Tarea B siempre termina en una propuesta + pregunta, no en creación automática. Un "sí", "ok", "dale", "hazlo", "procede" genérico NO es aprobación suficiente. El usuario debe indicar *qué eventos específicos* aprueba (por número, por nombre, o "todos" literal). Ver Paso B2 para casos válidos/inválidos. Interpretar aprobación genérica como permiso para crear todo es una violación dura.
4. **Verificar respuesta antes de proponer evento** — no proponer evento si el correo ya fue respondido.
5. **Si el usuario modifica fecha/hora**, usar exactamente los parámetros que indique.
6. **Si un MCP falla**, reportar en la sección correspondiente y continuar con las demás tareas.
7. **Priorizar cuenta** `colesa.manuel@gmail.com`.
8. **Máximo 3 líneas por correo** en la narrativa; usar tablas para densidad.
9. **Verificar Odoo ANTES de presentar resultados** — El Paso A4 (consulta de cotizaciones en Odoo) es OBLIGATORIO y debe ejecutarse usando `bash_tool` con `curl -sk` ANTES de generar la tabla de correos. Obtener credenciales del skill `odoo-quotation-generator`. Si no se ejecuta Odoo, el briefing está INCOMPLETO. El orden de ejecución es: A1 (búsqueda Gmail) → A2 (clasificación preliminar) → **A2.5 (lectura profunda de threads candidatos 🔴/🟡 y threads con saliente Colé)** → A3 (verificar respuestas) → **A4 (consultar Odoo)** → presentar tabla con columna "Cotización Odoo" completa.
10. **Resumen bajo demanda** — La Tarea D NO se ejecuta automáticamente. Solo se ejecuta cuando el usuario lo solicite explícitamente. Al finalizar las secciones A, B y C, ofrecer brevemente: `"¿Creo el borrador de resumen en Gmail?"`. Si el usuario no lo pide, no crearlo.
11. **Snippet ≠ estado** — Los snippets de Gmail sirven SOLO para descubrir threads. El estado comercial/operativo de un thread se determina leyendo el `plaintextBody` completo del último mensaje saliente Colé y del último mensaje entrante del cliente (Paso A2.5). Clasificar estado basándose solo en snippet es una violación dura.
12. **Léxico prohibido sin evidencia literal** — Términos como "declinación", "rechazado", "cerrado", "perdido", "ganado", "contraoferta", "cancelado", "urgente" NO pueden usarse en el briefing si el body del mensaje saliente no contiene frase explícita equivalente. Ver tabla en Paso A2.5. Si no hay evidencia, usar léxico neutro: "cotización enviada, pendiente respuesta", "en curso", "seguimiento pendiente".
13. **Match bidireccional Gmail ↔ Odoo obligatorio** — Antes de reportar "❌ No emitida" en la columna Cotización Odoo, agotar los tres filtros del Paso A2.5: (a) búsqueda por partner_id, (b) búsqueda por rango de fecha ±3 días, (c) match directo si el body del saliente Colé cita literalmente "COT-XXXX". Solo tras los 3 filtros vacíos, reportar ❌.
14. **Autoauditoría previa a presentar tabla** — Antes de emitir la tabla final de la Sección A, releer mentalmente cada fila clasificada 🔴/🟡 y preguntarse: *¿tengo evidencia textual del body para esta etiqueta, o la deduje del snippet?* Si la respuesta es "la deduje", ejecutar `Gmail:get_thread` sobre ese thread antes de publicar.
15. **Threads largos: la fecha visible miente (anti-falso-negativo de recencia)** — `Gmail:search_threads` puede truncar los mensajes de un thread largo, devolviendo como "último mensaje visible" uno antiguo aunque el thread tenga actividad de hoy. Esto provocó la omisión de threads activos reales (ej: COT-1953 con 13 mensajes, cuyo último mensaje visible era de hace 3 semanas mientras el real era del día). REGLA DURA: cualquier thread con N≥5 mensajes cuyo último mensaje visible parezca anterior a la ventana de 7 días NO puede descartarse por antigüedad sin antes verificar con `Gmail:get_thread` (FULL_CONTENT) cuál es el mensaje realmente más reciente. Que un thread haya sido descubierto por el barrido amplio (regla A1) no exime de esta verificación.

---

### TAREA D — Correo de resumen (SOLO BAJO DEMANDA)

**REGLA:** Esta tarea se ejecuta ÚNICAMENTE cuando el usuario lo solicite explícitamente (ej: "crea el borrador", "envía el resumen", "manda el correo resumen"). NO se ejecuta automáticamente al finalizar A, B y C.

**Paso D1: Generar resumen ejecutivo para correo**

Compilar un correo conciso con:
- **Asunto:** `📋 Briefing Colé S.A. — [DD/MM/YYYY]`
- **Cuerpo:** Resumen ejecutivo del briefing con:
  - Conteo total: N urgentes, N accionables, N informativos
  - Lista compacta de correos 🔴 urgentes pendientes (remitente + asunto, máx 1 línea c/u)
  - Lista compacta de correos 🟡 accionables pendientes
  - Cotizaciones Odoo pendientes detectadas (si aplica)
  - Eventos propuestos para calendario (títulos + fechas sugeridas)
  - Conflictos de agenda detectados (si los hay)
  - Próximos eventos relevantes (próximos 3 días)
- **Formato:** Texto plano, sin HTML. Breve y escaneable desde móvil.
- **Cierre:** `— Generado por Claude | Gmail Briefing Skill v2.1`

**Paso D2: Crear borrador y enviar**

Usar `Gmail:create_draft` con:
- **To:** `colesa.manuel@gmail.com`
- **Subject:** `📋 Briefing Colé S.A. — [DD/MM/YYYY]`
- **Body:** El resumen generado en D1

**⚠️ NOTA:** El MCP de Gmail solo permite crear borradores (`Gmail:create_draft`), no enviar directamente. Después de crear el borrador:
1. Informar al usuario: `"📧 Borrador de resumen creado en Gmail — revisar y enviar desde la bandeja de borradores."`
2. Si en el futuro el MCP soporta `gmail_send_message`, reemplazar `Gmail:create_draft` por envío directo.

**Alternativa si el usuario prefiere envío automático sin intervención:**
Si el usuario confirma que quiere envío directo sin revisar borrador, y el MCP lo soporta, enviar directamente. De lo contrario, mantener el flujo de borrador + notificación.

**Formato sección D:**

```
## SECCIÓN D — Resumen enviado

| Campo | Valor |
|---|---|
| Destinatario | colesa.manuel@gmail.com |
| Asunto | 📋 Briefing Colé S.A. — [DD/MM/YYYY] |
| Estado | ✅ Borrador creado / ⚠️ Error al crear |
```

---

## Comportamiento ante solicitudes derivadas

| El usuario pide | Acción |
|---|---|
| "Respóndele a [X]" | Redactar borrador con `Gmail:create_draft`, mostrar antes de enviar |
| "Muéstrame ese correo completo" | Usar `Gmail:get_thread` con el message ID |
| "Cambia la fecha del evento [X]" | Usar `Google Calendar:update_event` con el event ID creado |
| "Agrega otro recordatorio" | Actualizar evento con `Google Calendar:update_event` |
| "Archiva los informativos" | Informar que no está disponible vía MCP actual |
