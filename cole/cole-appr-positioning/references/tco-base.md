# Tabla TCO Base — APPR Colé S.A.

**Estado**: HÍBRIDO. Estructura cerrada, cifras numéricas marcadas como placeholders
hasta validación. NO publicar copy externo con marcadores `[VALIDAR-X]` visibles.

## Filosofía del TCO

El cliente compara precio inicial. Tu trabajo es mover la conversación a **costo/año real**.

```
TCO/año = (Precio inicial − Valor residual) / Vida útil años
        + Mantenimiento anual
        + Inspección anual
        + Costo esperado de no-cumplimiento × Probabilidad
```

Donde:
- **Vida útil**: años de uso clínico con integridad documentada (no años en bodega).
- **Mantenimiento**: limpieza, reparaciones menores.
- **Inspección anual**: verificación fluoroscópica de integridad (servicio Colé).
- **Costo esperado de no-cumplimiento**: multa MINSA + costo administrativo si auditan.

## Plantilla TCO comparativa (estructura para 5 productos ancla)

### Ancla 1 — Delantal frontal 0.5 mm Pb equivalente

| Concepto | Importador genérico | Colé Pb Light | Colé Pb Free Edge Bilayer |
|---|---|---|---|
| Precio inicial USD | `[VALIDAR-BENCHMARK-CR]` | `[VALIDAR-PRECIO-COLE]` | `[VALIDAR-PRECIO-COLE]` |
| Vida útil documentada (años) | `[VALIDAR-BENCHMARK-CR]` (estimado 1.5-2) | `[VALIDAR-KEMMETECH]` (estimado 5-7) | `[VALIDAR-KEMMETECH]` (estimado 5-7) |
| Garantía de fábrica | Variable | 2 años | 2 años |
| Inspección anual incluida | No | No (opcional, valor agregado) | No (opcional, valor agregado) |
| Trazabilidad de integridad | No | Sí (programa Colé) | Sí (programa Colé) |
| Atenuación 90 kVp | No documentada | 97% | 97% |
| Peso vs estándar | Estándar | −15% | −24% |
| Certificación | Variable | IEC 61331-1:2014, IEC 61331-3:2014, ISO 9001 | IEC 61331-1:2014, IEC 61331-3:2014, ISO 9001 |
| **TCO USD/año estimado** | `[CALCULAR]` | `[CALCULAR]` | `[CALCULAR]` |

**Argumento ancla derivable**: a igualdad de protección, Colé entrega documentación, garantía y peso reducido por una diferencia mensual menor a un café diario por usuario.

> El argumento se vuelve numérico **sólo cuando** Marco / Vanessa / Manuel cierren los placeholders. Hasta entonces, el copy describe la estructura sin afirmar la cifra final.

### Ancla 2 — Chaleco + Falda (intervencionismo prolongado)

| Concepto | Delantal frontal genérico | Chaleco-Falda Colé Pb Free 23912 |
|---|---|---|
| Precio inicial USD | `[VALIDAR-BENCHMARK-CR]` | `[VALIDAR-PRECIO-COLE]` |
| Distribución de peso | Toda en hombros | Cadera + hombros |
| Peso total comparable | Estándar | −24% Edge Bilayer |
| Costo médico personal (lumbalgia crónica) | No mitigado | Mitigado (evidencia ergonómica) |
| Vida útil esperada | 1.5-2 años | 5-7 años (`[VALIDAR-KEMMETECH]`) |
| **TCO USD/año estimado** | `[CALCULAR]` | `[CALCULAR]` |

**Argumento ancla derivable**: el costo médico personal de una hernia discal a 10 años por delantal mal distribuido excede cualquier diferencia de TCO de APPR.

> Soporte de evidencia: literatura sobre prevalencia de patología musculoesquelética en cardiólogos intervencionistas (Klein 2015, Orme 2015 — verificar metanálisis vigente al redactar copy).

### Ancla 3 — Lentes plomados (cristalino)

| Concepto | Sin lentes plomados | Lentes Colé/Phillips Star T9730 |
|---|---|---|
| Precio inicial USD | $0 | `[VALIDAR-PRECIO-COLE]` |
| Riesgo cristalino documentado | ICRP Pub 118: límite 20 mSv/año, antes 150 mSv/año | Mitigado |
| Atenuación frontal | 0% | 0.75 mm Pb |
| Atenuación lateral | 0% | 0.50 mm Pb |
| Vidrio | n/a | Schott SF-6 |
| Certificación | n/a | ANSI Z87-2+, EN 207 CE |
| Vida útil | n/a | `[VALIDAR-KEMMETECH]` (estimado 5+ años) |
| **TCO USD/año estimado** | $0 + riesgo no cuantificado | `[CALCULAR]` |

**Argumento ancla derivable**: el límite ICRP 118 redujo la dosis al cristalino de 150 a 20 mSv/año. Los operadores que no usaban lentes ahora son no-cumplientes.

### Ancla 4 — Programa institucional (jefe de servicio / gerente hospitalario)

