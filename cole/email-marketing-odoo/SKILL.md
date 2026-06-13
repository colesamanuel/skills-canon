---
name: email-marketing-odoo
description: "Campañas de email marketing en Odoo 18 de Colé S.A. vía JSON-RPC. Gestiona listas de contactos (mailing.list, mailing.contact), crea y envía campañas (mailing.mailing), diseña cuerpo HTML del email, programa envíos, consulta métricas (sent, opened, clicked, bounced), y segmenta destinatarios (res.partner, crm.lead, mailing.contact). SMTP configurado: mail.colecr.com:465 SSL. Activar con: email marketing, campaña de correo, mailing, newsletter, envío masivo, lista de correo, suscriptores, crear campaña, métricas de email, open rate, bounce, segmentar contactos, plantilla de email, enviar correo masivo, blast email, correo a clientes, correo a leads, email Odoo, marketing Odoo. Activar incluso si la solicitud parece simple."
---

# Email Marketing — Colé S.A. (Odoo 18)

## Alcance

Este skill gestiona campañas de email marketing en Odoo 18:
1. **Listas de contactos** — Crear/gestionar listas, agregar/importar contactos
2. **Campañas** — Crear mailings con HTML, segmentar destinatarios, programar envío
3. **Envío** — Enviar inmediato o programado, A/B testing
4. **Métricas** — Consultar sent/opened/clicked/bounced/replied
5. **Segmentación** — Enviar a listas, contactos, partners CRM o leads

## Servicios y Productos de Colé S.A.

Para diseñar campañas con contenido relevante, consultar `references/cole-services.md`.
Incluye el catálogo completo de servicios autorizados por el Ministerio de Salud:
- **Capacitación** — Cursos básicos y avanzados en protección radiológica (médica, veterinaria, industrial)
- **Servicios técnicos** — QC de equipos, mantenimiento, blindaje, levantamientos, pruebas de fuga
- **Equipos** — IBA/Radcal, Ludlum, Polimaster, Diagnomatic, Klarity, Radsource, Xstrahl, Eckert & Ziegler
- **Temas sugeridos** para campañas educativas y comerciales

Resoluciones vigentes: UGR-CR-050-2006-S (servicios) y MS-DPRSA-UPR-SC-0003-2025 (cursos).
Vigencia: 12 de abril 2026. Instructor: Ing. Manuel Rubio Gutiérrez.

## Presencia Digital y Representación Comercial — REGLAS OBLIGATORIAS

Toda campaña de email marketing generada por este skill DEBE cumplir TODAS las reglas
siguientes. No son opcionales. Verificar cumplimiento antes de generar el HTML.

### A. Representación Exclusiva

**Texto estándar obligatorio:** Al describir CUALQUIER producto de terceros en una campaña,
incluir la frase:

> **Colé S.A. — Representante exclusivo para Costa Rica y la región**

Esto aplica a TODAS las marcas del catálogo:
IBA Dosimetry, Radcal, Diagnomatic, Leeds Test Objects, Polimaster, Ludlum,
Klarity, Rad Source, Xstrahl, Eckert & Ziegler, LG Electronics Medical Division,
CIRS, Kyoto Kagaku, Pure Imaging Phantoms, Phillips Safety.

**Excepción:** Productos marca propia Colé S.A. (delantales, blindaje, accesorios)
NO llevan "representante exclusivo" — llevan "Fabricación/Diseño propio Colé S.A."

**Ubicación en el email:** Inmediatamente debajo del nombre/descripción del producto,
como subtítulo o línea de texto con estilo diferenciado (color `#3155e2` o itálica).

### B. Links a Productos en la Web

**Estructura de URLs de productos en colecr.com:**
- Producto individual: `https://colecr.com/producto/[slug-del-producto]/`
- Categoría: `https://colecr.com/categoria-producto/[slug-categoria]/`
- Catálogo general: `https://colecr.com/productos/`

**Regla:** Al mencionar un producto específico en una campaña, SIEMPRE buscar su URL
en colecr.com (vía web search `site:colecr.com [nombre producto]`) e incluir el link
directo. Si no se encuentra página individual, vincular a la categoría más cercana.
Si no existe categoría, vincular a `https://colecr.com/productos/`.

**Formato en el email:** Botón CTA o texto con link:
`🔗 Ver producto en nuestra web → [URL]`

### C. Link a Cursos

**Regla:** Si la campaña promociona, menciona o referencia CUALQUIER curso, capacitación,
taller, o formación en protección radiológica, incluir SIEMPRE el link a la página de cursos:

`https://colecr.com/cursos-de-capacitacion-en-proteccion-radiologica-formulario-f12-minsa-costa-rica/`

**Formato:** Botón CTA prominente o sección dedicada:
`📚 Conozca nuestros cursos autorizados por el Ministerio de Salud → [URL]`

Esto aplica incluso si los cursos no son el tema principal de la campaña pero se
mencionan incidentalmente (ej: "Además, recuerde que ofrecemos capacitación...").

### D. Redes Sociales — OBLIGATORIO en TODA campaña

**Toda campaña DEBE incluir en el footer los iconos/links a redes sociales:**

| Red | URL | Handle |
|---|---|---|
| Web | https://www.colecr.com | www.colecr.com |
| Facebook | https://www.facebook.com/ColeLatam/ | /ColeLatam |
| LinkedIn Empresa | https://www.linkedin.com/company/104677153/ | /ColéLatam |
| LinkedIn Personal | https://www.linkedin.com/in/ing-manuel-rubio-msc/ | /ing-manuel-rubio-msc |
| X (Twitter) | https://x.com/colesacr | @colesacr |

**Formato en footer HTML:** Iconos alineados horizontalmente con links, seguidos de
"Síguenos en nuestras redes sociales" como texto introductorio.

**CTA de redes:** Incluir al menos una mención a redes sociales en el cuerpo del email
(no solo en footer), por ejemplo:
`Síganos en nuestras redes para más novedades → [iconos con links]`

### E. Checklist Pre-Generación de HTML

Antes de generar el `body_html` de cualquier campaña, verificar:

```
☐ 1. ¿Productos de terceros llevan "Representante exclusivo para CR y la región"?
☐ 2. ¿Productos marca Colé llevan "Diseño propio Colé S.A."?
☐ 3. ¿Cada producto mencionado tiene link a su página en colecr.com?
☐ 4. ¿Si se mencionan cursos, está el link a la página de cursos?
☐ 5. ¿El footer incluye los 5 canales de redes sociales con URLs correctas?
☐ 6. ¿Hay al menos 1 mención a redes sociales en el cuerpo (no solo footer)?
☐ 7. ¿El logo oficial está en el encabezado a ancho completo?
☐ 8. ¿email_from es m.rubio@colecr.com?
```

