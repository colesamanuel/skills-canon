---
name: exam-bank-converter
description: >
  Convierte bancos de preguntas de examen a formatos tabulares (TSV, CSV, XLSX) para Google Sheets o LMS.
  Genera bancos de preguntas nuevos desde cero a partir de un tema, documento o manual.
  Soporta texto estructurado, texto libre, PDF o DOCX como entrada.
  Activar con: "convertir preguntas", "banco de preguntas", "examen a Google Sheets", "preguntas a Excel",
  "pasar preguntas a tabla", "crear examen", "generar preguntas", "quiz", "test de conocimiento",
  "evaluación", "preguntas de opción múltiple", "examen para operadores", "preguntas para capacitación",
  "banco de preguntas desde manual", o cualquier solicitud que involucre transformar o crear preguntas
  en formato tabular. Activar incluso si la solicitud parece simple.
---

# Exam Bank Converter

Skill para convertir bancos de preguntas de examen existentes a formato tabular, y para generar bancos de preguntas nuevos desde cero.

## Capacidades

1. **CONVERTIR** — Toma preguntas en cualquier formato de entrada y las transforma a formato tabular limpio.
2. **GENERAR** — Crea preguntas de opción múltiple desde cero a partir de un tema, documento o manual.
3. **AMBOS** — Genera preguntas y las entrega directamente en formato tabular.

---

## 1. Detección del formato de entrada

Antes de procesar, identificar qué tipo de entrada proporcionó el usuario:

| Tipo de entrada | Señales de detección | Acción |
|---|---|---|
| **Texto estructurado** | Tiene `[Puntos: N]`, opciones a/b/c/d, marcas `(Correcta)`, agrupación por temas | Parsear directamente |
| **Texto semi-estructurado** | Preguntas numeradas con opciones pero sin formato consistente | Normalizar → parsear |
| **Texto libre / narrativo** | Sin estructura de pregunta-respuesta clara | Solicitar clarificación o generar preguntas |
| **PDF / DOCX subido** | Archivo en `/mnt/user-data/uploads/` | Leer con skill apropiado (pdf-reading, file-reading), luego parsear |
| **Solicitud de generación** | "Generá preguntas sobre X", "creá un examen de..." | Ir a sección 4 (Generación) |

---

## 2. Formato tabular de salida (estándar)

El formato canónico tiene **7 columnas**, separadas por tabuladores:

```
Pregunta	a	b	c	d	Correcta	Puntos
```

### Reglas de formato

- **Pregunta**: Incluir el prefijo de categoría/tema si existe (ej: `Seguridad Operacional: ¿Qué...`). Si no existe categoría, usar solo el texto de la pregunta.
- **a, b, c, d**: Texto de cada opción, sin letra ni paréntesis al inicio. Solo el contenido.
- **Correcta**: Letra minúscula de la respuesta correcta (`a`, `b`, `c` o `d`).
- **Puntos**: Valor numérico. Si no se especifica, usar `1` por defecto.
- **Sin comillas** envolventes en ningún campo.
- **Sin saltos de línea** dentro de un campo — si el texto original tiene saltos, unirlos con espacio.
- **Encoding**: UTF-8.

### Formato de salida por defecto: TSV (copiar/pegar directo a Google Sheets)

El formato primario de salida es **siempre un archivo `.tsv`** (tab-separated values) optimizado para copiar y pegar directamente en Google Sheets.

**Método — Generación directa con `create_file`:**

1. Construir el contenido TSV en memoria: primera fila = encabezado, filas siguientes = preguntas.
2. Separar cada campo con un carácter tabulador (`\t`). **Sin comillas envolventes** en ningún campo.
3. Crear el archivo directamente en `/mnt/user-data/outputs/` con extensión `.tsv` usando `create_file`.
4. Presentar con `present_files`.
5. Indicar al usuario: "Abrí el archivo, seleccioná todo (Ctrl+A), copiá (Ctrl+C) y pegá en la celda A1 de Google Sheets. Las columnas se separan automáticamente."

**Reglas críticas del TSV:**
- **Sin comillas** — Ningún campo debe ir envuelto en comillas dobles ni simples.
- **Sin comas como separador** — El separador es exclusivamente tabulador.
- **Sin saltos de línea dentro de campos** — Si el texto original tiene saltos, unirlos con espacio.
- **Encoding UTF-8** — Para preservar tildes, eñes y caracteres especiales.

### Variantes alternativas de salida

Solo usar estas si el usuario las solicita explícitamente:

| Destino solicitado | Formato | Acción |
|---|---|---|
| Excel | `.xlsx` | Usar skill `xlsx` para generar archivo formateado |
| CSV genérico | `.csv` | Generar con comas, campos con comas envueltos en comillas dobles |
| Moodle | `.xml` | Generar Moodle XML (ver sección 5) |
| Google Sheet directa | API | Crear vía `gspread` si hay credenciales disponibles |

---

## 3. Proceso de conversión (entrada existente → tabla)

### Paso 1: Parseo

Extraer de cada pregunta:
- Texto de la pregunta (con categoría si aplica)
- Opciones a, b, c, d
- Respuesta correcta (letra)
- Puntos (si están indicados)

**Señales comunes de respuesta correcta en texto de entrada:**
- `(Correcta)` o `(correcta)` junto a la opción
- `Respuesta: X` al final
- Asterisco `*` junto a la opción
- Negrita o marca especial

### Paso 2: Validación

