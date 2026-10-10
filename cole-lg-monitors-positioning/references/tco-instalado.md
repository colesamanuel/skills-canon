# Tabla TCO Instalado — Monitores LG Medical (Colé S.A.)

**Estado**: HÍBRIDO. Estructura completa, cifras numéricas marcadas como placeholders
hasta validación. NO publicar copy externo con marcadores `[VALIDAR-X]` visibles.

## Filosofía del TCO instalado

A diferencia de APPR (que el cliente piensa como "compra"), monitores médicos son
**inversión de capital con vida útil prolongada**. El cliente compara precios entre
proveedores, pero rara vez incluye el **costo total instalado**. Tu trabajo es mover
la conversación a TCO/año real.

```
TCO/año = (Precio CIF + Logística CR + Instalación + Calibración aceptación
            + QA periódico × años + Soporte × años − Valor residual) / Vida útil años
```

Donde:
- **Precio CIF**: precio LG en puerto destino (Colé absorbe parte del flete).
- **Logística CR**: nacionalización, transporte interno, manejo.
- **Instalación**: montaje, integración a estación de lectura.
- **Calibración aceptación**: QA inicial con phantom + software (TG-18 + TG-270).
- **QA periódico**: contrato anual de calibración (TG-270).
- **Soporte**: garantía extendida + escalamiento técnico.
- **Vida útil**: vida del backlight a 50% luminancia (típicamente 5-7 años en uso clínico).

## Plantilla TCO comparativa (estructura para 4 líneas ancla)

### Ancla 1 — Diagnóstico general 3MP (estación standard)

**Modelo Colé**: 21HQ513D (3MP) a $4.160 PV.

| Concepto | Monitor LG 21HQ513D vía Colé | Importador no especializado | Competidor premium |
|---|---|---|---|
| Precio inicial USD | $4.160 | `[VALIDAR-BENCHMARK-CR]` | `[VALIDAR-BENCHMARK-CR]` |
| Logística + nacionalización | Incluido | Cliente asume | Cliente asume |
| Instalación + integración PACS | `[VALIDAR-COSTO-INSTALADO]` | No incluido | A cargo del cliente |
| Calibración aceptación TG-18 | `[VALIDAR-COSTO-INSTALADO]` | No disponible | Externo |
| QA periódico anual TG-270 | `[VALIDAR-COSTO-INSTALADO]` | No disponible | Externo (alto costo) |
| Soporte local | Sí (San José) | No | Escalamiento internacional |
| Garantía LG | `[VALIDAR-LG]` años | Variable | Comparable |
| Extensión Colé | Disponible | No | No |
| Vida útil documentada | `[VALIDAR-LG]` h backlight | No documentada | Comparable |
| **TCO USD/año a 5 años** | `[CALCULAR]` | `[CALCULAR]` | `[CALCULAR]` |

**Argumento ancla derivable**: a igualdad de cumplimiento técnico (DICOM GSDF + TG-270),
la oferta Colé+LG entrega producto + instalación + QA + soporte local en un solo
contrato. Versus oferta de retail o competidor premium donde el cliente debe sumar
costos de instalación, QA y soporte por separado.

### Ancla 2 — Mamografía diagnóstica primaria (12MP)

**Modelo Colé**: 31HN713D (12MP) a $13.000 PV — **único modelo cumplidor para mamografía**.

| Concepto | 31HN713D vía Colé | Alternativa premium |
|---|---|---|
| Precio inicial USD por unidad | $13.000 | `[VALIDAR-BENCHMARK-CR]` |
| Par calibrado para lectura | $26.000 (par) | `[VALIDAR-BENCHMARK-CR]` |
| Logística + instalación + calibración | `[VALIDAR-COSTO-INSTALADO]` | No siempre incluido |
| Cumplimiento ACR/MQSA | Sí | Sí |
| Calibración bilateral del par | Servicio Colé incluido | Externo, alto costo |
| Vida útil documentada | `[VALIDAR-LG]` h | Comparable |
| **TCO USD/año a 7 años** | `[CALCULAR]` | `[CALCULAR]` |

**Argumento ancla derivable**: la mamografía exige par calibrado y QA continuo. El
costo del programa institucional es predecible y auditable. El no-cumplimiento ACR/MQSA
expone a la institución a sanciones específicas de mamografía (verificar marco regulatorio
costarricense aplicable — `[VALIDAR-ACR-CR]`).

### Ancla 3 — Programa institucional (jefe servicio / gerente hospitalario)

| Concepto | Compra reactiva mixta | Programa Colé+LG estandarizado |
|---|---|---|
| Costo inicial | Distribuido en el tiempo, no presupuestable | Predecible, presupuestable |
| Estandarización de flota | Múltiples marcas, calibración inconsistente | Una sola línea, calibración uniforme |
| Trazabilidad de QA | Parcial o ausente | Documentada por unidad y por sesión QA |
| Riesgo regulatorio en auditoría | Alto | Bajo |
| Riesgo de demanda por error diagnóstico relacionado a calidad de imagen | No mitigado | Mitigado (cumplimiento documentado) |
| Soporte técnico | Escalado internacional, lead time alto | Local San José |
| Predictibilidad de costo | Baja | Alta |

**Argumento ancla derivable**: el programa institucional convierte un gasto reactivo
no presupuestable en un costo operativo predecible y auditable. El ROI se materializa
al evitar **un solo evento adverso** (multa, demanda, mala praxis).

### Ancla 4 — Flat Panel Detector (DR digital)