**Si algún punto falla → corregir antes de generar.** No pedir confirmación para
cumplir estas reglas — son automáticas. Sí pedir confirmación para el contenido
y los productos/servicios vinculados (paso 2 del Flujo Recomendado).

## Conexión — NO preguntar credenciales

```
URL:       https://colesamarco2020-colesa.odoo.com/jsonrpc
Database:  colesamarco2020-colesa-colesa-27146045
UID:       7
API Key:   c05ae3a29733ef6f21933c7a4c7d1b5ed091a2b4
Version:   Odoo 18 Enterprise
```

### Código base

```python
import subprocess, json

URL = "https://colesamarco2020-colesa.odoo.com/jsonrpc"
DB  = "colesamarco2020-colesa-colesa-27146045"
UID = 7
KEY = "c05ae3a29733ef6f21933c7a4c7d1b5ed091a2b4"

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

## Configuración actual

| Concepto | Valor |
|---|---|
| Servidor SMTP | mail.colecr.com:465 (SSL), user: m.rubio@colecr.com |
| Email remitente (email_from) | `"Colé S.A." <m.rubio@colecr.com>` **(OBLIGATORIO — debe coincidir con dominio SMTP)** |
| Reply-to | `colesa.manuel@gmail.com` (las respuestas llegan a Gmail) |
| Catchall domain | colesamarco2020-colesa-colesa-27146045.dev.odoo.com |
| Listas activas (catálogo aprobado) | **ID 2** Contactos Colé SA (978) · **ID 3** kermatek (332) · **ID 16** Contactos Activos Colé + Kermatek (1,147 — maestra consolidada) |
| Política de listas | **NO crear listas nuevas por campaña.** Reutilizar las 3 del catálogo. Excepción solo con aprobación explícita del Ing. Rubio (eventos puntuales, segmentación temporal acotada). |

**⚠️ REGLA CRÍTICA DE SMTP:** El `email_from` SIEMPRE debe usar `m.rubio@colecr.com`
(mismo dominio que el servidor SMTP). Si se usa `colesa.manuel@gmail.com` como remitente,
Gmail rechaza silenciosamente el email por fallo SPF. Las respuestas se dirigen a
`reply_to` que sí puede ser `colesa.manuel@gmail.com`.

## 1. Listas de Contactos (mailing.list)

### Crear lista

```python
list_id = call("mailing.list", "create", [{
    "name": "Clientes Radiodiagnóstico 2026",
    "is_public": False,  # No mostrar en preferencias públicas
}])
```

### Agregar contactos a lista

```python
# Crear contacto y asociar a lista
contact_id = call("mailing.contact", "create", [{
    "name": "Dr. Carlos Pérez",
    "email": "cperez@hospital.go.cr",
    "company_name": "Hospital San Juan de Dios",
    "country_id": 49,  # Costa Rica
    "list_ids": [(4, list_id)],  # Asociar a lista
    "tag_ids": [(4, TAG_ID)],    # Tags opcionales
}])
```

### Importar múltiples contactos

```python
contactos = [
    {"name": "Ing. Ana López", "email": "alopez@ccss.sa.cr", "company_name": "CCSS"},
    {"name": "Dr. Roberto Mora", "email": "rmora@hnn.sa.cr", "company_name": "HNN"},
    # ...
]
for c in contactos:
    c["list_ids"] = [(4, list_id)]
    call("mailing.contact", "create", [c])
```

### Importar desde res.partner (contactos CRM)

```python
# Buscar partners con etiqueta "MEDICINA NUCLEAR"
partners = call("res.partner", "search_read",
    [[["category_id.name", "=", "MEDICINA NUCLEAR"], ["email", "!=", False]]],
    {"fields": ["name", "email", "company_type"], "limit": 200})

# Crear como mailing.contact y asociar a lista
for p in partners:
    call("mailing.contact", "create", [{
        "name": p["name"],
        "email": p["email"],
        "list_ids": [(4, list_id)],
    }])
```

### Consultar contactos de una lista

```python
contacts = call("mailing.contact", "search_read",
    [[["list_ids", "in", [list_id]], ["opt_out", "=", False]]],
    {"fields": ["name", "email", "company_name", "country_id"],
     "limit": 200})
```

### Dar de baja (opt-out)

```python
call("mailing.contact", "write", [[contact_id], {"opt_out": True}])
```

## 2. Crear Campaña de Email

### Modelos de destinatarios disponibles

| model_id | Modelo | Uso |
|---|---|---|
| 591 | `mailing.list` | **FLUJO OBLIGATORIO** — Siempre enviar a listas de correo |
| 590 | `mailing.contact` | Contactos de mailing directamente (no recomendado para masivos) |
| 87 | `res.partner` | ⚠️ **NO USAR PARA ENVÍO MASIVO** — Odoo 18 SaaS no procesa la cola SMTP correctamente con este modelo. El envío queda en `done` con 0 enviados |
| 666 | `crm.lead` | ⚠️ **NO USAR PARA ENVÍO MASIVO** — misma limitación que res.partner |
| 639 | `sale.order` | ⚠️ **NO USAR PARA ENVÍO MASIVO** |

**⚠️ REGLA CRÍTICA DE ENVÍO (Odoo 18 SaaS):**
El único flujo que garantiza el envío masivo es:
1. **Seleccionar lista existente** del catálogo aprobado (ID 2, 3 o 16). NO crear lista nueva salvo aprobación explícita del Ing. Rubio.
2. Si hay contactos nuevos a incorporar: agregarlos a la lista 16 como `mailing.contact` (no crear lista temporal por campaña)
3. Crear `mailing.mailing` con `mailing_model_id: 591` y `contact_list_ids` apuntando a la lista seleccionada
4. Ejecutar `action_launch` → `action_send_mail`

Los modelos `res.partner` (87) y `crm.lead` (666) generan trazas pero el cron SMTP
no las despacha. **NUNCA** apuntar una campaña masiva directamente a res.partner.

### Flujo obligatorio: Lista existente → Campaña

#### Flujo A (DEFAULT) — Reutilizar lista del catálogo aprobado

```python
# PASO 1: Seleccionar lista del catálogo aprobado
TARGET_LIST_ID = 16  # Default: lista maestra consolidada (Colé + Kermatek)
# Otras opciones válidas:
#   2  = Contactos Colé SA (segmentación solo Colé, 978 contactos)
#   3  = kermatek (segmentación solo Kermatek, 332 contactos)
#   16 = Contactos Activos Colé + Kermatek (maestra consolidada, 1,147 contactos)

