# Clasificación de bultos — Lógica completa (IAEA SSR-6 Rev.1, 2018)

## Cadena de decisión

```
Radionucleido + Actividad conocidos
        │
        ▼
¿Bajo límites de exención? (Tabla 2: concentración Bq/g Y actividad total por envío)
  SÍ → EXENTO — fuera del reglamento (párr. 107(e), 402)
  NO ↓
¿Forma especial? (certificado de aprobación vigente — párr. 803)
  SÍ → usar A1   |   NO → usar A2
        │
        ▼
¿Actividad ≤ límite de bulto exceptuado? (Tabla 4)
  SÍ → BULTO EXCEPTUADO (UN 2908–2911)
  NO ↓
¿Es LSA o SCO? → BULTO INDUSTRIAL IP-1/2/3 (UN 2912, 2913, 3321, 3322)
  NO ↓
¿Actividad ≤ A1 (forma especial) o ≤ A2 (no especial)?
  SÍ → BULTO TIPO A (UN 3332 forma especial / UN 2915 no especial)
  NO ↓
BULTO TIPO B(U) o B(M) (UN 2916 / 2917) — requiere certificado de diseño
  Aéreo con actividad muy alta → TIPO C (UN 3323)
        │
        ▼
¿Fisionable? → capa adicional: CSI, UN 3324–3333, excepciones párr. 417
```

## Límites de bulto exceptuado (Tabla 4, SSR-6)

| Contenido | Límite |
|---|---|
| Material (forma especial) | 10⁻³ A1 |
| Material (forma no especial) | 10⁻³ A2 |
| Artículo/instrumento — por artículo | 10⁻² A1 (o A2) |
| Artículo/instrumento — por bulto | A1 (o A2) |
| Gas tritio por bulto | 2×10⁻² A2 |

Requisitos del bulto exceptuado (párrs. 515–520):
- Tasa de dosis en superficie ≤ **5 µSv/h** (párr. 516).
- Si es instrumento (UN 2911): además ≤ **0,1 mSv/h a 10 cm** del instrumento sin embalar (párr. 517(b)).
- Marca interna **"RADIOACTIVE"** visible al abrir (párr. 517(a)); excepción si el marcado va sobre el propio instrumento.
- Marcado exterior: número UN precedido de "UN" (párr. 531); expedidor y/o destinatario.
- Contaminación superficial transitoria ≤ **4 Bq/cm²** β/γ y α baja toxicidad; ≤ **0,4 Bq/cm²** otros α — promediado sobre 300 cm² (párr. 508).
- Retención del contenido en condiciones rutinarias (párr. 621).
- NO requiere etiquetas de trébol ni declaración completa de mercancías peligrosas (en aéreo sí requiere mención "Radioactive Material, Excepted Package..." en el air waybill — IATA DGR).

## Forma especial — requisitos reales (párrs. 602–604, 704–711, 803)

NO es automática por ser fuente sellada. Exige TODO esto:
1. Dimensión mínima ≥ **5 mm**.
2. Superar ensayos: impacto (caída 9 m), percusión, flexión, térmico (800 °C, 10 min), o ensayo de lixiviación según aplique.
3. **Certificado de aprobación de diseño unilateral** emitido por autoridad competente del país de origen del diseño, vigente.

Sin certificado → tratar como forma no especial → aplica **A2**. Para muchos radionucleidos A2 << A1 (ej. Am-241: A1 = 10 TBq vs A2 = 1×10⁻³ TBq — factor 10.000).

## Bulto Tipo A (párrs. 530, 633–649)

- Límite: ≤ A1 (forma especial) o ≤ A2 (no especial).
- Diseño debe resistir condiciones normales de transporte (ensayos de aspersión, caída libre, apilamiento, penetración).
- No requiere aprobación de autoridad competente para el diseño (autocertificación del expedidor con documentación de ensayos).
- UN 3332 (forma especial) / UN 2915 (forma no especial).
- Uso típico: radiofármacos (Tc-99m, F-18, I-131, Lu-177), fuentes de calibración medianas.

## Bulto Tipo B(U)/B(M) (párrs. 650–666)

- Para actividades > A1/A2. Diseño aprobado por autoridad competente (certificado).
- Debe resistir condiciones de accidente: caída 9 m, punzonado, fuego 800 °C 30 min, inmersión.
- B(U) = aprobación unilateral; B(M) = multilateral (cada país de tránsito).
- Uso típico: fuentes de gammagrafía industrial Ir-192/Se-75, teleterapia Co-60, irradiadores.

## Tipo C (párrs. 667–671)

- Solo transporte aéreo de actividades muy altas (> 3000 A1 o 3000 A2, o > 1000 TBq, lo que sea menor).
- Ensayos reforzados (impacto 90 m/s).

## LSA y SCO (párrs. 409–412)

- **LSA** (Low Specific Activity): material con actividad específica intrínsecamente baja. LSA-I (minerales, U/Th natural), LSA-II (ej. agua tritiada ≤ 0,8 TBq/L, concentración ≤ 10⁻⁴ A2/g), LSA-III (sólidos ≤ 2×10⁻³ A2/g).
- **SCO** (Surface Contaminated Object): objeto no radiactivo con contaminación superficial. SCO-I (límites bajos, puede ir sin embalar bajo condiciones), SCO-II, SCO-III (Rev.1 añadió SCO-III para objetos grandes).
- Viajan en bultos industriales IP-1, IP-2 o IP-3 según tabla de correspondencia (Tabla 6, párr. 521).

## Números UN — referencia rápida

| UN | Nombre |
|---|---|
| 2908 | Exceptuado — embalaje vacío |
| 2909 | Exceptuado — artículos de U natural / Th |
| 2910 | Exceptuado — cantidades limitadas de material |
| 2911 | Exceptuado — instrumentos o artículos |
| 2912 | LSA-I |
| 3321 / 3322 | LSA-II / LSA-III |
| 2913 | SCO-I, II o III |
| 2915 | Tipo A, forma no especial |
| 3332 | Tipo A, forma especial |
| 2916 | Tipo B(U) |
| 2917 | Tipo B(M) |
| 3323 | Tipo C |
| 2919 | Arreglo especial |
| 2977 / 2978 | UF6 fisionable / no fisionable |
| 3324–3333 | Variantes fisionables (LSA, SCO, A, B, C) |

## Material fisionable (párrs. 417, 674–686)

U-233, U-235, Pu-239, Pu-241 y combinaciones. Capa adicional: CSI (Criticality Safety Index), límites por bulto y por medio de transporte. Excepciones del párr. 417 (ej. ≤ 15 g de nucleidos fisionables por bulto, soluciones de nitrato de uranilo, etc.). Si el caso involucra fisionable real, recomendar revisión con especialista en criticidad — fuera del alcance educativo de este skill para cálculos.
