---
title: Inteligencia Artificial (LLM & RAG Master)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 07. Inteligencia Artificial
subcategory: Modelos de Lenguaje
tags: ["estándar-v1.1", "validado", "ai", "llm", "openai", "anthropic", "rag"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 007-IA
---

## Descripción
Esta skill proporciona las capacidades necesarias para integrar modelos de lenguaje de gran tamaño (LLMs) y sistemas de recuperación de información aumentada por generación (RAG) en cualquier aplicación. Cubre desde el diseño de prompts avanzados (Prompt Engineering) hasta la orquestación de agentes autónomos, permitiendo que la aplicación razone, genere contenido y procese información de manera inteligente.

## Cuándo usarla
- **Asistentes Inteligentes**: Creación de chatbots que comprenden el contexto del usuario.
- **Procesamiento de Datos**: Extracción de información estructurada a partir de texto no estructurado.
- **Generación de Contenido**: Automatización de redacción creativa, técnica o de código.
- **Búsqueda Semántica**: Implementación de sistemas RAG que consultan bases de conocimientos locales.

## Requisitos
- **Stack Recomendado**: OpenAI API (GPT-4o), Anthropic Claude 3.5, LangChain / LlamaIndex.
- **Herramientas**: Pinecone / Weaviate (Bases de datos vectoriales), MCP (Model Context Protocol).
- **Variables**: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `SERPAPI_KEY`.

## Impacto Humano y Empoderamiento Personal
La Inteligencia Artificial no es una herramienta para sustituir al humano, sino un **exoesqueleto cognitivo** que multiplica tus capacidades. Al automatizar tareas repetitivas de pensamiento, liberas tu mente para enfocarte en la estrategia, la creatividad y la conexión humana. Esta skill te empodera al permitirte construir soluciones que aprenden y evolucionan contigo, convirtiéndose en tu aliado más potente para alcanzar la libertad profesional y personal.

## Instrucciones y Pasos detallados que se debe seguir:

### 1. Selección y Configuración del Modelo
- Determinar el modelo adecuado según el compromiso coste/velocidad/capacidad (ej: GPT-4o-mini vs GPT-4o).
- Configurar parámetros clave: `temperature`, `max_tokens` y `system_prompt`.
- Implementar gestión de errores y reintentos (Exponential Backoff).

### 2. Diseño de Prompt Engineering (Expert Level)
- Crear `System Prompts` claros con instrucciones de rol, contexto y formato de salida.
- Utilizar técnicas de `Chain-of-Thought` para razonamientos complejos.
- Implementar `Few-Shot Prompting` con ejemplos del mundo real.

### 3. Implementación de RAG (Si aplica)
- Indexar documentos en una base de datos vectorial (Embeddings).
- Realizar búsquedas de similitud semántica para recuperar contexto relevante.
- Inyectar el contexto recuperado en el prompt final para evitar alucinaciones.

### 4. Orquestación y Agentes
- Utilizar LangChain para encadenar múltiples llamadas a la IA.
- Implementar herramientas (Tools) para que la IA pueda ejecutar código o consultar APIs externas.
- Validar las salidas de la IA antes de presentarlas al usuario final.

## Workflow N8N / Automatización
*Ver archivo `workflow.md` para la implementación técnica en Python, N8N y API.*

## Seguridad y Mejores Prácticas
- 🛡️ **Prevención de Prompt Injection**: Nunca confiar ciegamente en el input del usuario en el prompt.
- 📉 **Optimización de Tokens**: Limitar la longitud del historial de conversación para reducir costes.
- 🔒 **Privacidad de Datos**: No enviar información sensible a las APIs de IA sin anonimizar primero.

## Notas y advertencias
- ⚠️ **Alucinaciones**: La IA puede inventar información. Siempre incluir una capa de verificación humana o técnica para datos críticos.

## Changelog
- v1.0 — Versión inicial (Autogenerada)
- v1.1 — Normalización V1.1: Stack OpenAI/Anthropic + Sección Empoderamiento Humano.
