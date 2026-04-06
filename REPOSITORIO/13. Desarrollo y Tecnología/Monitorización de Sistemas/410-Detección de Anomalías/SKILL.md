---
title: Detección de Anomalías
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['anomaly-detection', 'fraud-detection', 'outliers', 'unsupervised-learning', 'isolation-forest', 'autoencoders', 'cybersecurity', 'monitoring']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 410
---

## Descripción
Habilidad de Machine Learning especializada en la identificación de puntos de datos, eventos u observaciones que se desvían significativamente de la norma o del comportamiento esperado en un dataset. La Detección de Anomalías es fundamental para la seguridad y la salud operativa, ya que el comportamiento inusual a menudo es el síntoma de un problema crítico: un ciberataque, un fraude bancario, un fallo en un sensor industrial o un error en la entrada de datos. Esta skill utiliza algoritmos tanto estadísticos (Z-score) como de aprendizaje no supervisado (Isolation Forest, One-class SVM) para encontrar la "aguja en el pajar" sin necesidad de conocer de antemano el aspecto del fallo.

## Cuándo usarla
Escenarios que activan esta skill:
- En sistemas de banca para bloquear transacciones con tarjetas de crédito que no encajan con el patrón de gasto habitual del usuario.
- Para monitorizar el tráfico de red y detectar intrusiones o ataques DoS en tiempo real.
- Durante el mantenimiento predictivo industrial, identificando vibraciones inusuales en motores antes de que ocurra una avería.
- En E-commerce para detectar bots que realizan scraping masivo o compras fraudulentas.
- Para la limpieza de datos, eliminando "outliers" que podrían distorsionar los resultados de un análisis estadístico.

## Requisitos
- Sólidas bases matemáticas (Distribuciones de probabilidad, desviación estándar).
- Manejo de algoritmos no supervisados para datos sin etiquetas (Isolation Forest, Local Outlier Factor).
- Experiencia en el preprocesamiento de datos (escalado y manejo de ruido).
- Conocimiento de técnicas de Deep Learning para anomalías (Autoencoders).
- Capacidad para definir umbrales de sensibilidad (Trade-off entre Falsos Positivos y Falsos Negativos).

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
