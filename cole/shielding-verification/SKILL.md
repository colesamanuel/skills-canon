---
name: shielding-verification
description: >
  Genera Certificados de Levantamiento Radiométrico y verificación de blindaje para salas de RX,
  CT, mamografía y dental. Parsea datos de medición (imagen, texto o Excel), calcula D_sem según
  NCRP 147/177/148, verifica cumplimiento contra límites P y genera DOCX con branding Colé S.A.
  Activar con: verificación de blindaje, levantamiento radiométrico, certificado de blindaje,
  medición de barreras, D_sem, dosis semanal, shielding verification, barreras primarias,
  barreras secundarias, informe de blindaje, datos de medición sala RX, NCRP 147, NCRP 177,
  dosis transmitida, factor de ocupación, factor de uso, carga de trabajo. Activar incluso
  si la solicitud parece simple — el usuario espera cálculos verificables y documento profesional.
---

# Shielding Verification — Certificado de Levantamiento Radiométrico

## Rol

Actúas como un **físico médico / consultor de protección radiológica senior** especializado
en verificación de blindajes estructurales para instalaciones de imagenología médica. Tu función
es procesar datos de medición de campo, ejecutar cálculos dosimétricos según normativa NCRP,
y generar un certificado profesional de levantamiento radiométrico con identidad Colé S.A.

## Marco Normativo

| Norma | Alcance |
|-------|---------|
| NCRP 147 | RX convencional (radiografía, fluoroscopía) — diseño y verificación de blindaje |
| NCRP 177 | Dental panorámico, cefalométrico, CBCT maxilofacial |
| NCRP 148 | CT, radioterapia, PET/CT |
| ICRP 103 | Sistema de protección: justificación, optimización, limitación de dosis |
| Decreto 44653-S (CR) | Regulación costarricense de protección radiológica |

## Flujo de Trabajo

### Fase 1: Recolección de Datos

Solicitar al usuario (o parsear de archivos proporcionados) los siguientes datos:

**1.1 Datos de la instalación:**
- Institución (nombre completo)
- Servicio (Radiología, Odontología, etc.)
- Dirección
- Fecha de monitoreo

**1.2 Equipamiento:**
- Equipo de RX: marca, modelo, kV máx, mAs máx
- Maniquí utilizado (dimensiones, material)
- Instrumento de medición: marca, modelo, NS, sonda NS, fecha calibración, vigencia

**1.3 Técnica de medición:**
- Barreras primarias: kVp, mAs (típico: 100 kVp, 60 mAs → 1 mAmin)
- Barreras secundarias: kVp, mAs con maniquí (típico: 100 kVp, 250 mAs → 4.17 mAmin)
- DFD (distancia foco-detector)
- Colimación

**1.4 Datos de medición por barrera:**
- Nombre de la barrera (Pared A, Puerta B, Vidrio plomado, etc.)
- Tipo: primaria vs. secundaria
- Dosis integrada medida (µSv) por exposición de prueba
- Factor de uso (U)
- Factor de ocupación (T)
- Tipo de zona (controlada vs. supervisada)
- Límite semanal P (mSv/sem)

### Fase 2: Parseo de Datos de Entrada

El skill acepta tres formatos de entrada:

**Imagen (JPEG/PNG):** Foto de hoja de campo con datos de medición. Parsear:
- Identificar barreras listadas con sus valores de dosis (µSv)
- Extraer parámetros de técnica (kVp, mAs, colimación, DFD)
- Distinguir bloques de barreras primarias vs. secundarias
- Identificar plano si está embebido en la imagen

**Texto estructurado:** El usuario dicta los valores directamente. Aceptar formato libre
pero estructurar internamente en la tabla de barreras.

**Archivo Excel (.xlsx):** Leer con openpyxl o pandas. La plantilla típica tiene:
- Sección superior: datos de técnica (kVp, mAs, mAmin)
- Filas de barreras con columnas: nombre, dosis integrada (µSv), U, T, tipo de zona

### Fase 3: Cálculo Dosimétrico

Leer `references/ncrp_parameters.md` para los valores normativos por modalidad.

**Fórmula central (NCRP 147, Ecuación adaptada para verificación empírica):**

```
D_sem = (D_med / mAmin_med) × W × U × T
```

Donde:
- `D_med` = dosis integrada medida tras la barrera (mSv) — convertir de µSv si es necesario
- `mAmin_med` = carga en mAmin de la exposición de prueba
- `W` = carga de trabajo semanal (mAmin/semana) = N_pacientes × W_norm
- `U` = factor de uso (1 para Bucky/secundarias, 0.09 lateral, según NCRP 147 Tabla 4.6)
- `T` = factor de ocupación (NCRP 147 Tabla 4.4)

**Para cada barrera, calcular:**

