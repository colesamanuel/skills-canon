# ⚠️ Manejo de secretos antes de versionar

Estos 5 archivos contienen tu **API key de Odoo en texto plano**:

- cole/card-reconciler/SKILL.md
- cole/email-marketing-odoo/SKILL.md
- cole/odoo-invoice-auditor-v2b/audit_invoices.py
- cole/odoo-quotation-generator/SKILL.md
- cole/social-media-cole/SKILL.md

## Riesgo
Si subís este repo a un host **público**, la key queda expuesta y un tercero podría
operar tu Odoo (facturar, leer clientes, etc.).

## Mitigaciones (elegí una)
1. **Mínimo:** repositorio **PRIVADO** obligatorio (GitHub private / GitLab private / Bitbucket).
2. **Recomendado:** extraer la key a una variable de entorno o a un archivo
   `secrets.local.json` listado en `.gitignore`, y que cada script la lea de ahí.
3. Si la key ya estuvo en cualquier repo público alguna vez: **rotarla** en Odoo
   (Ajustes → Usuario → API Keys → revocar y regenerar).

Decisión tuya (perfil §10.3). Esta nota solo señala el riesgo; no modifiqué los archivos.
