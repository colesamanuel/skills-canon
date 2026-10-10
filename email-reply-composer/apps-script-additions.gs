/**
 * ADD-ON PARA EL ENDPOINT DE COLÉ — email-reply-composer
 *
 * Agrega dos acciones nuevas: updateReply y findDraftInThread.
 * No modifica createReply ni ping existentes.
 *
 * Instrucciones de deploy al final del archivo.
 *
 * Validado contra Apps Script Gmail service (2026).
 */


// ============================================================================
// updateReply_  —  Actualiza el contenido de un draft existente por draftId.
//                  Preserva threading (el draft object está vinculado al thread).
// ============================================================================
function updateReply_(params) {
  var draftId = params.draftId;
  if (!draftId) {
    return jsonResponse({ ok: false, error: 'updateReply requires draftId' });
  }

  var draft;
  try {
    draft = GmailApp.getDraft(draftId);
  } catch (e) {
    return jsonResponse({ ok: false, error: 'Draft not found: ' + draftId + ' (' + e.message + ')' });
  }
  if (!draft) {
    return jsonResponse({ ok: false, error: 'Draft not found: ' + draftId });
  }

  var oldMsg = draft.getMessage();
  var thread = oldMsg.getThread();
  var threadId = thread.getId();
  var to = oldMsg.getTo();
  var subject = oldMsg.getSubject();

  // El método GmailDraft.update(recipient, subject, body, options) exige body como string.
  // Si viene htmlBody se pasa en options; si no, se usa params.body como plain text.
  var options = {};
  if (params.htmlBody) options.htmlBody = params.htmlBody;
  if (params.cc && params.cc.length) options.cc = params.cc.join(',');
  if (params.bcc && params.bcc.length) options.bcc = params.bcc.join(',');
  if (params.replyTo) options.replyTo = params.replyTo;

  var bodyText = params.body || '';  // plain text fallback (obligatorio como positional arg)

  try {
    draft.update(to, subject, bodyText, options);
  } catch (e) {
    return jsonResponse({ ok: false, error: 'update failed: ' + e.message });
  }

  // Refrescar el draft para devolver el messageId actualizado
  var updated = GmailApp.getDraft(draftId);
  var newMsg = updated.getMessage();

  return jsonResponse({
    ok: true,
    draftId: updated.getId(),
    messageId: newMsg.getId(),
    threadId: newMsg.getThread().getId(),
    subject: subject,
    updated: true,
    permalink: 'https://mail.google.com/mail/u/0/#drafts/' + updated.getId()
  });
}


// ============================================================================
// findDraftInThread_  —  Consulta si existe un draft del usuario en un threadId.
//                        Read-only. Devuelve draftId (o null si no hay).
// ============================================================================
function findDraftInThread_(params) {
  var threadId = params.threadId;
  if (!threadId) {
    return jsonResponse({ ok: false, error: 'findDraftInThread requires threadId' });
  }

  var drafts;
  try {
    drafts = GmailApp.getDrafts();
  } catch (e) {
    return jsonResponse({ ok: false, error: 'Cannot list drafts: ' + e.message });
  }

  for (var i = 0; i < drafts.length; i++) {
    try {
      var d = drafts[i];
      var msg = d.getMessage();
      if (msg.getThread().getId() === threadId) {
        return jsonResponse({
          ok: true,
          draftId: d.getId(),
          messageId: msg.getId(),
          threadId: threadId,
          subject: msg.getSubject()
        });
      }
    } catch (e) {
      // Ignorar drafts corruptos y continuar
      continue;
    }
  }

  return jsonResponse({
    ok: true,
    draftId: null,
    threadId: threadId
  });
}


// ============================================================================
// ROUTER — Agregar estas dos líneas dentro de doPost, junto a donde ya se
// manejan 'ping' y 'createReply'. NO reemplazar el router completo; solo
// añadir estas dos entradas.
// ============================================================================
/*
   Ejemplo de cómo debe quedar el router (fragmento):

   function doPost(e) {
     var params = JSON.parse(e.postData.contents);

     // Validación de secret (ya existente — NO tocar)
     if (params.secret !== SCRIPT_SECRET) {
       return jsonResponse({ ok: false, error: 'Bad secret' });
     }

     // --- Acciones existentes ---
     if (params.action === 'ping')        return jsonResponse({ ok: true, pong: true });
     if (params.action === 'createReply') return createReply_(params);

     // --- Acciones NUEVAS (agregar estas dos líneas) ---
     if (params.action === 'updateReply')        return updateReply_(params);
     if (params.action === 'findDraftInThread')  return findDraftInThread_(params);

     return jsonResponse({ ok: false, error: 'Unknown action: ' + params.action });
   }
*/


// ============================================================================
// PASOS DE DEPLOY
// ============================================================================
/*
   1. Abrir https://script.google.com y entrar al proyecto del endpoint
      (el mismo que tiene createReply y ping).

   2. Pegar las funciones updateReply_ y findDraftInThread_ al final de Code.gs
      (o en un archivo nuevo del proyecto — Apps Script comparte scope global).

   3. Modificar la función doPost para agregar las dos líneas del router
      indicadas en el bloque de arriba.

   4. Deploy → Manage deployments → lápiz del deploy activo →
      Version: New version → Description: "Add updateReply + findDraftInThread"
      → Deploy.

      IMPORTANTE: usar "New version" del deploy existente, NO "New deployment",
      para que la URL del endpoint no cambie.

   5. La primera ejecución puede pedir re-autorizar scopes (Gmail read + modify).
      Aceptar el prompt.

   6. Verificar con curl:

      URL='https://script.google.com/macros/s/AKfycbxc6H0RDld4DRSDHlUiUxCcDWkWDILtGvtqIAHF_joLEmxjXsBbQqqPQme2VKEGPn0ePw/exec'
      SECRET="${EMAIL_REPLY_APPS_SCRIPT_SECRET:?Falta EMAIL_REPLY_APPS_SCRIPT_SECRET}"

      # Test findDraftInThread contra un thread sin draft
      curl -sL "$URL" -H 'Content-Type: application/json' -d \
        '{"secret":"'"$SECRET"'","action":"findDraftInThread","threadId":"<un thread id sin draft>"}'
      # Esperado: {"ok":true,"draftId":null,"threadId":"..."}

      # Test contra el hilo SONDA (que tiene drafts que dejé el 15-jul)
      curl -sL "$URL" -H 'Content-Type: application/json' -d \
        '{"secret":"'"$SECRET"'","action":"findDraftInThread","threadId":"19e6183a83a09256"}'
      # Esperado: {"ok":true,"draftId":"r...","messageId":"...","threadId":"19e6183a83a09256","subject":"..."}

      # Test updateReply contra un draft existente
      curl -sL "$URL" -H 'Content-Type: application/json' -d \
        '{"secret":"'"$SECRET"'","action":"updateReply","draftId":"<draftId>","htmlBody":"<p>Nuevo contenido de prueba</p>"}'
      # Esperado: {"ok":true,"draftId":"<mismo id>","messageId":"...","threadId":"...","updated":true,...}

   7. Confirmar que el draft actualizado sigue anidado al hilo original
      (abrir Gmail → Borradores → el hilo → verificar que el draft está dentro).
*/
