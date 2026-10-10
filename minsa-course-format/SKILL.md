---
name: minsa-course-format
description: "Genera y formatea programas de curso de Proteccion Radiologica para entrega al MINSA segun Anexo XIII del Decreto 44653-S de Costa Rica. Produce documentos DOCX con branding Cole S.A., estructura de 5 secciones obligatorias, modulos en formato parrafo con temas del Anexo XIII, y validacion de cumplimiento normativo. Activar con: programa de curso, curso MINSA, programa PR, Anexo XIII, curso basico, curso avanzado, programa de capacitacion, crear curso, generar programa, formato MINSA, curso proteccion radiologica, programa para el Ministerio de Salud, Decreto 44653-S, cronograma de modulos, contenido tematico PR. Activar incluso si la solicitud parece simple."
---

# MINSA Course Format — Generador de Programas de Curso PR

Skill para generar, formatear y validar programas de capacitacion en Proteccion Radiologica conforme al Anexo XIII del Decreto 44653-S (Reglamento de Proteccion Radiologica de Costa Rica) con identidad visual Cole S.A.

## Contexto regulatorio

El Ministerio de Salud de Costa Rica (MINSA) exige que todo curso de PR se ajuste a la estructura y contenidos minimos definidos en el Anexo XIII del Decreto 44653-S. Existen dos niveles:

- Curso B (Basico): 16 horas minimo. Temas obligatorios segun XIII.3.1.
- Curso A (Avanzado): 80 horas minimo. Temas obligatorios segun XIII.3.2 (incluye todos los del basico + calculos de blindaje).

Cada practica (medica, industrial, investigacion, veterinaria) puede requerir temas adicionales especificos.

## 1. Estructura del documento

Cada programa de curso sigue exactamente esta estructura de 5 secciones. No usar estilos Heading de Word — todo va como parrafo "Normal" con formato manual. **NO incluir parrafos introductorios, descriptivos o de contexto fuera de las 5 secciones.**

### Encabezado de pagina (header)
Imagen oficial del programa: `header_curso_pr.png` (ubicada en la raiz del skill, NO en subcarpeta assets/) insertada en el header de la seccion del documento. Ancho: 16 cm, centrada. Sin linea azul adicional (la imagen ya incluye el diseno completo con logo Cole S.A., titulo "Programa del Curso de Proteccion Radiologica" y www.colecr.com). Se repite en todas las paginas.

### Pie de pagina (footer)
Texto centrado: "Inversiones e Importaciones Cole S.A. — Servicios de Proteccion Radiologica"
Open Sans 8pt, color #555b68.

### Bloque de titulo (3 parrafos)
PROGRAMA DE CAPACITACION EN PROTECCION RADIOLOGICA
[Nombre de la practica especifica]
[Linea en blanco o subtitulo opcional]
Formato: Calibri 14pt, Bold, color #3155e2 (Cole Blue).

### Seccion 1: INFORMACION GENERAL (6 parrafos)
Campos obligatorios: Nombre del curso, Nivel (Basico/Avanzado), Dirigido a, Duracion (16h/80h), Modalidad (Bimodal presencial + virtual), Facilitador(es) (Ing. Manuel Rubio, MSc — Inversiones e Importaciones Cole S.A.)

### Seccion 2: OBJETIVO GENERAL (1 parrafo)
Objetivo unico que describe la competencia a desarrollar vinculando la practica especifica con los principios de PR (justificacion, optimizacion, limitacion de dosis). **El encabezado "2. OBJETIVO GENERAL" va en un parrafo separado; el texto del objetivo va en otro parrafo. Nunca fusionarlos.**

### Seccion 3: CONTENIDO TEMATICO (parrafos por modulo)

**FORMATO: PARRAFOS, NO TABLA.** Cada modulo se presenta como dos parrafos consecutivos:

Parrafo 1 (titulo): "Modulo N: [Titulo del tema]" en **negritas** Calibri 11pt #363b47 + " (X.X horas)" en Calibri 11pt color #3155e2 (Cole Blue).

