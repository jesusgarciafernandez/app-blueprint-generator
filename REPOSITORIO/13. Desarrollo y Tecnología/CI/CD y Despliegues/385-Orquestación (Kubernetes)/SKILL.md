---
title: Orquestación (Kubernetes)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['kubernetes', 'k8s', 'orchestration', 'infrastructure-as-code', 'helm', 'gitops', 'service-mesh', 'auto-scaling']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 385
---

## Descripción
Habilidad de alto nivel para la gestión automatizada, escalabilidad y despliegue de aplicaciones contenedorizadas en clusters de Kubernetes (K8s). Esta skill abarca el diseño de arquitecturas resilientes que aprovechan las capacidades nativas de Kubernetes: auto-curación (auto-healing), escalado horizontal (HPA), actualizaciones progresivas (rolling updates) y descubrimiento de servicios. Enseña a definir el estado deseado de la infraestructura mediante manifiestos YAML, gestionar configuraciones complejas con Helm Charts y adoptar filosofías GitOps para sincronizar el código con el estado del cluster. El objetivo es operar plataformas cloud-native masivas con mínima intervención manual.

## Cuándo usarla
Escenarios que activan esta skill:
- Cuando una aplicación ha crecido más allá de lo que un solo servidor o Docker Compose puede manejar.
- Al implementar sistemas de alta disponibilidad (Zero Downtime) que requieren redundancia geográfica y lógica.
- Para gestionar ecosistemas de microservicios interconectados que necesiten balanceo de carga interno y externo sofisticado.
- Durante la implementación de ciclos de despliegue Green/Blue o Canary releases.
- Al automatizar la gestión de recursos cloud para optimizar costes mediante el escalado elástico.

## Requisitos
- Cluster de Kubernetes (local como Minikube/Kind o gestionado como EKS/GKE/AKS).
- Herramientas de CLI certificadas (`kubectl`, `helm`).
- Conocimientos avanzados de Docker e imágenes de contenedor.
- Comprensión de conceptos de red: Ingress Controllers, CNI Plugins, Service discovery.
- Experiencia previa en administración de sistemas o infraestructura Cloud.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
