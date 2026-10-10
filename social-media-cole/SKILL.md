---
name: social-media-cole
description: >
  Gestión de redes sociales de Colé S.A. vía Odoo 18 Social Marketing (JSON-RPC).
  Crea, programa y publica posts en Facebook, LinkedIn, X (Twitter) y YouTube desde
  Odoo. Genera contenido técnico optimizado por plataforma a partir de artículos SEO,
  temas de protección radiológica, productos del catálogo o campañas de email marketing.
  Incluye calendario editorial, mensajes diferenciados por red, hashtags del sector,
  métricas de engagement y vinculación con campañas UTM. Activar con: redes sociales,
  publicar en LinkedIn, post de Facebook, tweet, publicar en X, social media, contenido
  para redes, calendario editorial, programar publicación, engagement, post técnico,
  crear post, publicar producto, promocionar curso, difundir artículo, social marketing,
  social Odoo, publicación Odoo, compartir en redes, post de Instagram, campaña social,
  contenido multiplataforma. Activar incluso si la solicitud parece simple.
---

# Social Media — Colé S.A. (Odoo 18)

## Alcance

Este skill gestiona publicaciones en redes sociales de Colé S.A. vía Odoo 18 Social Marketing:
1. **Crear posts** — Redactar contenido técnico optimizado por plataforma
2. **Mensajes diferenciados** — Texto adaptado a Facebook, LinkedIn, X (cada red tiene su campo)
3. **Programar** — Publicación inmediata o programada (scheduled_date en UTC)
4. **Campañas** — Vincular posts a campañas UTM para trazabilidad
5. **Métricas** — Consultar engagement, clicks, estados de publicación
6. **Calendario editorial** — Planificar contenido semanal/mensual

## Cuentas Sociales Vinculadas

| ID | Red | Cuenta | Handle |
|---|---|---|---|
| 1 | Facebook | Colé S.A. | /ColeLatam |
| 2 | LinkedIn | Cole SA | /colelatam |
| 3 | X (Twitter) | Colé SA | @colesacr |
| 4 | YouTube | Colé SA | @colesacr |

**Media IDs:** Facebook=1, Instagram=2, LinkedIn=3, X=4, YouTube=5

## Servicios y Productos de Colé S.A.

Para generar contenido con relevancia comercial, consultar `references/cole-services.md`
(compartido con `email-marketing-odoo`). Incluye:
- **Capacitación** — Cursos básicos y avanzados en protección radiológica
- **Servicios técnicos** — QC, mantenimiento, blindaje, pruebas de fuga
- **Equipos** — IBA/Radcal, Ludlum, Polimaster, Diagnomatic, Klarity, Radsource, Xstrahl, E&Z
- **Temas sugeridos** para contenido educativo y comercial

## Presencia Digital — REGLAS OBLIGATORIAS

Toda publicación generada por este skill DEBE cumplir TODAS estas reglas:

### A. Representación Exclusiva

Al mencionar CUALQUIER producto de terceros:
> **Colé S.A. — Representante exclusivo para Costa Rica y la región**

Excepción: Productos marca propia Colé S.A. → "Diseño propio Colé S.A."

### B. Links a Productos

Al mencionar un producto, buscar su URL en colecr.com (`site:colecr.com [nombre producto]`).
Incluir link directo. Si no existe página individual → categoría más cercana →
`https://colecr.com/productos/`.

### C. Links a Cursos

Si se mencionan cursos o capacitaciones, incluir SIEMPRE:
`https://colecr.com/cursos-de-capacitacion-en-proteccion-radiologica-formulario-f12-minsa-costa-rica/`

### D. URLs de Redes Sociales

| Red | URL |
|---|---|
| Web | https://www.colecr.com |
| Facebook | https://www.facebook.com/ColeLatam/ |
| LinkedIn Empresa | https://www.linkedin.com/company/104677153/ |
| LinkedIn Personal | https://www.linkedin.com/in/ing-manuel-rubio-msc/ |
| X (Twitter) | https://x.com/colesacr |
| YouTube | https://www.youtube.com/@colesacr |

### E. Checklist Pre-Publicación

