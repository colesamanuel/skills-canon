# Checklist detallado de auditoría por pilares

Recorrer ítem por ítem. Marcar cada uno: ✅ cumple · ⚠️ mejorable · ❌ falla · ❔ sin dato. No resumir: el valor está en el detalle. Para cada ❌/⚠️, anotar la acción concreta y su impacto estimado en ocupación.

---

## Pilar A — Conversión del anuncio (la palanca #1 de ocupación)

### A1. Fotos
- [ ] Las **5 primeras** fotos muestran **5 espacios distintos** (no dos ángulos del mismo cuarto).
- [ ] Foto de portada = el espacio más distintivo, horizontal, luz óptima, sin personas, sin desorden.
- [ ] Total ~15 fotos de alta calidad para 1 dormitorio (escalar con tamaño); evitar 30-40 (fatiga).
- [ ] Líneas verticales rectas (paredes no convergen); cero desorden (cables, basura, objetos personales); sábanas planchadas.
- [ ] Photo Tour bajo control (orden de portada correcto; agrupamiento por habitación gestionado).
- [ ] Iluminación cálida/ambiental donde aplique (gatillo de confort) por encima de luz diurna plana.

### A2. Título (50 caracteres)
- [ ] Lidera con el rasgo más distintivo y específico (no adjetivos vacíos: "acogedor", "lujoso").
- [ ] **Regla de no repetición:** no describe lo obvio de la portada (si se ve piscina, no "Casa con Piscina").
- [ ] Usa el espacio para beneficios **invisibles** verificables: WiFi Mbps, early check-in, monitor/escritorio, café premium, parking.
- [ ] Escrito para humanos (CTR), no para "SEO": el keyword-stuffing no ayuda al ranking de Airbnb.

### A3. Descripción
- [ ] Escaneable: viñetas con 4-8 mejores comodidades; sin bloques densos.
- [ ] Arranca con un fragmento corto (5-10 palabras) de una reseña real de 5★.
- [ ] Cada línea aporta información nueva; no repite lo ya visible en fotos.

### A4. Amenidades y filtros
- [ ] Todas las amenidades reales marcadas (los huéspedes filtran por amenidad; un campo vacío = invisible a ese filtro).
- [ ] Activar palancas de pool de huéspedes si el mercado lo justifica: pet friendly, apto para niños/bebés, etc. (cada filtro desbloqueado amplía la demanda elegible).
- [ ] Plano de la propiedad entre fotos 6-10 (gestiona expectativa de tamaño) y mapa de distancias a pie a puntos de interés.

### A5. Configuración que afecta conversión
- [ ] Instant Book evaluado (mejora colocación; sopesar screening).
- [ ] Política de cancelación calibrada (estricta baja conversión).
- [ ] Estancia mínima no más rígida que la competencia (rigidez = menos "bookable").

### A6. Consistencia de datos estructurados (afecta match de búsqueda y filtros)
Cruzar lo que dice el resumen/campos contra lo que dice la descripción y la realidad. Las incoherencias sacan el anuncio de filtros y desalinean expectativas (genera reseñas de exactitud bajas).
- [ ] **Camas / habitaciones / capacidad:** el campo numérico coincide con la descripción y con la realidad (ej.: header "3 camas" vs descripción de 4 dormitorios con cama = inconsistencia que pierde el filtro de capacidad).
- [ ] **Baños:** número declarado vs descripción (medio baño + completos).
- [ ] **Ubicación / pin del mapa:** la zona del geocódigo (breadcrumb) coincide con la zona declarada en el texto (ej.: descripción "La Uruca, San José" vs pin en "Ulloa, Heredia"). Un pin fuera de zona pierde búsquedas por ubicación y distorsiona la distancia percibida.
- [ ] **Amenidades de seguridad:** detector de humo y CO presentes y marcados (su ausencia aparece tachada en la ficha, baja conversión y es riesgo real). Verificar también puertas/cerraduras de piscina/jacuzzi si aplica.
- [ ] **Tipo de propiedad / espacio entero vs habitación:** declarado correctamente.