# PASO 2 (opcional): Incorporar contactos nuevos a la lista 16
# Solo si la campaña requiere alcance extendido a contactos no presentes aún.
# Reportar al Ing. Rubio cuántos se agregaron antes de continuar.
nuevos_emails = [...]  # emails a incorporar
agregados = 0
for email in nuevos_emails:
    em = email.strip().lower()
    if not em or '@' not in em:
        continue
    existing = call("mailing.contact", "search",
        [[["email", "=ilike", em]]])
    if existing:
        # Ya existe — solo asociar a lista 16 (idempotente)
        call("mailing.contact", "write", [existing, {
            "list_ids": [(4, 16)]
        }])
    else:
        # No existe — crear y asociar a lista 16
        call("mailing.contact", "create", [{
            "name": em,
            "email": em.strip(),
            "list_ids": [(4, 16)],
        }])
    agregados += 1
# Reportar: f"Agregados {agregados} contactos a lista 16"

# PASO 3: Crear campaña apuntando a la lista existente
mailing_id = call("mailing.mailing", "create", [{
    "subject": "Asunto de la campaña — Colé S.A.",
    "mailing_type": "mail",
    "mailing_model_id": 591,  # mailing.list ← OBLIGATORIO
    "contact_list_ids": [(6, 0, [TARGET_LIST_ID])],
    "email_from": '"Colé S.A." <m.rubio@colecr.com>',
    "reply_to_mode": "new",
    "reply_to": "colesa.manuel@gmail.com",
    "body_arch": BODY_HTML,
    "body_html": BODY_HTML,
}])

# PASO 4: Lanzar y forzar envío
call("mailing.mailing", "action_launch", [[mailing_id]])
call("mailing.mailing", "action_send_mail", [[mailing_id]])
```

#### Flujo B (EXCEPCIÓN) — Crear lista temporal con aprobación explícita

⚠️ **SOLO usar cuando el Ing. Rubio aprueba explícitamente** la creación de lista temporal
(ej.: campaña a asistentes confirmados de un evento puntual, segmentación geográfica
acotada con vencimiento). En todos los demás casos usar Flujo A.

Antes de crear lista temporal, plantear al Ing. Rubio:
- ¿Por qué no sirve la lista 16 (maestra)?
- ¿La lista temporal se archivará tras la campaña? (recomendado: SÍ)
- Nombre con prefijo `[TEMP]` y fecha de vencimiento (ej.: `[TEMP] Webinar XYZ - 2026-06`)

```python
# PASO 1: Crear lista temporal (solo con aprobación)
list_id = call("mailing.list", "create", [{
    "name": "[TEMP] Webinar XYZ — 2026-06",  # Prefijo [TEMP] OBLIGATORIO
    "is_public": False,
}])

# PASO 2: Obtener partners con email válido
partners = call("res.partner", "search_read",
    [[["email", "!=", False], ["email", "!=", ""]]],
    {"fields": ["name", "email", "company_name"], "limit": 500})

# PASO 3: Importar como mailing.contact (deduplicar por email)
# ⚠️ CRÍTICO: res.partner tiene muchos duplicados (ej: info@clinica.com con múltiples
# contactos). Si no se deduplica, Odoo genera trazas por cada contacto y cancela los
# repetidos al enviar — inflando artificialmente el conteo de cancelados.
# Además, verificar que el email no exista ya en mailing.contact antes de crear.
existing = call("mailing.contact", "search_read",
    [[["list_ids", "in", [list_id]]]], {"fields": ["email"], "limit": 1000})
seen_emails = set(c['email'].strip().lower() for c in existing if c.get('email'))
for p in partners:
    email = p['email'].strip().lower()
    if email in seen_emails or not email or '@' not in email:
        continue
    seen_emails.add(email)
    try:
        call("mailing.contact", "create", [{
            "name": p['name'] or email,
            "email": p['email'].strip(),
            "company_name": p.get('company_name') or '',
            "list_ids": [(4, list_id)],
        }])
    except:
        pass  # Duplicado u otro error

# PASO 4: Crear campaña apuntando a la lista
mailing_id = call("mailing.mailing", "create", [{
    "subject": "Asunto de la campaña — Colé S.A.",
    "mailing_type": "mail",
    "mailing_model_id": 591,  # mailing.list ← OBLIGATORIO
    "contact_list_ids": [(6, 0, [list_id])],
    "email_from": '"Colé S.A." <m.rubio@colecr.com>',
    "reply_to_mode": "new",
    "reply_to": "colesa.manuel@gmail.com",
    "body_arch": BODY_HTML,
    "body_html": BODY_HTML,
}])

# PASO 5: Lanzar y forzar envío
call("mailing.mailing", "action_launch", [[mailing_id]])
call("mailing.mailing", "action_send_mail", [[mailing_id]])

# PASO 6 (post-campaña): Archivar lista temporal
# call("mailing.list", "write", [[list_id], {"active": False}])
```

### Importar partners segmentados (por etiqueta CRM)

```python
# Ejemplo: solo partners con etiqueta "Radioterapia"
partners = call("res.partner", "search_read",
    [[["category_id.name", "=", "Radioterapia"], ["email", "!=", False]]],
    {"fields": ["name", "email", "company_name"], "limit": 200})