```
☐ 1. ¿Productos de terceros llevan "Representante exclusivo para CR y la región"?
☐ 2. ¿Productos marca Colé llevan "Diseño propio Colé S.A."?
☐ 3. ¿Cada producto mencionado tiene link a colecr.com?
☐ 4. ¿Si se mencionan cursos, está el link a la página de cursos?
☐ 5. ¿El mensaje de LinkedIn es técnico-profesional?
☐ 6. ¿El mensaje de X cumple con límite de 280 caracteres?
☐ 7. ¿El mensaje de Facebook es más conversacional/visual?
☐ 8. ¿Los hashtags son relevantes al sector?
```

## Conexión — credencial externa

```
URL:       https://colesamarco2020-colesa.odoo.com/jsonrpc
Database:  colesamarco2020-colesa-colesa-27146045
UID:       7
API Key:   variable de entorno `ODOO_API_KEY`
Version:   Odoo 18 Enterprise
```

Antes de cualquier llamada, comprobar que `ODOO_API_KEY` exista. Si falta, detenerse
y pedir al titular que la configure fuera del repositorio; nunca escribirla en el skill.

### Código base

```python
import os, subprocess, json

URL = "https://colesamarco2020-colesa.odoo.com/jsonrpc"
DB  = "colesamarco2020-colesa-colesa-27146045"
UID = 7
KEY = os.environ.get("ODOO_API_KEY")
if not KEY:
    raise RuntimeError("Falta ODOO_API_KEY. Configúrala fuera del repositorio.")

def call(model, method, args, kwargs=None):
    payload = {
        "jsonrpc": "2.0", "method": "call", "id": 1,
        "params": {
            "service": "object", "method": "execute_kw",
            "args": [DB, UID, KEY, model, method, args, kwargs or {}]
        }
    }
    r = subprocess.run(
        ["curl", "-sk", "-X", "POST", URL,
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload)],
        capture_output=True, text=True, timeout=30
    )
    data = json.loads(r.stdout)
    if "error" in data:
        msg = data["error"].get("data", {}).get("message", str(data["error"]))
        raise Exception(f"Odoo [{model}.{method}]: {msg}")
    return data.get("result")
```

**SSL:** Siempre `curl -sk`. Nunca `requests` ni `xmlrpc.client`.

## Modelo Principal: social.post

### Campos clave

| Campo | Tipo | Descripción |
|---|---|---|
| `message` | text | Mensaje base (se copia a todos los canales si no hay mensajes por red) |
| `facebook_message` | text | Mensaje específico para Facebook |
| `linkedin_message` | text | Mensaje específico para LinkedIn |
| `twitter_message` | text | Mensaje específico para X (máx 280 chars) |
| `youtube_title` | char | Título de video YouTube |
| `youtube_description` | text | Descripción de video YouTube |
| `account_ids` | many2many | Cuentas destino: `[(6, 0, [1,2,3])]` = FB+LI+X |
| `post_method` | selection | `'now'` (publicar al enviar) o `'scheduled'` (programar) |
| `scheduled_date` | datetime | Fecha de publicación programada (UTC, Costa Rica = UTC-6) |
| `state` | selection | `draft` → `scheduled` → `posting` → `posted` |
| `source_id` | many2one | utm.source (REQUIRED) — usar "Social Colé Claude" |
| `utm_campaign_id` | many2one | utm.campaign (opcional, para campañas con trazabilidad) |
| `image_ids` | many2many | Imágenes adjuntas (ir.attachment) |
| `facebook_image_ids` | many2many | Imágenes específicas para Facebook |
| `linkedin_image_ids` | many2many | Imágenes específicas para LinkedIn |
| `twitter_image_ids` | many2many | Imágenes específicas para X |
| `click_count` | integer | Número de clicks (solo lectura) |
| `engagement` | integer | Engagement total (solo lectura) |

### Estados y transiciones

```
draft → (action_schedule) → scheduled → (cron de Odoo) → posting → posted
draft → (action_post) → posting → posted  [inmediato con post_method='now']
```

**Nota:** No existe `action_set_to_draft`. Para cancelar un post programado,
usar `unlink` (eliminar) o `write` para cambiar `state` directamente.

### Modelo secundario: social.live.post

Cada `social.post` genera un `social.live.post` por cuenta al momento de publicar.
Estados: `ready` → `posting` → `posted` | `failed`

