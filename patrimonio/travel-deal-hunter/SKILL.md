---
name: travel-deal-hunter
description: >-
  Buscador de ofertas de viaje y ocio: hoteles, vuelos, paquetes, day pass, restaurantes, eventos,
  actividades, autos, tarifas opacas, upgrades, status match. Barrido completo por ventana de tiempo
  con precios verificados. Activar con: ofertas hotel, vuelo barato, day pass, pase de dia, happy
  hour, kids eat free, 2x1, eventos, conciertos, que hacer, planes fin de semana, actividades
  familia, escapada, staycation, Marriott, Hilton, Aloft, Hyatt, IHG, Booking, Expedia, error fare,
  flash sale, millas, puntos, Bonvoy, tarifa opaca, Hotwire, upgrade, status match, rent a car,
  Autoslash, Viator, GetYourGuide, Klook, Civitatis, tours, busca ofertas, mejor precio, quiero
  viajar, comparar hoteles, comparar vuelos, Groupon, Fever, ResortPass, DayPassCR. Activar incluso
  si la solicitud parece simple.
---

# Travel Deal Hunter

## Propósito
Buscar, comparar y presentar ofertas de ocio y viaje (hoteles, vuelos, paquetes, day pass, restaurantes, entretenimiento, actividades y más) mediante web search exhaustivo. El skill opera en dos modos:
1. **Modo específico (Tipos A–N, O, P):** Búsqueda enfocada en una categoría.
2. **Modo Briefing Integral (Tipo Ω):** Barrido completo de TODAS las categorías para una ventana de tiempo dada, entregando un reporte consolidado de todo lo disponible para pasarla bien.

## Referencia Obligatoria
Antes de ejecutar cualquier búsqueda, leer:
- `references/sources.md` — Catálogo completo de fuentes, plataformas y estrategias de búsqueda por tipo de consulta.

---

## Flujo de Trabajo

### PASO 1 — Captura de Intención
Clasificar la consulta del usuario en uno de estos tipos:

| Tipo | Descripción | Dato mínimo requerido |
|---|---|---|
| **A. Precio específico** | "¿Cuánto cuesta hotel/vuelo a X en fechas Y?" | Destino + fechas (o mes) |
| **B. Flash / Promo activa** | "¿Hay ofertas ahora?" | Cadena/aerolínea o destino (opcional) |
| **C. Exploración** | "Quiero vacaciones baratas en [región/época]" | Región o presupuesto |
| **D. Mejor momento** | "¿Cuándo es más barato ir a X?" | Destino |
| **E. Comparación** | "Compara hoteles/vuelos para X" | Destino + criterios |
| **F. Day Pass / Daycation** | "Busca day pass / pase de día / acceso a piscina de hotel" | Zona geográfica + fecha (o "hoy/este fin de semana") |
| **G. Tarifa Opaca / Secreta** | "Quiero hotel barato sin importar cuál" | Destino + fechas + presupuesto máximo |
| **H. Upgrade** | "¿Puedo conseguir upgrade barato?" | Reserva existente o cadena/aerolínea + ruta |
| **I. Status Match / Challenge** | "Quiero igualar mi estatus élite" | Programa actual + nivel + programa destino |
| **J. Tarjetas de Crédito Viajero** | "¿Qué tarjeta me conviene para viajes?" | País de residencia + patrones de gasto |
| **K. Paquete Staycation** | "Escapada romántica / staycation con cena" | Zona + tipo (pareja/familia) + presupuesto |
| **L. Estancia Extendida** | "Hotel por semana/mes barato" | Destino + duración + presupuesto |
| **M. Actividades / Experiencias** | "Tours / qué hacer en [destino]" | Destino + fechas + intereses |
| **N. Alquiler de Autos** | "Rent a car barato en [destino]" | Destino + fechas + tipo vehículo |
| **O. Restaurantes / Gastronomía** | "Ofertas de restaurante / dónde comer barato / happy hour" | Zona + fecha + tipo (familiar, pareja, casual) |
| **P. Entretenimiento / Eventos** | "Qué hacer / conciertos / eventos / planes familiares" | Zona + fechas + perfil (familia, pareja, solo) |
| **Ω. BRIEFING INTEGRAL** | "Qué hay este finde / corre el skill / ofertas para [ventana]" | Ventana de tiempo + zona (default: GAM/CR) + perfil |

