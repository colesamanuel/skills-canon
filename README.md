# Skills Canon — Ing. Manuel Rubio, MSc

Fuente única de verdad de las skills personales y corporativas. El canon contiene
52 skills en una estructura plana: cada directorio de primer nivel es una skill y
debe contener `SKILL.md`.

## Regla de operación

1. Crear o actualizar skills únicamente en este repositorio.
2. Hacer que Claude trabaje directamente sobre esta carpeta, no sobre copias de sesión.
3. Exponer las skills a Codex y Gemini mediante enlaces de directorio.
4. No copiar manualmente versiones entre `.codex`, `.gemini` y Claude.
5. Confirmar cambios con Git después de validar las skills.

## Automatización local

`tools/Sync-Skills.ps1` crea los enlaces faltantes hacia `.codex\skills` y
`.gemini\skills`. No reemplaza carpetas físicas ni corrige conflictos de forma
automática. Se ejecuta al iniciar sesión mediante la tarea `Skills Canon Sync`.
`sync-exclusions.json` conserva en el canon las skills específicas de Claude o que
duplican capacidades integradas, pero evita enlazarlas a consumidores incompatibles.

La separación entre operaciones de Colé S.A. y patrimonio personal sigue siendo
obligatoria aunque la estructura sea plana. Las reglas de identidad se encuentran
en cada skill, especialmente `cole-brand-identity`.

## Secretos

Las credenciales no se versionan. Los flujos actuales usan:

- `ODOO_API_KEY`
- `EMAIL_REPLY_APPS_SCRIPT_SECRET`

Leer `SECRETOS-LEER-PRIMERO.md` antes de publicar o rotar credenciales.
