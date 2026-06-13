# Plantilla del Documento — Certificado de Levantamiento Radiométrico

## Estructura del DOCX

El documento DOCX debe generarse con `docx-js` (npm) siguiendo la estructura exacta
descrita a continuación. Usar el skill `docx` para las instrucciones de docx-js y
el skill `cole-brand-identity` para los tokens de marca.

---

## Sección 0: Encabezado (Header de todas las páginas)

**Layout:**
- Logo Colé S.A. (esquina superior izquierda, ~180px ancho)
- A la derecha del logo, texto corporativo:
  - Línea 1: **INVERSIONES E IMPORTACIONES COLE S.A.** (bold, 11pt)
  - Línea 2: SERVICIOS DE PROTECCIÓN RADIOLÓGICA. VENTA DE EQUIPOS Y ACCSESORIOS (9pt, azul #3155e2)
  - Línea 3: Cédula Jurídica: 3-101-392010 (8pt, gris)
  - Línea 4: Teléfono: (506) 2285 3211 / 2285 9561   Fax: (506) 2245 3283 (8pt)
  - Línea 5: Celular/whatsapp: (506) 8395 7547 / 6050 0161 (8pt)
  - Línea 6: Web: www.colecr.com   Email: colesa.manuel@gmail.com (8pt)
  - Línea 7: Dirección: Del BCR 125m Este, Calle de Piedra, Zapote. San José, Costa Rica (8pt)
- Línea horizontal azul #3155e2 debajo

## Sección 1: Título y Datos Generales

**Título:** CERTIFICADO DE LEVANTAMIENTO RADIOMÉTRICO
- Font: Roboto Bold, 18pt, negro
- Centrado, con espacio superior

**Tabla de datos:**
| Campo | Valor |
|-------|-------|
| Institución: | {nombre_institucion} |
| Servicio: | {servicio} |
| Dirección: | {direccion} |
| Fecha Monitoreo: | {fecha_monitoreo} |

Los labels en bold, los valores en regular.

## Sección 2: Antecedentes y Objetivo de la Medición (Heading azul)

Texto estándar (adaptar nombre de empresa contratante):

> {empresa_contratante} instaló en la Institución un equipo de RX Convencional y contrató
> a nuestra Empresa para certificar que el blindaje actual es suficiente para la protección
> de Trabajadores Ocupacionalmente Expuestos (TOE) y Público en general.

## Sección 3: Equipamiento Utilizado (Heading azul)

Lista con bullets:
- **Equipo de RX:** {marca} {modelo} con kV máx. {kv_max} y mAs máx. {mas_max}
- **Maniquí:** {descripcion_maniqui}
- **Instrumento de Medición:** {marca_instrumento} {modelo_instrumento} NS {ns_instrumento}
  sonda {ns_sonda} — Fecha calibración: {fecha_cal} — Vigencia: {vigencia_cal}

## Sección 4: Fundamento Metodológico y Formulación (Heading azul)

Párrafo introductorio:
> El propósito de este informe es realizar una verificación de blindaje, un proceso técnico
> que valida si las barreras de protección cumplen con los límites de dosis normativos. La
> conclusión sobre la idoneidad del blindaje se obtiene al comparar un cálculo teórico (El
> Deber Ser) con una medición empírica de la condición real (El Ser). El blindaje se
> considera seguro si la dosis medida es inferior al límite calculado.

### 4.1 Dosis Semanal Calculada (D_sem)

Fórmula (insertar como imagen o texto formateado):
```
D_sem = (D_med / mAmin_med) × W × U × T
```

Tabla de variables:
| Variable | Descripción |
|----------|------------|
| D_sem | Dosis semanal calculada en el área adyacente (mSv/semana) |
| D_med | Dosis integrada medida tras la barrera en una exposición de prueba (mSv) |
| mAmin_med | Carga de la medición de prueba (mAmin) |
| W | Carga de trabajo semanal (mAmin/semana) |
| U | Factor de uso (adimensional) |
| T | Factor de ocupación (adimensional) |

### 4.2 Parámetros de Cálculo

**Carga de Trabajo (W):** Se asume una sala de alta ocupación con **{n_pacientes}
pacientes/semana**.
- W = N ({n_pacientes} pacientes/semana) × W_norm (mAmin/paciente)

Tabla de W por tipo:
| Tipo de Barrera | W_norm (mAmin/paciente) | W total (mAmin/semana) |
|-----------------|------------------------|----------------------|
| Barreras primarias Bucky | {w_norm_bucky} | {w_bucky} |
| Barreras primarias piso/lateral | {w_norm_lateral} | {w_lateral} |
| Barreras secundarias (todas) | {w_norm_sec} | {w_sec} |

**Factor de Uso (U):**
- Primaria (Bucky): 1
- Primaria (Lateral): 0.09
- Secundaria: 1

**Factor de Ocupación (T):**
- Oficinas / Áreas controladas: 1
- Baños / Vestidores / Pasillos: 1/5
- Pasillos (menor ocupación): 1/5

**Límites de Dosis Permitidos (P):**
- Áreas controladas: 0.1 mSv/semana
- Áreas no controladas/público: 0.02 mSv/semana

**Criterio de Aceptabilidad:** La barrera es aceptable si D_sem ≤ P.

## Sección 5: Procedimiento de Monitoreo (Heading azul)

1. **Inspección Visual:** Se verificó que todas las barreras estructurales (paredes,
   puerta, ventana) están libres de grietas o defectos.
2. **Medición de Atenuación:** Se midió la dosis integrada en los puntos A hasta {ultimo_punto}
   (ver plano adjunto) para verificar que los niveles de radiación son inferiores a los
   valores objetivo.
   - **Técnica Primaria:** {kv_primaria} kV, {mas_primaria} mAs.
   - **Técnica Secundaria:** {kv_secundaria} kV, {mas_secundaria} mAs con maniquí para
     simular dispersión.

## Sección 6: Resultados del Monitoreo (Heading azul)

Párrafo:
> No se encontraron defectos visibles en la inspección visual. La Tabla 1 resume los
> resultados de las mediciones y la capacidad de pacientes.

**Tabla 1. Resultados de Mediciones y Capacidad de Pacientes**

| Barrera | Dosis integrada transmitida Primaria/Secundaria (µSv) | No. de pacientes semanales que pudieran ser examinados | Cumple |
|---------|------------------------------------------------------|-------------------------------------------------------|--------|
| {barrera_1} | {dosis_1} | {n_pac_1} | {cumple_1} |
| ... | ... | ... | ... |

## Sección 7: Conclusiones y Recomendaciones (Heading azul)

**Si todas cumplen:**
> Todas las barreras atenúan adecuadamente la dosis en los locales adyacentes a los
> valores de dosis objetivo establecidos. Los resultados confirman la adecuación del
> blindaje existente para el uso proyectado de la instalación, soportando una carga de
> trabajo superior a {n_pacientes} pacientes por semana.
>
> Los resultados de este monitoreo son aplicables únicamente a la utilización del equipo
> en las condiciones de trabajo especificadas en este informe.

**Si alguna no cumple:** Agregar recomendaciones específicas por barrera.

## Sección 8: Firma

**Realizado por:**
- Ing. Manuel Rubio, Código de autorización: UGR-CR-050-2006-S
- Ing. Marco Arias Blanco, Código de autorización: UGR-CR-050-2006-S

## Sección 9: Referencias

[1] National Council on Radiation Protection and Measurements. Structural Shielding
Design for Medical X Ray Imaging Facilities, NCRP Report No. 147, November 2004

[2] Guía reguladora de seguridad radiológica para la práctica de radiodiagnóstico
médico, ARCAL XX, OIEA

## Sección 10: Anexo — Factores de Ocupación y Dosis Objetivo por Barrera

Tabla detallada:
| Barrera | Tipo de Zona | T | U (Rad. Primaria) | Hlm (mSv/sem) |
|---------|-------------|---|-------------------|----------------|
| {barrera} | {tipo_zona} | {T} | {U} | {P} |

## Sección 11: Plano de la Sala (si disponible)

Insertar imagen del plano con caption: "Vista general de la sala de RX"

## Pie de Página (Footer de todas las páginas)

Barra de logos de proveedores/distribuidores (si se tiene la imagen).
Texto: "INVERSIONES E IMPORTACIONES COLÉ S.A."
"SERVICIOS DE PROTECCIÓN RADIOLÓGICA. VENTA DE EQUIPOS Y ACCESORIOS."
"Visítenos en www.colecr.com"
Número de página centrado: "- {n} -"
