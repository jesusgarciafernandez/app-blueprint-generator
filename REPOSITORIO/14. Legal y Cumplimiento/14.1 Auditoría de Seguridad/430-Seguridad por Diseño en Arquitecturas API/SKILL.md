---
title: Seguridad por Diseño en Arquitecturas API
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 14. Legal y Cumplimiento
subcategory: 14.1 Auditoría de Seguridad
tags: [seguridad, api, oauth, jwt, owasp, blindaje-comunicaciones]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 430
---

## Descripción
Esta habilidad blinda las "arterias" por donde fluye la información corporativa. El profesional diseña APIs que no solo son funcionales, sino resilientes por naturaleza. Se enfoca en mitigar los riesgos del OWASP API Security Top 10 (ej: BOLA, BFLA, Mas Assignment) mediante el uso de protocolos de autenticación robustos, validación de esquemas y limitación de tasas (rate limiting). Su objetivo es que cada endpoint sea una puerta acorazada.

## Cuándo usarla
- **Exposición de APIs a terceros**: Para asegurar que solo los clientes autorizados accedan a los datos permitidos.
- **Microservicios y Comunicaciones Internas**: Para evitar movimientos laterales de un atacante dentro de la red corporativa.
- **Cumplimiento Normativo (PSD2, Fintech)**: Donde la seguridad de las transacciones vía API es un mandato legal.

## Requisitos
- Protocolos de Identidad (OAuth 2.0, OpenID Connect, JWT).
- Herramientas de Gateway de API (Kong, Apigee, AWS API Gateway).
- Frameworks de validación de esquemas (Zod, Marshmallow).

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
