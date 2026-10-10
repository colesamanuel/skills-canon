# Fórmulas y Cálculos Hipotecarios — Referencia Operativa

## Tabla de Contenidos
1. Sistemas de Amortización
2. Cálculo de CAE (Costo Anual Equivalente)
3. Análisis de Prepago
4. Análisis de Refinanciamiento
5. Stress Testing
6. Métricas de Cartera
7. Descalce Cambiario
8. Ejemplos Resueltos

---

## 1. Sistemas de Amortización

### 1.1 Sistema Francés (Cuota Fija)

**Fórmula de cuota mensual:**
```
C = P × [r(1+r)^n] / [(1+r)^n - 1]

Donde:
  C = Cuota mensual fija
  P = Principal (monto del préstamo)
  r = Tasa de interés periódica mensual = tasa anual / 12
  n = Número total de pagos mensuales = años × 12
```

**Descomposición de cada cuota k:**
```
Interés(k) = Saldo(k-1) × r
Principal(k) = C - Interés(k)
Saldo(k) = Saldo(k-1) - Principal(k)
```

**Total de intereses:**
```
Total_Intereses = (C × n) - P
```

**Característica clave:** La cuota es constante, pero la proporción interés/principal cambia.
En los primeros años, ~70-80% de la cuota es interés.

### 1.2 Sistema Alemán (Cuota Decreciente)

**Fórmula:**
```
Amortización_fija = P / n
Interés(k) = Saldo(k-1) × r
Cuota(k) = Amortización_fija + Interés(k)
Saldo(k) = P - (Amortización_fija × k)
```

**Característica clave:** Cuotas altas al inicio, decrecientes. Menor costo total de intereses
vs. francés para mismo monto/tasa/plazo, pero requiere mayor capacidad de pago inicial.

**Comparación de costo total (mismo P, r, n):**
- Alemán siempre genera menor total de intereses que Francés
- Diferencia típica: 5-15% menos intereses totales
- Tradeoff: primera cuota del alemán es ~20-30% mayor que la cuota fija del francés

### 1.3 Sistema Americano (Bullet)

**Fórmula:**
```
Cuota(k) = P × r          (para k = 1 a n-1, solo intereses)
Cuota(n) = P × r + P      (último período: intereses + principal completo)
```

**Uso:** Créditos puente, inversionistas con expectativa de venta antes del vencimiento.
**Riesgo:** Si no se vende el activo, el deudor debe pagar el principal completo al vencimiento.

---

## 2. Cálculo de CAE (Costo Anual Equivalente)

### Definición

El CAE es la **TIR anualizada del flujo completo** desde la perspectiva del deudor, incluyendo
TODOS los costos: intereses, comisiones, seguros obligatorios, gastos de formalización.

### Fórmula

Resolver para CAE en:
```
Desembolso_neto = Σ [Cuota_total(k) / (1 + CAE/12)^k]   para k = 1 a n

Donde:
  Desembolso_neto = Monto recibido - gastos de formalización deducidos
  Cuota_total(k) = Cuota capital+interés + prima seguro saldo + prima seguro incendio + comisiones periódicas
```

### Componentes del flujo

**Momento 0 (desembolso):**
```
Flujo_0 = Monto_prestamo - Comisión_formalización - Gastos_legales - Avalúo - Timbres
```

**Cada mes k:**
```
Flujo_k = Cuota_amortización + Seguro_saldo_deudor(k) + Seguro_incendio(k) + Comisiones_mensuales
```

**El CAE captura costos que la tasa nominal no muestra.** Es la ÚNICA métrica válida
para comparar créditos con diferente estructura de costos.

### Implementación Python (referencia)
```python
import numpy as np
from scipy.optimize import brentq

def calcular_cae(monto, gastos_iniciales, cuotas_totales_mensuales, n_meses):
    """
    monto: monto nominal del préstamo
    gastos_iniciales: total de gastos deducidos al momento 0
    cuotas_totales_mensuales: array de n_meses con cuota total mensual (capital+interés+seguros+comisiones)
    """
    desembolso_neto = monto - gastos_iniciales
    
    def npv(tasa_mensual):
        flujos = [-desembolso_neto]
        for k in range(n_meses):
            flujos.append(cuotas_totales_mensuales[k])
        return np.npv(tasa_mensual, flujos)
    
    # Encontrar TIR mensual
    tir_mensual = brentq(lambda r: sum(f / (1+r)**k for k, f in enumerate([-desembolso_neto] + list(cuotas_totales_mensuales))), 0.0001, 0.05)
    
    # Anualizar
    cae = (1 + tir_mensual)**12 - 1
    return cae * 100  # en porcentaje
```

---

## 3. Análisis de Prepago

