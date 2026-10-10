---
name: email-reply-composer
description: >-
  Redacta respuestas a correos existentes o correos nuevos a contactos frecuentes
  de Colé S.A., firmando siempre como Ing. Manuel Rubio. Pipeline obligatorio:
  search_threads → get_thread con FULL_CONTENT → leer TODOS los mensajes del hilo →
  redactar. Prohibido redactar solo con snippets. Detecta idioma del hilo (ES/EN),
  preserva CCs originales y crea o actualiza un único borrador anidado al hilo.
  Activar con "responde el correo de", "contesta a", "respóndele a", "redacta
  respuesta", "redacta correo a", "escríbele a", "mándale correo a", "draft email
  to", "reply to", o cualquier solicitud de correspondencia saliente.
---

# Email Reply Composer — Colé S.A.

Skill para redactar correspondencia saliente firmada como **Ing. Manuel Rubio, MSc** (Presidente de Colé S.A.). Cubre dos casos:

1. **Respuestas a hilos existentes** (caso principal).
2. **Correos nuevos** a contactos frecuentes.

---

## Regla de Oro: Contexto Completo Antes de Redactar

**Prohibido** redactar una respuesta basándose únicamente en el snippet devuelto por `search_threads`. Los snippets están truncados a ~200 caracteres y frecuentemente cortan información crítica (cifras, fechas de entrega, condiciones de pago, adjuntos mencionados).

**Pipeline obligatorio para toda respuesta**:

```
1. Gmail:search_threads  →  localizar el hilo (obtener threadId)
2. Gmail:get_thread      →  messageFormat=FULL_CONTENT  (leer TODOS los mensajes)
3. Analizar el hilo completo
4. Redactar con message_compose_v1
5. Detectar draft previo en el hilo (ver Paso 5)
6. Crear o actualizar borrador anidado al hilo:
   - createReply si NO existe draft previo
   - updateReply si YA existe uno (nunca crear un segundo draft para el mismo hilo)
```

Si el usuario da una instrucción vaga ("responde el último correo de X"), se busca, se lee el hilo completo, y se redacta. Nunca se pide al usuario que pegue el contenido — se obtiene con las tools.

---

## Paso 1 — Localizar el Hilo

Se usa `Gmail:search_threads` con queries precisas. Patrones útiles:

| Intención | Query |
|---|---|
| Por remitente | `from:murat@radixray.com newer_than:30d` |
| Por remitente + asunto | `from:jorge subject:planilla` |
| Sin hilo seguro, por palabra clave | `"Order 39" newer_than:30d` |
| Hilos no leídos | `is:unread newer_than:7d` |

Si hay varios hilos posibles, presentar al usuario los 3–5 más recientes por fecha y pedir confirmación antes de continuar. No asumir.

---

## Paso 2 — Leer el Hilo Completo

```
Gmail:get_thread
  threadId: <id del paso 1>
  messageFormat: FULL_CONTENT   ← OBLIGATORIO
```

Al analizar el hilo, extraer:

- **Último mensaje de la contraparte** (a qué se está respondiendo).
- **Idioma predominante** — revisar los últimos 2–3 mensajes de la contraparte, no los de Colé.
- **Compromisos ya hechos por Colé** en el hilo (fechas, cifras, condiciones).
- **CCs originales** — quiénes estaban copiados en el último mensaje (se preservan).
- **Adjuntos mencionados** — si el interlocutor adjuntó algo relevante para la respuesta.

---

## Paso 3 — Redactar

### Idioma

- **Español**: clientes/proveedores CR, LatAm, España, Jorge Hernández (MYH), CCSS, MINSA, hospitales locales.
- **Inglés**: proveedores internacionales (Murat/Radixray, IBA/Radcal, Ludlum, Polimaster, Klarity, Standard Imaging, LG Medical).
- Si el hilo está mezclado, se usa el idioma del **último mensaje de la contraparte**.

### Tono

- **Formal-profesional pero natural** (sin burocracia).
- **Denso, conciso, sin relleno**.
- Nada de "¡Excelente!", "Muchas gracias por tu mensaje", "Espero que te encuentres bien" salvo que el usuario lo pida explícitamente.
- En correos técnicos (cotizaciones, especificaciones, cumplimiento normativo): cifras y hechos primero, cortesía al cierre.

### Estructura de Respuesta

