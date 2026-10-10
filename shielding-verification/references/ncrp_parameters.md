# Parámetros Normativos NCRP para Verificación de Blindaje

## 1. NCRP 147 — RX Convencional (Radiografía + Fluoroscopía)

### 1.1 Carga de Trabajo Normalizada (W_norm) — Tabla 4.7

| Tipo de barrera | W_norm (mAmin/paciente) | Fuente |
|-----------------|------------------------|--------|
| Barreras primarias Bucky (piso) | 0.6 | NCRP 147, Tabla 4.7 |
| Barreras primarias piso/lateral (cross-table) | 1.9 | NCRP 147, Tabla 4.7 |
| Barreras secundarias (todas) | 2.5 | NCRP 147, Tabla 4.7 |

**Carga de trabajo semanal:** W = N × W_norm
- N = número de pacientes por semana (default: 400 para sala de alta ocupación)
- W_Bucky = 400 × 0.6 = 240 mAmin/sem
- W_lateral = 400 × 1.9 = 760 mAmin/sem
- W_secundarias = 400 × 2.5 = 1000 mAmin/sem

### 1.2 Factor de Uso (U) — Tabla 4.6

| Dirección del haz | U | Notas |
|-------------------|---|-------|
| Bucky (hacia el piso) | 1 | 100% del haz dirigido al piso/Bucky |
| Lateral (cross-table) | 0.09 | ~9% del haz en dirección lateral |
| Pared/techo sin Bucky | Variable | Depende de la geometría; verificar caso por caso |
| Secundarias | 1 | Radiación dispersa se emite en todas direcciones |

### 1.3 Factor de Ocupación (T) — Tabla 4.4

| Área adyacente | T | Ejemplos |
|----------------|---|----------|
| Ocupación completa | 1 | Oficinas, consultorios, laboratorios, farmacia, recepción, cuarto de control, áreas de enfermería, zonas de espera permanente |
| Ocupación parcial | 1/5 (0.2) | Pasillos, baños de personal, vestidores, salas de descanso con tránsito frecuente |
| Ocupación ocasional | 1/8 (0.125) | Puertas de acceso, escaleras poco transitadas |
| Ocupación baja | 1/20 (0.05) | Pasillos exteriores, áreas de servicio, azoteas con acceso restringido |
| Ocupación mínima | 1/40 (0.025) | Áreas exteriores, estacionamientos, zonas de tránsito muy bajo, techos inaccesibles |

### 1.4 Límites de Dosis Semanales (P) — §2.3

| Tipo de zona | P (mSv/sem) | P (mSv/año) | Aplica a |
|-------------|-------------|-------------|----------|
| Controlada | 0.1 | 5.0 | TOE (operador, cuarto de control) |
| Supervisada / No controlada (público) | 0.02 | 1.0 | Público, pasillos, salas de espera, oficinas adyacentes |

### 1.5 Técnica de Medición Estándar

| Parámetro | Barreras primarias | Barreras secundarias |
|-----------|-------------------|---------------------|
| kVp | 100 | 100 |
| mAs | 60 (→ 1 mAmin) | 250 (→ 4.17 mAmin) |
| Maniquí | No | Sí (cilindro agua 50×30 cm) |
| DFD | 1 m | 1 m |
| Colimación | 40 × 40 cm | 40 × 40 cm |

---

## 2. NCRP 177 — Dental / Maxilofacial

### 2.1 Carga de Trabajo Normalizada

| Tipo de equipo | W_norm | Unidad |
|---------------|--------|--------|
| Intraoral periapical | 0.15 mAmin/paciente | Por exposición |
| Panorámico | 0.5 mAmin/paciente | Por estudio |
| Cefalométrico | 0.3 mAmin/paciente | Por exposición |
| CBCT maxilofacial | 1.5 mAmin/paciente | Por estudio |

### 2.2 Factor de Uso (U) — Dental

| Equipo | U piso | U paredes | Notas |
|--------|--------|-----------|-------|
| Intraoral | 0.7 | 0.3 | Haz dirigido mayormente hacia abajo |
| Panorámico | N/A (secundarias) | 1 | Fuente rota 360° — todas las barreras son secundarias |
| CBCT | N/A (secundarias) | 1 | Fuente rota — todas secundarias |

### 2.3 Factores T y P

Mismos valores que NCRP 147 (ver sección 1.3 y 1.4 arriba).

---

## 3. NCRP 148 — CT / Radioterapia

### 3.1 CT — Carga de Trabajo

| Parámetro | Valor típico | Notas |
|-----------|-------------|-------|
| N (pacientes/semana) | 300-500 | Variable según volumen |
| CTDI_vol promedio | 15-25 mGy | Depende de protocolo |
| W expresada en DLP | Usar AAPM TG-235 | La carga de trabajo en CT se expresa en DLP/semana |

**Nota:** La verificación de blindaje para CT es más compleja que para RX convencional.
La dosis transmitida depende del espectro, filtración y geometría del gantry. Cuando se
realice verificación empírica de CT, los principios de D_sem aplican con la carga de
trabajo apropiada para CT.

### 3.2 CT — Límites de Dosis

| Tipo de zona | P (mSv/sem) | Mismo que NCRP 147 |
|-------------|-------------|-------------------|
| Controlada | 0.1 | Sí |
| Supervisada | 0.02 | Sí |

---

## 4. Fórmulas de Referencia

### Fórmula de verificación empírica:

```
D_sem = (D_med / mAmin_med) × W × U × T
```

### Variables:

| Variable | Descripción | Unidad |
|----------|------------|--------|
| D_sem | Dosis semanal calculada en el área adyacente | mSv/semana |
| D_med | Dosis integrada medida tras la barrera en una exposición de prueba | mSv |
| mAmin_med | Carga de la medición de prueba | mAmin |
| W | Carga de trabajo semanal | mAmin/semana |
| U | Factor de uso | adimensional |
| T | Factor de ocupación | adimensional |
| P | Límite de dosis permitido | mSv/semana |

### Criterio de aceptabilidad:

```
D_sem ≤ P → ACEPTABLE
D_sem > P → NO ACEPTABLE
```

### Cálculo de capacidad máxima:

```
mAmin_max = P / (D_norm × U × T)
N_pac_max = mAmin_max / W_norm
```

Donde D_norm = D_med / mAmin_med
