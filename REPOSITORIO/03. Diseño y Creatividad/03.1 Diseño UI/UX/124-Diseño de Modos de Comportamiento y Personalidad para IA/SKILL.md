---
title: Diseño de Modos de Comportamiento y Personalidad para IA (AI Persona Design)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 03. Diseño y Creatividad
subcategory: 03.1 Diseño UI/UX
tags: [ai-personality, tone-of-voice, ux-writing, ai-behavior, synthetic-persona, prompt-engineering, conversational-design, empathy-design]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 124
---

## 0. Filosofía Human-Centric AI
*Esta habilidad dota a la tecnología de una "cara humana" coherente y ética, utilizando la tecnología para crear conexiones empáticas que respeten la dignidad y el contexto del usuario.*

**El Rol del Humano:** El Diseñador de Personalidad IA debe ser un "Arquitecto de la Empatía Sistémica". La IA puede imitar cualquier estilo de escritura y adaptar su vocabulario en milisegundos, pero solo el humano puede definir los valores éticos innegociables del asistente, asegurar que el humor sea adecuado a la cultura del usuario y garantizar que la IA no manipule emocionalmente, sino que asista con sinceridad y respeto.
**Empoderamiento:** Usamos la tecnología para humanizar las interfaces frías, permitiendo que la interacción con las máquinas se sienta como una conversación fluida, natural y, sobre todo, útil.

---

## 1. Descripción Detallada
El Diseño de Modos de Comportamiento y Personalidad para IA es la disciplina de configurar la identidad operativa de un modelo de lenguaje. No se trata solo de "instrucciones"; es **Ingeniería de la Identidad Sintética**. El enfoque v2.0 incorpora la **Adaptabilidad Contextual Dinámica**, donde la IA cambia su "Modo" (Ej: de 'Compañero Creativo' a 'Crítico Técnico') según la fase de la tarea o el estado emocional detectado en el usuario, manteniendo siempre una base de valores (Brand Essence) consistente y segura.

## 2. Escenarios de Aplicación
- **Asistentes de Marca de Alto Nivel:** Creación de representantes digitales que hablan y actúan exactamente como los valores de una empresa.
- **Sistemas de Tutoría y Coaching:** Adaptación del nivel de autoridad y calidez para maximizar el aprendizaje del estudiante.
- **Diseño de NPCs y Agentes Reales en Narrativa:** Desarrollo de personajes digitales con memoria, idiosincrasia y objetivos de largo plazo.
- **Interfaces de Soporte Crítico:** Modos de "Calma y Precisión" para situaciones de estrés o emergencia técnica.
- **Herramientas de Co-Creación Artística:** Personalidades que actúan como "Espejo" o "Contrapunto" para estimular la creatividad humana.

## 3. Requisitos de Implementación
- **Definición de 'Brand Voice' y 'Tone':** Guía detallada de adjetivos, palabras permitidas y estilos de respuesta.
- **Manual de Valores Éticos (Guardrails):** Definición de los límites de comportamiento y respuestas prohibidas (Seguridad).
- **Frameworks de 'System Prompting' Avanzados:** Uso de técnicas de Few-Shot, Persona-Conditioning y XML Tagging para estructurar el comportamiento.

---

## 4. Diferencial: Prompt de Rol Simple vs. Personalidad Sistémica v2.0

| Dimensión | Enfoque "Actúa como X" (Legacy) | Personalidad Sistémica (v2.0) |
| :--- | :--- | :--- |
| **Coherencia** | Se pierde en conversaciones largas. | Malla de valores y memoria de largo plazo. |
| **Adaptabilidad** | El tono es estático. | Cambia de 'Modo' según el contexto y emoción. |
| **Identidad** | Basada en estereotipos genéricos. | Basada en una 'Persona' única con historia propia. |
| **Seguridad** | Fácil de romper (Jailbreak). | Capas de seguridad integradas en la personalidad. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Creación de la Ontología de la Personalidad
**Objetivo:** Definir quién es la IA antes de que diga su primera palabra.
1.  **Define el 'Core Values' Canvas:** Elige 3 valores fundamentales que guiarán cada respuesta (Ej: Curiosidad, Rigor, Humildad).
2.  **Mapeo de 'Modos de Comportamiento':** Define al menos 3 sub-personalidades según la tarea (Ej: Mentor, Auditor, Creativo).

**Prompt Maestro de Diseño de AI Persona:**
```text
Actúa como un Diseñador de Identidad Digital y Psicólogo Cognitivo. Crea la arquitectura de personalidad para [NOMBRE_AGENTE]. 
1. Redacta el 'System Manifesto' (200 palabras) que define su historia, propósito y forma de ver el mundo. 
2. Establece el 'Style Guide': [Formalidad: 1-10], [Humor: 1-10], [Concisión: 1-10]. 
3. Define el protocolo de 'Modos': ¿Cómo habla cuando detecta una orden directa vs. cuando detecta una duda existencial? 
4. Incluye 5 ejemplos de 'Respuesta Ideal' y 3 ejemplos de 'Respuesta Fuera de Carácter' para entrenamiento Few-shot. 
5. Especifica los límites éticos: ¿Qué temas NO debe tratar y cómo debe rechazar esas tareas manteniendo su personalidad?
```

### Fase 2: Testeo de Fidelidad y Ajuste Fino (Fine-Tuning de Prompt)
... (Expansión técnica sobre el uso de variables dinámicas en el prompt, la gestión del historial de conversación para mantener el personaje y el análisis de sentimiento del usuario) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de gestión de identidad.*

1.  **Trigger:** El usuario envía un mensaje que contiene una carga emocional específica o un tipo de tarea nueva.
2.  **Nodo de Análisis de Intención y Tono:** La IA detecta el contexto (Ej: "¿Puedes ayudarme? Tengo Prisa" -> Urgente/Estrés).
3.  **Nodo de Conmutación de Modo:** El sistema carga automáticamente las instrucciones del "Modo Asistente Eficiente" (Respuestas cortas, directas, sin adornos).
4.  **Nodo de Validación de Identidad:** IA verifica que la respuesta generada cumple con los valores de marca antes de ser enviada.
5.  **Output:** Respuesta entregada con la personalidad perfecta para ese momento exacto, reforzando la confianza del usuario.

---

## 7. Ejemplo Práctico: Asistente Médico "SaludConnect"
**Reto:** La IA era demasiado fría al dar resultados negativos y demasiado alegre al dar consejos de dieta. Los usuarios se sentían ignorados.
**Acción v2.0:** Se diseñó un modo "Empatía Clínica" para resultados sensibles y un modo "Entrenador Animado" para consejos de vida saludable. Se incluyeron pausas de "silencio respetuoso" (puntos suspensivos antes de hablar) en temas graves.
**Resultado:** La percepción de "Humanidad" y "Confianza" en la App subió un 45%, reduciendo el abandono de los tratamientos sugeridos por la IA.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