Antes de generar el archivo de salida, verificar:
- [ ] Cada pregunta tiene exactamente 4 opciones (a, b, c, d)
- [ ] Cada pregunta tiene exactamente 1 respuesta correcta marcada
- [ ] No hay preguntas duplicadas
- [ ] Los puntos son numéricos
- [ ] El conteo total de preguntas coincide con lo esperado

Si hay inconsistencias, reportarlas al usuario antes de generar el archivo.

### Paso 3: Generación (TSV por defecto)

1. Parsear todas las preguntas a filas de texto separadas por tabuladores
2. Crear archivo `.tsv` directamente en `/mnt/user-data/outputs/` con `create_file`
3. Presentar con `present_files`
4. Indicar instrucciones de copiar/pegar a Google Sheets

### Paso 4: Resumen

Reportar al usuario:
- Total de preguntas convertidas
- Distribución por tema/categoría (si aplica)
- Cualquier anomalía detectada

---

## 4. Proceso de generación (tema → preguntas nuevas)

Cuando el usuario pida **crear** preguntas desde cero:

### Entradas requeridas

- **Tema o documento fuente** — Puede ser un tema verbal, un PDF/DOCX subido, o referencia a un manual
- **Cantidad de preguntas** — Si no se especifica, sugerir 10-20 como rango razonable
- **Nivel de dificultad** — Operador básico / Técnico intermedio / Auditor/experto
- **Formato de salida** — Aplicar el mismo estándar de la sección 2

### Principios de redacción de preguntas

1. **Una sola respuesta correcta inequívoca** — Las 3 opciones incorrectas deben ser plausibles pero claramente erróneas para quien domina el tema.
2. **Preguntas situacionales** — Preferir "¿Qué hace si...?" sobre "¿Cuál es la definición de...?". Las preguntas deben evaluar criterio, no solo memoria.
3. **Prefijo de categoría** — Cada pregunta lleva un prefijo temático descriptivo seguido de dos puntos (ej: `Seguridad Operacional:`, `Dosimetría Ocupacional:`).
4. **Distractores inteligentes** — Los distractores deben reflejar errores comunes reales, no absurdos evidentes.
5. **Base normativa** — Para temas regulados (protección radiológica, seguridad industrial, etc.), las respuestas correctas deben alinearse con normativa vigente (ICRP, IAEA, NCRP, decreto local aplicable).
6. **Sin ambigüedad** — Si dos opciones podrían considerarse correctas, reescribir hasta que solo una lo sea.
7. **Puntuación por defecto**: 2 puntos por pregunta (ajustable por el usuario).

### Estructura temática sugerida

Si el examen cubre múltiples temas, organizar las preguntas en bloques temáticos. Ejemplo para un irradiador de sangre:

```
Tema 1: Operación del equipo (10 preguntas)
Tema 2: Magnitudes y límites de dosis (8 preguntas)
Tema 3: Dosimetría personal y de área (8 preguntas)
Tema 4: Riesgos y efectos biológicos (6 preguntas)
Tema 5: Principios ALARA (10 preguntas)
Tema 6: Cumplimiento normativo y licencias (8 preguntas)
```

### Flujo de generación

1. Confirmar tema, cantidad, nivel y formato de salida
2. Generar preguntas agrupadas por tema
3. Aplicar validación (sección 3, paso 2)
4. Entregar en formato solicitado (sección 3, pasos 3-4)

---

## 5. Formato Moodle XML (referencia)

Si el usuario solicita exportación para Moodle, generar XML con esta estructura:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<quiz>
  <question type="multichoice">
    <name><text>Nombre corto de la pregunta</text></name>
    <questiontext format="html">
      <text><![CDATA[<p>Texto completo de la pregunta</p>]]></text>
    </questiontext>
    <defaultgrade>2</defaultgrade>
    <single>true</single>
    <shuffleanswers>true</shuffleanswers>
    <answer fraction="100" format="html">
      <text><![CDATA[<p>Opción correcta</p>]]></text>
    </answer>
    <answer fraction="0" format="html">
      <text><![CDATA[<p>Opción incorrecta 1</p>]]></text>
    </answer>
    <answer fraction="0" format="html">
      <text><![CDATA[<p>Opción incorrecta 2</p>]]></text>
    </answer>
    <answer fraction="0" format="html">
      <text><![CDATA[<p>Opción incorrecta 3</p>]]></text>
    </answer>
  </question>
</quiz>
```

Guardar como `.xml` y presentar al usuario.

---

## 6. Coordinación con otros skills

| Skill | Cuándo coordinar |
|---|---|
| `radiological-protection-auditor` | Si el tema de generación es protección radiológica — usar como fuente de rigor técnico |
| `xlsx` | Si el formato de salida es Excel — leer SKILL.md de xlsx antes de generar |
| `pdf-reading` | Si la entrada es un PDF subido — leer SKILL.md de pdf-reading para extraer contenido |
| `file-reading` | Si hay archivos subidos de cualquier tipo — usar como router de lectura |
| `cole-brand-identity` | Si el examen se genera como documento formal de Colé S.A. |

---

## 7. Checklist de calidad pre-entrega

Antes de presentar el archivo final:

- [ ] Encabezado presente y correcto (7 columnas)
- [ ] Sin filas vacías ni campos faltantes
- [ ] Respuesta correcta es siempre una letra válida (a/b/c/d)
- [ ] Puntos son numéricos en todas las filas
- [ ] Conteo de filas = número esperado de preguntas
- [ ] Archivo en UTF-8
- [ ] Archivo copiado a `/mnt/user-data/outputs/`
- [ ] Resumen entregado al usuario (total preguntas, temas, anomalías)