**Modelos Colé**: 14HQ701G ($17.280) y 17HQ701G ($17.800).

| Concepto | Flat Panel LG vía Colé | Competidor premium |
|---|---|---|
| Precio inicial USD | $17.280 - $17.800 | `[VALIDAR-BENCHMARK-CR]` |
| Logística + instalación | `[VALIDAR-COSTO-INSTALADO]` | A cargo del cliente |
| Integración con generador RX | Servicio Colé incluido | Externo |
| Calibración inicial | Incluida | Variable |
| Vida útil esperada | `[VALIDAR-LG]` exposiciones | Comparable |
| Soporte local | Sí | Escalamiento internacional |
| **TCO USD/año a 7 años** | `[CALCULAR]` | `[CALCULAR]` |

**Argumento ancla derivable**: el flat panel es el componente más caro de la cadena
RX digital. Su integración con generador y software de adquisición es crítica.
Servicio local Colé reduce tiempo de puesta en marcha y mantenimiento.

## Reglas de uso de la tabla TCO en copy

### Lo permitido (con placeholders activos)

- "El TCO instalado a 5 años es competitivo frente a alternativas premium cuando se
  considera logística, instalación y QA periódico."
- "La diferencia se mide en TCO total, no en precio de etiqueta."
- "Programa institucional Colé+LG entrega producto + servicio en un solo contrato."
- Estructura comparativa cualitativa.

### Lo prohibido (mientras placeholders activos)

- Cifras específicas de TCO ($X/año vs $Y/año) presentadas como definitivas.
- Promesas de ahorro porcentual ("ahorra 30%").
- Tablas con números completos sin aviso de validación pendiente.
- Comparación competitiva nominal con marca específica del competidor (regla #3 del SKILL).

### Cuándo se libera la tabla con cifras definitivas

Cuando los placeholders críticos estén cerrados:

1. `[VALIDAR-LG]` — Vida útil de backlight + FDA 510(k) + datasheet técnico LG por modelo.
2. `[VALIDAR-PRECIO-COLE]` — Confirmar PV vigente en Odoo de los 11 modelos.
3. `[VALIDAR-COSTO-INSTALADO]` — Cálculo interno Colé S.A. de costo logística +
   instalación + calibración por modelo.
4. `[VALIDAR-BENCHMARK-CR]` — Benchmark precio competidores premium en CR (mystery shopping).
5. `[VALIDAR-ACR-CR]` — Marco regulatorio costarricense aplicable a mamografía
   (¿Decreto 44653-S o normativa específica?).

## Plan de validación documentado

| # | Placeholder | Acción de validación | Responsable | Plazo |
|---|---|---|---|---|
| 1 | `[VALIDAR-LG]` | Solicitar datasheet técnico oficial LG por modelo (vida útil backlight, FDA 510(k), brillo cd/m²) | Manuel + Carlos LG | 1-2 semanas |
| 2 | `[VALIDAR-PRECIO-COLE]` | Confirmar PV vigente en Odoo de los 11 modelos | Vanessa | 1 semana |
| 3 | `[VALIDAR-COSTO-INSTALADO]` | Cálculo interno: logística + instalación + calibración por modelo | Marco + Manuel | 2-4 semanas |
| 4 | `[VALIDAR-BENCHMARK-CR]` | Mystery shopping: competidores premium en CR (cotización equivalente) | Marco | 4-8 semanas |
| 5 | `[VALIDAR-ACR-CR]` | Verificar marco regulatorio CR para mamografía (Decreto 44653-S, MINSA, ACR) | Manuel + asesor legal | 2-4 semanas |
| 6 | Phantom + software TG-18/TG-270 propio | Inventario interno Colé: ¿tenemos el equipo para QA? | Marco / área técnica | Inmediato |

## Soporte de evidencia técnica para el TCO

Estos respaldan los argumentos de la tabla. Verificar vigencia al redactar.

- **DICOM Part 14 (GSDF)** — Curva de luminancia estándar para imagen médica.
  Disponible en `nema.org`.
- **AAPM TG-18** — Patrones de QA inicial de displays médicos (legacy, vigente
  para QA de aceptación).
- **AAPM TG-270** — QA periódico continuo de displays médicos (vigente, reemplaza
  al TG-18 para QA periódico). Disponible en `aapm.org`.
- **IEC 62563-1** — Métodos de evaluación de calidad de displays médicos.
- **FDA 510(k)** — Verificación por modelo en `accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/`.
- **ACR Mammography Quality Standards Act** — Exigencias específicas para mamografía.

## Ítem crítico operacional pendiente

**¿Colé tiene phantom + software de calibración TG-18/TG-270 propio?**

Si la respuesta es **no**, el servicio "calibración" prometido en el copy es
promesa sin recurso. Hay dos caminos:

1. Adquirir phantom + software (Diagnomatic, NDS Surgical, JVCKenwood u otro)
   y formalizar el servicio. Convierte TG-270 en foso competitivo real.
2. Subcontratar calibración con tercero local. Desventaja: dependencia + margen
   reducido.

**Esta decisión debe resolverse antes de prometer "calibración Colé" en copy.**
Marcar como bloqueante en el plan.

## Disclaimer interno

Esta tabla TCO es un **marco de argumentación**, no un instrumento contable. Las cifras
finales dependen de variables del cliente (configuración GPU, número de estaciones,
PACS instalado, condiciones ambientales, plan de QA). Toda propuesta cerrada debe
pasar por `odoo-quotation-generator` con cifras del catálogo vigente, no por este skill.