**Detección automática de Tipo Ω:** Cuando el usuario da una ventana de tiempo sin especificar categoría ("este fin de semana", "próxima semana", "mayo 2026"), o pide "todas las ofertas", "qué hay disponible", "planes para pasarla bien", activar Tipo Ω automáticamente.

Si faltan datos mínimos, solicitar antes de buscar. Preguntar:
- Fechas o flexibilidad de fechas
- Origen del vuelo (default: SJO — San José, Costa Rica)
- Número de personas / habitaciones
- Presupuesto aproximado (opcional pero útil para filtrar)
- Preferencias de cadena/aerolínea/clase

### PASO 2 — Ejecución de Búsqueda

Ejecutar **mínimo 4 búsquedas web** (más si la consulta es compleja). La estrategia depende del tipo:

#### Tipo A — Precio Específico
```
Búsqueda 1: "[destino] hotel deals [mes] [año]"
Búsqueda 2: "[destino] hotel [cadena preferida] rate [fechas]"  
Búsqueda 3: "flights [origen] to [destino] [mes] [año] cheap"
Búsqueda 4: "[destino] vacation package [mes] [año]"
Búsqueda 5: "[cadena] [destino] promotion [año]" (si aplica)
```

#### Tipo B — Flash / Promo Activa
```
Búsqueda 1: "[cadena/aerolínea] deals [mes actual] [año]"
Búsqueda 2: "hotel flash sale [hoy/esta semana] [año]"
Búsqueda 3: "cheap flights deals [mes] [año]"
Búsqueda 4: "travel deals this week [año]"
Búsqueda 5: "[cadena] points promotion [año]"
```

#### Tipo C — Exploración
```
Búsqueda 1: "cheapest destinations from [origen] [época]"
Búsqueda 2: "best travel deals [región] [mes] [año]"
Búsqueda 3: "budget vacation [región] [año]"
Búsqueda 4: "all inclusive deals [región] [mes] [año]"
Búsqueda 5: "flight deals [origen] [región]"
```

#### Tipo D — Mejor Momento
```
Búsqueda 1: "cheapest time to visit [destino]"
Búsqueda 2: "flight price calendar [origen] [destino] [año]"
Búsqueda 3: "[destino] low season months"
Búsqueda 4: "[destino] hotel cheapest month [año]"
```

#### Tipo E — Comparación
```
Búsqueda 1: "[hotel A] vs [hotel B] [destino] price"
Búsqueda 2: "[destino] best hotel deals [fechas]"
Búsqueda 3: "compare [aerolíneas] [ruta] price"
Búsqueda 4: "[destino] hotel reviews comparison [año]"
```

#### Tipo F — Day Pass / Daycation
Acceso a amenidades de hotel (piscina, spa, gym, habitación de día) sin hospedarse.
```
Búsqueda 1: "day pass hotel [zona/ciudad] piscina [año]"
Búsqueda 2: "pase de día hotel [zona/ciudad] precio"
Búsqueda 3: "resortpass [ciudad/país]"
Búsqueda 4: "daypasscr [zona]" (si Costa Rica)
Búsqueda 5: "[hotel específico] day pass rate"
```
**Fuentes prioritarias para Day Pass:**
1. **ResortPass** (resortpass.com) — mayor inventario global de day passes
2. **DayPassCR** (daypasscr.com) — plataforma local Costa Rica
3. **WorldDayPass** (worlddaypass.com) — cobertura internacional
4. **DayPass.com** (daypass.com) — inventario complementario
5. **Sitios directos de hoteles** — muchos venden day pass solo llamando o en su web
6. **Prensa local** — artículos tipo "day pass hoteles [ciudad]" con tablas comparativas

