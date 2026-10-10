# job-hunter

Skill personalizado para Manuel Rubio (Colé S.A.) que automatiza la búsqueda y auditoría de ofertas de empleo activas para candidatos de su red profesional.

## ¿Qué hace?

Ejecuta un pipeline de 5 fases:
1. Carga el perfil del candidato desde `assets/profiles/`
2. Barre múltiples job boards (Get on Board, HN Hiring, Real Work From Anywhere, AgileEngine, Gorilla Logic, IceRock, etc.)
3. **Verifica HTTP cada oferta candidata** — sin verificación no hay reporte
4. Filtra por elegibilidad geográfica
5. Genera reporte tabular + borrador de correo al candidato

## ¿Cómo se activa?

Frase trigger principal: `tarea diaria de [nombre del candidato]`

Ejemplos:
- `tarea diaria de Eddy`
- `ofertas para Eddy`
- `briefing Eddy`
- `job hunt Eddy`

## Estructura

```
job-hunter/
├── SKILL.md               # Pipeline principal y reglas duras
├── assets/
│   ├── email-template.md  # Plantilla del borrador de correo
│   └── profiles/
│       └── eddy_fresno.json  # Perfil del primer candidato
├── references/
│   ├── sources-catalog.md     # Catálogo de fuentes con tier de calidad
│   ├── talent-pools.md        # Pools de staffing/EOR (separados de ofertas)
│   └── calendar-setup.md      # Setup del evento recurrente
├── scripts/
│   └── update_state.py    # Utilidad CLI para mantener seen.json
└── state/
    └── seen.json          # Estado persistente entre ejecuciones
```

## Instalación

1. Subir el ZIP del skill a Claude.
2. Crear evento recurrente en Calendar Cole S.A. con frecuencia lun/mié/vie a las 09:00 CR (descripción: `tarea diaria de [Nombre]`).
3. Para agregar candidatos nuevos: copiar `assets/profiles/eddy_fresno.json` como template, ajustar campos.

## Frecuencia

Recomendada: lun/mié/vie. Diaria genera ruido (las ofertas no rotan tan rápido). Semanal pierde ofertas que cierran rápido en Get on Board (~250-300 aplicaciones).

## Versión

v1.0 — 06-Mayo-2026
