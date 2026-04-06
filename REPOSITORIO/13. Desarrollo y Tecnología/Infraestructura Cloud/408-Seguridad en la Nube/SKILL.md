---
title: Seguridad en la Nube
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['cloud-security', 'aws', 'iam', 'compliance', 'soc2', 'encryption', 'pentesting', 'cloud-native', 'cybersecurity']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 408
---

## Descripción
Habilidad técnica crítica para proteger datos, aplicaciones e infraestructuras desplegadas en proveedores de nube (AWS, Azure, GCP). Esta skill se centra en el modelo de responsabilidad compartida, garantizando la confidencialidad, integridad y disponibilidad mediante la configuración avanzada de identidades (IAM), el cifrado de datos en reposo y en tránsito, y la implementación de perímetros de red seguros (VPC, WAF). Abarca el cumplimiento de normativas internacionales (ISO 27001, SOC2, GDPR) y la automatización de la seguridad mediante el concepto de "Security as Code". El objetivo es mitigar riesgos de filtración de datos y ataques externos en infraestructuras altamente escalables y dinámicas.

## Cuándo usarla
Escenarios que activan esta skill:
- Al configurar por primera vez una infraestructura en la nube para asegurar que no haya recursos expuestos públicamente por error (ej: buckets S3 abiertos).
- Para gestionar el acceso de usuarios y servicios siguiendo el Principio de Menor Privilegio (PoLP).
- Durante la preparación de una auditoría de cumplimiento para obtener certificaciones de seguridad.
- Cuando se detecta un incidente de seguridad y se requiere realizar una respuesta ante incidentes (IR) coordinada.
- Al implementar flujos de CI/CD que necesiten escaneos de vulnerabilidades automáticos en la infraestructura definida por código.

## Requisitos
- Dominio de servicios de seguridad del proveedor (ej: AWS IAM, GuardDuty, AWS Config).
- Conocimientos de herramientas de Infrastructure as Code (Terraform, CloudFormation) con enfoque en seguridad.
- Entendimiento de estándares industriales (CIS Benchmarks).
- Familiaridad con herramientas de escaneo de seguridad cloud (ej: Checkov, Prowler).
- Conceptos de gestión de secretos (Vault, AWS Secrets Manager).

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
