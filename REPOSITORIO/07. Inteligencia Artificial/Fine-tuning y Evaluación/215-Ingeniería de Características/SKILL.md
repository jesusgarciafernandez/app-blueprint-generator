---
title: Ingeniería de Características
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 07. Inteligencia Artificial
subcategory: General
tags: ['feature-engineering', 'data-preprocessing', 'dimensionality-reduction', 'feature-selection', 'encoding', 'scaling', 'machine-learning']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 215
---

## Descripción
Habilidad técnica crítica en el ciclo de vida del Machine Learning dedicada a transformar datos crudos en variables (features) que representen de forma óptima el problema subyacente para los algoritmos predictivos. La Ingeniería de Características actúa como el "puente de inteligencia" entre los datos y el modelo; un mejor set de características a menudo supera a un algoritmo más complejo. Esta skill abarca la limpieza avanzada, la imputación de valores faltantes, la codificación de variables categóricas, el escalado, la creación de características derivadas (matemáticas o de dominio) y la reducción de dimensionalidad (PCA/t-SNE). El objetivo es maximizar la señal predictiva y minimizar el ruido estadístico.

## Cuándo usarla
Escenarios que activan esta skill:
- Al preparar datos de transacciones bancarias donde la "hora del día" o el "día de la semana" son más relevantes que la fecha completa.
- Para manejar conjuntos de datos con cientos de variables donde muchas son redundantes o no aportan valor (maldición de la dimensionalidad).
- Durante la preparación de datos de texto para modelos que requieren vectores numéricos.
- En la construcción de modelos de recomendación donde se deben normalizar escalas de precios o volúmenes de compra.
- Cuando el rendimiento del modelo es pobre a pesar de usar algoritmos potentes (indicio de mala calidad de características).

## Requisitos
- Dominio de Python y librerías como Pandas, NumPy y Scikit-Learn.
- Sólidas bases estadísticas (correlación, varianza, distribuciones).
- Conocimiento profundo del dominio de negocio (para crear características con sentido).
- Familiaridad con técnicas de codificación (One-Hot, Label Encoder, Target Encoding).
- Capacidad para automatizar pipelines de transformación reproducibles.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