Campos útiles: `state`, `failure_reason`, `account_id`, `engagement`.

## Operaciones

### 1. Obtener o crear UTM Source

```python
source_ids = call("utm.source", "search",
    [[["name", "=", "Social Colé Claude"]]])
if source_ids:
    SOURCE_ID = source_ids[0]
else:
    SOURCE_ID = call("utm.source", "create",
        [{"name": "Social Colé Claude"}])
```

### 2. Crear post con mensajes diferenciados por red

```python
post_id = call("social.post", "create", [{
    "message": "Mensaje base",
    "facebook_message": "📢 Mensaje optimizado para Facebook...",
    "linkedin_message": "🔬 Contenido técnico para LinkedIn...",
    "twitter_message": "⚡ Post corto para X #Hashtag #Otro",
    "account_ids": [(6, 0, [1, 2, 3])],  # FB + LinkedIn + X
    "post_method": "scheduled",
    "scheduled_date": "2026-04-01 15:00:00",  # UTC
    "source_id": SOURCE_ID,
}])
```

**Nota sobre account_ids:**
- Facebook: `[(6, 0, [1])]`
- LinkedIn: `[(6, 0, [2])]`
- X: `[(6, 0, [3])]`
- YouTube: `[(6, 0, [4])]`
- Todas (sin YT): `[(6, 0, [1, 2, 3])]`
- Todas: `[(6, 0, [1, 2, 3, 4])]`

### 3. Programar post (cambiar estado a scheduled)

```python
call("social.post", "action_schedule", [[post_id]])
# state: draft → scheduled
```

### 4. Publicar inmediatamente

```python
# Crear con post_method='now' y llamar action_post
post_id = call("social.post", "create", [{
    "message": "Publicación inmediata",
    "account_ids": [(6, 0, [1, 2, 3])],
    "post_method": "now",
    "source_id": SOURCE_ID,
}])
call("social.post", "action_post", [[post_id]])
```

### 5. Adjuntar imágenes

```python
import base64

# Leer imagen local
with open("/path/to/image.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

# Crear attachment en Odoo
att_id = call("ir.attachment", "create", [{
    "name": "post_image.png",
    "type": "binary",
    "datas": img_b64,
    "res_model": "social.post",
    "res_id": post_id,
}])

# Vincular a post
call("social.post", "write", [[post_id], {
    "image_ids": [(4, att_id)]
}])
```

### 6. Vincular a campaña UTM

```python
# Crear campaña
campaign_id = call("utm.campaign", "create",
    [{"name": "Campaña Q2 2026 - Protección Radiológica"}])

# Vincular al post
call("social.post", "write", [[post_id], {
    "utm_campaign_id": campaign_id
}])
```

### 7. Consultar posts existentes

```python
posts = call("social.post", "search_read", [[]],
    {"fields": ["name", "state", "message", "post_method",
                "scheduled_date", "published_date", "account_ids",
                "click_count", "engagement"],
     "order": "create_date desc",
     "limit": 20})
```

### 8. Consultar métricas de live posts

```python
live_posts = call("social.live.post", "search_read",
    [[["post_id", "=", post_id]]],
    {"fields": ["state", "account_id", "engagement", "failure_reason"]})
```

### 9. Listar cuentas sociales

```python
accounts = call("social.account", "search_read", [[]],
    {"fields": ["name", "media_id", "social_account_handle",
                "is_media_disconnected"]})
```

## Guía de Contenido por Plataforma

### LinkedIn (account_id=2) — Canal principal

**Tono:** Técnico-profesional, educativo, thought leadership.
**Formato:**
- Párrafo gancho (pregunta retórica o dato impactante)
- 2-3 párrafos de contenido técnico denso
- CTA (link a web, curso, contacto WhatsApp)
- 3-5 hashtags técnicos

**Hashtags frecuentes:**
`#ProtecciónRadiológica` `#MedicalImaging` `#RadiationSafety`
`#DoseOptimization` `#QualityControl` `#Dosimetry`
`#RadiologicalProtection` `#ImagenMédica` `#FísicaMédica`
`#SeguridadRadiológica` `#ControlDeCalidad`

**Límite:** 3,000 caracteres. Ideal: 1,200-1,800.

### Facebook (account_id=1)

