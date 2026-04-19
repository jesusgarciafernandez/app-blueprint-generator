---
title: RAG (Retrieval-Augmented Generation & Contextual AI)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 07. Inteligencia Artificial
subcategory: RAG y Bases de Conocimiento
tags: [ia, rag, embeddings, vector-db, pinecone, chromadb, context-injection, hallucinations-reduction, semantic-search, knowledge-management, architecture]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 226
---

## 0. Filosofía Human-Centric AI
*Esta habilidad dota a la inteligencia artificial de una memoria experta y veraz, utilizando la recuperación de datos aumentada (RAG) para conectar el razonamiento sintético con el conocimiento real de las personas y permitir que la tecnología actúe como un bibliotecario omnisciente que apoya la toma de decisiones basada en hechos, no en suposiciones.*

**El Rol del Humano:** El Curador de Conocimiento debe ser un "Garantes de la Fuente y la Calidad". La IA puede procesar millones de documentos, generar embeddings y recuperar fragmentos de información en milisegundos, pero solo el humano puede asegurar que los datos introducidos en el sistema sean veraces, estén actualizados y respeten la privacidad. Su función es supervisar que la "sabiduría" inyectada en la IA provenga de fuentes fidedignas, garantizando que el sistema sea una herramienta de precisión y no una fuente de desinformación automatizada.
**Empoderamiento:** Usamos la tecnología para sustituir la búsqueda manual infructuosa por un acceso instantáneo al conocimiento experto y contextual.

---

## 1. Descripción Detallada
El sistema RAG o **Retrieval-Augmented Generation** (v2.0) es la arquitectura que permite a un LLM interactuar con datos externos privados sin necesidad de re-entreno. No es solo "buscar en un PDF"; es **Ingeniería de la Memoria Semántica**. El enfoque v2.0 se centra en el **Ciclo de Precisión Contextual**: desde la partición inteligente de documentos (Chunking semántico), la generación de vectores de alta fidelidad (Embeddings) y su almacenamiento en bases de datos vectoriales (Pinecone, ChromaDB), hasta la recuperación y re-ranking de los fragmentos más relevantes para inyectarlos en el prompt del modelo. El objetivo es eliminar alucinaciones y proporcionar respuestas citadas y verificables basadas en una base de conocimientos específica.

## 2. Escenarios de Aplicación
- **Asistentes de Soporte Técnico Especializado:** Chatbots que responden problemas de usuarios consultando manuales de ingeniería, logs de fallos y bases de soluciones internas.
- **Buscadores de Documentación Legal y Contractual:** Sistemas que permiten preguntar "qué cláusulas de penalización tenemos" analizando miles de contratos PDF de forma instantánea.
- **Analítica de IA sobre Datos de Cliente:** Procesamiento de transcripciones de ventas y tickets para que un asesor pueda preguntar "¿Cuál es el dolor principal de este cliente en las últimas 5 llamadas?".
- **Cerebros Digitizados de Expertos:** Creación de una base de conocimientos que destila el "Saber-Hacer" de un sénior que se jubila, permitiendo a los nuevos empleados consultar su experiencia.
- **Sistemas de Fact-checking en Tiempo Real:** Validación de noticias o declaraciones comparándolas con bases de datos de fuentes oficiales verificadas.

## 3. Requisitos de Implementación
- **Domino de Pipelines ETL para IA:** Capacidad para limpiar, estructurar y fragmentar datos (documentos, webs, DBs) para su vectorización.
- **Habilidad en Bases de Datos Vectoriales:** Manejo experto de índices, namespaces y búsqueda de similitud (Cosine Similarity, Euclidean distance).
- **Conocimiento de Modelos de Embedding:** Selección del modelo adecuado (OpenAI v3, BGE, Cohere) según el idioma y el dominio del conocimiento.
- **Implementación de Lógica de Recuperación (Retrieval):** Habilidad para usar técnicas de 'Hybrid Search' (KNS + Keyword) y 'Re-ranking' para maximizar la relevancia del contexto recuperado.

---

## 4. Diferencial: Búsqueda por Palabra Clave vs. RAG v2.0