**Datos a recolectar para cada Day Pass:**
- Precio por persona (adulto/niño) + impuestos
- Qué incluye: piscina, habitación, gym, spa, comidas
- Horario de acceso (check-in / check-out del day pass)
- Restricciones: mascotas, alimentos externos, disponibilidad
- Si requiere reserva anticipada o acepta walk-in

#### Tipo G — Tarifa Opaca / Secreta
Hoteles a precio reducido (30-60% off) donde la identidad se revela después del pago.
```
Búsqueda 1: "hotwire hot rate [destino] [fechas]"
Búsqueda 2: "priceline express deals [destino]"
Búsqueda 3: "hotwire hotel reveal [destino] [star rating]" (foros que decodifican)
Búsqueda 4: "bidding traveler [destino]" (comunidad de decodificación)
```
**Fuentes:** Hotwire (hotwire.com), Priceline Express Deals, BiddingTraveler.com, BetterBidding.com.
**Advertencia obligatoria:** Reservas NO reembolsables. Señalar siempre este riesgo.

#### Tipo H — Upgrade Barato
Subastas o ofertas de upgrade a clase superior (vuelo o habitación) por fracción del precio regular.
```
Búsqueda 1: "[aerolínea] bid upgrade [ruta] [año]"
Búsqueda 2: "Plusgrade [aerolínea] bid [clase]"
Búsqueda 3: "[cadena hotelera] pre-arrival upgrade offer"
Búsqueda 4: "[aerolínea] upgrade auction tips [año]"
```
**Fuentes:** Plusgrade (aerolíneas), emails pre-arrival de Marriott/Hilton/IHG, app de la aerolínea (sección upgrade).
**Dato clave:** Buscar rangos de bid ganadores reportados por viajeros en foros (FlyerTalk, One Mile at a Time).

#### Tipo I — Status Match / Challenge
Igualar nivel élite de un programa de lealtad en otro competidor.
```
Búsqueda 1: "[programa origen] to [programa destino] status match [año]"
Búsqueda 2: "status match hotel [año] current offers"
Búsqueda 3: "[cadena] status challenge requirements [año]"
Búsqueda 4: "statusmatcher.com" (base de datos de matches activos)
```
**Fuentes:** StatusMatcher.com, FlyerTalk Status Match forums, páginas oficiales de programas.
**Dato clave:** Indicar requisitos (prueba de estatus, estancias mínimas en challenge, ventana de tiempo).

#### Tipo J — Tarjetas de Crédito para Viajero
Tarjetas con beneficios de viaje: companion tickets, créditos, lounges, seguros.
```
Búsqueda 1: "best travel credit cards [país residencia] [año]"
Búsqueda 2: "credit card companion ticket [aerolínea] [año]"
Búsqueda 3: "credit card travel credits [año] comparison"
Búsqueda 4: "[tarjeta específica] travel benefits review [año]"
```
**Fuentes:** The Points Guy, NerdWallet, Doctor of Credit, Upgraded Points.
**Restricción:** No recomendar tarjeta específica como asesoría financiera. Presentar opciones con pros/contras para que el usuario decida.

#### Tipo K — Paquete Staycation
Diferente al day pass: incluye NOCHE + cena + desayuno + experiencia empaquetada.
```
Búsqueda 1: "[hotel/zona] staycation package [año]"
Búsqueda 2: "[ciudad] romantic getaway hotel deal"
Búsqueda 3: "[cadena] staycation promotion [país/ciudad]"
Búsqueda 4: "[ciudad] hotel package dinner spa [año]"
```
**Comparar:** Precio del paquete vs componentes por separado (noche + restaurante + spa). Calcular ahorro real.

