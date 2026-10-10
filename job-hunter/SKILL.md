---
name: job-hunter
description: >
  Buscador y auditor de ofertas de empleo activas para candidatos del entorno de Colé S.A.
  Pipeline de 5 fases: carga del perfil desde assets/profiles/, barrido multi-fuente
  (Get on Board, HN Hiring, AgileEngine, Gorilla Logic, IceRock, LinkedIn, Indeed),
  verificación dura de cada oferta mediante fetch HTTP del HTML (NUNCA confiar en snippets),
  filtrado por elegibilidad geográfica, y reporte tabular con activas verificadas,
  descartadas auditadas y pools de talento. Estado persistente en state/seen.json evita
  re-reportes. Genera borrador de correo al candidato listo para revisar manualmente.
  Activar con: "tarea diaria de Eddy", "tarea diaria de [candidato]", "buscar empleo para
  [candidato]", "ofertas para [candidato]", "job hunt", "briefing de empleos", "qué ofertas
  hay para [candidato]", "ofertas Android", "ofertas Kotlin", o cualquier barrido del
  mercado laboral para un candidato. Activar incluso si la solicitud parece simple — la
  verificación oferta-por-oferta requiere disciplina activa.
---

# Job Hunter — Búsqueda y auditoría de ofertas activas

## Objetivo del skill

Reemplazar la búsqueda artesanal de empleo por un pipeline auditable que:

1. Devuelve solo ofertas que **fueron verificadas vivas hoy** mediante fetch directo del HTML.
2. Documenta explícitamente las ofertas descartadas (transparencia anti-falsos positivos).
3. Mantiene memoria entre ejecuciones para no re-enviar ofertas ya reportadas.
4. Genera un borrador de correo al candidato listo para enviar manualmente.

**Filosofía:** preferir 3 ofertas verificadas hoy a 30 ofertas que parecían reales en el buscador. Cada oferta no verificada es tiempo perdido del candidato.

---

## Herramientas requeridas

- **`web_search`** — descubrimiento de ofertas
- **`web_fetch`** — verificación HTTP del HTML de cada oferta candidata
- **`bash_tool`** — manipulación del estado persistente y empaquetado del reporte
- **Google Calendar MCP** (opcional) — solo para validar que el evento recurrente disparó la sesión

Si `web_fetch` no está disponible, **detener la ejecución y reportar el bloqueo**. Sin verificación HTTP no hay skill — la promesa central no se puede cumplir.

---

## Pipeline de 5 fases

### FASE 1 — Carga del perfil del candidato

**Paso 1.1: Identificar al candidato.**

Buscar el nombre del candidato en la frase trigger del usuario. Casos típicos:

- "tarea diaria de Eddy" → candidato = `eddy_fresno`
- "ofertas para [Nombre]" → buscar perfil correspondiente

**Paso 1.2: Cargar perfil.**

```bash
view /mnt/skills/user/job-hunter/assets/profiles/<candidato>.json
```

Si el perfil no existe en `assets/profiles/`, declararlo al usuario y ofrecer crearlo a partir del CV. No proceder sin perfil cargado.

El perfil contiene:
- `name`, `email`, `location`, `citizenship`, `work_authorization`
- `seniority`, `years_experience`
- `tech_stack` (lista priorizada)
- `eligibility_geographies` (países donde puede trabajar legalmente)
- `salary_expectation_usd_monthly` (rango)
- `availability` (fecha o "inmediato")
- `notes` (banderas críticas: estatus migratorio, sponsorship, etc.)

Ver `assets/profiles/eddy_fresno.json` como referencia.

**Paso 1.3: Cargar estado persistente.**

```bash
view /mnt/skills/user/job-hunter/state/seen.json
```

Si no existe, inicializarlo vacío. El archivo registra:
- `reported_urls` — ofertas ya incluidas en reportes previos
- `applied_urls` — ofertas a las que el candidato ya aplicó (marcadas por el usuario)
- `expired_urls` — ofertas verificadas como cerradas (auditoría)
- `last_run_iso` — timestamp del último briefing

---

### FASE 2 — Barrido multi-fuente

**Paso 2.1: Construir queries dirigidas al perfil.**

Usar `tech_stack` y `seniority` del perfil. Para Senior Android+KMM: queries tipo:
- `"Senior Android" Kotlin remote LATAM 2026`
- `"Kotlin Multiplatform" KMM remote 2026 hiring`
- `"Android developer" Costa Rica remote site:getonbrd.com`
- `Android Kotlin job site:linkedin.com Costa Rica`

**Paso 2.2: Fuentes prioritarias** (consultar en este orden, ver `references/sources-catalog.md`):

