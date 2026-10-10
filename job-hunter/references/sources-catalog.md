# Catálogo de fuentes — Job Hunter

Fuentes ordenadas por calidad de verificación de status. Una fuente "buena" es la que **declara explícitamente cuándo una oferta está cerrada o expirada**. Una fuente "ruidosa" requiere verificación manual oferta por oferta.

---

## Tier 1 — Fuentes con verificación explícita de status

### Get on Board (`getonbrd.com`)
- **Cobertura:** LATAM + España, fuerte presencia en Chile/Colombia/México.
- **Status visible:** sí. Marca "Closed job - No longer accepting applications" cuando cierra. También muestra "Last checked today/yesterday".
- **Patrón URL:** `https://www.getonbrd.com/jobs/<categoria>/<slug>-remote`
- **Fetch:** funciona sin restricciones, HTML completo retornable.
- **Filtros útiles:** `mobile-developer` y `desarrollo-mobile` para Android/iOS.
- **Notas:** plataforma con mayor relación señal/ruido para LATAM. Empezar siempre por aquí.

### Real Work From Anywhere (`realworkfromanywhere.com`)
- **Cobertura:** Solo ofertas 100% worldwide, sin restricción geográfica.
- **Status visible:** sí. Marca "Job Expired" + fecha "Apply before".
- **Patrón URL:** `https://www.realworkfromanywhere.com/jobs/<slug>-<id>`
- **Notas:** muy útil para descartar rápido posiciones cerradas que aparecen en otros buscadores.

### HN Hiring (`hnhiring.com`, `nchelluri.github.io/hnjobs/`)
- **Cobertura:** Hilo mensual "Who is hiring?" de Hacker News.
- **Status visible:** parcial (la fecha del comentario indica ventana de hire).
- **Reglas:** solo considerar posts del mes actual o anterior. Más antiguos suelen estar cerrados aunque no lo declaren.
- **Notas:** alta señal — empresas pagan visibilidad implícita por el estatus del foro. Buscar tags como `[REMOTE]`, `[LATAM]`, `[WORLDWIDE]`.

---

## Tier 2 — Plataformas de empresa con timestamp

### AgileEngine (`join.agileengine.com/open-positions`)
- **Cobertura:** LATAM (AR, BR, CO, GT, MX) + USA + Europa + India.
- **Status visible:** los listings tienen `meta-article:modified_time` en el HTML.
- **Filtro crítico:** verificar la sección "Locations" en el HTML — Costa Rica frecuentemente NO está incluida.
- **Notas:** si Eddy aplica con un ID que no incluye CR, es no-match aunque el rol sea perfecto.

### Gorilla Logic (`gorillalogic.com/careers`, `jobs.lever.co/gorillalogic`)
- **Cobertura:** Costa Rica, Colombia, México, USA.
- **Status visible:** Lever bloquea fetch automático con 403, pero el listing en `gorillalogic.com/careers` sí se puede leer.
- **Estrategia:** ir directo a la página de careers, filtrar por Costa Rica, y revisar IDs de Lever. Si tras 7+ días siguen ahí, son reales.

### IceRock Development (`icerockdev.com/vacancies/`)
- **Cobertura:** Worldwide remote.
- **Status visible:** sí, listing completo con descripción de cada vacancy.
- **Especialización:** Kotlin Multiplatform (KMM) — match nicho extremadamente alto para perfiles KMM senior.
- **Riesgo:** empresa rusa. Auditar payment processing y restricciones de sanciones antes de invertir tiempo en proceso.

---

## Tier 3 — Volumen alto, ruido alto

### LinkedIn Costa Rica (`cr.linkedin.com/jobs/...`)
- **Cobertura:** Costa Rica + remoto.
- **Status visible:** parcial. Las ofertas pueden permanecer visibles después de cerradas.
- **Limitación:** `web_fetch` retorna `ROBOTS_DISALLOWED` para LinkedIn.
- **Estrategia:** usar `web_search` con `site:linkedin.com` para descubrir, luego validar contra sitio de empresa cuando sea posible.

### Indeed Costa Rica/LATAM (`indeed.com`)
- **Cobertura:** Volumen alto, mucho repost de otras plataformas.
- **Notas:** verificar siempre fuente original — Indeed es agregador.

### Working Nomads (`workingnomads.com/remote-kotlin-jobs`)
- **Cobertura:** Catálogo crowd-sourced.
- **Status visible:** no consistente. Verificar cada oferta individualmente.

### RemoteOK (`remoteok.com`)
- **Cobertura:** Catálogo crowd-sourced.
- **Notas:** el listado a veces incluye perfiles de candidatos confundidos con vacancies. Filtrar.

### Glassdoor Costa Rica (`glassdoor.com/Job/costa-rica-...`)
- **Cobertura:** Mediano.
- **Notas:** los listings que ya cerraron permanecen indexados. Verificar siempre con fetch.

---

## Tier 4 — Pools de talento (NO son ofertas; son embudos)

Los siguientes NO se reportan como "ofertas activas" en el briefing. Van en sección separada.

| Empresa | URL | Modelo | Rango Senior LATAM |
|---|---|---|---|
| Gorilla Logic | gorillalogic.com/careers | Hub Costa Rica + nearshore | Variable por proyecto |
| BairesDev | bairesdev.com | LATAM 27 países, 3500 empleados | $50K-$80K USD/año |
| Tecla | tecla.io | EOR Costa Rica, vetting estricto | $60K-$90K USD/año |
| Mismo | mismo.team | Entidad legal en Costa Rica + clientes US | $58K-$80K USD/año |
| Revelo | revelo.com | Vetting riguroso, mayor con clientes US | $6,800/mes |
| Hireinsouth (South) | hireinsouth.com | LATAM, KMM senior tier | $44K-$68K USD/año |
| AgileEngine | join.agileengine.com | LATAM + Europe + India | Variable |
| Turing | turing.com | Vetting global automatizado | Variable |
| Lemon.io | lemon.io | Freelance/contract LATAM | Variable |
| Toptal | toptal.com | Freelance senior global | Variable |
| Lupa | lupahire.com | LATAM, vetting humano | Variable |

---

## Queries canónicas por tech stack

### Senior Android + Kotlin + KMM (perfil de Eddy)
- `"Senior Android" Kotlin remote LATAM 2026`
- `"Kotlin Multiplatform" KMM remote 2026 hiring`
- `"Compose Multiplatform" developer remote 2026`
- `"Android developer" Costa Rica site:getonbrd.com`
- `KMM Android job remote 2026`

### Variantes para escapar de spam SEO
- Agregar términos específicos del stack: `Jetpack Compose`, `Coroutines`, `Hilt`
- Filtrar por dominios con `site:`: `getonbrd.com`, `realworkfromanywhere.com`, `linkedin.com`
- Excluir `agency`, `staffing`, `recruiting` cuando se buscan ofertas directas (si el query lo permite sin operadores prohibidos)

---

## Banderas rojas en HTML que confirman cierre

Estas señales son veredicto inmediato:

| Señal | Veredicto |
|---|---|
| `Closed job` (Get on Board) | ❌ CERRADA |
| `No longer accepting applications` | ❌ CERRADA |
| `This job posting has expired` | ❌ EXPIRADA |
| `Apply before [fecha pasada]` | ❌ EXPIRADA |
| Redirect 302 a `/jobs/` o `/applications/` general | ❌ REMOVIDA |
| `404 Not Found` o `410 Gone` | ❌ REMOVIDA |
| HTTP 403 + dominio Lever/Greenhouse/Ashby | ⚠️ NO concluyente; verificar por canal alternativo |