#### Tipo L — Estancia Extendida / Long-Stay
Descuentos por semana (10-20%) o mes (30-50%) vs tarifa diaria.
```
Búsqueda 1: "[destino] extended stay hotel weekly rate"
Búsqueda 2: "[destino] monthly hotel rate [año]"
Búsqueda 3: "[destino] apart-hotel long stay deals"
Búsqueda 4: "sonder OR selina OR anyplace [destino] monthly"
```
**Fuentes:** Booking.com (filtro estancias largas), Sonder, Selina, Anyplace, Marriott Homes & Villas, Airbnb (descuento mensual).
**Dato clave:** Incluir comparación tarifa diaria × días vs tarifa paquete semanal/mensual.

#### Tipo M — Actividades y Experiencias
Tours, excursiones, entradas a atracciones con descuento.
```
Búsqueda 1: "best tours [destino] deals [año]"
Búsqueda 2: "viator [destino] top rated"
Búsqueda 3: "getyourguide [destino] discount"
Búsqueda 4: "klook OR civitatis [destino] promo"
```
**Fuentes:** Viator, GetYourGuide, Klook, Civitatis, Airbnb Experiences, Tiqets.
**Priorizar:** Ofertas con cancelación gratuita y mejores reviews.

#### Tipo N — Alquiler de Autos
Tarifas de rental car optimizadas.
```
Búsqueda 1: "cheap car rental [destino] [fechas] [año]"
Búsqueda 2: "autoslash [destino]"
Búsqueda 3: "rental car deals [destino] [mes] [año]"
Búsqueda 4: "[empresa] promo code [destino] [año]"
```
**Fuentes:** Autoslash (renegociación automática), Kayak Cars, Discover Cars, RentalCars.com, Costco Travel.
**Dato clave:** Incluir cobertura de seguro (CDW/LDW), política de combustible, cargos por conductor joven/adicional.

#### Tipo O — Restaurantes / Gastronomía
Ofertas, promos y experiencias gastronómicas.
```
Búsqueda 1: "restaurant deals [zona/ciudad] [mes] [año]"
Búsqueda 2: "happy hour [zona/ciudad] best [año]"
Búsqueda 3: "kids eat free [ciudad] [día de la semana]"
Búsqueda 4: "groupon OR fever restaurants [ciudad]"
Búsqueda 5: "[ciudad] brunch deals OR prix fixe OR 2x1"
```
**Fuentes:** Groupon, Fever, TheFork/ElTenedor, OpenTable (promos), Google Maps (ofertas locales), redes sociales del restaurante, apps de delivery (promos primer pedido).
**Datos a recolectar:** Nombre, ubicación, tipo de promo (2x1, happy hour, kids free, menú especial), horario, restricciones, si requiere reserva.
**Filtro familia:** Priorizar restaurantes con menú infantil, áreas de juego, o promos "niños comen gratis".

#### Tipo P — Entretenimiento / Eventos
Conciertos, festivales, teatro, cine, ferias, parques, actividades familiares.
```
Búsqueda 1: "eventos [ciudad] [fecha/mes] [año]"
Búsqueda 2: "qué hacer [ciudad] este fin de semana [fecha]"
Búsqueda 3: "conciertos OR teatro OR festivales [ciudad] [mes] [año]"
Búsqueda 4: "actividades familiares [ciudad] [mes] [año]"
Búsqueda 5: "fever OR eventbrite [ciudad] [mes]"
```
**Fuentes:** Fever, Eventbrite, Facebook Events, Google Events, prensa local (agenda cultural), Tiqets (atracciones), páginas de municipalidades/centros culturales.
**Filtro familia:** Clasificar por apto para niños (sí/no), rango de edad, si es al aire libre, si incluye comida.

#### Tipo Ω — BRIEFING INTEGRAL DE OCIO
Modo maestro. Ejecuta barrido de TODAS las categorías relevantes para una ventana de tiempo.