Parrafo 2 (descripcion): Texto descriptivo del contenido del modulo en Calibri 11pt Regular #363b47.

Al final de todos los modulos, un parrafo: "Total de horas: XX.X"

Reglas de contenido:
- Numeracion secuencial sin saltos
- Suma de horas = duracion declarada EXACTA (no 79.2, no 80.2 — debe ser 80.0 o 16.0)
- Incluir los temas obligatorios del Anexo XIII que apliquen segun la practica (ver seccion 6 para condicionalidad)
- **ORDEN OBLIGATORIO**: Los temas DEBEN seguir EXACTAMENTE el orden del Anexo XIII (ver seccion 6). No reordenar segun criterio pedagogico propio.
- Temas especificos de la practica van AL FINAL, despues de todos los temas obligatorios del Anexo XIII
- NO duplicar temas (error frecuente: "Transporte" y "Transporte seguro" como modulos separados)
- **Contenido pertinente a la practica**: Cada descripcion de modulo debe adaptarse a la practica especifica. NO copiar descripciones genericas ni contenido de otra practica (ver seccion 8: Anti-patrones).

### Seccion 4: METODOLOGIA DE ENSENANZA (2 parrafos)
1. Componente teorico: clases magistrales, material audiovisual, estudios de caso.
2. Componente practico: ejercicios con equipos, simulaciones, demostraciones in situ.

**Seccion 4 y Seccion 5 son independientes. Nunca anidar la seccion 5 dentro de la 4.**

### Seccion 5: METODOLOGIA DE EVALUACION (4 parrafos)
Evaluacion continua, actividades practicas evaluadas, examen final teorico, nota minima 70/100.

## 2. Branding Cole S.A.

Tokens de color:
- Cole Blue #3155e2: Titulos, encabezados de seccion, horas de cada modulo
- Cole Dark #363b47: Texto de cuerpo, titulos de modulo (negritas), descripciones
- Cole Cyan #70e7ff: Acentos secundarios (uso discreto)
- Cole Gray-600 #555b68: Pie de pagina

Tipografia:
- Titulo del programa: Calibri 14pt Bold #3155e2
- Encabezado de seccion: Calibri 12pt Bold #3155e2
- Titulo de modulo: Calibri 11pt Bold #363b47
- Horas de modulo: Calibri 11pt Regular #3155e2
- Texto de cuerpo/descripcion: Calibri 11pt Regular #363b47
- Pie de pagina: Open Sans 8pt Regular #555b68

## 3. Convencion de nombres de archivo
Curso [Nivel] [PR] [Tipo Practica] [Especializacion].docx
Nivel: A (Avanzado) o B (Basico). PR siempre presente. Tipo: PM (Medica), PI (Industrial), PInv (Investigacion), PV (Veterinaria).

## 4. Generacion con python-docx

Usar python-docx para generar DOCX. Configurar estilo Normal con Calibri 11pt #363b47.

Ruta de imagen del encabezado: `/mnt/skills/user/minsa-course-format/header_curso_pr.png`

Encabezado: insertar la imagen en el header de la seccion con `add_picture(path, width=Cm(16))`, centrado. No agregar linea azul adicional.

Pie de pagina: parrafo centrado, Open Sans 8pt #555b68 con texto corporativo.

Titulos del programa: add_run bold 14pt #3155e2.

Modulos en formato parrafo (NO tabla):
```python
for num, title, hours, desc in modules:
    p = doc.add_paragraph()
    p.space_before = Pt(6)
    r1 = p.add_run(f"Módulo {num}: {title}")
    r1.bold = True
    r1.font.size = Pt(11)
    r1.font.color.rgb = COLE_DARK  # #363b47
    r2 = p.add_run(f" ({hours} horas)")
    r2.font.size = Pt(11)
    r2.font.color.rgb = COLE_BLUE  # #3155e2
    p2 = doc.add_paragraph()
    r3 = p2.add_run(desc)
    r3.font.size = Pt(11)
    r3.font.color.rgb = COLE_DARK
```

