# Plantilla de Briefing Diario

## Tabla de Contenidos
1. Estructura del Briefing
2. Formato del Termómetro de Mercado
3. Formato de Estado del Portafolio
4. Formato de Watchlist
5. Formato del Semáforo de Acción
6. Formato de Eventos del Día
7. Formato de Riesgo Dominante
8. Criterios de Semáforo
9. Ejemplos

---

## 1. Estructura del Briefing

El briefing diario sigue SIEMPRE esta estructura exacta. No reordenar ni omitir secciones.

```
## 📊 BRIEFING — [Día, Fecha]

### 1. TERMÓMETRO DE MERCADO
[Resumen macro 4-5 líneas]

### 2. PORTAFOLIO — Estado de Posiciones
[Tabla de posiciones activas con semáforo]

### 3. WATCHLIST — Candidatos en Radar
[Tabla de candidatos con evaluación]

### 4. 🚦 SEMÁFORO DE ACCIÓN
[Decisiones claras por ticker]

### 5. EVENTOS PRÓXIMOS (24-48h)
[Lista de catalizadores]

### 6. ⚠️ RIESGO DOMINANTE
[El factor #1 del día]

---
**VEREDICTO:** [Una frase directa]

> *Disclaimer estándar*
```

---

## 2. Formato del Termómetro de Mercado

Resumen ejecutivo del estado del mercado. Máximo 5 líneas. Incluir siempre:
- S&P 500: nivel y cambio %
- VIX: nivel y lectura (bajo/moderado/elevado/extremo)
- Crudo WTI: precio y cambio %
- Treasury 10Y: rendimiento
- Sentencia de 1 línea: "Mercado en modo [risk-on/risk-off/indeciso/rotación]"

**Ejemplo:**
```
S&P 500 cerró en 5,870 (-0.8%). VIX en 22.3 — moderadamente elevado.
WTI a $74.50 (+2.1%), Brent $78.20 (+1.8%). Treasury 10Y en 4.15%.
DXY estable en 104.2. Futuros apuntan apertura plana.
Mercado en modo ROTACIÓN — capital saliendo de tech hacia energía y defensivos.
```

---

## 3. Formato de Estado del Portafolio

Tabla obligatoria para cada posición activa:

```
| Ticker | Precio | Cambio | P&L | Semáforo | Nota |
|--------|--------|--------|-----|----------|------|
| CVX    | $187.50| +1.2%  | +3% | 🟢      | Tesis intacta, div 4.5% |
| RTX    | $146.20| -0.5%  | +1% | 🟢      | Contratos defensa sólidos |
| MU     | $82.10 | -2.3%  | -4% | 🟡      | Presión por rotación anti-tech |
```

Para cada posición:
- **Precio:** Cierre del día anterior (o último disponible)
- **Cambio:** Variación vs. día anterior
- **P&L:** Ganancia/pérdida desde entrada (requiere precio de entrada del usuario)
- **Semáforo:** Estado actual según criterios de la sección 8
- **Nota:** Máximo 10 palabras con lo más relevante

Si el usuario no ha confirmado precios de entrada, omitir columna P&L y solicitar datos.

---

## 4. Formato de Watchlist

Tabla para candidatos no comprados aún:

```
| Ticker | Precio | Zona Entrada | Distancia | Semáforo | Catalizador |
|--------|--------|-------------|-----------|----------|-------------|
| ADBE   | $281   | $260-270    | -4% a -8% | 🟡      | Earnings 19/Mar |
| CF     | $95    | $88-92      | -3% a -7% | 🟡      | Fertilizantes + gas |
```

Para cada candidato:
- **Precio:** Último cierre
- **Zona Entrada:** Rango de precios donde la relación riesgo/recompensa es favorable
- **Distancia:** % que falta para llegar a zona de entrada
- **Semáforo:** Si hoy cumple condiciones de entrada o no
- **Catalizador:** Evento o razón que podría mover el precio hacia la zona

---

## 5. Formato del Semáforo de Acción

Esta es la sección más importante. Cada ticker con una línea de acción clara:

```
### 🚦 SEMÁFORO DE ACCIÓN

🟢 **CVX — MANTENER** Tendencia alcista, soporte en $180 respetado. Dividendo ex-date 15/Mar.
🟢 **RTX — MANTENER** En máximos pero tesis estructural vigente. Sin señal de salida.
🟡 **MU — ESPERAR** Bajo presión con sector tech. Soporte crítico en $78. Si pierde, revisar tesis.
🟡 **ADBE — ESPERAR** Acercándose a zona de entrada pero falta confirmación de volumen.
⚪ **BRK.B — SIN SEÑAL** Cotiza en rango estrecho. Sin catalizador inmediato.
🔴 **[ticker] — SALIR** Tesis invalidada por [razón específica]. Stop en $XXX violado.
```

**Regla crítica:** Nunca poner 🟢 con "ENTRAR" a menos que TODAS las condiciones de entrada
del framework técnico se cumplan simultáneamente:
1. Tendencia confirmada (o soporte extremo para largo plazo)
2. Zona de precio favorable (no comprar después de rally de +20%)
3. Ratio riesgo/recompensa ≥ 1:2
4. Sin earnings en próximos 5 días (para swing)
5. VIX no extremo (< 30 para swing trades)

---

## 6. Formato de Eventos del Día

Lista corta de catalizadores relevantes para las próximas 24-48 horas:

```
### EVENTOS PRÓXIMOS
- **08:30 ET** — NFP (Nonfarm Payrolls). Consenso: +180K. Impacto: Fed, tasas, growth vs. value.
- **10:00 ET** — ISM Servicios. Si > 55, confirma expansión.
- **Pre-market** — Earnings COST. Impacto indirecto en consumer defensive.
- **Geopolítico** — Reunión del Consejo de Seguridad ONU sobre Irán. Impacto en crudo y defensa.
```

Solo incluir eventos que afecten directamente al portafolio o watchlist. No listar todo el
calendario económico — solo lo relevante.

---

## 7. Formato de Riesgo Dominante

UN solo riesgo, el más importante del día. No una lista — EL riesgo:

```
### ⚠️ RIESGO DOMINANTE
**Escalada en Estrecho de Ormuz.** Si Irán ataca más petroleros, WTI podría saltar a $95+.
Impacto: CVX sube pero inflación se dispara → Fed hawkish → MU y tech caen fuerte.
Probabilidad estimada: Media-Alta. Monitorear noticias al mediodía.
```

Estructura fija:
- Qué es el riesgo
- Cómo impacta cada posición del portafolio
- Probabilidad subjetiva (Baja / Media / Media-Alta / Alta)
- Qué monitorear

---

## 8. Criterios de Semáforo

### Para POSICIONES ABIERTAS

**🟢 VERDE (Mantener/Acumular):**
- Precio sobre SMA 50 (largo plazo) o sobre EMA 20 (swing)
- Tesis fundamental intacta (sin deterioro de earnings, moat, o guidance)
- Sin noticias negativas materiales
- RSI no en sobrecompra extrema (< 75)
- Flujo de volumen neutral o positivo

**🟡 AMARILLO (Precaución/Vigilar):**
- Precio entre SMA 50 y SMA 200 con momentum decreciente
- Algún dato fundamental cambió pero no invalida tesis
- Noticia relevante que requiere evaluación (no claramente negativa aún)
- RSI en zona de sobrecompra (> 70) o señal de divergencia
- Acercándose a nivel de stop o invalidación

**🔴 ROJO (Considerar salida):**
- Precio rompe SMA 200 al cierre (largo plazo) o pierde soporte clave (swing)
- Tesis fundamental invalidada: earnings miss + guidance recortada, pérdida de moat, cambio regulatorio
- Stop-loss técnico violado
- Correlación adversa: pérdida en esta posición amplifica pérdidas del portafolio
- RSI < 30 combinado con volumen alto (selling climax) — evaluar si es oportunidad o señal de salida

### Para WATCHLIST (candidatos)