# Luego importar a lista con el mismo flujo del PASO 3 arriba
```

### Crear mailing básico a lista existente

```python
mailing_id = call("mailing.mailing", "create", [{
    "subject": "Nuevos equipos de control de calidad — Colé S.A.",
    "mailing_type": "mail",
    "mailing_model_id": 591,  # mailing.list
    "contact_list_ids": [(6, 0, [list_id])],
    "email_from": '"Colé S.A." <m.rubio@colecr.com>',
    "reply_to_mode": "new",
    "reply_to": "colesa.manuel@gmail.com",
    "body_arch": BODY_HTML,
    "body_html": BODY_HTML,
    "schedule_type": "now",   # "now" o "scheduled"
    # "schedule_date": "2026-04-01 14:00:00",  # Si es programado
}])
```

## 3. Diseño del Email (body_html)

El cuerpo del email es HTML. Odoo 18 usa `body_arch` (editor) y `body_html` (envío).
Ambos deben contener el mismo HTML.

### Elementos multimedia soportados

| Elemento | Método | Notas |
|---|---|---|
| **Imágenes** | `<img src="URL">` con URL externa | Hospedar en colecr.com o CDN. No usar base64 en masivos |
| **Videos** | Thumbnail con link a YouTube/Vimeo | Los clientes de correo NO ejecutan `<video>` ni `<iframe>` |
| **Links web** | `<a href="URL">` | Odoo los trackea automáticamente (link.tracker) |
| **Botones CTA** | Table-based button con `<a>` | Máximo 2-3 por email |
| **PDFs adjuntos** | `attachment_ids: [(6, 0, [att_id])]` | Catálogos, fichas técnicas |
| **Redes sociales** | Iconos con links | En footer |
| **GIFs** | `<img src="URL.gif">` | Soportado, mantener <500KB |


Para la plantilla HTML completa con multimedia (banner, imágenes de producto,
video thumbnail, grid de productos, botones CTA, redes sociales, footer),
consultar `references/email-templates.md`.

### Buenas prácticas para email HTML

- **Ancho máximo 600px** — compatible con todos los clientes de correo
- **Estilos inline** — No usar `<style>` externo, Gmail lo elimina
- **Imágenes:** siempre incluir `alt`, `style="display:block"`, ancho máximo 540px
- **No usar:** `<video>`, `<iframe>`, JavaScript, CSS `position:absolute` (no funciona en email)
- **Videos:** siempre como thumbnail estático + link. Usar `https://img.youtube.com/vi/[ID]/hqdefault.jpg` para thumbnail automático de YouTube
- **Peso total:** <100KB HTML + imágenes externas referenciadas por URL
- **Testear:** Enviar prueba a Gmail, Outlook y móvil antes de masivo
- **Branding Colé:** Azul `#3155e2`, Cyan `#70e7ff`, Gris `#363b47`, Roboto + Open Sans
- **⚠️ LOGO OBLIGATORIO EN ENCABEZADO:** Todo email DEBE incluir el logotipo oficial de Colé S.A. como primer elemento visible (antes del banner), a **ancho completo** (width:100%, display:block, padding:0). URL de producción: `https://colecr.com/wp-content/uploads/2026/03/Logo-Doc1-scaled.png` (600px ancho, display:block, con link a colecr.com). Ver bloque HTML en `references/email-templates.md`.

### Adjuntar archivos (PDFs, catálogos)

```python
import base64

# 1. Subir adjunto a Odoo
with open("catalogo-cole-2026.pdf", "rb") as f:
    pdf_b64 = base64.b64encode(f.read()).decode()

att_id = call("ir.attachment", "create", [{
    "name": "Catálogo Colé S.A. 2026.pdf",
    "type": "binary",
    "datas": pdf_b64,
    "mimetype": "application/pdf",
}])

# 2. Asociar al mailing
call("mailing.mailing", "write", [[mailing_id], {
    "attachment_ids": [(4, att_id)],
}])
```

### Variables dinámicas disponibles

**⚠️ REGLA QWEB vs JINJA INLINE — CRÍTICA.** Odoo 18 mass mailing usa motores de render distintos según el campo. Confundirlos deja el placeholder literal en el correo entregado.

| Campo del `mailing.mailing` | Motor de render | Sintaxis correcta |
|---|---|---|
| `subject`, `email_from`, `reply_to`, `preview` | `inline_template` | `{{ object.name }}` |
| `body_html`, `body_arch` | `qweb` | `<t t-out="object.name"/>` |

> Incidente de referencia: campaña 27 enviada 2026-05-15 con `{{ object.name }}` dentro de `body_html`. 478 destinatarios recibieron "Estimado/a {{ object.name }}," literal porque el motor Qweb no procesa la sintaxis Jinja.

**Fallback recomendado en Qweb** cuando el campo `name` puede venir vacío o ser igual al email del contacto:

```html
Estimado/a <t t-if="object.name and '@' not in object.name"><t t-out="object.name"/></t><t t-else="">colega</t>,
```

#### Variables para `subject`, `email_from`, `reply_to`, `preview` (Jinja inline)

| Variable | Modelo | Descripción |
|---|---|---|
| `{{ object.name }}` | Todos | Nombre del destinatario |
| `{{ object.email }}` | Todos | Email |
| `{{ object.company_name }}` | mailing.contact | Empresa |
| `{{ object.partner_id.name }}` | crm.lead | Nombre partner en lead |
| `{{ object.stage_id.name }}` | crm.lead | Stage del pipeline |
| `{{ user.name }}` | — | Nombre del remitente |
| `{{ object.country_id.name }}` | mailing.contact | País del contacto |

#### Variables para `body_html` / `body_arch` (Qweb)

| Variable | Modelo | Descripción |
|---|---|---|
| `<t t-out="object.name"/>` | Todos | Nombre del destinatario |
| `<t t-out="object.email"/>` | Todos | Email |
| `<t t-out="object.company_name"/>` | mailing.contact | Empresa |
| `<t t-out="object.partner_id.name"/>` | crm.lead | Nombre partner en lead |
| `<t t-out="object.stage_id.name"/>` | crm.lead | Stage del pipeline |
| `<t t-out="user.name"/>` | — | Nombre del remitente |
| `<t t-out="object.country_id.name"/>` | mailing.contact | País del contacto |

#### Excepción: URLs en `href` de `body_html`

El link de unsubscribe se inserta en el `href` con sintaxis Jinja URL-encoded — Odoo lo procesa post-render del Qweb:

```html
<a href="{{ unsubscribe_url }}">cancelar suscripción</a>
```

## 4. Envío

### Enviar inmediatamente — Flujo completo obligatorio

**⚠️ REGLA CRÍTICA:** El cron de Odoo 18 SaaS solo despacha ~50 emails por ciclo.
Para campañas con más de 50 destinatarios, se DEBE forzar el envío en lotes vía `mail.mail.send`.
Este flujo de 3 pasos es OBLIGATORIO para TODA campaña masiva.

**⚠️ LÍMITES SMTP — RESPETAR SIEMPRE:**

| Servidor | Límite por hora | Límite por día | Pausa entre lotes |
|---|---|---|---|
| cPanel (`mail.colecr.com`) | ~250 | ~500-1500 (varía según hosting) | 10s por lote de 20 |
| Gmail SMTP | ~100 | ~500 (Workspace: ~2000) | 15s por lote de 20 |

