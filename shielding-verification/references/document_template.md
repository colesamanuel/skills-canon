# Plantilla del Certificado de Levantamiento Radiométrico
## Formato COMPACTO (por defecto — validado en Hospital Tomás Casas y Meza Dental Care, jul-2026)

Generar con docx-js (skill `docx`) + branding Colé S.A. (skill `cole-brand-identity`:
letterhead COLÉSA página 1, encabezado compacto páginas 2+, línea azul #3155e2, footer con
paginación). Letter, márgenes 1". Cuerpo Open Sans 10.5pt; H1 Roboto Bold azul; tablas con
encabezado azul/texto blanco y filas alternas #eeeef2. Extensión objetivo: 4–6 páginas.

REGLA DE ESTILO: no citar artículos del decreto en el cuerpo (sí anexos/secciones, p. ej.
"sección VII.3, punto 11.6, Anexo VII del Decreto 44653-S", y el decreto completo en referencias).

## Estructura

### Título
**CERTIFICADO DE LEVANTAMIENTO RADIOMÉTRICO** (Roboto Bold, centrado)

### Portada — líneas con etiqueta en negrita (sin tabla)
- **N° de levantamiento:** LEVddMMMaaaa (fecha de monitoreo; ej. LEV08JUL2026)
- **Institución:** …
- **Razón social / Propietario:** … — Cédula Jurídica …
- **Representante legal:** …
- **Servicio:** … (sala evaluada y modalidad)
- **Ubicación:** Provincia: … · Cantón: … · Distrito: …
- **Dirección exacta:** …
- **Profesional responsable:** Ing. … — Código de autorización …
- **Fecha de monitoreo:** … / **Fecha de elaboración:** …

### Índice de Contenidos
Lista simple: secciones 1–7 + Anexos A y B.

### 1. Antecedentes y Objetivo de la Medición
Párrafo único: quién opera qué equipo, quién contrató la verificación, para qué (protección TOE
y público), y el antecedente de la memoria de cálculo de blindaje (autor y fecha) como
referencia del levantamiento.

### 2. Equipamiento Utilizado (3 bullets)
- **Equipo de RX (FDR):** marca, modelo, tubo, kV máx., modalidades (según fabricante).
- **Maniquí:** descripción del dispersor y su propósito.
- **Instrumento de Medición:** MARCA, MODELO — Fecha de calibración: … (SOLO estos datos).

### 3. Fundamento Metodológico y Formulación
Párrafo "Deber Ser vs Ser". Luego:

**3.1. Dosis Semanal Calculada (D_sem)** — fórmulas centradas en monoespaciada:
`D_sem = ( D_med / mAmin_med ) × W × U × T    D_anual = D_sem × 50`
Tabla de variables (2 columnas: Variable | Descripción; 7 filas: D_sem, D_anual, D_med,
mAmin_med, W, U, T).

**3.2. Parámetros de Cálculo** — párrafos con etiqueta en negrita:
- **Carga de Trabajo (W):** N declarado por el propietario × W_norm; mostrar el W resultante.
  (RX convencional: tabla de 3 filas Bucky/lateral/secundarias como en Tomás Casas; dental:
  una línea con el criterio conservador CBCT.)
- **Factor de Uso (U):** valores por tipo de barrera (dental rotatorio: U=1 todas).
- **Factor de Ocupación (T):** valores por local, o T=1 envolvente con su justificación.
- **Límites de Dosis Permitidos (P):** 0.1 controlada / 0.02 supervisada-público, derivados del
  Anexo I del Decreto 44653-S.
- **Criterio de Aceptabilidad:** D_sem ≤ P.
- **Consistencia con la memoria de cálculo:** parámetros idénticos o más conservadores;
  justificar cualquier diferencia (sección VII.3, punto 11.6, Anexo VII).

### 4. Procedimiento de Monitoreo
- **Inspección Visual:** barreras libres de grietas/defectos.
- **Puntos y distancias de medición:** puntos según memoria/plano (letras mayúsculas), posición
  del detector (~0.3 m tras barrera; distancias reales a piso/techo), referencia al Anexo B.
- **Técnica(s) de exposición:** kV, mAs/mA·s efectivos y carga en mAmin por exposición de
  prueba (primaria y secundaria si aplica; dental: barrido único a técnica clínica máxima).

### 5. Resultados del Monitoreo y Cálculo de Dosis
Párrafo introductorio + **Tabla 1. Lecturas, cálculo de dosis semanal y anual, y capacidad**
Columnas: Barrera | Dosis integrada (µSv) | D_sem (mSv/sem) | D_anual (mSv/año) |
Hlím (mSv/sem) | Capacidad (pac o est/sem) | Cumple
- Notación científica (2.0×10⁻⁴). Lecturas al límite de detección: "≤ 0.01".
- **Notas** al pie de tabla: criterio conservador ante lecturas múltiples/límite de detección,
  suma primaria+secundaria cuando aplique, técnica utilizada, y el cálculo ejemplo.
- Si piso/techo no se midieron: párrafo de **Alcance** declarándolo y comprometiendo medición
  complementaria (punto 10 de la sección VII.3).

### 6. Conclusiones y Recomendaciones
- Veredicto: todas las barreras (indicar si incluye piso/techo) cumplen; margen %; capacidad;
  consistencia con la memoria.
- Cláusula de aplicabilidad: condiciones especificadas; repetir ante modificación estructural,
  cambio de FDR, cambio de uso de colindancias o aumento de carga.
- **Profesionales que realizaron las mediciones, cálculos y elaboración del informe:**
  bullet con nombre — código de autorización — Firma: ______________

### 7. Referencias Bibliográficas
[1] Decreto Ejecutivo N° 44653-S, Reglamento sobre Protección y Seguridad Radiológica,
Alcance N° 164 a La Gaceta, 25-set-2024. [2] NCRP 147. [3] NCRP 177 (si dental). [4] ARCAL XX,
OIEA. [5] Memoria de cálculo de blindaje (autor, fecha).

### Anexo A: Factores de Ocupación y Dosis Objetivo por Barrera
Tabla: Barrera | Ubicación (colindancia real) | Tipo de Zona (Controlada/Supervisada) | T | U |
Hlím (mSv/sem). Nota al pie si T=1 envolvente.

### Anexo B: Plano de planta — zonas y puntos de medición
Imagen del plano INCRUSTADA (ancho ~580 px, mantener proporción) + leyenda: ZC/ZS, letras de los
puntos, ubicación de la FDR, y qué hay en niveles superior/inferior.

## Variante DETALLADA (solo bajo pedido del titular)

Añade a la compacta: portada en tabla de 2 columnas con clasificación de la instalación y
permiso sanitario; sección de especificaciones FDR ampliada (filtración, geometría,
foco-isocentro); tabla de variables con columnas Valor y Justificación (incluye F_cal y factor
de transmisión); sección separada de análisis de consistencia con la memoria; conclusiones en
bullets. Extensión típica 8–9 páginas. La tabla de conformidad VII.3 es SOLO auditoría interna.

## Verificación antes de entregar

1. `soffice --convert-to pdf` + `pdftoppm` + inspección visual de portada, tabla y anexos.
2. `pdftotext | grep -ioE "artículo[s]? [0-9]+"` → debe devolver vacío.
3. Confirmar presencia de: LEV, D_anual, Hlím, firma, plano.
4. Cotejar los 15 puntos de `vii3_checklist.md`.
