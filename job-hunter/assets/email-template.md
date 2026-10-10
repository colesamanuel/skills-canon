# Plantilla de correo al candidato — Job Hunter

Esta es la estructura que sigue el borrador generado en Fase 5, Paso 5.2.

## Variables

- `{NOMBRE_CANDIDATO}` — del perfil
- `{FECHA_HOY}` — formato DD-MMM
- `{N_OFERTAS_ACTIVAS}` — cantidad de ofertas 🟢 verificadas
- `{N_OFERTAS_DESCARTADAS}` — cantidad de ofertas 🔴 auditadas
- `{LISTA_OFERTAS}` — bloque generado dinámicamente
- `{BRECHAS_CV}` — del campo `cv_gaps_to_close_before_applying` del perfil
- `{TONO}` — formal-cercano (default) o formal-estricto

---

## Estructura del cuerpo

```
{NOMBRE_CANDIDATO}, buenas tardes,

Hice un barrido del mercado para tu perfil ({DESCRIPCION_PERFIL_CORTA}) y verifiqué status oferta por oferta. De {N_OFERTAS_TOTAL} resultados, solo {N_OFERTAS_ACTIVAS} están realmente activas y aceptan candidatos desde {LOCATION_CANDIDATO}. Te las paso priorizadas, con el link directo y mi lectura de cada una.

— — —

{BLOQUE_OFERTA_1}

— — —

{BLOQUE_OFERTA_2}

— — —

{BLOQUE_OFERTA_N}

— — —

{BLOQUE_BRECHAS_CV}

— — —

Si querés, en una segunda iteración te paso los pools de talento permanentes que conviene tener como estrategia paralela: no son ofertas puntuales, sino embudos abiertos todo el año.

Cualquier duda me decís.

Saludos,
Ing. Manuel Rubio, MSc
```

---

## Estructura de cada bloque de oferta

```
{N}) {EMPRESA_UPPERCASE} — {TITULO_POSICION}
{URL_VERIFICADA}

{LECTURA_DEL_MATCH} (1-3 oraciones explicando por qué encaja con un elemento específico del CV).

{ADVERTENCIAS} (si aplican: part-time, restricción geográfica, riesgo de pago, gap técnico a cubrir, etc.).

{TELEMETRIA} (datos del fetch: cantidad de aplicaciones, fecha de última verificación, urgencia).
```

---

## Estructura del bloque de brechas

```
DOS BRECHAS DEL CV QUE CONVIENE CERRAR ANTES DE APLICAR

En la versión que me compartiste, los campos {LISTA_GAPS}. Son los dos campos que más rechazan los filtros automáticos. Mi sugerencia para tu rango ({DESCRIPCION_RANGO_SENIOR}):

  - Disponibilidad: {SUGERENCIA_AVAILABILITY}
  - Salario: USD {RANGO_ANUAL} / año, o USD {RANGO_MENSUAL} / mes. Cotiza en USD, no en colones. {RATIONALE_DEL_PERFIL}.

{NOTAS_ADICIONALES} (ej: estatus migratorio + recomendación de framing como contractor).
```

---

## Reglas de redacción del correo

1. **Idioma:** español por default (a menos que el perfil diga otra cosa).
2. **Tono:** formal-cercano. Evitar "estimado/a". Usar "buenas tardes" + nombre.
3. **Densidad:** máximo 600 palabras totales. El correo es para acción, no para análisis.
4. **Links:** siempre como URL plana, NO hyperlink en el texto. El cliente Gmail los detecta.
5. **Advertencias:** explícitas y en su propio párrafo. No mezclar con el match.
6. **Cierre:** firma fija como Ing. Manuel Rubio, MSc.

---

## Anti-patrones (NO hacer)

- ❌ Listar ofertas que NO pasaron verificación HTTP. El candidato pierde confianza si una de las URLs está cerrada.
- ❌ Mezclar pools de talento con ofertas activas en el mismo bloque.
- ❌ Aplicar a la oferta en nombre del candidato. Solo enviar el link.
- ❌ Decir "esta oferta es perfecta para ti" — usar "encaja con tu experiencia en X" con referencia específica.
- ❌ Incluir más de 5 ofertas. Si hay más, elegir top 3-4 por match score y mencionar las otras como ítem corto al final.
