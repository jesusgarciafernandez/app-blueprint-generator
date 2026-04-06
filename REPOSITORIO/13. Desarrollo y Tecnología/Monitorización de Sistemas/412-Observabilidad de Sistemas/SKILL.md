---
title: Observabilidad de Sistemas
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['observability', 'telemetry', 'tracing', 'metrics', 'logs', 'opentelemetry', 'prometheus', 'grafana', 'jaeger']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 412
---

## Descripción
Habilidad avanzada para la implementación de estrategias de observabilidad profunda basadas en los tres pilares fundamentales: Métricas, Logs y Trazas (Tracing). Esta skill se centra en el dominio de estándares abiertos como OpenTelemetry (OTel) para la instrumentación de aplicaciones, permitiendo entender no solo si un sistema falla, sino *por qué* falla mediante la correlación de datos. Abarca la configuración de ecosistemas de visualización (Grafana) , almacenamiento de series temporales (Prometheus, Mimir) y seguimiento distribuido (Jaeger, Tempo) para identificar cuellos de botella en arquitecturas de microservicios complejas y mejorar la resiliencia operativa.

## Cuándo usarla
Escenarios que activan esta skill:
- Al gestionar sistemas distribuidos donde un solo error de usuario puede involucrar llamadas a múltiples servicios internos.
- Para reducir el tiempo medio de resolución (MTTR) mediante la identificación visual del punto exacto de fallo en un flujo de traza.
- Durante la optimización de rendimiento, localizando latencias acumuladas en consultas a bases de datos o llamadas externas.
- Cuando se requiere un monitoreo proactivo del comportamiento del sistema frente a eventos de escalado o despliegues.
- Para establecer niveles de servicio (SLIs/SLOs) basados en datos reales de telemetría y salud de la aplicación.

## Requisitos
- Conocimientos sólidos de OpenTelemetry (SDKs, Collectors y Protocolo OTLP).
- Dominio de lenguajes de consulta para métricas (PromQL).
- Experiencia en la configuración de dashboards interactivos en Grafana.
- Entendimiento de conceptos de Distributed Tracing (Span IDs, Trace IDs, Context Propagation).
- Capacidad para instrumentar código de forma manual y automática en diversos lenguajes.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
