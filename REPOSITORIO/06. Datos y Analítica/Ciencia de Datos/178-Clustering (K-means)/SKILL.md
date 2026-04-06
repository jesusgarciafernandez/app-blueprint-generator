---
title: Clustering (K-means)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 06. Datos y Analítica
subcategory: General
tags: ['clustering', 'k-means', 'unsupervised-learning', 'segmentation', 'dimensionality-reduction', 'elbow-method', 'silhouette-score']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 178
---

## Descripción
Habilidad de aprendizaje no supervisado centrada en el descubrimiento de patrones ocultos y agrupaciones naturales dentro de conjuntos de datos sin etiquetas previas. El algoritmo K-means es la técnica más utilizada, funcionando mediante la partición del espacio de datos en 'K' grupos, donde cada punto pertenece al grupo con el centroide más cercano. Esta skill abarca la preparación de datos para clustering, la determinación del número óptimo de grupos, la interpretación de los perfiles de cada segmento y la visualización de estructuras complejas. El objetivo es permitir la segmentación automática de clientes, productos o comportamientos, facilitando estrategias personalizadas para cada nicho.

## Cuándo usarla
Escenarios que activan esta skill:
- Al realizar una segmentación de clientes (Buyer Personas) basándose en comportamiento de compra y demografía.
- Para agrupar productos en categorías lógicas según su rendimiento de ventas y stock.
- Durante la detección de anomalías: los puntos que quedan muy lejos de cualquier centroide pueden ser fraudes o errores.
- En el procesamiento de imágenes para la segmentación de colores o compresión de paletas.
- Para reducir la complejidad de un dataset previo al entrenamiento de modelos supervisados.

## Requisitos
- Conocimientos sólidos de álgebra lineal y distancias geométricas (Euclídea, Manhattan).
- Manejo de técnicas de escalado de datos (imprescindible para K-means).
- Experiencia en Python con Scikit-Learn.
- Dominio de métricas de validación interna: Método del Codo (Elbow), Puntuación de Silueta (Silhouette).
- Habilidad para la visualización de datos multidimensionales (medias de perfiles, gráficos de radar).

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
