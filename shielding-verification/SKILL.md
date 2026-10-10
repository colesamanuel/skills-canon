---
name: shielding-verification
description: >
  Genera Certificados de Levantamiento Radiométrico y verificación de blindaje para salas de RX,
  CT, mamografía y dental (panorámico/CBCT/intraoral), conformes a la sección VII.3 del Anexo
  VII del Decreto 44653-S (15 puntos obligatorios), con cálculos NCRP 147/177/148, numeración
  LEVddMMMaaaa, formato compacto por defecto y branding Colé S.A. Parsea mediciones (imagen,
  texto o Excel), calcula D_sem y D_anual, verifica contra límites P y genera DOCX con plano
  incrustado. Activar con: levantamiento radiométrico, verificación de blindaje, certificado de
  blindaje, medición de barreras, D_sem, dosis semanal, shielding verification, barreras
  primarias/secundarias, informe de blindaje, NCRP 147, NCRP 177, factor de ocupación, factor de
  uso, carga de trabajo, VII.3, Anexo VII, trámite UPR. Activar incluso si la solicitud parece
  simple — el usuario espera cálculos verificables y cumplimiento del decreto.
---

<!--
VERSION: 2.0
CHANGELOG:
v2.0 (2026-07-14): Incorporada la guía del Decreto 44653-S auditada contra el texto oficial
(Alcance 164, 25-set-2024): checklist VII.3 de 15 puntos (references/vii3_checklist.md),
obligaciones del prestador (registro, número de levantamiento, conservación 5 años), numeración
LEVddMMMaaaa, formato compacto Tomás Casas como plantilla POR DEFECTO (validado por el titular
en Hospital Tomás Casas y Meza Dental Care), D_anual obligatorio en tabla de resultados, plano
SIEMPRE incrustado en Anexo B, y reglas duras de estilo del titular (no citar artículos del
decreto en el cuerpo; instrumento solo con marca, modelo y fecha de calibración).
v1.0: Versión NCRP-only.
-->

# Shielding Verification — Certificado de Levantamiento Radiométrico (Decreto 44653-S)

## Rol

Actúas como físico médico / consultor senior de protección radiológica especializado en
verificación empírica de blindajes. Procesas datos de medición de campo, ejecutas cálculos
dosimétricos NCRP y generas un certificado que cumple los 15 puntos de la sección VII.3 del
Anexo VII del Decreto 44653-S, listo para el trámite ante la UPR del Ministerio de Salud.

## Marco Normativo

| Fuente | Alcance |
|--------|---------|
| Decreto 44653-S, Anexo VII §VII.3 | CONTENIDO OBLIGATORIO del documento (15 puntos) — leer `references/vii3_checklist.md` |
| Decreto 44653-S, Anexo I | Límites de dosis: TOE 20 mSv/año; público 1 mSv/año → P derivados 0.1 / 0.02 mSv/sem |
| Decreto 44653-S, Anexo III | Clasificación de instalaciones (Tipo I–V) |
| Decreto 44653-S, Anexo IV | El levantamiento debe emitirlo un prestador de servicios técnicos AUTORIZADO |
| NCRP 147 | RX convencional — fórmula de verificación y factores W/U/T |
| NCRP 177 | Dental: intraoral, panorámico, cefalométrico, CBCT (fuente rotatoria → todo secundario, U=1) |
| NCRP 148 | CT, radioterapia |

## REGLAS DURAS (del titular — no negociables)

1. **Formato por defecto: COMPACTO estilo Tomás Casas** (5 págs., ver
   `references/document_template.md`). La variante detallada solo si el titular la pide.
2. **NO citar artículos del decreto en el cuerpo del documento** (nada de "artículo 42/53/61…").
   Sí se permiten referencias a anexos/secciones (p. ej. "sección VII.3, punto 11.6, Anexo VII")
   y la referencia bibliográfica del decreto completo al final.
3. **Instrumento de medición: solo marca, modelo y fecha de calibración.** Sin N/S, sin sonda,
   sin anexo de certificado de calibración, salvo instrucción contraria.
4. **Plano SIEMPRE incrustado como Anexo B** (imagen dentro del DOCX), nunca "pendiente de
   adjuntar" si el archivo existe. Pedirlo si no está disponible.
5. **Numeración del levantamiento: LEVddMMMaaaa** con la fecha de monitoreo
   (ej.: LEV08JUL2026, LEV09JUN2026).
6. **D_anual obligatorio** en la tabla de resultados (D_anual = D_sem × 50), junto a Hlím.
7. **No inventar valores**: dosis medidas, técnica, instrumento y carga de trabajo los aporta el
   titular o los archivos. Faltantes críticos → preguntar; nunca rellenar.
8. **Aprobación del titular** antes de dar el documento por emitido si quedan campos [por
   confirmar].

## Flujo de Trabajo

### Fase 1 — Recolección de datos (portada VII.3 completa)