**REGLA DE VELOCIDAD:** Enviar en lotes de **20 emails** con **10 segundos** de pausa entre
lotes. Esto produce ~120 emails/hora, muy por debajo de cualquier límite. Para campañas
grandes (>500 destinatarios), distribuir el envío en **múltiples sesiones** separadas por
al menos 1 hora, o idealmente en días consecutivos (~400/día máximo seguro para cPanel).

**ANTES DE ENVIAR:** Verificar cuántos emails se han enviado HOY desde el mismo servidor
consultando campañas con `sent_date` del día actual. Si el acumulado diario + destinatarios
de la nueva campaña supera 400, ADVERTIR al Ing. Rubio y sugerir programar el envío
en tramos o al día siguiente.

```python
import time

# ═══════════════════════════════════════════════
# PASO 0: Verificar acumulado diario SMTP
# ═══════════════════════════════════════════════
from datetime import datetime, timedelta
today_utc = datetime.utcnow().strftime("%Y-%m-%d 00:00:00")
today_mailings = call("mailing.mailing", "search_read",
    [[["sent_date", ">=", today_utc], ["state", "=", "done"]]],
    {"fields": ["subject", "sent"], "limit": 50})
daily_total = sum(m["sent"] for m in today_mailings)
print(f"📊 Emails enviados hoy: {daily_total}")
# ⚠️ Si daily_total + nuevos_destinatarios > 400 → ADVERTIR

# ═══════════════════════════════════════════════
# PASO 1: Poner en cola (genera trazas y mail.mail)
# ═══════════════════════════════════════════════
call("mailing.mailing", "action_launch", [[mailing_id]])
# state: draft → in_queue

# ═══════════════════════════════════════════════
# PASO 2: Primer despacho SMTP (~50 emails)
# ═══════════════════════════════════════════════
call("mailing.mailing", "action_send_mail", [[mailing_id]])
# Despacha el primer lote. state: in_queue → sending → done
# NOTA: después de esto, action_send_mail YA NO funciona (campaña en done)

time.sleep(10)

# ═══════════════════════════════════════════════
# PASO 3: Forzar envío de emails restantes con throttling
# ═══════════════════════════════════════════════
BATCH_SIZE = 20        # Lotes pequeños para evitar saturar SMTP
PAUSE_SECONDS = 10     # Pausa entre lotes (10s = ~120/hora)
MAX_PER_SESSION = 400  # Máximo por sesión de envío

outgoing_mails = call("mail.mail", "search",
    [[["mailing_id", "=", mailing_id], ["state", "=", "outgoing"]]],
    {"limit": 2000})

if outgoing_mails:
    total_sent = 0
    total_errors = 0
    session_limit = min(len(outgoing_mails), MAX_PER_SESSION - daily_total)
    if session_limit <= 0:
        print("⚠️ Límite diario alcanzado. Programar reenvío para mañana.")
    else:
        for i in range(0, session_limit, BATCH_SIZE):
            batch = outgoing_mails[i:i+BATCH_SIZE]
            try:
                call("mail.mail", "send", [batch])
                total_sent += len(batch)
                print(f"  ✅ Lote {i//BATCH_SIZE+1}: {len(batch)} OK (acum: {total_sent})")
            except Exception as e:
                error_msg = str(e)
                total_errors += 1
                if "limit exceeded" in error_msg.lower() or "552" in error_msg:
                    print(f"  🛑 Límite SMTP alcanzado tras {total_sent} emails.")
                    print(f"     Restantes: {len(outgoing_mails) - total_sent}")
                    print(f"     → Ejecutar recuperación de fallos (ver sección 4.1)")
                    break
                else:
                    print(f"  ⚠️ Error lote {i//BATCH_SIZE+1}: {error_msg[:100]}")
            time.sleep(PAUSE_SECONDS)
        
        remaining = call("mail.mail", "search_count",
            [[["mailing_id", "=", mailing_id], ["state", "=", "outgoing"]]])
        failed = call("mail.mail", "search_count",
            [[["mailing_id", "=", mailing_id], ["state", "=", "exception"]]])
        
        print(f"\n📊 RESUMEN DE ENVÍO:")
        print(f"   Enviados esta sesión: {total_sent}")
        print(f"   Pendientes (outgoing): {remaining}")
        print(f"   Fallidos (exception): {failed}")
        print(f"   Errores de lote: {total_errors}")
        if remaining > 0 or failed > 0:
            print(f"   → Ejecutar recuperación (sección 4.1) en próxima sesión")
else:
    print("✅ Todos los emails fueron despachados en el paso 2")
```

**¿Por qué 3 pasos?**
- `action_launch` genera las trazas (`mailing.trace`) y los `mail.mail` en estado `outgoing`
- `action_send_mail` despacha el primer lote (~50), luego la campaña pasa a `done`
- Una vez en `done`, `action_send_mail` ya no funciona → los restantes se fuerzan
  directamente con `mail.mail.send` en lotes de 20 con pausas de 10s

### 4.1 Recuperación de fallos (exception → reenvío)

Cuando emails quedan en estado `exception` por límite SMTP u otro error transitorio,
este procedimiento los resetea y reenvía. **Ejecutar al día siguiente o tras esperar
al menos 1 hora si el error fue por límite horario.**

