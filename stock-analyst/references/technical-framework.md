# Framework de Análisis Técnico

## Tabla de Contenidos
1. Identificación de Tendencia
2. Soportes y Resistencias
3. Indicadores Principales
4. Indicadores Secundarios
5. Análisis de Volumen
6. Patrones de Precio
7. Reglas Operativas — Swing Trading
8. Reglas Operativas — Largo Plazo
9. Position Sizing
10. Gestión de Riesgo

---

## 1. Identificación de Tendencia

La tendencia es el factor #1. No operar contra la tendencia primaria.

**Medias móviles para clasificar tendencia:**

| Tendencia | Condición | Interpretación |
|-----------|-----------|---------------|
| Alcista fuerte | Precio > EMA 20 > SMA 50 > SMA 200 | Todas alineadas — máximo momentum |
| Alcista | Precio > SMA 50 > SMA 200 | Tendencia sana, posible consolidación |
| Neutral | SMA 50 ≈ SMA 200, precio oscila | Sin dirección — evitar swing trades direccionales |
| Bajista | Precio < SMA 50 < SMA 200 | No operar long en swing, solo evaluar para largo plazo en soporte extremo |

**Cruces relevantes:**
- Golden Cross: SMA 50 cruza al alza SMA 200 — señal alcista de mediano plazo
- Death Cross: SMA 50 cruza a la baja SMA 200 — señal bajista, precaución extrema en longs

**Regla operativa:**
- Swing trading: solo long cuando precio > SMA 50 Y SMA 50 > SMA 200
- Largo plazo (acumulación): puede considerar compras cuando precio está por debajo de SMA 200
  si el análisis fundamental es sólido y hay soporte técnico importante

## 2. Soportes y Resistencias

**Niveles horizontales:**
- Máximos/mínimos previos significativos (daily y weekly)
- Zonas de alta concentración de volumen (Volume Profile si disponible)
- Números redondos psicológicos ($50, $100, $200, etc.)

**Niveles dinámicos:**
- SMA 50, SMA 200 como soporte/resistencia dinámica
- EMA 20 como soporte en tendencias fuertes

**Fibonacci:**
- Retrocesos desde el swing más reciente significativo
- Niveles clave: 38.2%, 50%, 61.8%
- Zona de "Golden Pocket": 61.8%-65% — zona óptima de compra en retroceso
- Solo usar si el swing previo es claro y significativo (>15% de rango)

**Regla de validación:**
- Un nivel es más fuerte cuando coinciden 2+ tipos de soporte/resistencia (confluencia)
- Un nivel se fortalece con cada testeo que respeta, pero se debilita si es testeado demasiadas veces en poco tiempo

## 3. Indicadores Principales

### RSI (Relative Strength Index) — Período 14

| RSI | Interpretación |
|-----|---------------|
| > 70 | Sobrecompra — no es señal de venta automática, pero precaución para entradas nuevas |
| 50-70 | Zona alcista — momentum positivo |
| 30-50 | Zona bajista — momentum negativo |
| < 30 | Sobreventa — potencial rebote, especialmente si coincide con soporte |

**Divergencias (la señal más valiosa del RSI):**
- Divergencia bajista: precio hace nuevo máximo, RSI no → debilitamiento de momentum
- Divergencia alcista: precio hace nuevo mínimo, RSI no → posible reversión al alza
- Divergencia oculta alcista: precio hace mínimo más alto, RSI hace mínimo más bajo → continuación alcista
- Divergencias solo son válidas en zonas extremas (>65 o <35)

### MACD (12, 26, 9)

- **Cruce de señal:** Línea MACD cruza signal line — señal de cambio de momentum
  - Cruce al alza por debajo de 0: señal de compra más fuerte
  - Cruce a la baja por encima de 0: señal de venta más fuerte
- **Histograma:** Expansión = momentum creciente, contracción = momentum decreciente
- **Divergencias:** Misma lógica que RSI pero en MACD — muy potentes cuando coinciden

### ATR (Average True Range) — Período 14

No es indicador direccional — es de volatilidad.

Usos:
- **Stop-loss:** Stop = Precio entrada - (1.5 a 2.0 × ATR)
- **Target:** Target mínimo = Precio entrada + (3.0 × ATR) para ratio 1:2 con stop de 1.5 ATR
- **Position sizing:** ATR alto = posición más pequeña para mismo riesgo en $
- **Filtro de operación:** ATR extremadamente bajo puede indicar compresión antes de movimiento fuerte

## 4. Indicadores Secundarios

Usar para confirmación — nunca como señal primaria.

- **Bollinger Bands (20, 2):** Precio tocando banda inferior en tendencia alcista = potencial compra
  en pullback. Squeeze (bandas estrechas) = volatilidad comprimida, movimiento fuerte inminente.
- **Stochastic (14, 3, 3):** Útil en rangos laterales. Sobrecompra/sobreventa con cruces para timing.
- **ADX (14):** > 25 = tendencia fuerte (bueno para swing), < 20 = rango (evitar swing direccional).

## 5. Análisis de Volumen

El volumen confirma o niega el precio. Precio sin volumen es sospechoso.

**Reglas:**
- Breakout de resistencia con volumen > 50% del promedio → confirmación fuerte
- Breakout con volumen bajo → alta probabilidad de fakeout
- Rally con volumen decreciente → distribución, debilitamiento
- Caída con volumen decreciente → selling exhaustion, posible suelo
- Volumen excepcionalmente alto en un día = "climax" — puede marcar giro