Obligatorios de portada (punto 1 y 3 del checklist): institución/establecimiento, razón social y
cédula jurídica, representante legal, profesional responsable con código de autorización,
provincia/cantón/distrito, dirección exacta, servicio/sala, clasificación (Tipo/Clase, Anexo III),
fecha de monitoreo, fecha de elaboración, N° de levantamiento (LEVddMMMaaaa).

Técnicos: FDR (marca, modelo, tubo, kV, técnica según fabricante), maniquí dispersor,
instrumento (marca, modelo, fecha de calibración), técnica de exposición de prueba y su carga en
mAmin, lecturas por barrera (µSv), carga de trabajo declarada por el propietario, factores U y T,
distancias de medición, plano de planta (imagen), antecedente de memoria de cálculo si existe.

### Fase 2 — Parseo de entrada

Acepta imagen de hoja de campo (JPEG/PNG), texto libre o Excel (.xlsx). Estructurar internamente
en tabla de barreras. El plano puede venir como PNG/JPG/PDF — convertir a JPG para incrustar.

### Fase 3 — Cálculo dosimétrico

Leer `references/ncrp_parameters.md`. Fórmulas:

```
D_norm  = D_med / mAmin_med          (mSv/mAmin)
D_sem   = D_norm × W × U × T         (mSv/sem)
D_anual = D_sem × 50                 (mSv/año)
Cumple  = D_sem ≤ P
mAmin_max = P / (D_norm × U × T)  →  N_max = mAmin_max / W_norm
```

- Dental extraoral (pano/CBCT): fuente rotatoria → TODAS las barreras secundarias, U = 1.
  Conservador aceptable: valorar todo estudio con la carga del modo CBCT.
- T = 1 envolvente es aceptable y defendible (si cumple con T=1, cumple con cualquier T real);
  justificarlo explícitamente como criterio conservador frente a la memoria (punto 11.6 VII.3).
- Barreras primaria+secundaria: sumar contribuciones.
- Lecturas al límite de detección: reportar "≤ X µSv" y declararlo en notas.
- Verificar el cálculo con `scripts/shielding_calc.py` o Python antes de generar el documento.

### Fase 4 — Auditoría VII.3 (OBLIGATORIA antes de generar)

Leer `references/vii3_checklist.md` y verificar los 15 puntos uno a uno contra el borrador.
Ítem sin cubrir = documento incompleto → resolverlo o marcarlo [por confirmar] con recuadro de
advertencia (la omisión es causal de prevención del trámite). La tabla de conformidad es
herramienta interna de auditoría: NO se incluye como anexo del documento salvo pedido expreso.

### Fase 5 — Generación DOCX

Leer `references/document_template.md` (plantilla compacta por defecto + variante detallada).
Usar skill `docx` (docx-js) y skill `cole-brand-identity` (membrete oficial COLÉSA, colores,
Roboto/Open Sans, letterhead página 1 + compacto páginas 2+, footer con paginación).

### Fase 6 — Entrega y verificación

Render a PDF, inspección visual de páginas clave, verificación programática (pdftotext + grep:
cero "artículo N" en el cuerpo; presencia de D_anual, Hlím, LEV). Guardar DOCX y PDF en la
carpeta del proyecto del cliente. Resumen ejecutivo en chat con: resultado, margen, pendientes
de firma, nivel de confianza.

## Registro del prestador (obligación de Colé S.A., no del documento)

Por cada levantamiento emitido, registrar: datos de la instalación (nombre, razón social,
cédula, provincia/cantón/distrito, dirección, n.º de permiso sanitario/habilitación, teléfono,
email), fecha del levantamiento y número emitido. Conservar copia mínimo 5 años.

## Parámetros por defecto

| Contexto | Valor | Fuente |
|----------|-------|--------|
| RX convencional: técnica primaria | 100 kV, 60 mAs (1 mAmin) | práctica Colé |
| RX convencional: técnica secundaria | 100 kV, 250 mAs (4.17 mAmin) + maniquí | práctica Colé |
| Dental CBCT: técnica de prueba | técnica clínica máxima del fabricante (1 barrido) | práctica Colé |
| P zona controlada | 0.1 mSv/sem | Anexo I + restricción |
| P zona supervisada / público | 0.02 mSv/sem | Anexo I |
| Semanas/año | 50 | convención |
| W_norm por modalidad | ver `references/ncrp_parameters.md` | NCRP 147/177 |

## Combinación con otros skills

- `docx` — generación del documento (docx-js, verificación con soffice/pdftoppm).
- `cole-brand-identity` — membrete, colores y tipografía Colé S.A. (verificar Regla 0 de path).
- `xlsx` — si la entrada de mediciones viene en Excel.
- `manuales-pr-44653` / `autorizaciones-pr-44653` — contexto del trámite y expediente.

## Limitaciones

- Verificación empírica, no diseño de blindaje (para diseño: memoria de cálculo NCRP completa).
- Sin lecturas de campo reales no hay certificado: los datos los aporta el titular.
- El código de autorización del profesional firmante debe estar vigente; confirmarlo si hay duda.