### Post-generacion: fix XML obligatorio

python-docx genera archivos con dos problemas de validacion conocidos que deben corregirse SIEMPRE:

```bash
# 1. Unpack
python /mnt/skills/public/docx/scripts/office/unpack.py output.docx unpacked/

# 2. Fix Content_Types (imagen PNG no declarada)
cd unpacked
sed -i 's|</Types>|<Default Extension="png" ContentType="image/png"/></Types>|' '[Content_Types].xml'

# 3. Fix zoom (atributo percent faltante)
sed -i 's|<w:zoom/>|<w:zoom w:percent="100"/>|' word/settings.xml

# 4. Repack con validacion
python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ /mnt/user-data/outputs/FILENAME.docx --original output.docx
```

Verificar que la salida diga "All validations PASSED!" antes de entregar.

## 5. Validacion de cumplimiento

Checklist obligatorio antes de entregar:
- Nivel correcto (B=16h min, A=80h min)
- Temas obligatorios del Anexo XIII presentes (respetando condicionalidad segun practica — ver seccion 6)
- **Orden Anexo XIII**: Los temas obligatorios siguen EXACTAMENTE el orden del Anexo XIII. Temas de la practica especifica van DESPUES de los obligatorios.
- Sin duplicados (especialmente Transporte, Gestion de Desechos, Proteccion Radiologica)
- Numeracion secuencial sin saltos
- Suma de horas = duracion declarada EXACTA (80.0 o 16.0, no aproximada)
- 5 secciones completas en orden correcto (sin parrafos extra fuera de las secciones)
- Encabezado con imagen header_curso_pr.png en todas las paginas
- Pie de pagina corporativo en todas las paginas
- Formato parrafo para modulos (NO tabla)
- Titulos de modulo en negritas
- Horas en color Cole Blue
- Branding Cole aplicado
- Nombre de archivo segun convencion
- Nota de aprobacion 70/100
- Modalidad Bimodal (presencial + virtual) — sin redundancia ("Bimodal (Bimodal...)" es error)
- Contenido de cada modulo pertinente a la practica (sin contenido medico en cursos industriales ni viceversa)
- Al menos 2-3 modulos especificos de la practica al final
- Validacion XML pasada ("All validations PASSED!")

Temas que causan duplicados frecuentes (NO deben aparecer dos veces):
- Transporte de Material = Transporte seguro de material radiactivo
- Gestion de Desechos = Gestion de desechos radiactivos
- Proteccion Radiologica = Principios basicos de proteccion radiologica
Si aparecen ambas variantes, fusionar en un solo modulo.

## 6. Temas obligatorios Anexo XIII — ORDEN NORMATIVO Y CONDICIONALIDAD

**REGLA CRITICA: El orden de los temas en los modulos del programa DEBE respetar exactamente la secuencia del Anexo XIII. Los temas especificos de la practica van DESPUES de los temas obligatorios, nunca intercalados.**

### XIII.3.1 Curso Basico (16h) — Orden obligatorio:
1. Nociones basicas de las radiaciones ionizantes
2. Interaccion de la radiacion con la materia
3. Magnitudes y unidades radiometricas, dosimetricas y de proteccion radiologica, asi como magnitudes operacionales
4. Deteccion de las radiaciones ionizantes
5. Efectos biologicos de las radiaciones ionizantes
6. Principios basicos de la proteccion radiologica
7. Proteccion radiologica ocupacional, medica y del publico
8. Gestion de residuos radiactivos — **CONDICIONAL** (ver tabla abajo)
9. Transporte de materiales radiactivos — **CONDICIONAL** (ver tabla abajo)
10. Emergencias radiologicas
11. Marco legal nacional e internacional en proteccion radiologica
12. Importancia del Manual de Procedimientos de PR de la instalacion
13. Verificacion de generadores de radiacion ionizante — **CONDICIONAL** (ver tabla abajo)
[14 en adelante: temas especificos de la practica]