| Concepto | Compra reactiva sin programa | Programa Colé institucional |
|---|---|---|
| Costo inicial | Distribuido en el tiempo, no presupuestable | Predecible, presupuestable |
| Trazabilidad | Ninguna o parcial | Sí, por unidad y por usuario |
| Reposición | Reactiva (cuando falla) | Planificada (vida útil + inspección) |
| Riesgo de hallazgo en auditoría MINSA | `[VALIDAR-44653-S]` (alto, no cuantificado) | Bajo (documentación al día) |
| Riesgo de demanda laboral | No mitigado | Mitigado (EPP cumplimiento) |
| **Predictibilidad de costo** | Baja | Alta |

**Argumento ancla derivable**: el programa institucional convierte un gasto reactivo no presupuestable en un costo operativo predecible y auditable. El ROI se materializa al evitar **un solo evento** (multa, demanda, suspensión).

### Ancla 5 — Cumplimiento veterinario (Decreto 44653-S Anexo XIII)

| Concepto | Sin EPP / EPP no certificado | Paquete Colé (delantal + guantes + tiroides + dosimetría + curso) |
|---|---|---|
| Costo USD inicial | $0 a parcial | `[VALIDAR-PAQUETE-VET]` |
| Cumplimiento 44653-S | No | Sí |
| Multa potencial MINSA | `[VALIDAR-44653-S]` | $0 |
| Suspensión de licencia clínica | Posible | No aplica |
| Capacitación POE certificada | n/a | Incluida (curso MINSA) |
| **TCO/año estimado** | `[CALCULAR]` (incluye riesgo de multa) | `[CALCULAR]` |

**Argumento ancla derivable**: el paquete completo de cumplimiento es menor al costo combinado de una multa MINSA + reposición forzada + curso obligatorio comprado por separado.

## Reglas de uso de la tabla TCO en copy

### Lo permitido (con placeholders activos)

- "El TCO/año del delantal Colé Pb Free es competitivo frente al importador genérico cuando se considera la vida útil documentada y la inspección anual."
- "La diferencia de costo/año se mide en dólares, no en cientos."
- "Por una diferencia mensual menor a un café diario, el operador obtiene…"
- Estructura comparativa cualitativa.

### Lo prohibido (mientras placeholders activos)

- Cifras específicas de TCO ($45/año vs $70/año) presentadas como definitivas.
- Promesas de ahorro porcentual ("ahorra 60%").
- Tablas con números completos sin aviso de validación pendiente.
- Comparación competitiva nominal con marca específica del importador.

### Cuándo se libera la tabla con cifras definitivas

Cuando los 5 placeholders críticos estén cerrados:

1. `[VALIDAR-KEMMETECH]` — Vida útil real material Kemmetech.
2. `[VALIDAR-PRECIO-COLE]` — Precio Colé activo en catálogo (ya en Odoo, validar sincronía).
3. `[VALIDAR-BENCHMARK-CR]` — Benchmark de mercado costarricense (3 importadores).
4. `[VALIDAR-44653-S]` — Costo de no-cumplimiento Decreto 44653-S (multa específica).
5. `[VALIDAR-PAQUETE-VET]` — Costo del paquete veterinario combinado.

## Plan de validación documentado

| # | Placeholder | Acción de validación | Responsable | Plazo objetivo |
|---|---|---|---|---|
| 1 | `[VALIDAR-KEMMETECH]` | Solicitar a Kemmetech UK datos de vida útil clínica documentada | Manuel | Antes de campaña madura |
| 2 | `[VALIDAR-PRECIO-COLE]` | Confirmar PV vigente en Odoo (catálogo APPR) | Vanessa | 1 semana |
| 3 | `[VALIDAR-BENCHMARK-CR]` | Estudio de mercado interno: cotizar APPR equivalente a 3 importadores CR | Marco | 2-4 semanas |
| 4 | `[VALIDAR-44653-S]` | Texto oficial decreto + casos públicos de sanción | Asesor legal | Verificar |
| 5 | `[VALIDAR-PAQUETE-VET]` | Configurar paquete combinado en Odoo y validar margen | Vanessa + Manuel | 1-2 semanas |

## Soporte de evidencia técnica para el TCO

Estos respaldan los argumentos de la tabla. Verificar vigencia al redactar.

- **ICRP Pub 103** — Recomendaciones generales de protección radiológica.
- **ICRP Pub 118** — Límite de dosis al cristalino reducido a 20 mSv/año.
- **NCRP Report 168** — Protección radiológica en cardiología intervencionista.
- **IEC 61331-1:2014** — Materiales para protección contra radiación X.
- **IEC 61331-3:2014** — Vestimenta de protección personal.
- **Decreto Ejecutivo 44653-S** — Costa Rica, protección radiológica, Anexo XIII para veterinaria.
- **Klein LW et al.** *JACC* 2015 — Patología musculoesquelética en operadores de cath lab. (Verificar referencia exacta y metanálisis posteriores).
- **Orme NM et al.** *Catheter Cardiovasc Interv* 2015 — Lesiones ortopédicas en cardiólogos intervencionistas. (Verificar).

## Disclaimer interno

Esta tabla TCO es un **marco de argumentación**, no un instrumento contable. Las cifras
finales dependen de variables del cliente (volumen de uso, frecuencia de procedimientos,
nivel de exposición, presupuesto institucional). Toda propuesta cerrada debe pasar por
`odoo-quotation-generator` con cifras del catálogo vigente, no por este skill.
