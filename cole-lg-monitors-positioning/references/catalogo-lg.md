# Catálogo LG Electronics Medical — Distribución Colé S.A.

Catálogo completo de monitores médicos y flat panels LG distribuidos por Colé S.A.
Precios PV final (no aplica margen distribuidor — son precios de catálogo Colé).

> **Fuente**: Lista de precios interna Colé S.A., actualizada Nov 2024. Validar
> sincronía con Odoo antes de publicar copy con cifra de precio definitiva.

## Tabla maestra — 11 modelos

| Modelo | Descripción | Tipo | PV USD | Uso clínico apropiado |
|---|---|---|---:|---|
| **31HN713D** | Monitor 12MP 31" | Diagnóstico mamografía | 13.000 | Mamografía diagnóstica primaria |
| **32HQ713D** | Monitor 8MP 31.5" | Diagnóstico avanzado | 6.700 | Diagnóstico primario, tomografía, RX general alta exigencia |
| **21HQ613D** | Monitor 5MP 21.3" Vertical | Diagnóstico | 7.700 | Diagnóstico primario radiografía, mamografía revisión |
| **32HL512D** | Monitor 8MP 31.5" | Diagnóstico (no mamografía) | 4.940 | Diagnóstico general, no mamografía |
| **21HQ513D** | Monitor 3MP 21.3" Vertical | Diagnóstico (no mamografía) | 4.160 | Diagnóstico general radiografía/CT, no mamografía |
| **24HR513C** | Monitor 2MP 24" | Revisión clínica | 1.690 | PACS, worklist, revisión secundaria, NO diagnóstico primario |
| **27HJ713C** | Monitor 8MP 27" | Revisión clínica avanzada | 2.272 | Revisión clínica de imagen volumétrica |
| **27HJ712C** | Monitor 8MP 27" | Revisión clínica | 2.158 | Revisión clínica de alto detalle |
| **14HQ701G** | Flat Panel Detector 14" | Detector RX digital | 17.280 | RX digital portátil/general, formato pequeño |
| **17HQ701G** | Flat Panel Detector 17" | Detector RX digital | 17.800 | RX digital general, formato estándar |
| **55MH5K** | Monitor 4K 55" 12G-SDI | Quirófano | 14.400 | Quirófano, sala de procedimientos, integración con cámara endoscópica |

## Guía de selección por uso clínico

### Mamografía diagnóstica primaria
**Único modelo cumplidor**: `31HN713D` (12MP).

> **REGLA DURA**: Para diagnóstico mamográfico primario, ACR/MQSA exige resoluciones
> ≥5MP y certificación específica. Recomendar 3MP u 8MP no-mamográfico para mamografía
> primaria es no-cumplimiento regulatorio. **Nunca cotizar 21HQ513D, 32HL512D ni 32HQ713D
> para mamografía primaria.**

Si el cliente busca pareja diagnóstica + revisión mamográfica:
- Diagnóstica primaria: 31HN713D × 2 (par calibrado).
- Revisión: 21HQ613D (5MP).

### Diagnóstico primario general (RX, CT, RM, US)

| Necesidad | Modelo recomendado |
|---|---|
| Lectura primaria standard | 21HQ513D (3MP) o 21HQ613D (5MP) |
| Lectura primaria alta exigencia | 32HQ713D (8MP) |
| Lectura primaria sin mamografía | 32HL512D (8MP) — más económico |

### Revisión clínica / no-diagnóstico

| Necesidad | Modelo recomendado |
|---|---|
| PACS, worklist, revisión secundaria | 24HR513C (2MP) |
| Revisión avanzada con detalle | 27HJ712C o 27HJ713C (8MP) |

### Quirófano / Sala de procedimientos