```python
import time

# ═══════════════════════════════════════════════
# RECUPERACIÓN: Resetear y reenviar emails fallidos
# ═══════════════════════════════════════════════

BATCH_SIZE = 20
PAUSE_SECONDS = 10
MAX_PER_SESSION = 400

# Paso A: Verificar acumulado diario antes de reintentar
today_utc = datetime.utcnow().strftime("%Y-%m-%d 00:00:00")
today_mailings = call("mailing.mailing", "search_read",
    [[["sent_date", ">=", today_utc], ["state", "=", "done"]]],
    {"fields": ["sent"], "limit": 50})
daily_total = sum(m["sent"] for m in today_mailings)
print(f"📊 Emails enviados hoy: {daily_total}")

# Paso B: Obtener mail.mail en exception
failed_ids = call("mail.mail", "search",
    [[["mailing_id", "=", mailing_id], ["state", "=", "exception"]]],
    {"limit": 2000})
print(f"📬 Emails en exception: {len(failed_ids)}")

if not failed_ids:
    print("✅ No hay emails pendientes de recuperación.")
else:
    # Paso C: Verificar failure_reason (muestra)
    sample = call("mail.mail", "read", [failed_ids[:3],
        ["failure_reason", "email_from"]])
    for s in sample:
        print(f"  Razón: {str(s.get('failure_reason',''))[:100]}")
        print(f"  From: {s.get('email_from')}")
    
    # Paso D: Corregir email_from si es necesario
    wrong_from = call("mail.mail", "search",
        [[["mailing_id", "=", mailing_id], ["state", "=", "exception"],
          ["email_from", "not ilike", "m.rubio@colecr.com"]]],
        {"limit": 2000})
    if wrong_from:
        print(f"  ⚠️ Corrigiendo email_from en {len(wrong_from)} emails...")
        for i in range(0, len(wrong_from), 100):
            call("mail.mail", "write", [wrong_from[i:i+100], {
                "email_from": '"Colé S.A." <m.rubio@colecr.com>',
                "mail_server_id": False
            }])
    
    # Paso E: Resetear estado a outgoing
    session_limit = min(len(failed_ids), MAX_PER_SESSION - daily_total)
    if session_limit <= 0:
        print("⚠️ Límite diario alcanzado. Reintentar mañana.")
    else:
        batch_to_retry = failed_ids[:session_limit]
        for i in range(0, len(batch_to_retry), 100):
            batch = batch_to_retry[i:i+100]
            call("mail.mail", "write", [batch, {
                "state": "outgoing",
                "failure_reason": False,
                "failure_type": False
            }])
        
        # Resetear trazas correspondientes
        error_traces = call("mailing.trace", "search",
            [[["mass_mailing_id", "=", mailing_id], ["trace_status", "=", "error"]]],
            {"limit": 2000})
        for i in range(0, len(error_traces), 100):
            call("mailing.trace", "write", [error_traces[i:i+100], {
                "trace_status": "outgoing",
                "failure_type": False
            }])
        
        # Paso F: Reenviar con throttling
        outgoing = call("mail.mail", "search",
            [[["mailing_id", "=", mailing_id], ["state", "=", "outgoing"]]],
            {"limit": 2000})
        
        total_sent = 0
        for i in range(0, len(outgoing), BATCH_SIZE):
            batch = outgoing[i:i+BATCH_SIZE]
            try:
                call("mail.mail", "send", [batch])
                total_sent += len(batch)
                print(f"  ✅ Lote {i//BATCH_SIZE+1}: {len(batch)} OK (acum: {total_sent})")
            except Exception as e:
                if "limit exceeded" in str(e).lower():
                    print(f"  🛑 Límite SMTP. Enviados: {total_sent}. Reintentar después.")
                    break
                print(f"  ⚠️ Error: {str(e)[:100]}")
            time.sleep(PAUSE_SECONDS)
        
        # Verificación final
        still_failed = call("mail.mail", "search_count",
            [[["mailing_id", "=", mailing_id], ["state", "=", "exception"]]])
        still_outgoing = call("mail.mail", "search_count",
            [[["mailing_id", "=", mailing_id], ["state", "=", "outgoing"]]])
        print(f"\n📊 POST-RECUPERACIÓN:")
        print(f"   Enviados: {total_sent}")
        print(f"   Aún pendientes: {still_outgoing}")
        print(f"   Aún en exception: {still_failed}")
```

**⚠️ NUNCA reintentar sin verificar el acumulado diario primero.**
**⚠️ Si el error es `Daily email limit exceeded`, esperar mínimo hasta el día siguiente.**
**⚠️ Si el error es `5.4.5 Gmail sending limit`, el servidor Gmail NO debe usarse para masivos.**

### Programar envío

```python
call("mailing.mailing", "write", [[mailing_id], {
    "schedule_type": "scheduled",
    "schedule_date": "2026-04-15 14:00:00",  # UTC
}])
# Luego poner en cola
call("mailing.mailing", "action_launch", [[mailing_id]])
# NOTA: para envíos programados, el cron de Odoo se encarga del despacho.
# Si al ejecutarse quedan pendientes, aplicar el PASO 3 del flujo inmediato.
```

### Enviar prueba (test)

**Usar el wizard nativo `mailing.mailing.test`.** Renderiza con el motor real de Odoo, por lo que revela bugs de sintaxis (Qweb vs Jinja en `body_html`) que un envío manual con `mail.mail` no detectaría.

```python
# Crear wizard con la campaña y el email destino de la prueba
wid = call("mailing.mailing.test", "create", [{
    "mass_mailing_id": mailing_id,
    "email_to": "colesa.manuel@gmail.com",
}])

# Disparar el envío de prueba
call("mailing.mailing.test", "send_mail_test", [[wid]])

# Confirmación: aparece en el chatter del mailing como mail.message
# "El correo de prueba se envió con éxito a colesa.manuel@gmail.com"
```

**⚠️ Limitación conocida del wizard.** `send_mail_test` selecciona un `mailing.contact` pseudo-aleatorio (típicamente el primero del modelo destinatario) como `object` para el render — NO usa el `email_to` del wizard como datos. Si necesita probar el render contra un contact específico (por ejemplo, su propio registro con `name` humano), limite temporalmente `mailing_domain`:

```python
import json

# Guardar dominio original
orig = call("mailing.mailing", "read", [[mailing_id], ["mailing_domain"]])[0]["mailing_domain"]

# Limitar a un contact específico (ej: contact_id = 1730 = Manuel Rubio)
call("mailing.mailing", "write", [[mailing_id], {
    "mailing_domain": json.dumps([["id","=",1730]])
}])

# Crear wizard y enviar
wid = call("mailing.mailing.test", "create", [{
    "mass_mailing_id": mailing_id,
    "email_to": "colesa.manuel@gmail.com",
}])
call("mailing.mailing.test", "send_mail_test", [[wid]])

# Restaurar dominio original
call("mailing.mailing", "write", [[mailing_id], {"mailing_domain": orig}])
```

**Alternativa: enviar campaña real limitada a un contact** (verificación definitiva del render):

```python
import json

# Duplicar campaña con domain limitado a 1 contact + asunto identificable
test_id = call("mailing.mailing", "copy", [[mailing_id], {
    "subject": "[VERIFICACIÓN RENDER] " + subject,
    "mailing_domain": json.dumps([["id","=",1730]]),
    "mail_server_id": 11,
}])
if isinstance(test_id, list): test_id = test_id[0]
call("mailing.mailing", "action_launch", [[test_id]])
call("mailing.mailing", "action_send_mail", [[test_id]])
# trace_status="sent" en mailing.trace confirma entrega al SMTP
```