### 3.1 Prepago parcial — Reducir plazo (cuota constante)

```
Nuevo_n = ceil( -log(1 - Nuevo_saldo × r / C) / log(1 + r) )

Donde:
  Nuevo_saldo = Saldo_actual - Monto_prepago
  C = Cuota actual (se mantiene)
  r = Tasa periódica mensual
```

**Ahorro en intereses:**
```
Ahorro = (C × n_restante_original) - (C × Nuevo_n)
         - Monto_prepago  # el prepago no es "ahorro", es desembolso
```

### 3.2 Prepago parcial — Reducir cuota (plazo constante)

```
Nueva_C = Nuevo_saldo × [r(1+r)^n_restante] / [(1+r)^n_restante - 1]
```

**Ahorro mensual:**
```
Ahorro_mensual = C_original - Nueva_C
```

### 3.3 Comparación de estrategias

| Criterio | Reducir plazo | Reducir cuota |
|----------|--------------|---------------|
| Ahorro total intereses | **Mayor** | Menor |
| Alivio flujo de caja | No | **Sí** |
| Recomendación general | Si capacidad de pago es holgada | Si DTI está al límite |

**Regla:** Siempre recomendar reducir plazo salvo que el DTI del deudor justifique alivio de cuota.

### 3.4 Penalidad por prepago

- Verificar si el contrato incluye penalidad
- CR: la tendencia regulatoria es limitar penalidades de prepago
- Calcular si el ahorro en intereses > penalidad antes de recomendar

---

## 4. Análisis de Refinanciamiento

### 4.1 Condiciones para evaluar refinanciamiento

Evaluar refinanciamiento cuando:
1. Diferencial de tasa ≥ 100 bps (1%)
2. Plazo restante ≥ 5 años (mayor horizonte = mayor ahorro potencial)
3. LTV actual permite mejores condiciones
4. Historial crediticio ha mejorado (mejor categoría CIC)

### 4.2 Cálculo de breakeven

```
Costos_refinanciamiento = Cancelación_hipoteca_actual + Formalización_nueva + Avalúo + Gastos_legales

Ahorro_mensual = Cuota_actual - Cuota_nueva

Breakeven_meses = Costos_refinanciamiento / Ahorro_mensual
```

**Regla de decisión:**
- Breakeven < 24 meses → Refinanciar (alto retorno)
- Breakeven 24-36 meses → Evaluar según planes de permanencia
- Breakeven > 36 meses → Generalmente no conviene

### 4.3 Análisis completo de refinanciamiento

```
VPN_ahorro = Σ [Ahorro_mensual(k) / (1 + d)^k] - Costos_refinanciamiento
             para k = 1 a n_restante

Donde d = tasa de descuento (costo de oportunidad del capital)
```

Si VPN_ahorro > 0 → Refinanciar es valor-positivo.

---

## 5. Stress Testing

### 5.1 Stress de tasa de interés

Para créditos a tasa variable, calcular impacto de incrementos:

```
Para cada escenario s en [+100bps, +200bps, +300bps, +400bps, +600bps]:
    r_stress = r_actual + s/12/100
    C_stress = Saldo × [r_stress(1+r_stress)^n_rest] / [(1+r_stress)^n_rest - 1]
    DTI_stress = (C_stress + Otras_deudas) / Ingreso_bruto × 100
    
    Si DTI_stress > 40% → Señalar como zona de riesgo
    Si DTI_stress > 50% → Señalar como insostenible
```

### 5.2 Stress cambiario (descalce CRC/USD)

```
Para cada escenario de depreciación d en [+10%, +20%, +30%]:
    TC_stress = TC_actual × (1 + d)
    Cuota_CRC_stress = Cuota_USD × TC_stress
    DTI_stress = (Cuota_CRC_stress + Otras_deudas_CRC) / Ingreso_CRC × 100
```

### 5.3 Stress combinado (tasa + tipo de cambio)

Matriz de escenarios cruzados:

```
Para cada combinación (tasa_stress, tc_stress):
    C_USD_stress = recalcular cuota con nueva tasa
    C_CRC_stress = C_USD_stress × TC_stress
    DTI_combinado = (C_CRC_stress + Otras_CRC) / Ingreso_CRC
```

Presentar como heatmap o tabla cruzada.

### 5.4 Interpretación

| DTI resultante | Semáforo | Acción |
|---------------|----------|--------|
| < 35% | 🟢 | Sostenible incluso en stress |
| 35-45% | 🟡 | Requiere plan de contingencia |
| 45-55% | 🟠 | Riesgo significativo — considerar conversión/prepago |
| > 55% | 🔴 | Insostenible — reestructuración urgente |

---

## 6. Métricas de Cartera