**🟢 VERDE (Entrar):**
- Precio dentro de zona de entrada definida previamente
- Todas las condiciones técnicas de entrada cumplidas (ver framework técnico)
- Fundamental sólido: valuación razonable, sin earnings inminentes (swing), tesis clara
- Ratio riesgo/recompensa calculado ≥ 1:2
- Capital disponible suficiente sin sobreconcentrar portafolio

**🟡 AMARILLO (Casi listo):**
- Precio acercándose a zona de entrada pero no la alcanzó
- O está en zona pero falta confirmación (volumen, patrón, indicador)
- O hay un evento próximo que podría dar mejor entrada (earnings, dato macro)
- Explicitar QUÉ FALTA para pasar a verde

**🔴 ROJO (No entrar):**
- Precio muy por encima de zona de entrada (perseguir precios)
- Condiciones de mercado desfavorables (VIX > 30, sector en caída libre)
- Fundamental deteriorado desde última evaluación
- Portafolio ya sobreexpuesto a ese sector

**⚪ GRIS (Sin señal):**
- Datos insuficientes para evaluar
- Mercado lateral sin dirección clara
- Candidato en fase de investigación (no tiene zona de entrada definida aún)

---

## 9. Ejemplos

### Ejemplo de Briefing Completo (Resumido)

```
## 📊 BRIEFING — Lunes, 10 de Marzo 2026

### 1. TERMÓMETRO DE MERCADO
S&P 500 cerró viernes en 5,920 (+0.3%). VIX en 18.5 — moderado.
WTI a $72.30 (-3.5%), retrocediendo tras señales de reapertura parcial de Ormuz.
Treasury 10Y en 4.08%, estable. DXY 103.8.
Mercado en modo CAUTELOSO — alivio geopolítico parcial pero sin convicción.

### 2. PORTAFOLIO
| Ticker | Precio | Cambio | P&L | Semáforo | Nota |
|--------|--------|--------|-----|----------|------|
| CVX    | $179.50| -2.8%  | -1% | 🟡      | Crudo en retroceso, vigilar $175 |
| RTX    | $148.00| +0.5%  | +2% | 🟢      | Tesis defensa intacta |

### 3. WATCHLIST
| Ticker | Precio | Zona Entrada | Distancia | Semáforo | Catalizador |
|--------|--------|-------------|-----------|----------|-------------|
| MU     | $80.50 | $76-80      | En zona   | 🟢      | P/E 13x, AI demand |
| BRK.B  | $518   | $500-515    | -0.6% a -3%| 🟡    | Casi en zona |

### 🚦 SEMÁFORO DE ACCIÓN
🟡 **CVX — VIGILAR** Crudo retrocede. Soporte clave $175. Si pierde, reconsiderar tramo 2.
🟢 **RTX — MANTENER** Flujo de contratos confirmado. Tesis estructural.
🟢 **MU — ENTRAR TRAMO 1** En zona de entrada. P/E 13x, demanda AI sólida.
     → Entrada: $80.50 | Stop: $74 | Target: $95 | Riesgo: $975 (3.25% portafolio)
🟡 **BRK.B — ESPERAR** Falta: caída de 1-3% adicional para zona óptima.

### EVENTOS PRÓXIMOS
- **Martes 08:30** — CPI Febrero. Consenso 2.8% YoY. Si > 3%: golpe a tech, impulso a energy.
- **Miércoles** — Reunión OPEC+ extraordinaria. Podría impactar crudo y CVX.

### ⚠️ RIESGO DOMINANTE
**Dato de inflación CPI martes.** Si sorprende al alza (> 3.0%), la Fed posterga recortes,
tech cae fuerte (MU afectado), pero CVX y RTX se benefician. Monitorear pre-market martes.
Probabilidad de sorpresa al alza: Media (crudo alto en febrero impacta con delay).

---
**VEREDICTO:** Hoy hay oportunidad de ENTRADA en MU (tramo 1). Resto del portafolio estable.
Vigilar CVX si crudo sigue bajando. Esperar CPI martes antes de mover más capital.

> *Este análisis es informativo y no constituye asesoría financiera profesional.*
```
