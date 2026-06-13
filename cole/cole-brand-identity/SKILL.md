---
name: cole-brand-identity
description: >
  Aplica la identidad visual oficial de Inversiones e Importaciones Colé S.A. SOLO en
  operaciones corporativas — NUNCA en paths de inversión patrimonial personal del titular.
  Incluye tokens de color (azul #3155e2, cyan #70e7ff, gris #363b47), tipografía (Roboto +
  Open Sans), componentes reutilizables y reglas de aplicación visual. Activar cuando el
  usuario genere documentos, presentaciones, artefactos visuales, componentes React, landing
  pages, material comercial, cotizaciones, reportes o piezas gráficas de OPERACIONES
  CORPORATIVAS DE COLÉ S.A. (protección radiológica, imagenología, equipos, servicios). NO
  activar en paths de inversión privada como "Oportunidades Inversion Hipotecaria/**" — en
  esos paths usar brand-guidelines (Anthropic) o identidad neutral. La verificación de path
  es OBLIGATORIA antes de aplicar cualquier elemento visual de marca.
---

<!--
VERSION: 2.0
CHANGELOG:
v2.0 (2026-05-11): Añadida REGLA 0 — VERIFICACIÓN PREVIA OBLIGATORIA POR PATH como
guardrail estructural al inicio del skill. Prohibida la aplicación de marca Colé en paths
de inversión patrimonial personal del titular. Modificada la description para indicar el
alcance estrictamente corporativo.
-->


# REGLA 0 — VERIFICACIÓN PREVIA OBLIGATORIA POR PATH

**Antes de aplicar CUALQUIER elemento de la identidad Colé S.A. (color, tipografía, logo,
razón social, datos de contacto, firma, footer), el agente DEBE verificar el path del
proyecto activo contra la siguiente lista de exclusión.**

## Paths excluidos — Prohibido aplicar marca Colé

| Path / Patrón | Razón de exclusión | Identidad a usar en su lugar |
|---|---|---|
| `Oportunidades Inversion Hipotecaria/**` | Inversión patrimonial personal del titular, no operativa corporativa de Colé | `brand-guidelines` (Anthropic) o neutral |
| `Inversiones/**` | Misma razón | `brand-guidelines` (Anthropic) o neutral |
| `Portafolio Personal/**` | Misma razón | `brand-guidelines` (Anthropic) o neutral |
| Cualquier path marcado en `MEMORY.md` con regla equivalente | Regla explícita registrada por el usuario | Según indique la memoria |

## Procedimiento de verificación al inicio

```
Paso 1 — Obtener el path del proyecto activo (working folder / connected folder).
Paso 2 — Comparar contra la lista de exclusión y MEMORY.md del usuario.
Paso 3 — Si el path está excluido:
    a. ABORTAR aplicación de Colé.
    b. Notificar al usuario: "Path detectado: [X]. Esta carpeta tiene regla de no aplicar
       marca Colé. Aplico identidad Anthropic neutral. Firmante: Ing. Manuel Rubio, MSc
       — Inversionista privado."
    c. Invocar brand-guidelines (Anthropic) o aplicar identidad neutral.
    d. NO mostrar logo, razón social, cédula jurídica, datos de contacto ni footer Colé.
Paso 4 — Si el path NO está excluido y la operación es corporativa Colé:
    a. Proceder con la aplicación de marca Colé descrita más abajo.
```

## Casos límite

- **Si el usuario pide explícitamente "con branding de Colé" en un path excluido**: confirmar
  explícitamente antes de aplicar. Posibilidad de error o de excepción consciente.
- **Si el path no es claramente corporativo ni inversión personal**: preguntar al usuario
  antes de decidir; NO asumir Colé por defecto.
- **Mezcla en un mismo documento**: si el documento debe combinar contenido corporativo Colé
  con contenido personal, NO aplicar Colé y usar identidad neutral; explicar al usuario.

## Razón estructural de esta regla

Inversiones e Importaciones Colé S.A. es operadora de servicios de protección radiológica
e imagenología. Mezclar la marca corporativa con operaciones de crédito privado, inversión
inmobiliaria o gestión patrimonial personal del titular genera:

1. **Riesgo reputacional**: si la marca Colé aparece en documentos de operaciones financieras
   privadas que terminan en disputa, ejecución de garantía o litigio, contamina la imagen
   corporativa de la empresa.