| Prioridad | Fuente | Razón |
|---|---|---|
| 1 | **Get on Board** (`getonbrd.com`) | LATAM/España, marca explícitamente status y "Last checked" |
| 2 | **HN Hiring** (`hnhiring.com`, `nchelluri.github.io/hnjobs`) | Mensual, empresas pagan visibilidad, alta señal |
| 3 | **Real Work From Anywhere** (`realworkfromanywhere.com`) | Marca claramente "Worldwide" sin restricción |
| 4 | **AgileEngine** (`join.agileengine.com/open-positions`) | Listings con timestamp `meta-article:modified_time` |
| 5 | **Gorilla Logic** (`jobs.lever.co/gorillalogic`) | Hub Costa Rica, Fortune 500 clientes |
| 6 | **LinkedIn CR** (`cr.linkedin.com/jobs/...`) | Volumen alto, requiere validación posterior |
| 7 | **Indeed CR/LATAM**, **Working Nomads**, **RemoteOK** | Catálogo crowd-sourced, mucho ruido |

**Paso 2.3: Recolectar candidatos.**

Capturar para cada candidato preliminar: `url`, `título`, `empresa`, `ubicación declarada`, `fecha aparente`. NO clasificar todavía. Lista bruta puede tener 15-30 entradas.

---

### FASE 3 — Verificación dura de status (regla central del skill)

**REGLA DURA #1:** Ninguna oferta entra al reporte sin pasar la verificación HTTP de Fase 3. Sin excepciones.

**Paso 3.1: Filtro previo de duplicados.**

Comparar URLs candidatas contra `state/seen.json`. Excluir las ya reportadas, ya aplicadas o ya verificadas como expiradas (a menos que hayan pasado >14 días desde la última verificación de expiración, en cuyo caso re-verificar por si re-abrieron).

**Paso 3.2: Fetch y análisis del HTML.**

Para cada URL candidata sobreviviente, ejecutar `web_fetch`. Buscar señales de cierre:

| Señal en HTML | Veredicto |
|---|---|
| "Closed job", "No longer accepting applications" | ❌ CERRADA |
| "Job Expired", "expired", "Apply before [fecha pasada]" | ❌ EXPIRADA |
| Redirect a listado general (URL final ≠ URL solicitada) | ❌ REMOVIDA |
| 403/404/410 | ⚠️ INACCESIBLE — si la fuente es Lever, Greenhouse o Ashby (que bloquean fetch automático), NO descartar; intentar verificación indirecta (búsqueda con query muy específica de los últimos 7 días) |
| Botón "Apply now" + fecha publicación reciente + sin marca de cierre | ✅ ACTIVA |

**Paso 3.3: Filtrado geográfico.**

Si el HTML declara países permitidos y la `location` del perfil no está incluida → ❌ NO ELEGIBLE. Documentar en auditoría.

**Paso 3.4: Match técnico.**

Comparar requisitos del HTML contra `tech_stack` del perfil. Calcular score:
- 🟢 Alto — todos los requisitos centrales presentes en stack del candidato
- 🟡 Medio — falta 1 requisito central; posible si se justifica en cover letter
- 🔴 Bajo — faltan 2+ requisitos centrales

**Paso 3.5: Persistir veredictos.**

Actualizar `state/seen.json`:
- Las ✅ ACTIVAS van a `reported_urls` (con timestamp y tier)
- Las ❌ CERRADAS van a `expired_urls` (con timestamp)

---

### FASE 4 — Búsqueda complementaria de pools de talento

**REGLA DURA #2:** Los pools de talento (staffing/EOR) NO entran en la sección de "ofertas activas". Son embudos paralelos. Reportarlos en sección separada al final.

Ver `references/talent-pools.md` para la lista canónica. Verificar que cada pool sigue activamente reclutando para el `tech_stack` del candidato (un fetch a su página de skills es suficiente).

---

### FASE 5 — Reporte y borrador de correo

**Paso 5.1: Generar reporte estructurado** con tres bloques claramente separados:

```markdown
# Briefing diario — [Nombre del candidato]
**Fecha:** [DD-MMM-YYYY]
**Ofertas verificadas hoy:** N activas / M descartadas / K pools

## 🟢 Ofertas activas verificadas (aplicar HOY)
| # | Empresa | Posición | Salario | Match | Link verificado |

## 🔴 Ofertas auditadas como NO ACTIVAS (transparencia)
| Empresa | Status | Razón |

## 🟡 Pools de talento permanentes
[Lista breve con link directo al portal de aplicación]

## ⚙️ Acciones recomendadas
1. [Acción más urgente con razón]
2. ...

## 📊 Confianza
🟢/🟡/🔴 + razón
```

**Paso 5.2: Borrador de correo al candidato.**

