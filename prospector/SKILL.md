---
name: prospector
description: "Buscador general de negocios locales en Google Maps vía Apify. Entrega un Excel (Leads / Resumen / Fuente y método) más CSV, con teléfono en E.164, link de WhatsApp clickeable y pipeline de estado. Sirve para cualquier nicho y cualquier zona: centros médicos con equipo de rayos X, clínicas dentales, veterinarias, empresas de ensayos no destructivos, inmobiliarias, hoteles, proveedores, o lo que el usuario pida. Acepta varios términos de búsqueda y varias zonas en una corrida, con deduplicación global. Usar cuando el usuario diga /prospector, pida prospectar, buscar clientes, scrapear negocios, armar lista de prospectos o base de leads. Requiere token Apify. No usa Airtable."
---

# Prospector

Google Maps (Apify) → normalización + dedupe global → **XLSX + CSV**.
Genérico: el nicho y la zona son parámetros, no supuestos.

Script en `scripts/prospector.py`. No lo copies al chat, ejecutalo desde ahí.

## 1. Protocolo de entrada — OBLIGATORIO

**Nunca corras el script con parámetros inventados.** Antes de gastar un centavo,
recolectá las cuatro variables. Si estás en una interfaz con `AskUserQuestion`,
preguntá con ese tool; si el usuario corre el script en su terminal, el propio script
pregunta lo que falte.

| # | Variable | Qué preguntar | Default si el usuario no opina |
|---|---|---|---|
| 1 | **Qué buscar** | Nicho o receta. Ofrecé las recetas de §2 como opciones | — (sin esto no hay corrida) |
| 2 | **Dónde** | Una o varias zonas. Sugerí incluir el país en el texto | — |
| 3 | **Alcance** | Tope por término y zona; mostrá el costo estimado | 200 |
| 4 | **Filtros** | Solo con teléfono · mínimo de reseñas · solo sin sitio web | solo con teléfono |

**Preguntá también cualquier duda de dominio que cambie el resultado.** Ejemplos reales:

- El usuario pide "centros médicos con equipos de RX" → Google Maps **no indexa
  capacidad instalada**. Decíselo y proponé el barrido por categorías (receta
  `rx-medico`) más una calificación posterior. No prometas un filtro que no existe.
- El usuario pide una provincia o un país entero → advertí que Google prioriza
  relevancia sobre exhaustividad y proponé varias zonas (`--zona A B C`), que ya
  deduplican entre sí.
- El nicho es patrimonial (inmuebles, hospedaje) → aplica identidad **neutral**, nunca
  marca Colé S.A.
- El usuario no dice el país → pedí el ISO2; sin él, los teléfonos nacionales no se
  pueden normalizar y quedan sin link de WhatsApp.

Cerrá el intake mostrando el plan y el costo, y esperá confirmación antes de correr.

## 2. Recetas

Paquetes de términos para casos frecuentes (`--receta <nombre>`, o
`--listar-recetas` para verlos con sus notas). Existen porque Google Maps indexa
**categorías**, no capacidades: un solo término deja fuera media población.

| Receta | Términos | Para qué |
|---|---|---|
| `rx-medico` | centro de radiología · centro de imágenes médicas · rayos x · clínica médica · hospital privado | Equipo e insumos de protección radiológica médica |
| `dental` | clínica dental · odontólogo · ortodoncista | RX dental, panorámico, CBCT |
| `veterinaria` | clínica veterinaria · veterinario · hospital veterinario | RX veterinario, EPP plomado |
| `industrial` | ensayos no destructivos · laboratorio de materiales · inspección industrial · soldadura industrial | Gammagrafía industrial |
| `inmobiliaria` | inmobiliaria · bienes raíces · corredor · administración de condominios | Patrimonial — identidad neutral |
| `hospedaje` | hotel · apartotel · hostal · cabinas | Patrimonial — identidad neutral |

Para cualquier otro caso, términos libres: `--buscar "término 1" "término 2"`.
Dos a cinco términos por corrida es el rango útil; más multiplica el costo sin agregar
cobertura, porque los resultados se solapan y el dedupe los descarta.

## 3. Ejecución

