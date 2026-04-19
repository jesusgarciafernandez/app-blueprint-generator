---
title: Patrones de Diseño Agénticos (Agentic Design Patterns & Robust AI)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 07. Inteligencia Artificial
subcategory: 07.2 Automatización Agéntica
tags: [ia, agentes, design-patterns, reflection, planning, tool-use, multi-agent, agentic-workflows, robustness, prompt-engineering-v2, autonomous-logic]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 202
---

## 0. Filosofía Human-Centric AI
*Esta habilidad establece las leyes fundamentales de construcción para sistemas de inteligencia artificial autónomos, utilizando la tecnología para implementar estructuras de razonamiento probadas (patrones) y permitir que el humano diseñe agentes que no solo responden, sino que piensan, planifican y aprenden de sus propios errores de manera robusta y predecible.*

**El Rol del Humano:** El Arquitecto de Patrones Agénticos debe ser un "Garantes de la Maestría Estructural". La IA puede seguir instrucciones complejas y ejecutar ciclos de mejora continua (Reflexión), pero solo el humano puede definir la arquitectura que garantiza la estabilidad del sistema, elegir el patrón adecuado para cada desafío de negocio (Ej: ¿Necesitamos un agente que planifique o uno que reaccione?) y asegurar que los bucles de autonomía de la IA incluyan puntos de control humano que eviten la deriva algorítmica o la ejecución de acciones indeseadas.
**Empoderamiento:** Usamos la tecnología para sustituir la improvisación en el prompting por una ingeniería de software aplicada a la inteligencia artificial.

---

## 1. Descripción Detallada
Patrones de Diseño Agénticos (v2.0) es la competencia de aplicar estructuras arquitectónicas recurrentes para mejorar el rendimiento de los LLMs en tareas autónomas. No es solo "pedirle a la IA que haga cosas"; es **Arquitectura del Razonamiento Sintético**. El enfoque v2.0 se basa en los 4 pilares de Andrew Ng: **Reflexión** (el agente revisa su propio trabajo), **Planificación** (desglose de metas en pasos), **Uso de Herramientas** (interacción con APIs/DBs) y **Colaboración Multi-Agente** (división de roles). El objetivo es pasar de una interacción de "un solo disparo" (Zero-shot) a flujos de trabajo iterativos (Agentic Workflows) que multiplican la precisión y fiabilidad del sistema.

## 2. Escenarios de Aplicación
- **Sistemas de Self-Correction para Código:** Agentes que escriben código, lo intentan ejecutar, leen el error en la consola y se auto-corrigen hasta que el test unitario pasa (Patrón de Reflexión).
- **Planificación de Proyectos de Marketing:** Un agente que primero diseña un cronograma detallado de 10 pasos y luego ejecuta cada paso secuencialmente, ajustando el plan si surge un imprevisto (Patrón de Planificación).
- **Asistentes de Investigación con Herramientas Reales:** Agentes que saben cuándo buscar en Google, cuándo leer un PDF local y cuándo consultar una base de datos SQL para responder (Patrón de Tool-use).
- **Flujos de Debate para Calidad Extrema:** Uso de dos agentes con visiones contrapuestas (Crítico vs Creador) para refinar un documento hasta alcanzar la excelencia (Patrón Multi-Agente).
- **Pipelines de Extracción de Datos Resistentes a Errores:** Sistemas que validan el formato de salida y, si no es el correcto, reintento la tarea con un prompt de corrección automático.

## 3. Requisitos de Implementación
- **Entendimiento de Cadenas de Pensamiento (CoT):** Conocimiento de cómo guiar al modelo para que "piense en voz alta" antes de actuar.
- **Frameworks de Orquestación Agéntica:** Uso de LangChain, CrewAI, AutoGen o PydanticAI para implementar la jerarquía de llamadas.
- **Domino de Esquemas Estructurados (JSON/Pydantic):** Capacidad para forzar salidas que los sistemas de software puedan procesar de forma determinista.
- **Gestión de 'State' y Memoria:** Habilidad para pasar el estado de la tarea entre diferentes iteraciones del agente sin pérdida de información.

