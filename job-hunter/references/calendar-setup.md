# Calendar setup — Job Hunter

## Evento recurrente recomendado

**Calendar:** Cole S.A. (`a6bitvljhejddblgg1dqglmrq4@group.calendar.google.com`)

**Título:** `🔍 Job Hunt — [Nombre del candidato]`

**Frecuencia:** Lunes / Miércoles / Viernes a las 09:00 Costa Rica (15:00 UTC)

**Duración:** 30 minutos (tiempo de reserva, no es trabajo activo del usuario; es el tiempo que tarda el skill).

**Recordatorio:** 10 minutos antes (notificación móvil).

**Frase trigger en descripción del evento** (debe ser literal para activar el skill):
```
tarea diaria de [Nombre del candidato]
```

Esto permite al usuario abrir el evento desde su teléfono, copiar la frase trigger, y pegarla en Claude para disparar el skill.

---

## Casos de uso por candidato

Cada candidato activo tiene su propio evento recurrente. Naming convention:

- `🔍 Job Hunt — Eddy` (perfil `eddy_fresno.json`)
- `🔍 Job Hunt — [siguiente candidato]` (cuando se agregue)

---

## Cuándo desactivar el evento

El evento del candidato se desactiva (no se elimina) cuando:

1. El candidato confirma que aceptó una oferta y firmó contrato.
2. El candidato pide pausar la búsqueda por motivos personales.
3. Después de 8 ejecuciones (4 semanas) sin reporte de aplicaciones por parte del usuario, ofrecer revisar si el candidato sigue activo en el mercado.

Para desactivar: cambiar el evento a "no se repite" y agregar `[PAUSADO]` al título.

---

## Cómo crear el evento desde Claude

```
Crea un evento recurrente en el calendar de Cole S.A. con:
- Título: 🔍 Job Hunt — [Nombre]
- Recurrencia: lun/mié/vie a las 09:00 hora CR
- Duración: 30 min
- Recordatorio: 10 min antes
- Descripción: "tarea diaria de [Nombre]"
```

El skill `gmail-briefing` ya está configurado para escribir al calendar Cole S.A. Si Claude no lo hace por defecto, indicar el `calendarId` específico arriba.