1. Saludo corto (`Dear <Nombre>,` / `Hola <Nombre>,`).
2. Punto principal en el primer párrafo — nada de rodeos.
3. Detalles operativos (cifras, fechas, condiciones) en párrafos cortos o bullets si son múltiples.
4. Acción solicitada o próximo paso, explícito.
5. Cierre + firma (ver abajo).

### Variantes con message_compose_v1

Se llama **siempre** a `message_compose_v1` con:

- **`kind: "email"`**
- **1 variante** si la respuesta es transaccional/técnica sin ambigüedad (confirmación de recibo, envío de documento, respuesta a pregunta factual).
- **2 variantes** si hay decisión de tono (conciliador vs. firme, agradecimiento cálido vs. neutro, push vs. wait).
- **3 variantes** solo si hay estrategias genuinamente distintas.

Cada variante lleva label corta orientada al objetivo (ej. "Firme pero cordial", "Push por urgencia", "Neutro discreto").

**Flujo sin pausas (regla del titular, 2026-07-15)**: mostrar variantes NUNCA detiene el flujo. Haya 1, 2 o 3 variantes, el borrador anidado al hilo se crea **de inmediato** con la variante recomendada (marcarla como tal en su label), sin preguntar al usuario. Las variantes alternas quedan visibles en el chat; si el usuario prefiere otra, la pide y se reemplaza el cuerpo del borrador.

---

## Paso 4 — Firma

Siempre firmar como Manuel. Firma fija:

```
Best regards / Saludos cordiales,

Ing. Manuel Rubio, MSc.
Presidente — Colé S.A.
Tel: (506) 2285 3211 | Mobile/WhatsApp: (506) 8395 7547
www.colecr.com | colesa.manuel@gmail.com
```

Ajustar "Best regards" vs "Saludos cordiales" según idioma.

Si el borrador va a enviarse desde la cuenta personal de Manuel (`colesa.manuel@gmail.com`), **no** repetir el email en la firma dentro del body del draft (redundante). Si el usuario especifica enviar desde `m.rubio@colecr.com` (dominio corporativo), sí incluirlo.

---

## Paso 5 — Detectar Draft Previo en el Hilo

**Regla dura**: para un mismo `threadId`, solo debe existir UN draft. Si el skill ya creó uno antes (misma conversación) o si el usuario tiene uno pendiente de sesiones anteriores, se **actualiza** ese draft en lugar de crear un segundo.

### Cómo decidir entre `createReply` y `updateReply`

**Prioridad 1 — draftId visible en la conversación actual**:
Si en un turno anterior de esta misma conversación el skill ya creó un draft para el mismo `threadId` (el `draftId` está visible en el contexto del modelo), se usa **directamente** `updateReply` con ese `draftId`. No hace falta consultar Gmail.

**Prioridad 2 — sin `draftId` en contexto**:
Si es la primera vez que se toca el hilo en esta conversación, se consulta al endpoint con la acción `findDraftInThread` pasando el `threadId`. El endpoint devuelve:
- `{ok:true, draftId:"<id>", ...}` → existe un draft previo → usar `updateReply`.
- `{ok:true, draftId:null, ...}` → no hay draft previo → usar `createReply`.

### Ejemplo

```json
// Payload de consulta
{
  "action": "findDraftInThread",
  "secret": "<valor de EMAIL_REPLY_APPS_SCRIPT_SECRET>",
  "threadId": "19e6183a83a09256"
}
```

Respuesta cuando existe:
```json
{"ok":true, "draftId":"r7710465823644634670", "messageId":"...", "threadId":"19e6183a83a09256"}
```

Respuesta cuando no existe:
```json
{"ok":true, "draftId":null, "threadId":"19e6183a83a09256"}
```

### Cuándo saltar la detección

- **Correos nuevos sin hilo previo** (sin `threadId`) → siempre `Gmail:create_draft`; no aplica.
- **El usuario pide explícitamente crear un draft adicional** ("hazme dos borradores para comparar") → override manual: se usan dos `createReply` consecutivos. Declarar en el chat que se está saltando la regla anti-duplicación.

---

## Paso 6 — Crear o Actualizar el Borrador Anidado al Hilo (Endpoint Apps Script)

**Siempre** se cierra el flujo creando el borrador anidado al hilo original. Nunca se termina mostrando solo las variantes.

### Método estándar — Apps Script `createReply`

