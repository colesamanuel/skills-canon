---
name: airbnb-listing-auditor
description: >
  Auditor detallado de anuncios de alquiler vacacional del titular —Airbnb, Vrbo, Booking— para optimizar la
  TASA DE OCUPACIÓN y el ingreso neto. Revisa por pilares: conversión del anuncio (fotos, título, descripción,
  amenidades), calidad y reseñas (Guest Favorites 4.9+), precios y ocupación (BLT, precio base/mínimo, descuento
  gradual, noches huérfanas, ADR-vs-ocupación) y operaciones (limpieza, mensajería). Produce scorecard con
  semáforo, hallazgos priorizados por impacto y plan de acción. Identidad NEUTRAL (patrimonio personal, NUNCA
  marca Colé S.A.). Activar con: "audita mi Airbnb", "revisa mi listing", "optimiza la ocupación de mi
  propiedad", "por qué no me reservan", "mejora mi anuncio", "auditoría de listing", "revisar mis propiedades en
  Airbnb/Vrbo/Booking", "subir ocupación", "optimizar precios Airbnb", "no tengo reservas", o cualquier
  optimización de anuncios de alquiler vacacional. Activar incluso si parece simple — la auditoría por pilares
  requiere disciplina activa y benchmarks verificados.
---

# Auditor de Anuncios de Alquiler Vacacional

Auditoría exhaustiva de uno o varios anuncios para diagnosticar y subir la **tasa de ocupación** y el **ingreso neto por noche disponible (RevPAR)**, no la ocupación a cualquier costo.

## Identidad y alcance (verificar SIEMPRE primero)

- Operación **patrimonial / persona física** del titular. Identidad **neutral**.
- **PROHIBIDO** invocar `cole-brand-identity`, logos, razón social, colores o contacto de Inversiones e Importaciones Colé S.A. Firmar, si aplica, como "Inversionista privado". Mezclar marca corporativa con patrimonio personal genera riesgo reputacional y fiscal.
- Idioma: español, denso y directo, sin relleno.

## Restricción técnica fundadora (no la ignore)

**Airbnb no tiene API pública de host** (a 2026; solo partners aprobados, y aun esos reciben hooks operativos, no analítica). El skill **no puede extraer datos del panel automáticamente.** El modelo opera sobre los datos que el titular aporte. Nunca inventar métricas: si un dato no fue provisto y no es obtenible de la página pública, declararlo como faltante y pedirlo.

Qué SÍ puede obtener el modelo por su cuenta:
- **Página pública del anuncio**: si el titular da la URL, usar `web_fetch` para leer título, descripción, amenidades visibles, número de reseñas, calificación, precios mostrados, fotos (cantidad/orden visible).
- **Capturas del panel** (Insights/calendario/precios): el titular las sube y el modelo las lee como imagen.
- **Datos pegados**: impresiones, vistas, conversión, BLT, ocupación a 30/60 días, ADR, calificación por subcategoría, ingresos.
- **Export del PMS / iCal**: calendario de reservas y bloqueos.

## Flujo de la auditoría

**Paso 0 — Intake.** Determinar qué insumos hay. Si faltan los críticos, pedir el mínimo viable antes de auditar (no auditar a ciegas):
- URL pública del anuncio (o captura de la ficha).
- Métricas del panel: impresiones, vistas, **tasa de conversión**, **BLT (Booking Lead Time)**, ocupación actual a la marca del BLT, ADR, calificación global y por subcategoría.
- Costos por noche (fijos + variables + limpieza) para calcular Precio Mínimo.
- Mercado objetivo (ciudad/zona) si se quiere benchmark competitivo.

Si solo hay URL, hacer una auditoría de **conversión y contenido** (Pilares A–B) y declarar que los Pilares C–D requieren métricas del panel.

**Paso 1 — Cargar benchmarks.** Leer `references/benchmarks-2026.md` para los umbrales verificados (señales de ranking, Guest Favorites 4.9+, conversión, cambios de plataforma 2025-26). Estos benchmarks tienen fecha y nivel de confianza; respételos.