**REGLA DURA #3:** El correo se crea como borrador, NUNCA se envía automáticamente. El usuario debe revisar y enviar manualmente desde Gmail. Esto previene falsos positivos (un layout cambiado en una página de oferta puede romper la verificación; el usuario es el último filtro).

Componer borrador con:
- **Para:** `email` del perfil del candidato
- **De:** `colesa.manuel@gmail.com` (firma del usuario)
- **Asunto:** `Ofertas activas para tu perfil — [DD-MMM]`
- **Cuerpo:** Solo las ofertas 🟢 activas. Para cada una:
  - Empresa + posición + link verificado
  - Por qué encaja con el candidato (referencia a 1-2 elementos específicos del CV)
  - Advertencias relevantes (part-time, restricción geográfica, riesgo de pago, etc.)
  - 1-3 puntos de revisión del CV antes de aplicar (gaps técnicos detectados)
- **Cierre:** `Saludos,\nIng. Manuel Rubio, MSc`

Crear el borrador con `Gmail:create_draft` (si está disponible) o vía endpoint Apps Script de la skill `email-reply-composer` si el usuario lo prefiere. Si ningún método está disponible, presentar el cuerpo del correo en chat con instrucciones de copia manual.

**Paso 5.3: Guardar reporte en disco.**

```bash
mkdir -p /mnt/user-data/outputs/job-hunter-briefings
# Guardar el reporte como markdown con timestamp
```

Usar `present_files` para que el usuario pueda descargar el reporte completo si lo desea.

---

## Reglas duras

1. **Ninguna oferta entra al reporte sin verificación HTTP.** Snippet de buscador ≠ status. Si `web_fetch` no está disponible, detener el skill.
2. **No envío automático de correos.** Solo borradores. El usuario es la última línea de defensa contra falsos positivos.
3. **Estado persistente obligatorio.** Cada ejecución actualiza `seen.json`. Sin esto, todas las ejecuciones reportan las mismas ofertas.
4. **Auditoría visible.** Las ofertas descartadas se reportan junto con las activas. La transparencia es parte del producto.
5. **Filtro geográfico estricto.** Una oferta que excluye al candidato por país no se reporta como activa, ni siquiera con asterisco.
6. **Pools ≠ ofertas.** Los staffing/EOR van en sección separada.
7. **Match técnico declarado, no inferido.** El score 🟢/🟡/🔴 debe basarse en match explícito requisito-por-requisito, no en impresión general.
8. **Idioma de salida: español.** Salvo que el perfil del candidato indique preferencia distinta.
9. **Si re-aparece una oferta marcada como expirada hace >14 días**, re-verificar (las empresas re-abren posiciones con frecuencia).
10. **Cero alcance especulativo (Karpathy):** No agregar análisis de mercado, tendencias salariales, ni recomendaciones de carrera salvo que el usuario las pida explícitamente. Solo ofertas + auditoría + borrador.

---

## Frecuencia y trigger recurrente

El skill está diseñado para ejecutarse en frecuencia **lun/mié/vie** mediante un evento recurrente en el calendario "Cole S.A.". El evento contiene en su descripción la frase trigger exacta para activar el skill cuando el usuario lo abra.

Ver `references/calendar-setup.md` para configuración del evento.

---

## Comportamiento ante solicitudes derivadas

| El usuario pide | Acción |
|---|---|
| "marcá X como aplicada" | Mover URL de `reported_urls` a `applied_urls` en `seen.json`, confirmar |
| "descartá X" | Mover URL a `expired_urls`, confirmar |
| "agregá perfil de [persona] desde este CV" | Generar nuevo `assets/profiles/<persona>.json` desde el CV adjunto |
| "envía el correo a [candidato]" | Solo si el usuario lo pide explícitamente: enviar borrador previamente revisado |
| "agregá fuente [URL]" | Agregar a `references/sources-catalog.md` y notificar |
| "cambiá frecuencia a diaria/semanal" | Modificar evento de Calendar y este SKILL.md |

---

## Output esperado por ejecución

Una ejecución típica produce:

1. **En chat:** reporte estructurado de tres bloques (5-15 ofertas evaluadas → 1-5 reportadas).
2. **En Gmail:** borrador con las ofertas 🟢 activas, listo para revisar y enviar.
3. **En disco** (`/mnt/user-data/outputs/job-hunter-briefings/`): reporte completo en markdown con timestamp.
4. **En estado:** `state/seen.json` actualizado.

---

## Versión y mantenimiento

- **v1.0** — Skill creado el 06-Mayo-2026 a partir del flujo de búsqueda manual ejecutado para Eddy Yoel Fresno Hernández (Senior Android+KMM, Costa Rica).
- **Mantenedor:** Ing. Manuel Rubio, MSc.
- **Próxima revisión sugerida:** después de 4 ejecuciones reales, ajustar fuentes y queries según hit rate observado.
