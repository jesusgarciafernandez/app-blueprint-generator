---
title: UX Writing, Diseño de Contenido y Narrativa de Interfaz
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 02. Generación de Contenido
subcategory: Diseño UI/UX
tags: [ux-writing, microcopy, content-design, voice-and-tone, user-experience, accessibility, localization, emotional-design, ia-copy-gen]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 076
---

## 0. Filosofía Human-Centric AI
*Esta habilidad utiliza el poder de la palabra para guiar, proteger y empoderar al ser humano en el entorno digital, utilizando la IA para simplificar el lenguaje y profundizar en la empatía verbal.*

**El Rol del Humano:** El UX Writer debe ser un "Arquitecto del Lenguaje Útil". La IA puede generar variantes de texto, corregir gramática y resumir contenidos técnicamente perfectos, pero solo el humano puede imbuir al mensaje de la "intencionalidad" ética necesaria, decidir qué tono de voz genera calma en un momento de error crítico y asegurar que la narrativa verbal respete la dignidad del usuario, evitando la manipulación y fomentando la claridad absoluta.
**Empoderamiento:** Usamos la tecnología para automatizar la traducción, la consistencia de terminología y la generación de borradores de microcopy, permitiendo que el experto se centre en la estrategia narrativa global y en la excelencia de la comunicación humana.

---

## 1. Descripción Detallada
El UX Writing es el diseño de contenido verbal para productos digitales. No es solo "escribir textos"; es **Ingeniería del Guion de Interacción**. El enfoque v2.0 incorpora el **Diseño de Microcopy de Alta Precisión y la Estrategia de Voz y Tono**, donde se diseñan mensajes de error, etiquetas de botones (CTAs), flujos de onboarding y sistemas de ayuda que reducen la carga cognitiva, eliminan la fricción operativa y humanizan la relación marca-usuario mediante un lenguaje claro, conciso y útil.

## 2. Escenarios de Aplicación
- **Optimización de Flujos Transaccionales (Pago/Registro):** Eliminación de dudas de último segundo mediante textos de confirmación empáticos y claros.
- **Rediseño de Mensajería de Error y Feedback:** Transformación de códigos técnicos crípticos en instrucciones humanas accionables y tranquilizadoras.
- **Definición del Manual de Voz y Tono de Marca:** Creación de una personalidad verbal consistente en todos los puntos de contacto de la App/Web.
- **Arquitectura de Ayuda y Centros de Conocimiento:** Estructuración de la información para que sea escaneable y resolutiva para el usuario con prisa.
- **Localización y Adaptación Cultural:** Garantía de que el mensaje no solo se traduce, sino que resuena con los valores y giros idiomáticos locales.

## 3. Requisitos de Implementación
- **Maestría en Síntesis y Claridad Verbal:** Capacidad de comunicar el máximo valor en el mínimo número de caracteres (Plain Language).
- **Psicología de la Lectura Digital:** Conocimiento de patrones de escaneo (F, Z, Spotted), carga cognitiva y jerarquía de la información.
- **Uso de Herramientas de Diseño Colaborativo:** Figma (plugins de copy), Notion para diccionarios de marca y herramientas de testeo de contenido (Cloze Test).

---

## 4. Diferencial: Redacción Genérica vs. UX Writing de Alta Densidad v2.0

| Dimensión | Enfoque "Rellenar huecos" | UX Writing Estratégico (v2.0) |
| :--- | :--- | :--- |
| **Meta** | Decorar / Informar. | Guiar / Ayudar / Convertir. |
| **Tono** | Neutro / Inconsistente. | Intencional / Marca-consciente / Empático. |
| **Estructura** | Párrafos largos. | Escaneabilidad total y jerarquía verbal. |
| **Relación** | Informativa (Maquinal). | Conversacional (Humana). |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Auditoría de Fricción Verbal y Definición del Tono
**Objetivo:** Identificar dónde el lenguaje está bloqueando al usuario y fijar la personalidad.
1.  **Red Flag Audit:** Busca mensajes que digan "error", "prohibido" o que usen jerga interna que el usuario no entienda.
2.  **Definición de las Dimensiones del Tono:** ¿Somos serios o divertidos? ¿Entusiastas o calmados? Crea una matriz de tono para diferentes escenarios (Ej: Tono entusiasta en el éxito, calmado y protector en el error).

**Prompt Maestro de Dirección de UX Writing:**
```text
Actúa como Director de UX Writing y Estratega de Contenido Digital. Para el flujo de [FLUJO], realiza el siguiente plan de diseño verbal: 
1. Redacta el 'Microcopy Maestro': Títulos, etiquetas de botones y textos de apoyo que sean 100% claros y 0% ambiguos. 
2. Diseña los 'Mensajes de Recuperación de Error': Di qué ha pasado, por qué es importante y qué debe hacer el usuario ahora. 
3. Establece la 'Jerarquía de Escaneo': Usa negritas, listas y titulares para que el usuario entienda la esencia en < 2 segundos. 
4. Crea la guía de 'Voz de Marca' para este contexto: [Ej: Hablamos al usuario como un 'Guía experto' que le facilita el camino]. 
5. Protocolo de 'Inclusividad y Accesibilidad': Asegura que el lenguaje es neutro, evita sesgos y es fácil de leer para personas con neurodiversidad.
```

### Fase 2: Aplicación, Test de Comprensión y Ajuste Iterativo
... (Expansión técnica sobre la realización de 'Cloze Tests' -rellenar huecos- para medir la previsibilidad del lenguaje, el ajuste de longitudes de línea para legibilidad móvil y la validación en tests A/B de impacto en la conversión) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de auditoría de copy automatizada.*

1.  **Trigger:** El equipo de desarrollo añade un nuevo mensaje de aviso al sistema de gestión de facturas.
2.  **Nodo de Análisis de Legibilidad IA:** El sistema detecta que la frase usa la voz pasiva y palabras excesivamente complejas ("Se procederá a la obliteración de la deuda").
3.  **Nodo de Sugerencia de Humanización:** IA propone 3 variaciones: "Pago completado con éxito", "Factura pagada" o "¡Todo listo! Tu pago ha llegado".
4.  **Nodo de Verificación de Marca:** El sistema comprueba que el tono coincide con el manual de estilo (Ej: Si la marca es joven, descarta las opciones demasiado formales).
5.  **Output:** Sugerencia de cambio enviada directamente al Product Manager para su validación rápida antes de publicar.

---

## 7. Ejemplo Práctico: App de Banca para Autónomos
**Reto:** El proceso de "Transferencia Internacional" fallaba mucho porque la gente no entendía qué era el "SWIFT/BIC". El mensaje de error era: "Error 504: Invalid code".
**Acción v2.0:** Se cambió el copy. Se añadió un texto de ayuda: "Este código suele empezar por el nombre de tu banco (ej. BBVA, SANT)". El error se cambió a: "Parece que falta una letra en el código. ¿Puedes revisarlo?".
**Resultado:** Los errores de transferencia bajaron un 40% y las llamadas al soporte técnico por "problemas con el código" se redujeron drásticamente.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