**⚠️ PRECAUCIÓN:** Siempre enviar prueba antes del envío masivo.
Pedir confirmación al usuario antes de `action_launch`.

### Cancelar envío en cola

```python
call("mailing.mailing", "action_cancel", [[mailing_id]])
```

## 5. Métricas y Reportes

### Consultar métricas de una campaña

```python
stats = call("mailing.mailing", "read", [[mailing_id],
    ["subject", "state", "sent", "delivered", "opened", "clicked",
     "replied", "bounced", "failed", "canceled",
     "opened_ratio", "clicks_ratio", "bounced_ratio",
     "received_ratio", "replied_ratio"]])
```

### Resumen de todas las campañas

```python
mailings = call("mailing.mailing", "search_read",
    [[["state", "=", "done"]]],
    {"fields": ["subject", "sent_date", "sent", "delivered",
                "opened", "opened_ratio", "clicked", "clicks_ratio",
                "bounced", "bounced_ratio"],
     "order": "sent_date desc",
     "limit": 20})
```

### Formato de salida de métricas

```
📊 Campaña: [SUBJECT]
Enviada: [FECHA]
──────────────────────────────────
Enviados:   XXX
Entregados: XXX (XX.X%)
Abiertos:   XXX (XX.X%)
Clicks:     XXX (XX.X%)
Respuestas: XXX (XX.X%)
Rebotados:  XXX (XX.X%)
──────────────────────────────────
```

### Consultar trazas individuales (quién abrió/clickeó)

```python
# En Odoo 18, el campo es trace_status (NO state)
# Valores: outgoing, sent, open, reply, bounce, error, cancel
traces = call("mailing.trace", "search_read",
    [[["mass_mailing_id", "=", mailing_id], ["trace_status", "=", "open"]]],
    {"fields": ["email", "trace_status", "sent_datetime",
                "open_datetime", "links_click_datetime", "failure_type"],
     "limit": 100})
```

### Distribución de trazas por estado

```python
groups = call("mailing.trace", "read_group",
    [[["mass_mailing_id", "=", mailing_id]]],
    {"fields": ["trace_status"], "groupby": ["trace_status"]})
for g in groups:
    print(f"  {g['trace_status']}: {g['trace_status_count']}")
```

## 6. Gestión de Listas

### Listar todas las listas

```python
lists = call("mailing.list", "search_read", [[]],
    {"fields": ["name", "contact_count", "is_public", "active"]})
```

### Contactos sin suscripción (opt-out) por lista

```python
opted_out = call("mailing.contact", "search_read",
    [[["list_ids", "in", [list_id]], ["opt_out", "=", True]]],
    {"fields": ["name", "email"], "limit": 100})
```

### Contactos rebotados

```python
bounced = call("mailing.contact", "search_read",
    [[["message_bounce", ">", 0]]],
    {"fields": ["name", "email", "message_bounce"], "limit": 100})
```

## 7. Flujo Recomendado

1. **Definir objetivo** — ¿Qué se quiere comunicar? ¿A quién?
2. **Cruce de servicios y productos** — OBLIGATORIO. Consultar `references/cole-services.md`
   y cruzar el tema de la campaña con los servicios y productos de Colé S.A. Presentar
   al Ing. Rubio una tabla como esta antes de diseñar el email:
   ```
   TEMA: [Tema de la campaña]
   ─────────────────────────────────────────────
   Servicios vinculables:
     ✅ [Servicio 1] — [por qué se vincula]
     ✅ [Servicio 2] — [por qué se vincula]
   Productos vinculables:
     ✅ [Producto/marca] — [por qué se vincula]
        🔗 URL web: [link encontrado en colecr.com]
        📌 Representante exclusivo para CR y la región
     ✅ [Producto/marca] — [por qué se vincula]
        🔗 URL web: [link encontrado en colecr.com]
        📌 Representante exclusivo para CR y la región
   ¿Incluye cursos?
     ✅/❌ [Si sí → link a página de cursos incluido automáticamente]
   CTAs sugeridos:
     🟢 WhatsApp: [mensaje pre-llenado contextualizado]
     ✉️ Email: [asunto contextualizado]
     🔗 Web: [URLs de productos vinculados]
     📚 Cursos: [si aplica]
   ─────────────────────────────────────────────
   → ¿Aprueba estos vínculos o quiere ajustar?
   ```
   **NUNCA diseñar el email sin esta aprobación previa.**
   **Las reglas de Presencia Digital (sección arriba) se aplican automáticamente
   sin necesidad de aprobación — son mandatorias.**
3. **Seleccionar lista existente** del catálogo aprobado (ID 2 Colé · ID 3 Kermatek · ID 16 maestra).
   NO crear lista nueva salvo aprobación explícita del Ing. Rubio.
4. **(Opcional) Incorporar contactos nuevos** a la lista 16 si el tema lo justifica.
   Reportar al Ing. Rubio cuántos contactos nuevos se agregaron y a cuál lista.
5. **Diseñar email** — HTML con branding Colé. Usar plantilla de `references/email-templates.md`.
   Integrar los servicios/productos aprobados en el paso 2.
   **OBLIGATORIO:** Incluir logo oficial full-width en encabezado (ver bloque
   `<!-- LOGO COLÉ S.A. -->` en templates).
   **OBLIGATORIO:** Pasar el Checklist Pre-Generación (sección Presencia Digital)
   antes de finalizar el HTML: representación exclusiva, links a productos,
   link a cursos (si aplica), redes sociales en footer y cuerpo.
6. **Crear campaña** en Odoo (`mailing.mailing` con `mailing_model_id: 591` y `contact_list_ids`)
   **NUNCA usar mailing_model_id: 87 (res.partner) — no funciona en Odoo 18 SaaS.**
7. **Enviar prueba** → wizard `mailing.mailing.test` (`send_mail_test`)
   (email_from SIEMPRE `m.rubio@colecr.com` — confirmar render en bandeja antes de masivo)
8. **Aprobación del Ing. Rubio** — Revisar prueba en bandeja de entrada
9. **Enviar masivo** → `action_launch` seguido de `action_send_mail`
10. **Monitorear métricas** — Verificar `trace_status` (outgoing→sent→open) y
    métricas de campaña (sent, delivered, opened, clicked, bounced)

**NUNCA enviar masivo sin prueba previa y aprobación.**

## Notas Técnicas