### 6.1 Promedio Ponderado de Tasa (WAC)

```
WAC = Σ (Saldo_i × Tasa_i) / Σ Saldo_i
```

### 6.2 Promedio Ponderado de Madurez (WAM)

```
WAM = Σ (Saldo_i × Plazo_restante_i) / Σ Saldo_i
```

### 6.3 Exposición Cambiaria

```
Exposición_USD = Σ Saldos_USD / Σ Todos_los_saldos × 100
```

### 6.4 DTI Agregado

```
DTI_total = Σ (Todas_las_cuotas + Otras_deudas) / Ingreso_total_bruto × 100
```

### 6.5 Score de Salud por Operación

```
Score = f(DTI_individual, LTV_actual, DSCR_si_aplica, Descalce_cambiario, Morosidad)

Pesos sugeridos:
  DTI: 30%
  LTV actual: 25%
  DSCR: 20% (si inversión; si vivienda, redistribuir)
  Descalce: 15%
  Morosidad: 10%
```

---

## 7. Descalce Cambiario

### Cuándo hay descalce

Existe descalce cuando la moneda del ingreso del deudor ≠ moneda del crédito.

**Caso típico CR:** Ingreso en CRC, deuda en USD.

### Métrica de riesgo cambiario

```
Ratio_descalce = Cuota_USD_en_CRC / Ingreso_CRC × 100

Umbral de alerta: > 20% del ingreso expuesto a riesgo cambiario
```

### Estrategias de mitigación

1. **Conversión de moneda:** Renegociar el crédito a CRC (acepta spread mayor pero elimina riesgo FX)
2. **Cobertura natural:** Si parte del ingreso es en USD (exportadores, empleados de multinacionales)
3. **Prepago acelerado:** Reducir saldo expuesto lo antes posible
4. **Reserva de contingencia:** Mantener 6-12 meses de cuotas en USD como buffer

---

## 8. Ejemplos Resueltos

### Ejemplo 1: Cuota mensual sistema francés

**Datos:**
- Monto: $100,000 USD
- Tasa: 8% anual
- Plazo: 20 años

**Cálculo:**
```
r = 0.08 / 12 = 0.006667
n = 20 × 12 = 240
C = 100,000 × [0.006667 × (1.006667)^240] / [(1.006667)^240 - 1]
C = 100,000 × [0.006667 × 4.9268] / [4.9268 - 1]
C = 100,000 × 0.032844 / 3.9268
C = 100,000 × 0.008364
C = $836.44 USD/mes
```

**Total pagado:** $836.44 × 240 = $200,746
**Total intereses:** $200,746 - $100,000 = $100,746

### Ejemplo 2: Impacto de prepago de $10,000

**Contexto:** Mismo préstamo, tras 5 años (60 cuotas pagadas).

**Saldo tras 60 cuotas:**
```
Saldo_60 = 100,000 × [(1.006667)^240 - (1.006667)^60] / [(1.006667)^240 - 1]
Saldo_60 ≈ $90,145
```

**Nuevo saldo tras prepago:** $90,145 - $10,000 = $80,145

**Opción A — Reducir plazo (mantener cuota $836.44):**
```
Nuevo_n = -log(1 - 80,145 × 0.006667 / 836.44) / log(1.006667)
Nuevo_n ≈ 147 meses (vs 180 restantes)
Ahorro = 33 meses × $836.44 = $27,603 en pagos futuros
Ahorro_neto_intereses = $27,603 - $10,000 = $17,603
```

**Opción B — Reducir cuota (mantener 180 meses restantes):**
```
Nueva_C = 80,145 × [0.006667 × (1.006667)^180] / [(1.006667)^180 - 1]
Nueva_C ≈ $765.70
Ahorro_mensual = $836.44 - $765.70 = $70.74/mes
```

**Recomendación:** Opción A ahorra $17,603 adicionales en intereses. Opción B solo si se necesita
alivio de flujo de caja inmediato.

### Ejemplo 3: Breakeven de refinanciamiento

**Situación:**
- Saldo actual: ₡50,000,000
- Tasa actual: TBP + 5% = 11.5%
- Plazo restante: 15 años
- Nueva oferta: TBP + 3.5% = 10% en otro banco
- Costos de refinanciamiento: ₡1,200,000

**Cálculo:**
```
Cuota_actual = ₡598,476
Cuota_nueva = ₡537,433
Ahorro_mensual = ₡61,043
Breakeven = ₡1,200,000 / ₡61,043 = 19.7 meses
```

**Veredicto:** Breakeven < 24 meses → Refinanciar es favorable.
Ahorro total proyectado: (₡61,043 × 180) - ₡1,200,000 = ₡9,787,740