**Activación:** Cuando el usuario da ventana de tiempo sin categoría específica.

**Flujo obligatorio:**
1. Confirmar ventana de tiempo y zona (default: GAM, Costa Rica)
2. Confirmar perfil: familia / pareja / individual / grupo de amigos
3. Ejecutar búsquedas en paralelo para CADA sección del briefing
4. Presentar reporte consolidado en el formato de salida definido abajo

**Búsquedas mínimas (10-15 web searches):**
```
Vuelos:    "cheap flights from SJO [ventana] [año]"
           "flight deals Costa Rica [mes] [año]"
Hoteles:   "hotel deals [zona] [ventana] [año]"
           "[cadena] promotion [zona] [año]"
Day Pass:  "day pass hotel [zona] [ventana]"
           "resortpass [zona]" / "daypasscr"
Restaur:   "restaurant deals [zona] [ventana]"
           "happy hour OR kids eat free [zona] [día]"
Eventos:   "eventos [zona] [fecha exacta]"
           "qué hacer [zona] este fin de semana"
           "actividades familiares [zona] [fecha]"
Activid:   "tours [zona] deals" / "viator [zona]"
Autos:     "rental car [zona] [ventana] deal" (solo si viaje fuera del GAM)
Promos:    "[cadena hotelera] current promotion [año]"
```

**Formato de salida obligatorio del Briefing Integral:**

```markdown
# 🎯 Briefing de Ocio — [Ventana de Tiempo]
**Perfil:** [Familia/Pareja/Individual] | **Zona:** [GAM/destino]

## ✈️ VUELOS desde SJO
| Destino | Aerolínea | Tarifa R/T | Fechas | Fuente |
(Top 5-8 deals verificados)

## 🏨 HOTELES — Ofertas y Promos
| Hotel | Zona | Precio/noche | Promo activa | Fuente |
(Top 5-8, incluir promos de lealtad vigentes)

## 🏊 DAY PASS
| Hotel | Zona | Precio | Incluye | Horario |
(Top 3-5 opciones)

## 🍽️ RESTAURANTES — Deals Activos
| Restaurante | Zona | Oferta | Tipo | Horario/Día |
(Top 5-8: happy hours, kids eat free, 2x1, prix fixe, brunch)

## 🎭 EVENTOS Y ENTRETENIMIENTO
| Evento | Lugar | Fecha | Precio | Apto familia |
(Todo lo que esté pasando en la ventana de tiempo)

## 🎢 ACTIVIDADES Y EXPERIENCIAS
| Actividad | Proveedor | Precio | Rating | Cancelación |
(Top 5: tours, parques, experiencias)

## 🚗 ALQUILER DE AUTOS (si aplica)
| Empresa | Tipo | Tarifa/día | Incluye | Fuente |

## 💡 RECOMENDACIÓN TOP
**Para este [ventana]:**
1. Mejor plan familiar: [descripción + presupuesto estimado total]
2. Mejor plan pareja: [descripción + presupuesto estimado total]  
3. Mejor deal absoluto: [la oferta que no se puede dejar pasar]
```

**Regla de profundidad:** Si los primeros resultados son insuficientes o genéricos, usar `web_fetch` en las URLs más prometedoras para extraer tarifas reales. Priorizar:
1. Páginas de ofertas directas de cadenas hoteleras
2. Resultados de metabuscadores con precios visibles
3. Artículos de agregadores de deals (TPG, Secret Flying, etc.)
4. Blogs de viaje con datos de precios recientes

### PASO 3 — Síntesis y Presentación

Presentar resultados en formato estructurado. Siempre incluir:

#### 3.1 Tabla Comparativa de Precios
Para cada opción encontrada:

| Hotel / Vuelo | Fuente | Precio | Condiciones | Ventaja |
|---|---|---|---|---|
| Nombre del alojamiento/vuelo | Plataforma donde se encontró | USD/noche o total | Cancelación, fechas blackout, etc. | Por qué destaca |

