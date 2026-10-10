---
name: prompt-optimizer
description: Convierte un prompt escueto + contexto en un prompt optimizado para Claude Fable 5, aplicando la guía de 7 puntos (intención, límites en positivo, acción directa, verificación anti-fabricación, nivel de output, consistencia interna, delegación en capacidades nativas) e inyectando automáticamente las reglas duras del dominio detectado (blindaje/dosimetría, bursátil, Odoo/cotizaciones, SEO, edición quirúrgica). Activar con "optimiza este prompt", "mejora el prompt", "genera el prompt optimizado", "prompt para...", "cómo le pido que...", "redacta el prompt", "conviérteme esto en un buen prompt", "prompt engineering", o cuando el usuario entregue una instrucción cruda y pida transformarla en prompt reutilizable. Activar incluso si la solicitud parece simple — la inyección de reglas de dominio requiere disciplina activa. NO activar para diseñar bucles iterativos generador-evaluador (eso es loop-designer) ni para ejecutar directamente la tarea del prompt sin optimizarlo.
---

# Prompt Optimizer — Fable 5

Transforma prompts escuetos en prompts optimizados aplicando metodología verificable y las reglas duras del perfil del titular. **No ejecuta la tarea del prompt** (salvo modo "optimiza y ejecuta"); su entregable es el prompt mismo.

## Flujo obligatorio

1. **Gate de trivialidad.** Evaluar el prompt recibido contra las 7 reglas (§Metodología). Si ya cumple ≥5 de 7 → devolverlo con ajuste mínimo y declararlo explícitamente ("cumple 6/7; ajuste único: ..."). No sobre-optimizar.
2. **Detección de dominio.** Clasificar contra la matriz (§Matriz de dominio). Si aplica más de un dominio, inyectar las cláusulas de todos. Si el dominio es ambiguo, preguntar UNA sola vez; nunca asumir marca Colé por defecto (perfil §4.4).
3. **Reconstrucción con las 7 reglas.**
4. **Salida en formato fijo** (§Formato de salida).
5. **Modo dual:** por defecto, entregar el prompt para revisión del titular. Solo si el usuario dice "optimiza y ejecuta" (o equivalente inequívoco), ejecutar el prompt optimizado inmediatamente después de mostrarlo.

## Metodología — Guía de 7 puntos (Fable 5)

Aplicar cada regla al reconstruir el prompt:

1. **Intención (el "porqué").** Explicitar objetivo final, consumidor del resultado y criterio de éxito. Si el prompt escueto no lo trae y no es inferible del contexto, preguntar — es el único dato bloqueante que justifica pausa.
2. **Límites en positivo.** Convertir prohibiciones en delimitación de alcance ("modifica solo X; el resto intacto"). Reservar negación dura (NUNCA/PROHIBIDO) para reglas absolutas del perfil (ej.: sin factura comercial en paquete Aeropost; nunca DAP/DDP sin confirmación).
3. **Acción directa.** Instruir ejecución en cuanto haya información suficiente; preguntar solo ante ambigüedad bloqueante. Eliminar del prompt invitaciones a generar opciones o planes no solicitados.
4. **Verificación anti-fabricación.** Exigir marcado de datos como verificado/inferido; si el dato puede cambiar en <1 semana, búsqueda en tiempo real obligatoria (perfil §6). Instruir "declara 'no lo sé' antes que estimar" (perfil §2.2).
5. **Nivel de output, no microgestión del razonamiento.** NUNCA incluir "no pienses paso a paso" ni "razona paso a paso" como control de calidad. En su lugar, especificar la profundidad del entregable: "solo resultado + margen de certeza" vs. "derivación visible para anexo auditable".
6. **Consistencia sobre brevedad.** El prompt puede ser largo si es consistente. Antes de entregar, auditar colisiones internas (ej.: "exhaustivo" + "media página"). Si el prompt original contenía contradicciones, resolverlas y reportarlas.
7. **Delegar en capacidades nativas.** Eliminar instrucciones que replican el comportamiento por defecto del modelo o de un skill ya activo (tono profesional, buen español, "no inventes"). Conservar solo desviaciones reales. Si existe un skill que ya cubre parte del prompt, referenciarlo en vez de duplicar sus reglas.

## Matriz de dominio — cláusulas de inyección automática

Detectar por palabras clave y contexto; inyectar la cláusula correspondiente en el prompt optimizado:

| Dominio | Señales | Cláusula a inyectar |
|---|---|---|
| **Blindaje / dosimetría / PR** | blindaje, dosis, dosimetría, NCRP, IAEA, ICRP, barrera, levantamiento, QC, kerma | "Declara margen de certeza del cálculo (ej. ±15% ICRU 90). Toda afirmación de dosis/riesgo con base cuantificada y norma citada (NCRP/IAEA/ICRP). Si el margen resultante es <10% bajo NCRP, PAUSA y solicita confirmación." (perfil §2.2, §4.5) |
| **Bursátil / macro** | acciones, ticker, VIX, earnings, portafolio, entrada, ATR, macro, CPI, yields | "Búsqueda en tiempo real OBLIGATORIA antes de opinar (precios, VIX, consenso, earnings). Marca cada dato verificado-hoy / no-verificado. Escenarios de riesgo obligatorios (ATR, event risk, liquidez). Regla dura: VIX>25 → mínimo 50% cash." (perfil §2.2, §6) |
| **Odoo / cotizaciones** | cotizar, cotización, proforma, Odoo, quote, precio de, cliente nuevo | "Cliente debe existir en res.partner (crear si no). NO crear oportunidad CRM. Tabla 3 columnas (Lista / Costo neto / PV 40%) y esperar aprobación del PV antes de emitir. USD: currency_id:1 Y pricelist_id:2. CR: country_id:50. Multi-empresa: nunca mezclar company_id 1 (Colé) y 2 (Kermatek)." (perfil §5.1, §5.2) |
| **Logística internacional** | flete, envío, exportar, aduana, DAP, DDP, Incoterm | "Flete incluido SOLO hasta puerto/aeropuerto de aduana destino. Nacionalización, impuestos, agente y transporte interno por cuenta del cliente. NUNCA prometer DAP/DDP door-to-door sin confirmación caso por caso." (perfil §5.1) |
| **SEO / contenido web** | artículo, blog, post web, SEO, colecr.com | "Formal-profesional, EAT estricto, sin fecha ni autor visible, Markdown renderizado, sección Preguntas y Respuestas obligatoria al cierre. Delegar el resto en seo-technical-writer." (perfil §5.7) |
| **Edición de documento/código** | corrige, edita, ajusta, refactoriza, modifica el archivo | "Regla Karpathy completa: tocar solo lo pedido; respetar estilo; problemas no relacionados se listan sin corregir; cero alcance especulativo; multi-paso → plan 'Paso → verificar: [criterio]' antes de ejecutar." (perfil §4.3) |
| **Entregable visual** | dashboard, HTML, visualiza, gráfico interactivo | "Verificar las 3 condiciones de §5.8 antes de invocar visualizador; si falla una → Markdown. Exclusión dura: cotizaciones formales, cartas regulatorias, artículos SEO, auditorías con trazabilidad." (perfil §5.8) |
| **Branding** | logo, marca, brochure, landing, presentación corporativa | "Identificar path/proyecto contra matriz §4.4 ANTES de aplicar identidad. Path patrimonial/personal → identidad neutral, prohibidos skills y elementos de marca Colé. Ambiguo → preguntar." (perfil §4.4) |
| **Ifá / Isẹ̀ṣe** | Odu, Ifá, Orisa, ebo, oriki | "Texto yorùbá original con diacríticos tonales junto a traducción al español." (perfil §5.7) |

Dominio no listado → aplicar solo las 7 reglas generales sin cláusula de inyección.

## Formato de salida (obligatorio)

```
## Prompt optimizado
[bloque de código copiable con el prompt final]

## Trazabilidad
| Regla aplicada | Cambio realizado | Fuente |
|---|---|---|
| 1. Intención | ... | Guía §1 |
| ...solo las reglas que produjeron cambio... | | |
| Inyección [dominio] | cláusula X añadida | Perfil §N.N |

## Contradicciones resueltas
[solo si el prompt original las tenía; si no, omitir sección]
```

Cierre estándar del perfil §9 (recomendación, pasos, riesgos, confianza) aplica a la respuesta completa, no dentro del prompt generado.

## Reglas del skill

- El prompt optimizado se redacta en el idioma del prompt original (default español).
- Nunca incluir en el prompt generado credenciales, API keys ni secretos, aunque el dominio Odoo/Apps Script aplique — referenciar "credenciales en memoria/perfil".
- Si el prompt escueto pide algo que violaría una pausa de escalada del perfil (§4.5), el prompt optimizado debe incorporar la pausa, no eludirla.
- Exclusión mutua con loop-designer: si el usuario pide diseñar/parametrizar un bucle iterativo, derivar a loop-designer. Si pide optimizar el prompt *interno* de un bucle ya diseñado, este skill sí aplica.
- Este skill no sustituye la aprobación del titular en flujos que la exigen (PV de cotizaciones, blindaje <10%): el prompt generado debe preservar esos checkpoints.

## Ejemplo mínimo

**Entrada:** contexto = "responder hoy a hemodinamista que compara contra competidor chino"; prompt escueto = "hazme tabla de delantales plomados".

**Salida (extracto del prompt optimizado):**
> Genera tabla comparativa de delantales plomados Colé S.A. con argumento TCO cuantificado por unidad, para anexar a email comercial dirigido a hemodinamista privado que evalúa alternativa de menor precio. Alcance: solo modelos del catálogo APPR vigente; no es cotización formal (sin tabla de márgenes ni aprobación de PV). Cada dato técnico (Pb-eq, peso, vida útil) verificable contra ficha de fabricante; si un dato no está en catálogo, márcalo como pendiente — no lo estimes. Output: tabla Markdown + 3 líneas de argumento TCO listas para pegar.

Trazabilidad: R1 (intención: email comercial, no cotización) · R2 (alcance en positivo: solo catálogo APPR) · R4 (anti-fabricación: pendiente vs. estimar) · R5 (nivel de output: tabla + 3 líneas) · R7 (deriva narrativa a cole-appr-positioning, no la duplica).
