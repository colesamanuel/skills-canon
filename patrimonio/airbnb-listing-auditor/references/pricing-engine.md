# Motor de precios y ocupación

Cálculos del Pilar C. Usar SIEMPRE los datos reales del titular; los números de ejemplo son ilustrativos.

## Las dos anclas

- **Precio Base:** lo que se cobraría una noche promedio en un mes promedio. Es el número que se ajusta semanalmente.
- **Precio Mínimo:** `gastos fijos por noche + gastos variables por noche + margen mínimo`. No es lo que se quiere cobrar; es el piso antes de ganar $0. Regla práctica: **≈ mitad del Precio Base**. Bloquearlo como piso duro en el motor de precios.

Cálculo del Precio Mínimo (por noche):
```
Fijos/noche      = (hipoteca + seguros + impuestos + servicios base mensuales) / noches_disponibles_mes
Variables/noche  = limpieza por estancia / noches_promedio_estancia + consumibles + utilities variables
Precio Mínimo    = Fijos/noche + Variables/noche + margen_mínimo
```

## Método BLT + Regla del 50%

- **BLT (Booking Lead Time):** días de antelación promedio con que reservan los huéspedes (panel de Airbnb).
- **Objetivo:** a la marca del BLT (ej. 30 días vista), el calendario debería estar ~50% ocupado. Punto de equilibrio de referencia.

### Árbol de decisión semanal (revisión de 30 s)
```
En la marca del BLT (ej. 30 días vista):
  Ocupación real > objetivo  → precios bajos  → SUBIR Precio Base ~10%
  Ocupación real < objetivo  → precios altos  → BAJAR Precio Base ~10%
Repetir semanalmente (auto-corrección).
```

## Corrección ADR-vs-ocupación (aplicar antes de descontar) 🟡

El objetivo de "50%" es occupancy-centric. En mercado sobreofertado (típico 2026), maximizar **RevPAR neto** puede exigir MENOS ocupación a mayor ADR. Antes de bajar precio para llenar, calcular:

```
RevPAR_neto/noche = (ADR × tasa_ocupación) − (costo_limpieza_y_turnover prorrateado por noche disponible)
```

Comparar dos escenarios (precio actual vs precio +X%). Si subir tarifa y perder algunos puntos de ocupación deja **mayor RevPAR neto**, no descontar. El costo de limpieza por turno ($85-150 típico) penaliza la estrategia de "llenar a cualquier precio".

Regla: **ocupación es medio, no fin.** El fin es ingreso neto por noche disponible.

## Personalizaciones

- **Descuento gradual de última hora:** reducción progresiva que arranca en el BLT (ej. 1% a 30 días, subiendo hasta un tope ~30-50% el día previo), en vez de una caída brusca. Se adapta a cómo cae la demanda. **Regla de hierro: nunca por debajo del Precio Mínimo.**
- **Noches huérfanas (orphan days):** si la estancia mínima es 3 y quedan huecos de 1-2 noches entre reservas, permitir automáticamente reservas de 1-2 noches **solo** en esos huecos. Prima opcional 20-25% sobre esas noches. Recupera ingreso que de otro modo quedaría en cero.
- **Flexibilidad de estancia mínima:** menor rigidez → anuncio más "bookable" → mejor visibilidad.

## Herramienta

PriceLabs (control granular, ejecuta BLT y personalizaciones) sobre Smart Pricing nativo (sesgo documentado a ocupación sobre margen; Airbnb cobra comisión por reserva). Hospitable/Hostfully sirven como PMS de mensajería/calendario, no como motor de precios.