```bash
pip3 install requests openpyxl -q
export APIFY_TOKEN="..."

# Ensayo: muestra búsquedas, crédito y costo. No gasta.
python3 scripts/prospector.py --receta rx-medico \
  --zona "San José, Costa Rica" "Cartago, Costa Rica" \
  --country CR --max-results 50 --dry-run

# Corrida real
python3 scripts/prospector.py --receta rx-medico \
  --zona "San José, Costa Rica" "Cartago, Costa Rica" \
  --country CR --max-results 50 --solo-con-telefono --out-dir out

# Términos libres, cualquier rubro
python3 scripts/prospector.py --buscar "bufete de abogados" "notaría" \
  --zona "Heredia, Costa Rica" --country CR --max-results 100
```

Sin argumentos y con terminal, el script entra en **modo interactivo** y pregunta
receta/términos, zonas, país y tope.

Corré `--dry-run` siempre que el usuario no haya fijado `--max-results`. El script
consulta `/users/me/limits` y **aborta si el costo estimado excede el crédito del
ciclo** (`--ignorar-presupuesto` lo desactiva).

La guarda **sólo funciona si la cuenta declara `maxMonthlyUsageUsd`**. Si no lo
declara, el script imprime `[!] La cuenta no declara tope mensual` y corre sin
verificar. Ese aviso no es decorativo: es la única señal de que la protección de
presupuesto está inactiva.

Al terminar, el script lee el **costo real** (`usageTotalUsd`) de cada run y lo
compara contra la tarifa de referencia `USD_POR_LUGAR`. Un desvío mayor al 20% se
advierte en pantalla y en la hoja `Fuente y método`: significa que la tarifa del
actor cambió y hay que actualizar la constante.

**Costo = términos × zonas × `--max-results` × USD 0.0050.** Es multiplicativo: 5
términos × 3 zonas × 30 = 450 lugares ≈ USD 2.25. Mostrale siempre esa cuenta antes
de correr.

Después de generar el XLSX, si hay LibreOffice, recalculalo — openpyxl escribe
fórmulas sin valor en caché y la hoja `Resumen` se ve vacía hasta que Excel la abra:

```bash
python3 /mnt/skills/public/xlsx/scripts/recalc.py out/leads-*.xlsx
```

### Flags

| Flag | Efecto |
|---|---|
| `--buscar T1 T2 ...` (`--niche`) | Términos de búsqueda |
| `--zona Z1 Z2 ...` (`--zone`) | Zonas; una corrida de Apify por zona, dedupe global |
| `--receta NOMBRE` | Paquete de términos predefinido |
| `--listar-recetas` | Muestra las recetas y sale |
| `--country CR` | ISO2. Evita geocodificar y habilita normalización telefónica |
| `--max-results N` | Tope **por término y por zona** (default 200) |
| `--min-rating` / `--min-reviews` | Filtro local de calidad |
| `--solo-con-telefono` | Descarta lo que no genera link de WhatsApp |
| `--sin-web` | Solo negocios sin sitio web |
| `--incluir-cerrados` | Por defecto se omiten los cerrados |
| `--mensaje "..."` | Plantilla del WhatsApp; `{empresa}` se sustituye |
| `--formato xlsx\|csv\|ambos` | Default `ambos` |
| `--nombre` / `--out-dir` | Nombre base de archivos / carpeta |
| `--ignorar-presupuesto` | Salta la verificación de crédito |

## 4. Entregables

Tres archivos con prefijo `leads-<etiqueta>`:

| Archivo | Contenido |
|---|---|
| `.xlsx` | Libro de 3 hojas |
| `.csv` | Mismas 14 columnas, plano, UTF-8 con BOM |
| `_raw.json` | Respuesta íntegra de Apify. **Guardalo**: en plan FREE los datasets se borran a los 7 días |

**`Leads`** — 14 columnas, filtro automático, panel congelado, desplegable de pipeline
en `Estado`. `WhatsApp`, `Web` y `Google Maps` son hipervínculos con etiqueta corta
(*Escribir* / *Sitio* / *Ficha*). La columna `Zona buscada` dice de qué corrida vino
cada lead.

**`Resumen`** — conteos, rating promedio, mediana de reseñas, distribución del
pipeline y, si hubo varias zonas, desglose por zona. Todo por fórmula: se actualiza
solo al mover leads de estado.

**`Fuente y método`** — run IDs, términos, zonas, filtros, volumen, descartes, costo y
tres advertencias resaltadas (cobertura, calificación pendiente, cumplimiento). Es lo
que hace el archivo defendible ante auditoría; no la borres.

## 5. Reglas de calidad de datos

1. **Teléfono**: si viene con `+` o `00` se respeta; si viene nacional se le antepone el
   código de `--country`. Si el país es desconocido, el WhatsApp queda **vacío** en vez
   de generar un `wa.me/` roto.
