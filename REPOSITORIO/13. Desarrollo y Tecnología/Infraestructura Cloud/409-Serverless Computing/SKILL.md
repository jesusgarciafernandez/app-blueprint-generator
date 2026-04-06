---
title: Serverless Computing
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['serverless', 'lambda', 'cloud-functions', 'faas', 'event-driven', 'aws', 'automation', 'scalability']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 409
---

## Descripción
Habilidad técnica especializada en la construcción y despliegue de aplicaciones utilizando el modelo de ejecución Cloud en el que el proveedor gestiona automáticamente la asignación de recursos de computación. Esta skill se centra en FaaS (Function as a Service), permitiendo ejecutar código en respuesta a eventos sin necesidad de aprovisionar o gestionar servidores. Abarca el diseño de arquitecturas orientadas a eventos (Event-Driven), la optimización de tiempos de arranque (Cold Starts), la gestión de estados externos y la integración con servicios gestionados (Bases de Datos, Colas, Almacenamiento). El objetivo es maximizar la agilidad de desarrollo y pagar únicamente por el tiempo de ejecución real del código.

## Cuándo usarla
Escenarios que activan esta skill:
- Para procesar tareas asíncronas disparadas por eventos (ej: subida de una imagen, recepción de un mensaje).
- Al construir microservicios con tráfico altamente variable que necesiten escalar de cero a miles de peticiones instantáneamente.
- Durante la implementación de APIs REST ligeras que no necesiten un servidor dedicado funcionando 24/7.
- Para automatizar tareas de mantenimiento cloud (Scheduled Jobs) de forma económica y fiable.
- Cuando se busca reducir drásticamente los costes operativos de infraestructura en proyectos con tráfico esporádico.

## Requisitos
- Acceso a proveedores cloud (AWS Lambda, Google Cloud Functions, Azure Functions).
- Herramientas de despliegue serverless (ej: Serverless Framework, AWS SAM, Terraform).
- Conocimientos de lenguajes soportados (Node.js, Python, Go).
- Familiaridad con el ecosistema de eventos del proveedor elegido (S3 Events, SNS/SQS, EventBridge).
- Comprensión de límites de ejecución y time-outs.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