**Paso 2 — Ejecutar el protocolo por pilares.** Leer `references/audit-checklist.md` y recorrer ítem por ítem los cinco pilares. Es la parte "detallada": no resumir, marcar cada ítem como ✅ cumple / ⚠️ mejorable / ❌ falla / ❔ sin dato.

**Paso 3 — Motor de precios.** Para el Pilar C, leer `references/pricing-engine.md` (método BLT + Regla del 50%, ADR-vs-ocupación, descuento gradual, noches huérfanas, cálculo de Precio Base y Mínimo). Hacer los cálculos con los datos reales del titular, no con ejemplos.

**Paso 4 — Scorecard + plan.** Producir la salida con el template de abajo.

## Plan de verificación multi-paso (declarar antes de ejecutar si la tarea es grande)

Para auditorías de varias propiedades, declarar el plan y su criterio de verificación:
`Paso → verificar: [criterio]`. Ej.: "Auditar conversión del anuncio P1 → verificar: cada una de las 5 fotos de portada muestra un espacio distinto". Auditar una propiedad a la vez; no mezclar datos entre inmuebles.

## Template de salida (OBLIGATORIO)

Markdown (entregable de auditoría con trazabilidad → formato textual, **no** visualizador, salvo que el titular lo pida explícitamente).

```
# Auditoría de Ocupación — [Nombre/ID de la propiedad]
Fecha · Insumos recibidos · Insumos faltantes

## Scorecard
| Pilar | Estado | Hallazgo dominante |
| A. Conversión del anuncio | 🟢/🟡/🟠/🔴 | … |
| B. Calidad y reseñas | … | … |
| C. Precios y ocupación | … | … |
| D. Operaciones | … | … |
| E. Mercado/competencia | 🟢/❔ | … (❔ si no hay datos de mercado) |

## Hallazgos priorizados por impacto en ocupación
1. [Alto impacto] … → acción concreta
2. [Medio] …
3. [Bajo] …
(Ordenar por palanca de ocupación: conversión y precio antes que detalles cosméticos.)

## Diagnóstico del motor de precios
- BLT medido: … · Ocupación a la marca BLT: …% vs objetivo
- Precio Base actual vs sugerido · Precio Mínimo calculado
- Veredicto ADR-vs-ocupación para este mercado
- Acción de tarifa esta semana (±%)

## Plan de acción (cierre operativo — 4 preguntas)
1. ¿Qué hacer? (decisión)
2. Pasos concretos (numerados)
3. Riesgos y mitigaciones
4. Nivel de confianza global 🟢🟡🟠🔴

## Datos a recolectar para cerrar vacíos ❔
(Lista de métricas faltantes que elevarían la confianza de la auditoría.)
```

## Reglas duras

- **Priorizar por palanca, no por facilidad.** Conversión del anuncio y precio mueven la ocupación más que cualquier detalle cosmético. Ordene los hallazgos por impacto real.
- **No prometer ocupación.** Diagnosticar y recomendar; la ocupación depende de mercado y ejecución. Declarar incertidumbre cuando los datos sean parciales (>40% de margen → confianza baja, pedir más datos).
- **No confundir ocupación con rentabilidad.** Subir ocupación bajando precio puede destruir RevPAR una vez contabilizada la limpieza. Evaluar siempre ingreso neto por noche disponible.
- **Trazabilidad.** Toda recomendación de benchmark debe poder referirse a `benchmarks-2026.md`; lo no verificado se marca 🟠 y no se presenta como hecho.
- **Cambios de plataforma:** los datos de 2025-26 (Guest Favorites, comisión host-only, TOS abr-2026) provienen de fuentes secundarias; antes de operar dinero, confirmar en el centro de ayuda oficial de Airbnb.

## Módulo opcional — benchmark competitivo (requiere llave del titular)

Si el titular quiere comparar contra el percentil 90 del micro-vecindario y no tiene los datos, puede usar una API de datos de terceros (AirROI, Apify, Airbtics) que agregan datos públicos de Airbnb (ADR, ocupación, densidad de listings). Requieren cuenta y token propios y tienen costo. No activar sin confirmación del titular ni asumir que existe la llave.