2. **Dedupe global** por `placeId` y por teléfono normalizado — entre términos y entre
   zonas, no solo dentro de cada corrida.
3. **Filtro de país**: solo descarta leads que *declaran* otro país. Un lead sin
   `countryCode` se conserva; descartarlo es pérdida silenciosa de datos pagados.
4. `--min-rating` y `--min-reviews` se aplican **localmente**: el parámetro
   `placeMinimumStars` del actor espera un enum (`four`, `fourAndHalf`) y un valor
   numérico haría fallar el run.
5. Si una zona falla, se omite y las demás continúan. El script imprime el desglose de
   descartes; reproducilo al usuario tal cual.

## 6. Cumplimiento — leer antes de la primera corrida

No soy abogado; esto es señalamiento de riesgo, no asesoría legal.

- Scrapear Google Maps contraviene los Términos de Servicio de Google. Riesgo
  contractual (bloqueo, acción de Google), no penal, pero existe.
- Teléfonos de negocios unipersonales, autónomos y profesionales independientes son
  **datos personales**. En Costa Rica aplica la Ley 8968 y la PRODHAB; en la UE el RGPD
  (interés legítimo, con derecho de oposición y deber de informar en el primer contacto).
  El contacto en frío por WhatsApp sin base legal ni canal de baja es la exposición real.
- Mitigación mínima: identificar emisor y motivo en el primer mensaje, ofrecer baja
  explícita, conservar la trazabilidad (`Capturado` + `_raw.json`) y borrar a quien pida
  no ser contactado.
- Si se automatiza el envío, revisar además la WhatsApp Business Policy.

## 7. Relación con el servidor Apify MCP

Si la sesión tiene el servidor **Apify MCP** activo, existen dos rutas hacia Apify. No
son intercambiables: **el script ejecuta, el MCP diagnostica y califica.**

**El MCP se usa para:**

1. **Validar el actor antes de una campaña grande.** El script fija
   `ACTOR_ID = "nwua9Gu5YrADL7ZDj"` (`compass/crawler-google-places`). Si el proveedor
   cambia el input schema, el run falla con un 400 opaco. `fetch-actor-details` sobre
   ese ID confirma schema y tarifa vigentes antes de gastar.
2. **Calificar leads después de la corrida.** `apify--rag-web-browser` sobre el sitio
   web de cada lead cierra el hueco que este skill declara en §1: Google Maps no
   indexa capacidad instalada. Un centro médico que menciona "tomografía" o
   "densitometría" en su web es un prospecto calificado; la ficha de Maps no lo dice.
3. **Cortar una corrida desbocada** — `get-actor-run` / `abort-actor-run`, sin abrir
   apify.com.
4. **Evaluar alternativas** — `search-actors`, para fuentes que este script no cubre
   (directorios sectoriales, padrones, LinkedIn).

**Prohibido vía MCP:** descargar el dataset de una corrida de prospección con
`get-dataset-items`. Carga los leads en la ventana de contexto del modelo (cientos de
registros = decenas de miles de tokens) y no produce dedupe global, normalización
E.164, guarda de presupuesto ni hoja `Fuente y método`. Los leads van a disco por el
script, no al contexto.

**Advertencia de facturación:** el MCP inyecta el token de la sesión, que puede
pertenecer a una cuenta o plan distinto del token que usa el script. Si los costos no
cuadran, verificar primero que ambas rutas apunten a la misma cuenta.

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Apify 401 | Token inválido | Regenerar en apify.com |
| Aborta por presupuesto | Crédito del ciclo insuficiente | Bajar `--max-results`, quitar términos o zonas |
| Costo inesperadamente alto | Es multiplicativo | Recontar términos × zonas × tope |
| Una zona en `FAILED` | Término sin resultados en esa zona | Se omite sola; revisar apify.com/runs/`<id>` |
| 0 leads tras filtros | Umbrales altos | Bajarlos; el desglose de descartes dice cuál mordió |
| Hoja `Resumen` en blanco | Fórmulas sin valor en caché | Abrir en Excel o correr `recalc.py` |
| Muchos leads sin WhatsApp | Teléfonos nacionales sin `--country` | Repetir con `--country XX` |
| Resultados solo de la capital | Google prioriza relevancia | Agregar zonas: `--zona A B C` |
| `ModuleNotFoundError: openpyxl` | Falta la dependencia | `pip3 install openpyxl` o `--formato csv` |
