---
title: Sintetización de Datos
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 06. Datos y Analítica
subcategory: General
tags: ['synthetic-data', 'data-privacy', 'gan', 'sdv', 'data-augmentation', 'privacy-preserving', 'machine-learning', 'anonymization']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 191
---

## Descripción
Habilidad avanzada de Ciencia de Datos que permite la creación de datasets artificiales que mantienen las propiedades estadísticas, correlaciones y patrones de un dataset real, pero sin contener información de individuos reales. La Sintetización de Datos es la solución definitiva al conflicto entre la necesidad de datos masivos para entrenar IA y las estrictas leyes de privacidad (RGPD). Mediante el uso de Redes Generativas Antagónicas (GANs) o modelos Bayesianos, se pueden "clonar" bases de datos enteras de forma que sean indistinguibles para un modelo de ML, pero 100% seguras desde el punto de vista legal.

## Cuándo usarla
Escenarios que activan esta skill:
- Cuando el equipo de Ciencia de Datos necesita entrenar modelos con registros médicos o financieros confidenciales que no pueden salir de un entorno seguro.
- Para balancear datasets donde una clase es muy rara (ej: detección de fraudes o enfermedades poco comunes) creando ejemplos sintéticos de la clase minoritaria.
- Al desarrollar aplicaciones que requieren datos realistas para pruebas de estrés pero no quieres usar datos de producción reales.
- Para "aumentar" el tamaño de un dataset pequeño y mejorar la generalización de un modelo de Deep Learning.
- Al compartir datasets con terceros o colaboradores externos cumpliendo con la privacidad por diseño.

## Requisitos
- Dominio de librerías de síntesis (SDV - Synthetic Data Vault, Gretel.ai, YData-synthetic).
- Sólidos conocimientos de estadística descriptiva y distribuciones de probabilidad.
- Experiencia con redes neuronales generativas (GANs, Variational Autoencoders - VAEs).
- Capacidad para evaluar la "Fidelidad" (parecido estadístico) y la "Privacidad" (riesgo de re-identificación) del dato sintético.
- Familiaridad con métricas como la Distancia de Jensen-Shannon o el score de Propensión.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