| Dimensión | Enfoque Legacy (Ctrl+F / SQL Like) | RAG Semántico (v2.0) |
| :--- | :--- | :--- |
| **Búsqueda** | Literal; busca letras iguales. | Conceptual; busca significados similares. |
| **Contexto** | Fragmentado y sin relación con la respuesta. | Inyectado directamente en el "pensamiento" del LLM. |
| **Veracidad** | No garantiza que el dato sea el actual. | Consulta la fuente más reciente en tiempo real. |
| **Interacción** | Devuelve una lista de links/ficheros. | Devuelve una respuesta redactada y razonada. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Ingesta, Fragmentación y Vectorización
**Objetivo:** Crear el mapa de conocimiento que la IA podrá "leer".
1.  **Auditoría de Fuentes:** IA ayuda a priorizar qué documentos son críticos y deben ser indexados.
2.  **Diseño del Chunking Strategy:** Selección del tamaño de fragmento (Ej: 500 tokens con 10% de solapamiento) para no perder el contexto de las frases.

**Prompt Maestro de Implementación RAG (Knowledge Linker):**
```text
Actúa como un Senior AI Solution Architect y Experto en Retrieval-Augmented Generation. Diseña el pipeline de RAG para: [DESCRIPCIÓN_DATASET/DOMINIO]. 
1. Estrategia de Chunking: ¿Cómo dividirías los documentos (Ej: por párrafos, encabezados, o tamaño fijo) para maximizar la coherencia según [TIPOLOGÍA_DOCS]? 
2. Selección de Modelos: Propón el modelo de Embedding y el LLM de síntesis ideal, justificando la relación entre calidad de recuperación y coste de tokens. 
3. Arquitectura Vectorial: Diseña el esquema de metadatos (Metadata) que guardaremos junto a los vectores para poder filtrar por fecha, autor o categoría. 
4. Pipeline de Recuperación: Describe cómo manejaremos las consultas del usuario para transformarlas en vectores (Query Embedding) y cómo seleccionaremos los 'K' fragmentos más relevantes. 
5. Protocolo Anti-Alucinación: Redacta las 'Instrucciones de Sistema' que obliguen a la IA a decir 'No lo sé' si la información no está en el contexto recuperado.
```

### Fase 2: Ejecución, Evaluación del 'Retrieval' y Re-ranking
... (Expansión técnica sobre el uso de la técnica de 'Query Expansion' donde la IA genera variantes de la pregunta del usuario para buscar mejor, la implementación de un proceso de 'Re-ranking' con modelos como Cohere para ordenar los resultados por relevancia lingüística real y la monitorización de la 'Fidelidad de Respuesta' usando métricas como RAGAS) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de memoria contextual.*

1.  **Trigger:** Recepción de una consulta que requiere conocimiento específico no contenido en el entrenamiento base del modelo.
2.  **Nodo de Transformación Vectorial (Encoding):** El sistema convierte la pregunta del usuario en un vector numérico multienfoque.
3.  **Nodo de Búsqueda de Similitud:** La base de datos vectorial identifica los fragmentos de texto con la distancia semántica más corta a la pregunta.
4.  **Nodo de Generación de Respuesta Contextual:** El LLM recibe la pregunta + los fragmentos recuperados y redacta la respuesta citando las fuentes.
5.  **Output:** Respuesta precisa y verificable entregada al usuario; feedback de relevancia guardado para ajustar los pesos del buscador.

---

## 7. Ejemplo Práctico: Bufete de Abogados 'LexBot'
**Reto:** Los abogados tardaban días en revisar jurisprudencia buscando casos similares a los actuales en una base de datos de 50.000 sentencias.
**Acción v2.0:** Implementaron RAG (Skill 226). El sistema ahora permite preguntar "¿Hay sentencias previas sobre reclamación de vicios ocultos en naves industriales de más de 20 años?".
**Resultado:** El sistema recupera los 5 casos más parecidos en 3 segundos, resume los puntos clave de cada uno y enlaza al PDF original. La productividad del equipo de investigación aumentó un 500%.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
