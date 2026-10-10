# Manejo de secretos

El árbol de trabajo actual no debe contener credenciales literales. Las integraciones
leen sus valores desde variables de entorno:

- `ODOO_API_KEY`: acceso JSON-RPC a Odoo.
- `EMAIL_REPLY_APPS_SCRIPT_SECRET`: autenticación del endpoint de borradores Gmail.

## Incidente pendiente

Este repositorio es público y las credenciales anteriores estuvieron presentes en
su historial. Eliminarlas del árbol actual no revoca las copias ya publicadas.

Acciones obligatorias:

1. Revocar la API key anterior en Odoo y generar una nueva.
2. Cambiar el secreto del endpoint Apps Script y volver a desplegarlo.
3. Actualizar las dos variables de entorno con los valores nuevos.
4. Reiniciar Claude, Codex, Gemini y cualquier terminal que deba heredarlas.
5. Reescribir el historial de Git o crear un repositorio nuevo sin secretos.

No pegar credenciales en chats, skills, scripts, ejemplos, logs o commits.
