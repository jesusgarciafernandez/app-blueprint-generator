---
title: Site Reliability Engineering (SRE)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['sre', 'devops', 'availability', 'reliability', 'slo', 'sli', 'error-budget', 'incident-management', 'automation']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 413
---

## Descripción
Habilidad avanzada que aplica principios de ingeniería de software a problemas de infraestructura y operaciones para crear sistemas de software altamente escalables y fiables. Esta skill se centra en el equilibrio proactivo entre la velocidad de lanzamiento de nuevas funcionalidades y la estabilidad del sistema mediante el uso de Objetivos de Nivel de Servicio (SLO), Indicadores de Nivel de Servicio (SLI) y Presupuestos de Error (Error Budgets). Abarca la automatización de tareas operativas manuales (Toil reduction), la gestión de incidentes sin culpa (Blameless Postmortems), la planificación de capacidad y la ingeniería de caos para predecir y mitigar fallos antes de que afecten al usuario final. El objetivo es garantizar que los servicios cumplan con las promesas de disponibilidad y rendimiento de forma sostenible.

## Cuándo usarla
Escenarios que activan esta skill:
- Al definir las métricas de éxito de un servicio web crítico basadas en la experiencia real del usuario (ej: 99.9% de peticiones exitosas en <200ms).
- Durante la gestión de una gran interrupción del servicio, coordinando la respuesta técnica y la comunicación con los interesados.
- Para reducir la carga operativa de las guardias (On-call) mediante la creación de scripts de autoreparación.
- Cuando se desea implementar una cultura de aprendizaje tras los fallos, analizando las causas raíz de forma constructiva.
- Para tomar decisiones basadas en datos sobre cuándo frenar los despliegues si el presupuesto de error se ha agotado.

## Requisitos
- Comprensión profunda de arquitecturas distribuidas y sistemas cloud.
- Programación/Scripting (Go, Python, Bash) para automatización.
- Experiencia en herramientas de observabilidad (Prometheus, Grafana, Datadog).
- Conocimiento de los "Cuatro Señales Doradas" (Latencia, Tráfico, Errores y Saturación).
- Mentalidad de ingeniería aplicada a la resolución de problemas operativos.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
