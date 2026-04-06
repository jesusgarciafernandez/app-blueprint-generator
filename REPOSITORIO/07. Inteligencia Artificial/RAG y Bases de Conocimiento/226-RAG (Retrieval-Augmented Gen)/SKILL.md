---
title: RAG (Retrieval-Augmented Gen)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 07. Inteligencia Artificial
subcategory: General
tags: ['rag', 'vector-database', 'embeddings', 'llm', 'pinecone', 'chromadb', 'semantic-search', 'knowledge-retrieval']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 226
---

## Descripción
Habilidad de arquitectura de IA centrada en la conexión dinámica de Modelos de Lenguaje de Gran Escala (LLMs) con fuentes de datos externas y privadas en tiempo real, sin necesidad de re-entrenamiento. Esta skill se centra en el flujo completo de RAG: desde la ingesta y particionamiento de documentos (Chunking), la generación de representaciones numéricas (Embeddings) y el almacenamiento en bases de datos vectoriales. El objetivo es mitigar alucinaciones proporcionando al modelo un contexto verificado y actualizado, permitiendo crear sistemas expertos en bases de conocimiento corporativas.

## Cuándo usarla
Escenarios que activan esta skill:
- Al desarrollar chatbots de atención al cliente que deban responder basados únicamente en manuales de producto internos.
- Para implementar sistemas de búsqueda semántica en grandes repositorios de archivos PDF, Markdown o bases de datos SQL.
- Durante la creación de asistentes legales o médicos que requieran citar fuentes exactas para garantizar la veracidad de la información.
- Cuando se necesita que la IA tenga "memoria a largo plazo" sobre interacciones previas o documentos de usuario específicos.
- Para reducir los costes de inferencia y mejorar la precisión del modelo mediante la inyección de contexto relevante (In-context learning).

## Requisitos
- Comprensión de arquitecturas LLM y ventanas de contexto.
- Experiencia en el uso de bases de datos vectoriales (Pinecone, ChromaDB, FAISS).
- Conocimiento de modelos de embedding (OpenAI text-embedding-3, HuggingFace models).
- Programación en Python utilizando frameworks como LangChain o LlamaIndex.
- Dominio de técnicas de limpieza y preprocesamiento de texto (ETL para IA).

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