**Tono:** Más visual, conversacional, accesible.
**Formato:**
- Emoji + frase gancho
- Explicación breve y accesible (menos jerga que LinkedIn)
- Imagen o foto obligatoria para engagement
- CTA claro con link
- 2-3 hashtags

**Límite:** 63,206 caracteres. Ideal: 400-800.

### X / Twitter (account_id=3)

**Tono:** Directo, conciso, impactante.
**Formato:**
- Dato o afirmación fuerte
- Link corto
- 2-3 hashtags
- **MÁXIMO 280 caracteres** (incluyendo hashtags y link)

### YouTube (account_id=4)

Solo para videos. Usar `youtube_title`, `youtube_description`, `youtube_video`.

## Flujo Recomendado

1. **Definir tema/objetivo** — ¿Producto? ¿Artículo SEO? ¿Curso? ¿Campaña?
2. **Cruce de servicios/productos** — OBLIGATORIO. Misma lógica que email-marketing-odoo:
   ```
   TEMA: [Tema del post]
   ─────────────────────────────────────────────
   Productos/servicios vinculables:
     ✅ [Producto] — [relevancia]
        🔗 URL web: [link]
        📌 Representante exclusivo para CR y la región
   Plataformas destino:
     ✅ LinkedIn (técnico)
     ✅ Facebook (visual/accesible)
     ✅ X (conciso)
   ─────────────────────────────────────────────
   → ¿Aprueba estos vínculos y plataformas?
   ```
3. **Generar mensajes diferenciados** — Un mensaje por red, adaptado al tono
4. **Presentar preview** — Mostrar los 3 mensajes al Ing. Rubio
5. **Aprobación** — NUNCA publicar sin aprobación explícita
6. **Crear post en Odoo** — `social.post` con `post_method` según preferencia
7. **Programar o publicar** — `action_schedule` o `action_post`
8. **Confirmar** — Leer estado y reportar

**NUNCA publicar directamente sin preview y aprobación.**

## Calendario Editorial

Para planificación semanal/mensual, generar tabla:

```
CALENDARIO EDITORIAL — [MES/SEMANA]
────────────────────────────────────────────────────────
Fecha       | Plataformas | Tema                | Estado
────────────────────────────────────────────────────────
Lun 01/04   | LI, FB, X   | Monitor LG 8MP     | Draft
Mié 03/04   | LI, X       | Artículo: TC dosis  | Pendiente
Vie 05/04   | FB, LI      | Curso PR abril      | Pendiente
────────────────────────────────────────────────────────
```

Programar cada post con `scheduled_date` en UTC (Costa Rica = UTC-6).
Horarios recomendados: LinkedIn martes-jueves 9-11am, Facebook lun-vie 1-3pm,
X cualquier día 8-10am o 5-7pm (hora local).

## Conversión de Artículos SEO a Posts

Cuando la fuente es un artículo del skill `seo-technical-writer`:

1. Extraer: título, párrafo clave, dato impactante, conclusión
2. LinkedIn: resumen técnico denso + link al artículo en colecr.com
3. Facebook: versión accesible + imagen + CTA
4. X: dato impactante + link + hashtags (≤280 chars)

## Notas Técnicas

- **scheduled_date en UTC** — Costa Rica = UTC-6. Si el Ing. Rubio dice "publicar a las 9am",
  usar `15:00:00` UTC.
- **source_id REQUIRED** — Siempre crear/usar "Social Colé Claude" como utm.source.
- **Imágenes** — Crear `ir.attachment` con base64, vincular a `image_ids` o a los campos
  específicos por red (`linkedin_image_ids`, etc.)
- **Instagram** — Requiere módulo `social_instagram` (actualmente NO instalado).
  Si el Ing. Rubio solicita Instagram, notificar que debe instalar el módulo primero.
- **YouTube** — Solo para publicar videos. Usa campos `youtube_*` en lugar de `message`.
- **No existe action_set_to_draft** — Para cancelar un post scheduled, usar `unlink`.
- **action_schedule** cambia state `draft→scheduled`, no genera live_posts inmediatamente.
  Los live_posts se crean cuando el cron de Odoo dispara la publicación.
- **action_post** publica inmediatamente (genera live_posts y los envía).
- **Deduplicar UTM sources** — Verificar existencia antes de crear.