---

## 4. Diferencial: Prompting Lineal vs. Patrones Agénticos v2.0

| Dimensión | Enfoque Legacy (Zero-shot) | Patrones Agénticos (v2.0) |
| :--- | :--- | :--- |
| **Precisión** | Baja; acierto a la primera o fallo. | Muy alta; el sistema itera hasta acertar. |
| **Complejidad** | Limitada a tareas simples. | Capaz de resolver misiones multi-etapa. |
| **Fiabilidad** | Impredecible; depende del "humor" del modelo. | Determinista; basada en protocolos de validación. |
| **Autonomía** | Requiere que el humano guíe cada paso. | El humano define la meta y el patrón guía la ejecución. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Selección del Patrón y Diseño del Flujo
**Objetivo:** Elegir la estructura de razonamiento que mejor resuelve el problema.
1.  **Diagnóstico de la Tarea:** IA ayuda a determinar si el reto requiere crítica interna (Reflexión) o coordinación de especialistas (Multi-agente).
2.  **Diseño de los Nodos de Control:** Definición de qué sucede entre una llamada y la siguiente (Ej: "Si el código falla, vuelve al nodo de edición").

**Prompt Maestro de Patrones Agénticos (Agentic Design):**
```text
Actúa como un Senior AI Architect y Experto en Agentic Workflows. Diseña el sistema autónomo para [MISIÓN/TAREA]. 
1. Selección de Patrón: ¿Usaremos Reflexión, Planificación o Multi-Agente? Justifica por qué esta estructura es la más robusta para este caso. 
2. Diseño del 'Loop' de Mejora: Define los criterios que el agente usará para auto-evaluar su trabajo (Rúbrica de crítica interna). 
3. Definición de Herramientas (Tools): Lista las habilidades externas que el agente debe invocar y cómo manejaremos una respuesta de error del software. 
4. Punto de Escalamiento Humano: Define la 'Condición de Parada' en la que el agente debe dejar de iterar y pedir ayuda al humano (Ej: Tras 3 intentos fallidos). 
5. Esquema de Salida (Output Schema): Genera el modelo Pydantic o JSON que asegure que el resultado final sea estructurado y validable.
```

### Fase 2: Implementación, Calibración y Red Teaming
... (Expansión técnica sobre el uso de la técnica de 'Self-Consistency' para votar entre múltiples caminos de razonamiento, la implementación de límites de recursividad (Max Loops) para evitar costes infinitos y la creación de tests de 'Robustez Agéntica' donde se introducen fallos a propósito para ver si el patrón de diseño es capaz de recuperarse solo) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de razonamiento iterativo.*

1.  **Trigger:** Recepción de una misión compleja de larga duración.
2.  **Nodo de Planificador (Planner):** IA descompone la misión en una lista jerárquica de subtareas ejecutables.
3.  **Nodo de Ejecución y Reflexión:** El agente realiza la primera subtarea, revisa el resultado y, si es necesario, vuelve a ejecutar con correcciones.
4.  **Nodo de Verificación de Hitos:** Un proceso supervisor valida que el paso actual es correcto antes de permitir el avance al siguiente punto del plan.
5.  **Output:** Resultado final verificado y consolidado; el sistema genera un informe del proceso de "Pensamiento" seguido para auditoría humana.

---

## 7. Ejemplo Práctico: Agencia de Traducción 'ContextTrans'
**Reto:** Traducir libros técnicos de 400 páginas manteniendo la coherencia de términos complejos. Un traductor de IA estándar (GPT) cometía errores de glosario a partir de la página 50.
**Acción v2.0:** Implementaron un Patrón de Reflexión. Un agente traducía el capítulo, otro comparaba los términos con el "Glosario de Oro" y, si encontraba una discrepancia, obligaba al primero a re-traducir el párrafo.
**Resultado:** La calidad fue idéntica a la traducción humana experta. El sistema se auto-corrigió en más de 200 puntos críticos sin intervención del supervisor, que solo validó el resultado final impecable.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