- **FLUJO OBLIGATORIO: mailing.list (591)** — Crear lista → importar contactos → campaña a lista.
  Los modelos res.partner (87) y crm.lead (666) generan trazas pero el cron SMTP de Odoo 18 SaaS
  no las despacha. El envío queda en `done` con 0 enviados. **NUNCA** usar estos modelos para masivos.
- **Deduplicar por email** al importar partners a mailing.contact — usar set() de emails en lowercase.
  Saltar emails sin '@' o vacíos. Reportar importados vs. saltados.
- **Secuencia de envío (3 pasos obligatorios):**
  1. `action_launch` → genera trazas y mail.mail en outgoing
  2. `action_send_mail` → despacha primer lote (~50), campaña pasa a done
  3. `mail.mail.send` en lotes de **20** con **10s de pausa** → fuerza envío controlado
  Sin el paso 3, campañas con >50 destinatarios quedan incompletas.
  El cron de Odoo 18 SaaS despacha ~50 por ciclo cada ~15 min, insuficiente.
- **⚠️ RATE LIMITING OBLIGATORIO (REGLA NUEVA):**
  - Lotes de **20 emails** (no 50) con **10 segundos** de pausa entre lotes
  - Máximo **400 emails por día** por servidor SMTP cPanel (margen seguro)
  - **SIEMPRE** verificar acumulado diario antes de lanzar nueva campaña
  - Si acumulado + nuevos > 400 → advertir y sugerir distribución multi-día
  - Gmail SMTP **NUNCA** usar para masivos (límite 500/día, fallo SPF frecuente)
- **⚠️ RECUPERACIÓN DE FALLOS (sección 4.1):**
  - Si hay `mail.mail` en `exception`, PRIMERO diagnosticar `failure_reason`
  - Si es `Daily limit exceeded` → esperar al día siguiente
  - Si es error de `email_from` → corregir a `m.rubio@colecr.com` y `mail_server_id: False`
  - Resetear `state: outgoing` y `mailing.trace.trace_status: outgoing`
  - Reenviar con el mismo throttling (lotes de 20, 10s pausa)
  - **NUNCA reintentar sin verificar acumulado diario**
- **⚠️ SERVIDOR SMTP — REGLA ABSOLUTA:**
  - `email_from` SIEMPRE `"Colé S.A." <m.rubio@colecr.com>`
  - `mail_server_id` SIEMPRE `False` (auto-select por dominio)
  - **NUNCA** usar SMTP Gmail (server_id: 6) para campañas masivas
  - Si se detecta `email_from` con `gmail.com`, corregir ANTES de enviar
- **body_arch y body_html** deben contener el mismo HTML
- **⚠️ ESTRUCTURA HTML OBLIGATORIA (body_arch):** NO usar el wrapper `o_layout`/`oe_structure`/`o_mail_no_options`
  de Odoo al escribir via API. El editor sanitiza ese markup y **elimina `<img>` tags y otros elementos**.
  Usar **HTML puro** con estructura `<div>` → `<table>` (mismo patrón de campaña ID 20).
  Estructura correcta del body_arch:
  ```html
  <div style="margin:0;padding:0;background-color:#f4f5f7;font-family:'Open Sans',Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f5f7;">
  <tr><td align="center" style="padding:20px 10px;">
  <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff;border-radius:8px;overflow:hidden;">
  <!-- LOGO --><tr><td style="padding:0;background-color:#ffffff;">
  <a href="https://colecr.com" target="_blank" style="display:block;">
  <img src="https://colecr.com/wp-content/uploads/2026/03/Logo-Doc1-scaled.png" alt="Cole S.A." width="600" style="display:block;width:100%;height:auto;border:0;">
  </a></td></tr>
  </table></td></tr></table></div>
  ```
  **Nunca** usar el wrapper que Odoo genera por defecto (`<div class="o_layout oe_unremovable...">`) —
  este wrapper activa el sanitizador del editor que elimina imágenes y elementos HTML válidos.
- **⚠️ NO USAR COMENTARIOS HTML en body_arch:** Odoo sanitiza los comentarios `<!-- ... -->` y puede
  descartar bloques completos de contenido asociados al guardar via API. Usar solo elementos HTML visibles.
  Si se necesita marcar secciones internamente, usar atributos `data-section="nombre"` en `<tr>` o `<td>`.
- **⚠️ ENVÍO DE PRUEBAS:** Usar el wizard nativo `mailing.mailing.test` (método `send_mail_test`).
  Verificado funcional en Odoo 18 SaaS de Colé el 2026-05-15. Ventaja sobre `mail.mail` directo:
  renderiza con el motor real (revela bugs Qweb vs Jinja en `body_html`). Limitación: usa un
  `mailing.contact` pseudo-aleatorio como `object` para el render — para forzar render contra
  un contact específico (ej. su propio registro), limite temporalmente `mailing_domain`. Ver
  sección "Enviar prueba (test)" para flujo completo.
- **Integración WordPress colecr.com:** Cuando una campaña tiene artículo asociado en el blog,
  incluir sección CTA con dos botones: "Leer artículo completo" (→ URL del post en colecr.com)
  y "Descargar PDF" (→ fuente original). Auth WordPress API: usuario `manuel`, Application Password.
  Publicar como `draft` para revisión del Ing. Rubio. ModSecurity bloquea uploads de archivos
  (PDF, imágenes) vía REST API — usar links externos para PDFs y archivos pesados.
- **schedule_date** en UTC (Costa Rica = UTC-6)
- **Adjuntos:** Usar `attachment_ids` con tupla `[(6, 0, [att_id])]`
- **A/B Testing:** `ab_testing_enabled: True`, crear 2+ mailings con mismo `campaign_id`
- **Monitoreo de trazas:** Usar `mailing.trace` con campo `trace_status` (outgoing, sent, open, error).
  El campo antiguo `state` no existe en Odoo 18. Agrupar con `read_group` por `trace_status`.
- **Logo:** URL de producción `https://colecr.com/wp-content/uploads/2026/03/Logo-Doc1-scaled.png`
  a ancho completo (width:100%, display:block, padding:0).
- **LinkedIn empresa:** `https://www.linkedin.com/company/104677153/` (slug con tilde NO funciona, usar solo ID numérico)
- **X (Twitter):** `https://x.com/colesacr`
- **Footer:** Tel y Cel en líneas separadas. Cel etiquetado como "Cel:" con link a WhatsApp.
  Web en línea independiente. Redes sociales obligatorias: Facebook, LinkedIn Empresa,
  LinkedIn Personal, X/Twitter (ver sección "Presencia Digital y Representación Comercial").