Único modelo: `55MH5K` (4K, 55", 12G-SDI). Compatible con cámara endoscópica y sistemas
de integración quirúrgica.

### Flat Panel Detector (DR digital)

| Formato | Modelo |
|---|---|
| 14" (pediátrico, extremidades, dental) | 14HQ701G |
| 17" (RX general, tórax, abdomen) | 17HQ701G |

## Especificaciones técnicas a citar (para copy)

> **Importante**: las cifras de brillo, contraste y vida útil de backlight requieren
> verificación con datasheet LG vigente antes de publicarlas como definitivas.
> Marcar como `[VALIDAR-LG]` en bloque de auditoría interna.

### Estándares aplicables

Todos los monitores diagnósticos y de revisión LG que figuran en este catálogo
declaran cumplimiento con (verificar datasheet del modelo específico antes de citar):

- **DICOM Part 14** — Grayscale Standard Display Function (GSDF). Curva de luminancia
  calibrable que asegura percepción uniforme de niveles de gris en la imagen médica.
- **AAPM TG-18** — patrones y métricas de QA inicial de displays médicos.
- **AAPM TG-270** — QA periódica continua de displays médicos. (Este es el referente
  vigente; reemplaza al TG-18 para QA periódico).
- **IEC 62563-1** — Métodos de evaluación de calidad de displays médicos.
- **FDA 510(k)** — Verificación de número de registro por modelo. `[VALIDAR-LG]`.

### Mamografía adicional

- **ACR Mammography Quality Standards Act** — exigencias específicas de monitor
  mamográfico (resolución ≥5MP, calibración periódica documentada, condiciones
  ambientales controladas).

## Argumento técnico defendible para LG Medical

Estos puntos son la columna del posicionamiento. Verificar antes de citar.

1. **Manufactura propia de panel**: LG Display fabrica el panel. Competidores premium
   típicamente integran panel de tercero (Hannstar, AUO, Innolux). Esto da a LG control
   vertical sobre vida útil del backlight, uniformidad y consistencia entre lotes.
   *Verificación pendiente: corroborar con datasheet de fabricación de cada modelo.*

2. **Escala global LG Display + línea médica certificada**: pocos fabricantes médicos
   tienen escala de fabricación de panel propia. Esto se traduce en costo por píxel
   más bajo a igual cumplimiento técnico.

3. **Backlight LED W-LED IPS**: tecnología estándar en línea diagnóstica LG. Vida útil
   declarada por LG `[VALIDAR-LG]` horas a 50% luminancia. Comparativo a competidores
   premium: requiere `[VALIDAR-BENCHMARK-CR]`.

4. **Calibración de fábrica**: LG entrega monitores diagnósticos con calibración DICOM
   GSDF de fábrica + certificado individual. Importante: la calibración de fábrica
   **no sustituye** la calibración de aceptación en sitio (servicio Colé).

## Servicios Colé asociados (a mencionar como ventaja)

| Servicio | Cuándo aplica |
|---|---|
| Instalación + puesta en marcha | Toda venta institucional |
| QA de aceptación con phantom Diagnomatic | Diagnóstico primario y mamografía (recomendado) |
| Calibración periódica AAPM TG-270 | Plan de servicio anual (recomendable) |
| Capacitación operativa al equipo | Toda venta institucional |
| Soporte técnico local San José | Garantía LG + extensión Colé |

> Recordatorio (REGLA #8 del SKILL.md): mencionar como **ventaja**, no como argumento
> principal. El producto LG sigue siendo la columna del copy.

## Validaciones pendientes específicas del catálogo

- [ ] Confirmar PV vigente en Odoo de los 11 modelos (`[VALIDAR-PRECIO-COLE]`).
- [ ] Datasheet técnico LG por modelo con: resolución exacta, brillo cd/m² (no nits),
      contraste, vida útil backlight horas, certificación FDA 510(k).
- [ ] Disponibilidad de inventario en Costa Rica vs lead time de importación por modelo.
- [ ] ¿Colé tiene phantom + software TG-18/TG-270 propio para QA de aceptación?
      Si no, el servicio "calibración" es promesa sin recurso.
- [ ] Garantía LG por modelo (años) y diferencia con extensión Colé.
- [ ] Compatibilidad de cada modelo con tarjetas gráficas médicas (NVIDIA Quadro
      Medical, Barco MXRT). Importante para IT hospitalario.

## Cross-reference con otros skills

- Para cotización formal con tabla de aprobación de precios → `odoo-quotation-generator`.
- Para email educativo sobre QA AAPM TG-270 (no comercial) → `seo-technical-writer`.
- Para carta a LG por RMA, garantía o solicitud técnica → `supplier-request-generator`.