**OBV (On Balance Volume):**
- OBV subiendo mientras precio lateral = acumulación → alcista
- OBV cayendo mientras precio lateral = distribución → bajista
- Divergencia entre OBV y precio es señal temprana de cambio

## 6. Patrones de Precio

Usar con cautela. Solo operar patrones cuando son inequívocos.

**Patrones de continuación (en tendencia alcista, para swing long):**
- Bull flag / pennant: consolidación estrecha después de movimiento fuerte
- Cup and handle: formación redondeada con retroceso menor
- Ascending triangle: mínimos ascendentes contra resistencia horizontal

**Patrones de reversión (para identificar suelos en largo plazo):**
- Double bottom / W pattern: testeo de soporte con divergencia alcista
- Inverse head and shoulders: cambio de estructura de mínimos descendentes
- Morning star (velas): en soporte clave con volumen

**Regla:** Un patrón sin confirmación de volumen no es un patrón — es ruido.

## 7. Reglas Operativas — Swing Trading

### Criterios de Entrada (deben cumplirse todos)
1. Tendencia alcista confirmada (precio > SMA 50 > SMA 200)
2. Pullback a soporte identificado (EMA 20, SMA 50, Fibonacci, o horizontal)
3. Señal de rebote: vela de reversión, divergencia RSI, o cruce MACD
4. Volumen: disminuyó en el pullback, aumenta en el rebote
5. Ratio riesgo/recompensa ≥ 1:2 (idealmente 1:3)

### Parámetros de Trade
```
Entrada:     [Precio específico o rango estrecho]
Stop-loss:   [Precio] = Entrada - (1.5-2.0 × ATR) o debajo del soporte técnico
Target 1:    [Precio] — parcial (50% de posición)
Target 2:    [Precio] — trailing stop con EMA 20 para el resto
Timeframe:   [3-20 días típico]
Riesgo:      [1-2% del portafolio]
Posición:    [# acciones calculado por position sizing]
```

### Gestión durante el Trade
- Si llega a Target 1: cerrar 50%, mover stop a breakeven
- Si rompe EMA 20 al cierre: cerrar resto
- Si el fundamento cambia (earnings miss, noticia negativa material): cerrar sin importar nivel técnico
- Máximo 3-4 swing trades simultáneos para mantener control

### Criterios de NO Entrada
- Earnings report en los próximos 5 días (riesgo de gap)
- VIX > 30 (volatilidad extrema distorsiona técnicos)
- Sin volumen en el activo (spread amplio, ejecución difícil)
- Contra la tendencia primaria

## 8. Reglas Operativas — Largo Plazo

### Criterios de Acumulación
1. Tesis fundamental sólida (moat, crecimiento, valuación razonable)
2. Precio en zona técnica favorable (soporte mayor, sobreventa extrema, o valuación históricamente baja)
3. Sin deterioro fundamental (earnings, márgenes, deuda estables o mejorando)

### Gestión de Posición
- No usar stop-loss rígido — usar invalidación de tesis
- Acumular en tramos: no entrar con 100% de la posición target de una vez
  - Tramo 1: 30-40% en zona de entrada inicial
  - Tramo 2: 30-40% si cae a segundo nivel de soporte y tesis se mantiene
  - Tramo 3: 20-30% restante si oportunidad excepcional (crash sectorial, sobreventa extrema)
- Revisar tesis trimestralmente coincidiendo con earnings
- Señales de salida: deterioro de moat, pérdida de pricing power, management questionable,
  3+ trimestres de miss en earnings sin plan claro

## 9. Position Sizing

**Fórmula base:**
```
Riesgo en $ = Capital total × % riesgo por trade (1-2%)
Acciones = Riesgo en $ / (Precio entrada - Stop loss)
Valor de posición = Acciones × Precio entrada
% del portafolio = Valor de posición / Capital total
```

**Ejemplo:**
```
Capital: $100,000
Riesgo por trade: 1.5% = $1,500
Entrada: $150
Stop: $142 (diferencia = $8)
Acciones: $1,500 / $8 = 187 acciones
Valor posición: 187 × $150 = $28,050 = 28% del portafolio
```

**Límites:**
- Máximo 25-30% del portafolio en una sola posición (swing)
- Máximo 40% en un solo sector
- Si el sizing resulta > 30% del portafolio, reducir tamaño o ampliar stop

## 10. Gestión de Riesgo — Portafolio

**Reglas de exposición:**
- Máximo capital en swing trades simultáneos: 60% del portafolio
- Siempre mantener 10-20% en cash o equivalentes para oportunidades
- Si 2 swing trades consecutivos dan stop, pausar 48h y reevaluar condiciones de mercado

**Correlación:**
- Evitar 3+ posiciones swing en el mismo sector (correlación amplifica pérdidas)
- Considerar beta del portafolio: si todas las posiciones son high-beta, el riesgo real es mayor al nominal
- En entorno de VIX elevado (>25), reducir tamaño de posiciones un 30-50%

**Registro:**
- Documentar cada trade: entrada, stop, target, tesis, resultado
- Revisar win rate y ratio promedio ganancia/pérdida mensualmente
- Si win rate cae por debajo de 40% con ratio 1:2, revisar proceso de selección