`Gmail:create_draft` no acepta `threadId` y crea correos sueltos fuera del hilo. **No se usa para respuestas.** En su lugar, se invoca el endpoint Apps Script de Colé que sí soporta threading nativo:

```
URL    : https://script.google.com/macros/s/AKfycbxc6H0RDld4DRSDHlUiUxCcDWkWDILtGvtqIAHF_joLEmxjXsBbQqqPQme2VKEGPn0ePw/exec
Secret : variable de entorno `EMAIL_REPLY_APPS_SCRIPT_SECRET`
Sender : colesa.manuel@gmail.com (default — no usar alias `from`)
```

Antes de llamar al endpoint, leer `EMAIL_REPLY_APPS_SCRIPT_SECRET` del entorno. Si
falta, detener el flujo e informar al usuario; nunca escribir el valor en el skill,
el payload mostrado en el chat, archivos versionados ni logs.

Acciones disponibles:

| Acción | Uso |
|---|---|
| `ping` | Health check del endpoint. Devuelve `{ok:true, pong:true}`. |
| `createReply` | Crea borrador **nuevo** anidado al `threadId`. Parámetros: `threadId`, `body` o `htmlBody`, `cc[]`, `bcc[]`, `replyAll` (bool). Usar solo si NO existe draft previo en el hilo. |
| `updateReply` | **Actualiza** un borrador existente por `draftId`, preservando el threading. Parámetros: `draftId`, `body` o `htmlBody`, `cc[]`, `bcc[]`. Reemplaza el contenido completo del draft. |
| `findDraftInThread` | Consulta si existe algún draft del usuario en un `threadId` dado. Parámetros: `threadId`. Devuelve `draftId` (o `null`). Sin efectos secundarios. |

### Llamada correcta — patrón obligatorio

```bash
SECRET="${EMAIL_REPLY_APPS_SCRIPT_SECRET:?Falta EMAIL_REPLY_APPS_SCRIPT_SECRET}"
curl -sL "$URL" -H 'Content-Type: application/json' -d '{...}'
```

⚠️ **Crítico — no usar nunca:**
- `-X POST`
- `--post301` / `--post302` / `--post303`

Razón técnica: Apps Script publica el endpoint `/exec` que internamente redirige a `script.googleusercontent.com`, y ese redirect requiere convertirse de POST a GET. Forzar POST en el redirect rompe con `HTTP 405 + "Sorry, unable to open the file"`. Solo `-L -d` permite el flujo POST→GET correcto.

### Payload típico — `createReply`

```json
{
  "action": "createReply",
  "secret": "<valor de EMAIL_REPLY_APPS_SCRIPT_SECRET>",
  "threadId": "<id del thread del paso 1>",
  "replyAll": false,
  "cc": ["addr1@x.com", "addr2@y.com"],
  "htmlBody": "<div>...cuerpo HTML...</div>"
}
```

Respuesta esperada: `{ok:true, draftId, messageId, threadId, subject, permalink}`.

### Payload típico — `updateReply`

```json
{
  "action": "updateReply",
  "secret": "<valor de EMAIL_REPLY_APPS_SCRIPT_SECRET>",
  "draftId": "<draftId obtenido de createReply o findDraftInThread>",
  "cc": ["addr1@x.com", "addr2@y.com"],
  "htmlBody": "<div>...nuevo cuerpo HTML...</div>"
}
```

Respuesta esperada: `{ok:true, draftId, messageId, threadId, subject, updated:true}`. El `draftId` devuelto es el mismo que se pasó (no se crea uno nuevo).

**Notas de updateReply:**
- No requiere `threadId` — se infiere del draft por su `draftId`.
- El destinatario `to` y el `subject` se preservan del draft original (no se pasan en el payload).
- El `htmlBody` (o `body`) reemplaza **completamente** el contenido anterior — no es un append.
- Si se pasa `cc[]`, reemplaza los CCs del draft; si se omite, se mantienen los CCs existentes.

Si `ok:false`, leer el error y reportar al usuario sin reintentos ciegos.

### Fallback si el endpoint falla

Tres escenarios y su protocolo:

| Escenario | Síntoma | Acción |
|---|---|---|
| Endpoint caído / sin respuesta | `curl` cuelga, timeout, o devuelve HTML de error de Google en lugar de JSON | (1) Reintentar con `action: ping` para confirmar caída; (2) si persiste, informar al usuario y **detener** el flujo; (3) opción degradada **solo si el usuario lo autoriza explícitamente**: borrador suelto con `Gmail:create_draft` y quoted history manual del último mensaje (rompe threading, debe declararse). |
| `ok:false` con error conocido (`Bad secret`, `Thread not found`, `Invalid threadId`) | JSON con campo `error` legible | Reportar el error literal al usuario; no reintentar; verificar si el `threadId` cambió, si el secret expiró, o si el hilo fue archivado/borrado. |
| `ok:false` con error desconocido | JSON con campo `error` no documentado | Capturar respuesta completa, reportar al usuario, NO reintentar. |

⚠️ **Regla dura**: ante cualquier `ok:false` o caída del endpoint, **no se hace fallback automático** a `Gmail:create_draft`. Eso degrada silenciosamente el threading y el usuario podría asumir que el borrador quedó anidado cuando no lo está. El degradado solo procede con autorización explícita y declarada.

### Reglas de cuerpo

- **Sin quoted history manual**: el endpoint enhebra automáticamente al hilo, no hace falta replicar el `On <fecha>... wrote:` del workaround anterior.
- **Subject**: el endpoint usa el subject del thread original; no se envía en el payload.
- **HTML preferido** sobre texto plano para correos formales (firmas, tablas, énfasis). Texto plano (`body`) solo cuando el hilo es claramente informal.

### Limitación: adjuntos

El endpoint `createReply` actual **no soporta adjuntos** (solo `body`/`htmlBody` + headers de threading). Si la respuesta requiere adjuntar archivo:

1. Crear el borrador de texto con `createReply` como siempre — queda anidado al hilo.
2. Informar al usuario que debe **abrir el borrador en Gmail UI y adjuntar el archivo manualmente** antes de enviar.
3. Mencionar el adjunto explícitamente en el cuerpo (ej. *"Adjunto la carta de respuesta a CARTA-MS-DSS-0604-2026"*) para que al revisar Manuel detecte si olvidó adjuntar.

⚠️ **No** usar `Gmail:create_draft` con adjunto como atajo — rompe el threading y deja el borrador suelto fuera del hilo.

### Preservación de CCs

Copiar **exactamente** la lista de CCs del último mensaje de la contraparte. Excluir `colesa.manuel@gmail.com` del array `cc` (es el sender; auto-CC genera ruido). Si Manuel estaba en To, la contraparte va al destinatario implícito de `createReply`; si Manuel estaba en CC, igual aplica — el endpoint determina el `to` por el remitente del thread.

### Decisión `replyAll` vs. `cc` explícito

| Caso | Configuración recomendada |
|---|---|
| Hilo con 2–3 participantes estables (proveedor + Colé + 1 CC) | `replyAll: false` + `cc` explícito copiado del último mensaje |
| Hilo institucional con muchos participantes (CCSS, MINSA, hospitales, Hacienda) donde todos deben permanecer en el loop | `replyAll: true` |
| Respuesta que excluye intencionalmente a alguien (ej. responder solo al remitente sin que vea su jefe, o sacar a un CC innecesario) | `replyAll: false` + `cc` minimizado o vacío — **declarar al usuario** la exclusión antes de crear el borrador |
| Hay duda sobre quién debe quedar copiado | `replyAll: false` + copiar los CCs del último mensaje de la contraparte, crear el borrador de inmediato y **declarar en el chat** los CCs usados para que el usuario los ajuste si corresponde |

**Default seguro**: `replyAll: false` con `cc` explícito y revisado. `replyAll: true` solo cuando el grupo del hilo está alineado con los destinatarios deseados sin recortes.

### Si se necesita correo nuevo (no respuesta)

Para correos nuevos sin hilo previo, se usa `Gmail:create_draft` (ver sección "Correos Nuevos" abajo). El endpoint Apps Script solo cubre `createReply`.

Crear el borrador **de inmediato** con la variante recomendada, sin preguntar. Si se mostraron variantes alternas, indicar en el chat que puede pedirse el reemplazo del cuerpo. No crear múltiples borradores salvo que el usuario lo pida.

---

## Correos Nuevos (Sin Hilo Previo)

Si el usuario pide redactar un correo nuevo (no una respuesta), se omite el paso de lectura de hilo. Flujo:

1. Confirmar destinatario(s) y asunto con el usuario si no quedó explícito.
2. Redactar con `message_compose_v1` siguiendo las mismas reglas de tono/idioma/firma.
3. Crear borrador con `Gmail:create_draft` (sin "Re:" en el subject, sin `threadId` — es correo nuevo, no necesita anidarse).

Contactos frecuentes (referencia de idioma y contexto; no es lista cerrada):

| Contacto | Email | Idioma | Rol |
|---|---|---|---|
| Marco Arias | colesa.marco@gmail.com | ES | Gerente Servicios Colé |
| Vanessa Mora | colesa.admi@gmail.com | ES | Administrativa/Facturación Colé |
| Jorge Hernández | (MYH Contadores) | ES | Contador externo |
| Murat Karademir | murat@radixray.com | EN | Proveedor Radixray/Meditek |
| IBA/Radcal, Ludlum, Polimaster, Klarity, LG Medical | varios | EN | Proveedores internacionales |
| CCSS, MINSA, hospitales CR | varios | ES | Clientes institucionales |

---

## Excepciones y Escalamientos

- **Temas legales/fiscales sensibles**: advertir al usuario antes de enviar; sugerir revisión por Jorge Hernández (contabilidad) o asesor legal.
- **Compromisos financieros >$10K o plazos regulatorios críticos**: crear el borrador de inmediato, pero exponer explícitamente en el chat lo que se está comprometiendo — el usuario revisa antes de enviar (el borrador nunca se envía solo).
- **Disputa comercial o cobro**: ofrecer al menos 2 variantes de tono (conciliador / firme).
- **MINSA, CCSS, reguladores**: usar referencias explícitas a número de carta, decreto o expediente; no redactar sin ellos.

---

## Qué NO Hacer

- ❌ Redactar basándose solo en el snippet de `search_threads`.
- ❌ Inventar cifras, fechas o compromisos que no estén en el hilo o que el usuario no haya confirmado.
- ❌ Usar "Excelente pregunta", "Espero que te encuentres bien", "Claro que sí" u otros rellenos vacíos.
- ❌ Enviar el correo directamente. **Siempre** es borrador — el usuario revisa y envía manualmente.
- ❌ Crear el borrador con CCs distintos a los del hilo original sin advertir al usuario.
- ❌ Cambiar el idioma del hilo sin instrucción explícita.
- ❌ Omitir la firma de Manuel.
- ❌ Usar `Gmail:create_draft` para responder a un hilo (genera correos sueltos fuera del hilo). Para respuestas, siempre `createReply` vía Apps Script.
- ❌ **Crear un draft nuevo cuando ya existe uno para el mismo hilo.** Si el `draftId` está visible en la conversación (creado en un turno anterior) o si `findDraftInThread` devuelve un id, usar `updateReply`. Nunca dejar dos drafts en el mismo hilo.
- ❌ Llamar al endpoint con `curl -X POST` o `--post301/302/303` (rompe con HTTP 405). Solo `curl -sL -d`.
- ❌ Cerrar sin crear el borrador anidado al hilo.
- ❌ Preguntar al usuario qué variante usar o pedir confirmación antes de crear el borrador — se crea de una vez con la variante recomendada; el usuario ajusta después si lo desea. Única pregunta permitida: desambiguar el hilo cuando hay varios candidatos (Paso 1).

---

## Checklist Final (Autoverificación Antes de Responder al Usuario)

1. ¿Leí el hilo completo con `FULL_CONTENT`? (no solo snippet)
2. ¿Detecté correctamente el idioma del hilo?
3. ¿Preservé los CCs originales (excluyendo `colesa.manuel@gmail.com` por ser sender)?
4. ¿La firma está correcta para el idioma?
5. ¿Verifiqué si ya existía un draft previo para este `threadId` (draftId en contexto o `findDraftInThread`)?
6. ¿Elegí la acción correcta (`createReply` para el primer draft del hilo, `updateReply` si ya había uno)?
7. ¿Llamé al endpoint Apps Script con `-sL -d` (sin `-X POST`)?
8. ¿Pasé el identificador correcto (`threadId` para `createReply`, `draftId` para `updateReply`)?
9. ¿La respuesta del endpoint trae `ok:true` y el `threadId` devuelto coincide con el del hilo original?
10. ¿Le confirmé al usuario que el borrador quedó anidado al hilo (no como correo suelto) y si fue creación o actualización?
