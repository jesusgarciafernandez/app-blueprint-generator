---
title: Gestión de Identidad (OAuth2OIDC)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['iam', 'oauth2', 'oidc', 'authentication', 'authorization', 'sso', 'jwt', 'mfa', 'security']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 422
---

## Descripción
Habilidad avanzada para el diseño e implementación de sistemas de gestión de identidad y control de acceso (IAM) utilizando los estándares modernos OAuth 2.0 y OpenID Connect (OIDC). Esta skill se centra en el dominio de los diferentes flujos (Grant Types) de autenticación y autorización, la gestión de tokens (JWT, Refresh Tokens) y la integración de soluciones de proveedores de identidad (IdP) como Auth0, Okta o Firebase Auth. Abarca desde la configuración de Single Sign-On (SSO) y autenticación multifactor (MFA) hasta el control de acceso basado en roles (RBAC) y atributos (ABAC), garantizando que solo los usuarios y aplicaciones autorizados puedan acceder a recursos específicos de forma segura y escalable.

## Cuándo usarla
Escenarios que activan esta skill:
- Al implementar flujos de inicio de sesión social (Google, GitHub, Apple) en una aplicación web o móvil.
- Para habilitar el acceso seguro de aplicaciones de terceros a las APIs de tu plataforma mediante Scopes y Consentimientos.
- Durante la configuración de infraestructuras corporativas que requieran SSO para unificar el acceso a múltiples herramientas internas.
- Cuando se busca securizar microservicios mediante la validación de tokens JWT en un API Gateway.
- Para cumplir con normativas de privacidad que exijan una gestión estricta de los datos de identidad de los usuarios.

## Requisitos
- Comprensión profunda de la diferencia entre Autenticación (quién eres) y Autorización (qué puedes hacer).
- Dominio del protocolo OAuth 2.0 (Roles: Client, Resource Owner, Authorization Server, Resource Server).
- Conocimientos de la capa de identidad OIDC y el ID Token.
- Experiencia en el manejo y validación de JSON Web Tokens (JWT).
- Familiaridad con librerías cliente (Passport.js, NextAuth, MSAL) y configuración de IdPs.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