---

## Pilar B — Calidad y reseñas

- [ ] Calificación global vs objetivo **Guest Favorites ≥ 4.9**.
- [ ] Subcategorías (limpieza, comunicación, exactitud, ubicación, llegada, precio): identificar la más baja → es la que arrastra.
- [ ] Exactitud del anuncio: ¿las fotos/descr. prometen lo que se entrega? (la sobre-promesa mata limpieza/exactitud).
- [ ] Volumen y recencia de reseñas (un anuncio nuevo necesita reseñas iniciales rápidas).
- [ ] Protocolo "Décima Reseña": ¿hay guion para el huésped difícil? (resolver + canal privado, no confrontar).
- [ ] Reseñas negativas presentes: ¿alguna califica para remoción real (ver benchmarks)? No malgastar disputas en opiniones subjetivas.
- [ ] Respuesta pública profesional a negativas dentro de 30 días.

---

## Pilar C — Precios y ocupación (ver `pricing-engine.md` para los cálculos)

- [ ] **BLT medido** (días de antelación promedio de reserva).
- [ ] Ocupación real a la marca del BLT vs objetivo → define la acción de tarifa de la semana.
- [ ] **Precio Base** definido y ajustado semanalmente (no "configurar y olvidar").
- [ ] **Precio Mínimo** calculado (fijos + variables + margen mínimo), ≈ mitad del Base, bloqueado como piso duro.
- [ ] Motor de terceros (PriceLabs) vs Smart Pricing nativo (sesgo documentado a ocupación sobre margen).
- [ ] **Descuento gradual** de última hora configurado (progresivo desde el BLT, tope ej. 50%, nunca bajo el Mínimo).
- [ ] **Noches huérfanas** habilitadas (huecos de 1-2 noches reservables aunque la estancia mínima sea mayor; prima opcional 20-25%).
- [ ] Precios por día de semana / temporada / eventos locales contemplados.
- [ ] **Veredicto ADR-vs-ocupación** para este mercado: ¿conviene subir tarifa y aceptar algo menos de ocupación? (calcular RevPAR neto, no ocupación bruta).
- [ ] Re-tarifación tras la comisión host-only ~15.5% (no aparecer caro por no haber ajustado).

---

## Pilar D — Operaciones

- [ ] **Buffer de limpieza** 30 min (checkout 11:00 → limpieza 11:30 → check-in 15:00) para evitar choques y burnout del personal.
- [ ] Checklist de limpieza con inspección de inventario por rotación (perdido/dañado/robado).
- [ ] Personal de limpieza pagado por encima de mercado y tratado como gerente táctico (control de daños, reposición).
- [ ] Cerradura digital fiable para check-in autónomo.
- [ ] **Mensajería automatizada**: respuesta inmediata; check-in 4 días antes (instrucciones + guía + código); mensaje de salida la mañana del checkout. Mensajes <100 palabras, info solo cuando se necesita.
- [ ] Táctica "sorpresa y deleite": goodie bag revelado la mañana del checkout (intercepta el momento de la reseña).
- [ ] Sincronización multicanal Airbnb/Vrbo/Booking (channel manager) para evitar doble reserva y bloqueos manuales.

---

## Pilar E — Mercado / competencia (requiere datos; ❔ si no hay)

- [ ] Percentil 90 de ocupación del mercado (top 10%) como referencia, no el promedio.
- [ ] Micro-vecindario correcto identificado (demanda más fuerte dentro de la ciudad).
- [ ] ADR y ocupación vs comparables directos del barrio.
- [ ] Estacionalidad y eventos locales que el calendario debería capturar.
- (Datos obtenibles vía export del PMS, observación manual de comparables, o módulo opcional de API de terceros con llave del titular.)