2. **Riesgo fiscal — precios de transferencia**: ingresos por intereses, comisiones o flujos
   de crédito privado que aparecen bajo timbre de Colé pueden ser interpretados por la
   administración tributaria como ingresos corporativos, sujetos a otro régimen de impuestos
   y a ajustes por precios de transferencia con el titular.
3. **Riesgo de imagen comercial**: clientes corporativos de Colé (clínicas, hospitales) no
   deben recibir documentación visualmente confundible con propuestas de inversión privada.

Esta regla NO es opcional, NO es soft guidance. Es condición estructural de uso del skill.

---

# Colé S.A. Brand Identity — Identidad Visual Corporativa

> *Las siguientes secciones aplican EXCLUSIVAMENTE cuando la Regla 0 confirma que el path
> es corporativo Colé.*

## Empresa

**Inversiones e Importaciones Colé S.A.**
Subtítulo corporativo: Servicios de Protección Radiológica. Venta de Equipos y Accesorios.
Representante Legal: Ing. Manuel Rubio, MSc — Presidente
Tagline: *Su mejor opción en servicios de protección radiológica de alto nivel profesional.*

### Datos de Contacto

| Campo | Valor |
|-------|-------|
| Cédula Jurídica | 3-101-392010 |
| Teléfono | (506) 2285-3211 / 2285-9561 |
| Fax | (506) 2245-3283 |
| Celular / WhatsApp | (506) 8395-7547 / 6050-0161 |
| Web | www.colecr.com |
| Email | colesa.manuel@gmail.com |
| Dirección | Del BCR 125m Este, Calle de Piedra, Zapote. San José, Costa Rica |

Estos datos deben usarse en encabezados de documentos DOCX, slides de cierre PPTX,
pie de página de cotizaciones, y footers de artefactos HTML cuando corresponda.

## Estética y Tono de Marca

### Brand Aesthetic
- Professional
- Technical
- Institutional
- Functional
- Trustworthy

### Tono de Voz
- Profesional
- Autoritario
- Especializado
- Informativo

### Valores de Marca
- Seguridad
- Optimización
- Calidad
- Compromiso con la salud y el medio ambiente
- Conocimiento y Capacitación

**Regla general:** Todo artefacto visual de Colé S.A. debe transmitir confianza institucional,
competencia técnica y seriedad profesional. Evitar diseños recargados, colores fuera de paleta,
o estilos que se perciban como informales, genéricos o comerciales.

## Tokens de Color

### Paleta Oficial

| Token | Nombre | Hex | RGB | Uso |
|-------|--------|-----|-----|-----|
| `--cole-blue` | Azul Colé | `#3155e2` | 49, 85, 226 | Color principal: encabezados, CTAs, elementos primarios, texto del logotipo "COLÉ" |
| `--cole-cyan` | Cyan Colé | `#70e7ff` | 112, 231, 255 | Acento secundario: highlights, badges, gradientes, decoración sutil |
| `--cole-dark` | Gris Oscuro | `#363b47` | 54, 59, 71 | Texto principal, fondos oscuros, texto "SA" y subtítulo en logo |
| `--cole-light` | Blanco Azulado | `#f7f7ff` | 247, 247, 255 | Fondo principal, áreas de contenido |
| `--cole-white` | Blanco | `#ffffff` | 255, 255, 255 | Fondo limpio, texto sobre fondos oscuros |

### Colores Derivados (uso interno)

| Token | Hex | Derivación | Uso |
|-------|-----|------------|-----|
| `--cole-blue-dark` | `#2544b8` | Blue -15% luminosidad | Hover states, énfasis, fondos de header |
| `--cole-blue-light` | `#e8edfc` | Blue 10% opacity sobre blanco | Fondos suaves de sección, cards destacadas |
| `--cole-cyan-light` | `#e0f9ff` | Cyan 15% opacity sobre blanco | Fondos de badges, tags informativos |
| `--cole-gray-600` | `#555b68` | Dark +20% luminosidad | Texto secundario, descripciones |
| `--cole-gray-300` | `#c2c5cc` | Dark +50% luminosidad | Bordes, líneas divisorias |
| `--cole-gray-100` | `#eeeef2` | Dark +80% luminosidad | Filas alternas en tablas, fondos neutros |

### Colores Funcionales (fijos)

| Token | Hex | Uso |
|-------|-----|-----|
| `--cole-success` | `#22C55E` | Confirmaciones, indicadores positivos |
| `--cole-warning` | `#F59E0B` | Alertas, precauciones |
| `--cole-danger` | `#EF4444` | Errores, alertas críticas, símbolo de radiación ☢ |
| `--cole-info` | `#3B82F6` | Notas informativas |