### XIII.3.2 Curso Avanzado (80h) — Orden obligatorio:
1. Fundamentos fisicos de las radiaciones ionizantes (reemplaza "Nociones basicas" con mayor profundidad)
2. Interaccion de la radiacion con la materia
3. Magnitudes y unidades radiometricas, dosimetricas y de proteccion radiologica, asi como magnitudes operacionales
4. Deteccion de las radiaciones ionizantes
5. Efectos biologicos de las radiaciones ionizantes
6. Principios basicos de la proteccion radiologica
7. Proteccion radiologica ocupacional, medica y del publico
8. Gestion de residuos radiactivos — **CONDICIONAL** (ver tabla abajo)
9. Transporte de materiales radiactivos — **CONDICIONAL** (ver tabla abajo)
10. Emergencias radiologicas
11. Marco legal nacional e internacional
12. Estructura y contenidos del Manual de PR (reemplaza "Importancia del Manual")
13. Verificacion de generadores de radiacion ionizante — **CONDICIONAL** (ver tabla abajo)
14. Nociones de calculos de blindaje y levantamientos radiometricos (EXCLUSIVO avanzado)
[15 en adelante: temas especificos de la practica]

### Condicionalidad de modulos por practica

| Practica | Item 8 (Residuos) | Item 9 (Transporte) | Item 13 (Verif. generadores) |
|---|---|---|---|
| PM Radiologia (RX) | OMITIR — no genera residuos radiactivos | OMITIR — no transporta material radiactivo | INCLUIR (obligatorio) — generadores de RX |
| PM Medicina Nuclear | INCLUIR — genera residuos solidos, liquidos, gaseosos | INCLUIR — recibe radiofármacos en bultos Tipo A | INCLUIR si PET/CT o SPECT/CT (componente CT) |
| PM Radioterapia | Evaluar segun practica (Co-60 vs LINAC) | Evaluar segun practica (fuentes selladas) | INCLUIR si LINAC |
| PI Irradiadores Ind. | INCLUIR — fuentes selladas en desuso, leak test | INCLUIR — bultos Tipo B(U), fuentes alta actividad | OMITIR — usa fuentes selladas, no generadores |
| PI Perfilaje de Pozos | INCLUIR — fuentes selladas en desuso | INCLUIR — transporte de fuentes a locacion | OMITIR — usa fuentes selladas, no generadores |
| PI Gammagrafia | INCLUIR — fuentes en desuso | INCLUIR — transporte frecuente de fuentes | OMITIR — usa fuentes selladas |
| PI Medidores Nucleares | Evaluar — fuentes selladas de baja actividad | Evaluar — recepcion y reemplazo de fuentes | OMITIR |
| PInv Investigacion | INCLUIR — residuos de laboratorio | INCLUIR — recibe materiales radiactivos | Evaluar segun tipo de equipo |
| PV Veterinaria | Similar a PM segun modalidad | Similar a PM segun modalidad | INCLUIR si RX veterinario |

**Regla de omision**: Cuando un modulo condicional se OMITE, las horas liberadas se redistribuyen entre los modulos que son nucleo de la practica (especificos o de mayor peso tecnico). La numeracion de los modulos restantes se ajusta para mantener secuencia sin saltos.

**Regla de inclusion minima**: Cuando un modulo condicional se INCLUYE pero la practica solo tiene aplicabilidad tangencial, asignar 2-3 horas con contenido adaptado. No rellenar con contenido generico copiado de otra practica.

## 7. Datos de contacto Cole S.A.
- Empresa: Inversiones e Importaciones Cole S.A.
- Representante: Ing. Manuel Rubio, MSc
- Servicios: Proteccion Radiologica, Imagenologia, Dosimetria
- Telefono: (506) 2285-3211 / 2285-9561

## 8. Anti-patrones detectados — ERRORES RECURRENTES A EVITAR

Los siguientes errores se han detectado sistematicamente en programas generados y deben evitarse:

### 8.1 Contenido medico en cursos industriales (y viceversa)
**ERROR**: Insertar en el modulo 7 (PR Ocupacional, Medica y del Publico) contenido de justificacion de exposiciones medicas, DRL, proteccion de pacientes pediatricos, consentimiento informado, etc., en un curso de practica INDUSTRIAL (irradiadores, perfilaje, gammagrafia).
**CORRECCION**: El contenido del modulo 7 debe adaptarse a la practica. En cursos industriales: clasificacion de zonas, limites de dosis, monitoreo, EPP, control de acceso en campo/locacion. En cursos medicos: incluir DRL, proteccion del paciente, consentimiento informado.

### 8.2 Bloques "Ademas:" copy-paste
**ERROR**: Agregar al final de la descripcion de un modulo (tipicamente 8 y 9) un bloque extenso iniciando con "Además:" que contiene contenido generico identico en todos los cursos (texto calcado sobre SSR-6, GSR Part 3, etc.), inflando artificialmente las horas.
**CORRECCION**: Cada modulo debe tener UNA descripcion coherente, especifica a la practica, sin apendices genericos. Si el contenido normativo es relevante, integrarlo naturalmente en la descripcion.

### 8.3 Titulo de modulo 7 duplicado
**ERROR**: "Proteccion Radiologica Ocupacional, Medica y del Publico y Medica" — duplicacion de "y Medica".
**CORRECCION**: Usar el titulo exacto del Anexo XIII: "Proteccion radiologica ocupacional, medica y del publico".

### 8.4 Modulos obligatorios fuera de orden o intercalados
**ERROR**: Colocar "Principios de PR" o "PR Ocupacional" al final del programa (como modulos 14 o 15) mientras modulos especificos de la practica estan intercalados entre los obligatorios.
**CORRECCION**: Obligatorios primero en orden Anexo XIII, especificos de la practica despues. Sin excepciones.

### 8.5 Numeracion con saltos
**ERROR**: Modulo 9 seguido de Modulo 11 (falta el 10).
**CORRECCION**: Numeracion secuencial estricta. Si se omite un tema condicional, renumerar los restantes.

### 8.6 Horas que no cuadran
**ERROR**: Suma de horas = 74.8, 79.2, 79.5 u 80.2 en un curso de 80h.
**CORRECCION**: Verificar suma EXACTA antes de generar. Si no cuadra, ajustar modulos individualmente hasta lograr igualdad exacta con la duracion declarada.

### 8.7 Fusion de secciones
**ERROR**: Seccion 2 (Objetivo) fusionada con su encabezado en un solo parrafo. Seccion 5 (Evaluacion) anidada dentro de Seccion 4 (Ensenanza) via HTML comment o formato erroneo.
**CORRECCION**: Cada seccion tiene encabezado propio y contenido propio. Son 5 secciones independientes y secuenciales.

### 8.8 Redundancias textuales
**ERROR**: "Modalidad: Bimodal (Bimodal (presencial + virtual).)" o doble punto al final de descripciones.
**CORRECCION**: Revision de texto final para eliminar duplicaciones y puntuacion erronea.

### 8.9 "Evaluacion de Suficiencia" como modulo de contenido
**ERROR**: Incluir un modulo titulado "Evaluacion de Suficiencia" dentro del contenido tematico (Seccion 3) con horas asignadas, cuando la evaluacion pertenece a la Seccion 5.
**CORRECCION**: Si se incluye un modulo final de evaluacion practica, debe ser sustantivo ("Evaluacion practica integral") con descripcion de actividades concretas (calculo de blindaje, levantamiento radiometrico, respuesta a emergencias), no una mera declaracion de que habra examen.

### 8.10 Ausencia de modulos especificos de la practica
**ERROR**: Un programa que solo lista los temas obligatorios del Anexo XIII sin ningun modulo especifico de la practica al final.
**CORRECCION**: Todo programa debe incluir al menos 2-3 modulos especificos de la practica despues de los obligatorios. Ejemplos: Radiofarmacia (MN), Seguridad tecnologica de irradiadores (industrial), PR del paciente en radiodiagnostico (RX), Fuentes y tecnicas de perfilaje (pozos).