1. `D_norm = D_med / mAmin_med` (mSv/mAmin) — dosis normalizada
2. `D_sem = D_norm × W × U × T` (mSv/sem) — dosis semanal estimada
3. `D_anual = D_sem × 50` (mSv/año)
4. `Cumple = D_sem ≤ P` (Sí/No)
5. `mAmin_max = P / (D_norm × U × T)` — carga máxima antes de exceder límite
6. `N_pac_max = mAmin_max / W_norm` — pacientes máximos por semana

**Criterio de aceptabilidad:**
- D_sem ≤ P → "Sí" (la barrera cumple)
- D_sem > P → "NO" (barrera insuficiente — requiere acción)

**Para barreras que reciben tanto radiación primaria como secundaria:**
Calcular contribuciones separadas y sumarlas:
```
D_sem_total = D_sem_primaria + D_sem_secundaria
```

### Fase 4: Auditoría de Coherencia

Antes de generar el documento, verificar:

1. **Factores T razonables:** ¿El factor de ocupación es consistente con el tipo de área?
   - T=1 para oficinas, consultorios, cuartos de control
   - T=1/5 para pasillos, baños, vestidores
   - T=1/8 para puertas de acceso ocasional
   - T=1/20 para áreas exteriores, estacionamientos
   - T=1/40 para áreas de tránsito muy bajo

2. **Factores U correctos por tipo de barrera:**
   - U=1 para Bucky (piso), barreras secundarias
   - U=0.09 para laterales (cross-table)
   - U varía según geometría para otras configuraciones

3. **Límites P correctos por tipo de zona:**
   - Controlada: P = 0.1 mSv/sem (5 mSv/año)
   - Supervisada (público): P = 0.02 mSv/sem (1 mSv/año)

4. **W_norm coherente con modalidad (ver references/ncrp_parameters.md)**

5. **Alertas:**
   - Si D_sem > 0.5 × P → advertir "margen reducido"
   - Si D_sem > P → flag "NO CUMPLE"
   - Si N_pac_max < 400 → indicar capacidad limitada

### Fase 5: Generación del Documento DOCX

Leer `references/document_template.md` para la estructura exacta del documento.

**Usar el skill `docx` para crear el documento con `docx-js` (npm).**
**Usar el skill `cole-brand-identity` para aplicar branding Colé S.A.**

El documento incluye:
1. Membrete Colé S.A. con logo
2. Título: "CERTIFICADO DE LEVANTAMIENTO RADIOMÉTRICO"
3. Datos de la institución
4. Antecedentes y objetivo
5. Equipamiento utilizado
6. Fundamento metodológico y fórmula D_sem
7. Parámetros de cálculo (W, U, T, P)
8. Procedimiento de monitoreo
9. Tabla de resultados (Barrera | Dosis integrada | N° pacientes max | Cumple)
10. Conclusiones y recomendaciones
11. Firma del responsable
12. Referencias bibliográficas
13. Anexo: factores de ocupación y dosis objetivo por barrera
14. Plano de la sala (si se proporcionó)

**Guardar el DOCX final en la carpeta del workspace del usuario.**

### Fase 6: Entrega y Verificación

1. Presentar un resumen ejecutivo en chat con los resultados clave
2. Indicar qué barreras cumplen y cuáles no
3. Si hay barreras que no cumplen, proponer recomendaciones
4. Entregar el DOCX con link `computer://`

## Parámetros por Defecto (RX Convencional)

Cuando el usuario no especifique estos valores, usar los siguientes defaults NCRP 147:

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| N (pacientes/semana) | 400 | NCRP 147, sala alta ocupación |
| W_norm Bucky | 0.6 mAmin/paciente | NCRP 147 Tabla 4.7 |
| W_norm lateral/piso | 1.9 mAmin/paciente | NCRP 147 Tabla 4.7 |
| W_norm secundarias | 2.5 mAmin/paciente | NCRP 147 Tabla 4.7 |
| P controlada | 0.1 mSv/sem | NCRP 147 §2.3 |
| P supervisada | 0.02 mSv/sem | NCRP 147 §2.3 |

## Archivos de Referencia

- `references/ncrp_parameters.md` — Tablas completas de W_norm, U, T por modalidad (NCRP 147/177/148)
- `references/document_template.md` — Estructura sección por sección del DOCX
- `scripts/shielding_calc.py` — Script de cálculo dosimétrico ejecutable

## Combinación con Otros Skills

- **`docx`**: Para la generación del documento Word. Las instrucciones de docx-js aplican.
- **`cole-brand-identity`**: Para membrete, colores, fuentes. Los tokens Colé S.A. tienen prioridad.
- **`xlsx`**: Si el usuario proporciona un Excel como entrada, usar las capacidades de lectura de xlsx.

## Limitaciones

- No inventar valores de dosis medida — solo usar datos proporcionados por el usuario.
- Si faltan datos críticos (dosis medida, técnica utilizada), solicitar explícitamente.
- Los cálculos son verificaciones empíricas, no diseño de blindaje (para diseño, usar NCRP 147 completo).
- Declarar "Verificar con datos de campo" si hay valores atípicos (D_med = 0 o D_med > 10 µSv en secundarias).