## Tipografía

### Fuentes Oficiales

| Elemento | Fuente | Fallback | Peso | Uso |
|----------|--------|----------|------|-----|
| Headings H1-H3 | **Roboto** | Arial, Helvetica, sans-serif | 700 (Bold) | Títulos principales, nombres de sección |
| Headings H4-H6 | **Roboto** | Arial, Helvetica, sans-serif | 500 (Medium) | Subtítulos, etiquetas |
| Body text | **Open Sans** | Helvetica, Arial, sans-serif | 400 (Regular) | Texto general, párrafos, descripciones |
| Body emphasis | **Open Sans** | Helvetica, Arial, sans-serif | 600 (Semi-Bold) | Texto destacado dentro de párrafos |
| Datos/Tablas | **Roboto Mono** | Consolas, monospace | 400 | Valores numéricos, especificaciones, código |
| UI/Botones | **Roboto** | Arial, sans-serif | 500 (Medium) | Elementos interactivos, navegación |

### Escala Tipográfica

| Nivel | Tamaño (px) | Tamaño (pt) PPTX/DOCX | Line Height |
|-------|-------------|------------------------|-------------|
| H1 | 32-36px | 28-32pt | 1.2 |
| H2 | 24-28px | 22-26pt | 1.25 |
| H3 | 20-22px | 18-20pt | 1.3 |
| H4 | 18px | 16pt | 1.35 |
| Body | 16px | 11-12pt | 1.5-1.6 |
| Small/Caption | 14px | 9-10pt | 1.4 |

### Carga de Fuentes (Google Fonts)

Para HTML/React, incluir siempre:
```html
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Open+Sans:wght@400;600&family=Roboto+Mono:wght@400&display=swap" rel="stylesheet">
```

## Logotipo

- **Archivo:** `assets/Logotipo_Oficial_COLESA.jpg`
- **Estructura:** Átomo estilizado integrado en la "O" de "COLÉ" + texto "COLÉSA"
  con subtítulo "Servicios de Protección Radiológica"