#### 3.2 Resumen de Ofertas Detectadas
- **Mejor precio absoluto:** [opción] a [precio] vía [plataforma]
- **Mejor relación calidad-precio:** [opción] — justificación
- **Mejor promo activa:** [descripción] — vigencia, condiciones
- **Paquete más conveniente:** [si aplica] — ahorro vs componentes separados

#### 3.3 Alertas y Advertencias
Señalar explícitamente:
- ⚠️ Precios que parecen error fares (pueden cancelarse)
- ⚠️ Tarifas no reembolsables o con restricciones severas
- ⚠️ Ofertas próximas a expirar
- ⚠️ Diferencias significativas entre precio mostrado y precio final (impuestos, resort fees)
- ⚠️ Temporada alta / eventos que inflaron precios

#### 3.4 Recomendación Accionable
Cerrar con:
1. **Acción recomendada** — Qué reservar, dónde, cuándo
2. **Links directos** — URLs de las mejores ofertas encontradas
3. **Timing** — Si conviene esperar o reservar ya (basado en tendencia de precios)
4. **Alternativa** — Segunda opción si la primera no convence

---

## Reglas Operativas

### Búsqueda
- **Mínimo 4 web searches por consulta.** Consultas complejas pueden requerir 8-12.
- **Siempre buscar en inglés Y español** cuando el destino es hispanohablante.
- **Incluir año actual** en queries para evitar resultados obsoletos.
- **Usar web_fetch** en páginas de ofertas de cadenas hoteleras para obtener tarifas reales.
- **No inventar precios.** Si no se encuentra tarifa verificable, indicar "precio no confirmado, verificar en [URL]".

### Presentación
- **Moneda:** USD como base. Si el usuario pide otra, convertir al tipo de cambio del día (buscar si es necesario).
- **Siempre incluir impuestos y fees** si están disponibles, o advertir que el precio no los incluye.
- **Formato tabular** para comparaciones. Prosa solo para análisis y recomendación.
- **Links clickeables** a las ofertas cuando se encuentran URLs directas.

### Honestidad
- Si una búsqueda no arroja resultados útiles, decirlo. No rellenar con generalidades.
- Distinguir entre **precio verificado** (encontrado en fuente específica) y **rango estimado** (basado en históricos o promedios).
- Advertir si los resultados de búsqueda parecen desactualizados.

### Contexto del Usuario
- **Origen default:** SJO (Aeropuerto Juan Santamaría, Costa Rica), salvo que se indique otro.
- **Perfil:** Viajero experimentado. No necesita explicaciones básicas sobre booking, check-in, etc.
- **Interés en loyalty:** Considerar Marriott Bonvoy, Hilton Honors, IHG Rewards cuando sean relevantes.

---

## Casos Especiales

### Búsqueda de Day Pass / Daycation
Cuando la consulta es Tipo F:
1. Buscar en las plataformas especializadas (ResortPass, DayPassCR, WorldDayPass) Y directamente en hoteles de la zona
2. Buscar artículos de prensa local comparativos ("day pass hoteles [ciudad] precios")
3. Usar `web_fetch` en ResortPass para la zona específica

**Tabla de presentación obligatoria:**

| Hotel | Zona | Precio | Incluye | Horario | Reserva vía |
|---|---|---|---|---|---|
| Nombre | Ubicación | USD + IVA | Piscina/Hab/Gym/Comida | HH:MM–HH:MM | Plataforma o directo |

**Resumen obligatorio:**
- **Mejor precio absoluto:** [hotel] a [precio]
- **Mejor relación calidad-precio (pareja):** [hotel] — justificación
- **Mejor para familia:** [hotel] — justificación
- **Mejor experiencia premium:** [hotel] — justificación

**Comparación Day Pass vs Noche completa:** Cuando el day pass supere el 60% del precio de una noche con desayuno incluido, señalar que hospedarse puede ser más conveniente.

