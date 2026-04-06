---
title: Microservicios
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['microservices', 'distributed-systems', 'api-gateway', 'service-discovery', 'scalability', 'resilience', 'docker', 'kubernetes']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 376
---

## Descripción
Habilidad de arquitectura avanzada centrada en la descomposición de aplicaciones monolíticas en servicios pequeños, independientes y comunicados entre sí mediante protocolos ligeros. Esta skill abarca el diseño de límites de contexto (Bounded Contexts), la implementación de patrones de comunicación (síncrona por REST/gRPC y asíncrona por colas de mensajería), la gestión de datos distribuidos y la garantía de la resiliencia mediante Circuit Breakers. Enseña a orquestar servicios de forma que puedan escalarse de forma independiente, implementando estrategias de descubrimiento de servicios y observabilidad centralizada. El objetivo es construir sistemas masivamente escalables, fáciles de mantener por múltiples equipos y altamente tolerantes a fallos parciales.

## Cuándo usarla
Escenarios que activan esta skill:
- Al escalar aplicaciones donde diferentes módulos tienen requisitos de recursos (CPU/RAM) muy dispares.
- En organizaciones grandes con múltiples equipos de desarrollo que necesiten trabajar de forma autónoma en diferentes partes del sistema.
- Para implementar sistemas heterogéneos donde cada servicio puede estar escrito en un lenguaje de programación diferente.
- Cuando se requiere una altísima disponibilidad donde la caída de un módulo no comprometa la totalidad de la aplicación.
- Durante la modernización de infraestructuras Legacy que necesiten una migración progresiva y controlada.

## Requisitos
- Dominio de contenedores y orquestación (Docker, Kubernetes).
- Conocimientos de protocolos de red y mensajería (HTTP, gRPC, RabbitMQ, Kafka).
- Herramientas de observabilidad (Prometheus, Grafana, Jaeger).
- Comprensión de conceptos de bases de datos compartidas vs base de datos por servicio.
- Implementación de API Gateways para centralizar accesos y políticas.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