- **Colores del logo:** "COLÉ" y átomo en `--cole-blue` (#3155e2), "SA" y subtítulo
  en `--cole-dark` (#363b47), órbitas del átomo en gris medio
- **Zona de exclusión:** Mínimo 1x la altura del símbolo del átomo en todos los lados
- **Tamaño mínimo:** No reducir por debajo de 120px de ancho en digital, 30mm en impreso
- **Fondo permitido:** Solo sobre `--cole-white` (#ffffff) o `--cole-light` (#f7f7ff).
  Nunca sobre fondos oscuros con la versión estándar.
- **Versión invertida:** Si se necesita sobre fondo oscuro, usar versión monocromática
  en blanco (si el usuario la proporciona).

## Reglas de Aplicación por Formato

### PPTX (Presentaciones)

- **Fondo de slides:** `--cole-light` (#f7f7ff) por defecto
- **Slide de portada:** Fondo `--cole-dark` (#363b47), título en `--cole-white`,
  acento en `--cole-blue` (#3155e2), logo en esquina superior
- **Slide de cierre:** Fondo `--cole-blue` (#3155e2), texto en `--cole-white`,
  datos de contacto, tagline
- **Títulos de slide:** Roboto Bold, color `--cole-blue` (#3155e2)
- **Subtítulos:** Roboto Medium, color `--cole-dark` (#363b47)
- **Cuerpo:** Open Sans Regular, color `--cole-dark` (#363b47)
- **Tablas:** Encabezado fondo `--cole-blue` (#3155e2) texto blanco;
  filas alternas `--cole-white` / `--cole-gray-100` (#eeeef2)
- **Gráficos:** Serie 1: `--cole-blue`, Serie 2: `--cole-cyan`, Serie 3: `--cole-dark`
- **Acentos/shapes:** `--cole-blue` primario, `--cole-cyan` secundario
- **Footer:** "Inversiones e Importaciones Colé S.A." en Open Sans 9pt,
  color `--cole-gray-600` (#555b68), + número de slide
- **Línea decorativa:** Barra horizontal de 3px en `--cole-blue` bajo el título

### DOCX (Documentos)

- **Encabezado:** Logo Colé S.A. alineado izquierda + línea horizontal `--cole-blue` (2pt)
- **Títulos H1:** Roboto Bold, `--cole-blue` (#3155e2), 14pt
- **Títulos H2:** Roboto Bold, `--cole-dark` (#363b47), 12pt
- **Cuerpo:** Open Sans Regular, `--cole-dark` (#363b47), 11pt, interlineado 1.15
- **Tablas:** Mismo esquema que PPTX
- **Pie de página:** "Inversiones e Importaciones Colé S.A. — Servicios de Protección
  Radiológica" centrado, Open Sans 8pt, `--cole-gray-600` + número de página
- **Notas importantes:** Recuadro con borde izquierdo 4px `--cole-warning` (#F59E0B),
  fondo `#FEF9E7`
- **Advertencias de radiación:** Recuadro con borde izquierdo 4px `--cole-danger` (#EF4444),
  fondo `#FDEDEC`, ícono ☢
- **Hipervínculos:** Color `--cole-blue` (#3155e2), subrayado

### React / HTML (Artefactos Web)

**CSS Variables — Copiar en todo artefacto React/HTML de Colé S.A.:**

```css
:root {
  /* Colé S.A. — Paleta Oficial */
  --cole-blue: #3155e2;
  --cole-blue-dark: #2544b8;
  --cole-blue-light: #e8edfc;
  --cole-cyan: #70e7ff;
  --cole-cyan-light: #e0f9ff;
  --cole-dark: #363b47;
  --cole-gray-600: #555b68;
  --cole-gray-300: #c2c5cc;
  --cole-gray-100: #eeeef2;
  --cole-light: #f7f7ff;
  --cole-white: #ffffff;
  /* Funcionales */
  --cole-success: #22C55E;
  --cole-warning: #F59E0B;
  --cole-danger: #EF4444;
  --cole-info: #3B82F6;
  /* Tipografía */
  --font-heading: 'Roboto', Arial, Helvetica, sans-serif;
  --font-body: 'Open Sans', Helvetica, Arial, sans-serif;
  --font-mono: 'Roboto Mono', Consolas, monospace;
}
```

**Componentes React reutilizables:**

```jsx
// Header corporativo
const ColeHeader = ({ title, subtitle }) => (
  <header style={{
    backgroundColor: '#363b47',
    color: '#ffffff',
    padding: '1.5rem 2rem',
    fontFamily: "'Roboto', Arial, sans-serif"
  }}>
    <div style={{ fontSize: '0.8rem', opacity: 0.7, letterSpacing: '0.08em', textTransform: 'uppercase' }}>
      Inversiones e Importaciones Colé S.A.
    </div>
    <h1 style={{ margin: '0.5rem 0 0', fontWeight: 700, fontSize: '1.75rem' }}>{title}</h1>
    {subtitle && <p style={{ margin: '0.25rem 0 0', color: '#70e7ff', fontSize: '0.95rem' }}>{subtitle}</p>}
    <div style={{ height: '3px', backgroundColor: '#3155e2', marginTop: '1rem', width: '80px' }} />
  </header>
);
```

```jsx
// Tabla corporativa
const ColeTable = ({ headers, rows }) => (
  <table style={{ width: '100%', borderCollapse: 'collapse', fontFamily: "'Open Sans', sans-serif", fontSize: '0.9rem' }}>
    <thead>
      <tr style={{ backgroundColor: '#3155e2', color: '#ffffff' }}>
        {headers.map((h, i) => (
          <th key={i} style={{ padding: '10px 14px', textAlign: 'left', fontFamily: "'Roboto', sans-serif", fontWeight: 500 }}>{h}</th>
        ))}
      </tr>
    </thead>
    <tbody>
      {rows.map((row, i) => (
        <tr key={i} style={{ backgroundColor: i % 2 === 0 ? '#ffffff' : '#eeeef2' }}>
          {row.map((cell, j) => (
            <td key={j} style={{ padding: '8px 14px', borderBottom: '1px solid #c2c5cc', color: '#363b47' }}>
              {cell}
            </td>
          ))}
        </tr>
      ))}
    </tbody>
  </table>
);
```

```jsx
// Badge/Tag
const ColeBadge = ({ children, variant = 'blue' }) => {
  const styles = {
    blue: { bg: '#e8edfc', color: '#3155e2' },
    cyan: { bg: '#e0f9ff', color: '#0e7490' },
    dark: { bg: '#eeeef2', color: '#363b47' },
    danger: { bg: '#FDEDEC', color: '#EF4444' },
    warning: { bg: '#FEF9E7', color: '#D97706' },
    success: { bg: '#ECFDF5', color: '#16A34A' },
  };
  const s = styles[variant] || styles.blue;
  return (
    <span style={{
      backgroundColor: s.bg, color: s.color,
      padding: '2px 10px', borderRadius: '4px', fontSize: '0.8rem',
      fontFamily: "'Roboto', sans-serif", fontWeight: 500
    }}>
      {children}
    </span>
  );
};
```

**Reglas de estilo para Tailwind (React artifacts):**

- Header/Nav: `bg-[#363b47] text-white`
- Botón primario: `bg-[#3155e2] hover:bg-[#2544b8] text-white font-medium rounded`
- Botón secundario: `border border-[#3155e2] text-[#3155e2] hover:bg-[#e8edfc] rounded`
- Card: `bg-white border border-[#eeeef2] rounded-lg shadow-sm`
- Fondo página: `bg-[#f7f7ff]`
- Texto principal: `text-[#363b47]`
- Texto secundario: `text-[#555b68]`
- Acento decorativo: `bg-[#3155e2] h-[3px] w-20` (barra azul bajo títulos)
- Highlight/badge: `bg-[#e0f9ff] text-[#0e7490]`
- Table header: `bg-[#3155e2] text-white`
- Table row alterno: `even:bg-[#eeeef2]`

### Markdown (Artículos, Reportes)

- Markdown no soporta colores nativamente.
- Cuando se exporte a HTML o CMS, aplicar las CSS variables definidas arriba.
- Para Markdown puro: usar correctamente headings, tablas y formato estándar.
- Si se genera HTML desde Markdown, inyectar el bloque `:root` de variables CSS.

## Combinación con Otras Skills

- **Con `docx` skill:** Los colores y fuentes de esta skill tienen **prioridad** sobre
  los defaults de docx. Aplicar encabezado con logo, pie de página corporativo y
  esquema de colores Colé S.A.
- **Con `pptx` skill:** Aplicar slide master con paleta Colé. Portada y cierre
  con los esquemas definidos arriba.
- **Con `quotation-generator` skill:** La estructura comercial viene del quotation-generator;
  la identidad visual (colores, fuentes, encabezado, pie) se aplica desde aquí.
- **Con `frontend-design` skill:** Usar las CSS variables y clases Tailwind definidas
  aquí como sistema de diseño base.
- **Con `seo-technical-writer` skill:** Si el artículo se exporta a HTML, aplicar
  tipografía y colores Colé.
- **Con `hipoteca-analyst`, `fideicomiso-analyst`, `credit-risk-evaluator`, o cualquier
  trabajo dentro de `Oportunidades Inversion Hipotecaria/`:** NO aplicar branding Colé.
  Derivar al skill `brand-guidelines` (paleta Anthropic). El path manda sobre el skill:
  cualquier archivo con destino en esa carpeta o subcarpetas debe usar paleta neutra
  Anthropic, sin marca textual ni logo de Colé. Firmar como "Ing. Manuel Rubio, MSc"
  sin razón social.

## Qué NO Hacer

- No usar azules distintos a `#3155e2` como color primario.
- No usar el cyan `#70e7ff` como color de texto — solo como acento decorativo.
- No poner el logo sobre fondos de color que no sean blanco o `--cole-light`.
- No usar tipografías diferentes a Roboto y Open Sans en material oficial.
- No usar gradientes agresivos ni efectos de sombra pronunciados.
- No usar iconografía cartoon, clipart o ilustraciones fuera del estilo institucional.
- Nunca alterar las proporciones del logotipo.
- **REGLA POR PATH (prioridad sobre cualquier otra regla de este skill):** No aplicar logo, marca textual ("COLÉ S.A." / "Inversiones e Importaciones Colé S.A."), paleta corporativa, cédula jurídica 3-101-392010 ni datos de contacto de Colé en NINGÚN archivo cuyo destino sea la carpeta `C:\Users\colel\.claude\projects\Oportunidades Inversion Hipotecaria\` o cualquiera de sus subcarpetas (Carpeta 1, 2, 3, ..., N). Estas son operaciones personales de inversión privada del Ing. Rubio (hipotecas, fideicomisos, créditos privados) y NO deben mezclarse con la identidad de la empresa de protección radiológica. Aplica sin importar qué skill esté activo. Para estos casos, derivar al skill `brand-guidelines` (paleta Anthropic neutra: Dark `#141413`, Light `#faf9f5`, Orange `#d97757`, Blue `#6a9bcc`, Green `#788c5d`; tipografía Poppins/Lora). Firma: "Ing. Manuel Rubio, MSc" sin razón social.