### Búsqueda de All-Inclusive
Agregar búsquedas específicas:
```
"[destino] all inclusive resort deals [mes] [año]"
"[destino] all inclusive adults only [año]"
"apple vacations [destino] [mes]"
"costco travel [destino] all inclusive"
```

### Error Fares / Mistake Fares
Si se detectan:
- Confirmar en al menos 2 fuentes (Secret Flying + otra)
- Advertir que pueden cancelarse
- Recomendar reservar con tarjeta que permita reembolso fácil
- Sugerir no hacer reservas no reembolsables complementarias hasta confirmar

### Búsqueda con Puntos/Millas
Agregar:
```
"[cadena] points redemption [destino] value"
"best use [programa] points [destino]"
"award flights [ruta] availability"
```
Calcular cents-per-point (cpp) cuando sea posible para evaluar si el canje vale la pena.

### Tarifas Opacas — Decodificación
Cuando el usuario quiere usar Hotwire/Priceline Express:
1. Buscar en BetterBidding.com o BiddingTraveler.com reportes recientes del destino
2. Cruzar zona + estrellas + amenidades para identificar probable hotel
3. Comparar tarifa opaca vs tarifa pública del hotel identificado
4. **Siempre advertir:** reserva no reembolsable, no cancelable, hotel no garantizado

### Status Match — Validación
Antes de recomendar un status match:
1. Verificar que la oferta esté **vigente** (muchas expiran sin aviso)
2. Confirmar requisitos: prueba fotográfica de tarjeta/estatus, estancias mínimas en challenge period
3. Evaluar si el challenge es completable dado el patrón de viaje del usuario
4. Alertar sobre matches encadenados (A→B→C) — algunos programas detectan y bloquean

### Estancias Extendidas — Comparación Cruzada
Para consultas Tipo L:
1. Buscar en plataformas de hotel Y en Airbnb/Vrbo (descuentos semanales/mensuales)
2. Calcular: tarifa diaria regular × N días vs tarifa paquete semanal/mensual
3. Incluir factores ocultos: cocina (ahorro en comida), lavandería, WiFi/utilities incluidos
4. Para CR: considerar apart-hoteles locales que no aparecen en OTAs internacionales

---

## Anti-Patrones (NO hacer)
1. ❌ Listar plataformas sin buscar precios reales
2. ❌ Recomendar "visita booking.com" sin haber buscado primero
3. ❌ Inventar tarifas o rangos sin fuente
4. ❌ Ignorar fees ocultos (resort fee, baggage, etc.)
5. ❌ Asumir que la primera opción encontrada es la mejor sin comparar
6. ❌ Dar respuestas genéricas tipo guía de viaje cuando se pidieron precios
7. ❌ Omitir la fecha de vigencia de una promoción
8. ❌ Recomendar day pass sin comparar contra tarifa de noche completa
9. ❌ Omitir horario de acceso del day pass (dato crítico para el usuario)
10. ❌ No verificar si el day pass incluye o excluye comidas/habitación
11. ❌ Recomendar tarifa opaca sin advertir que es no reembolsable
12. ❌ Dar asesoría financiera sobre tarjetas de crédito — solo presentar opciones
13. ❌ Recomendar status match sin verificar vigencia de la oferta
14. ❌ Omitir seguro CDW/LDW en comparaciones de rental car
15. ❌ No comparar paquete staycation vs componentes por separado
16. ❌ Listar restaurantes sin indicar tipo de promo, horario y si es apto para niños
17. ❌ Listar eventos sin verificar fecha exacta (eventos pasados = inútil)
18. ❌ En Briefing Integral, omitir alguna sección — TODAS las secciones son obligatorias aunque alguna quede vacía (indicar "No se encontraron ofertas activas")
19. ❌ En Briefing Integral, no incluir presupuesto estimado total en la recomendación TOP
