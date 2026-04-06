---
title: Registro e Inicio de sesión (Auth Master)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: Seguridad y Accesos
tags: ["estándar-v1.1", "validado", "auth", "supabase", "oauth"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 006
---

## Descripción
Esta skill proporciona un sistema robusto de autenticación y autorización para aplicaciones modernas. Cubre desde el registro de usuarios hasta el inicio de sesión seguro (Login), gestión de sesiones mediante JWT y autenticación de terceros (OAuth 2.0). Utiliza un enfoque enfocado en la seguridad y la experiencia del usuario (UX), garantizando que el acceso a la plataforma sea fluido y protegido.

## Cuándo usarla
- **Nuevos Proyectos**: Configuración inicial de la puerta de entrada a la aplicación.
- **Seguridad Crítica**: Necesidad de implementar MFA (Multi-Factor Authentication) o protección contra fuerza bruta.
- **Ecosistemas Multi-App**: Implementación de Single Sign-On (SSO).

## Requisitos
- **Stack Recomendado**: Supabase Auth (PostgreSQL) o Clerk / Auth0.
- **Protocolos**: HTTPS obligatorio, JWT para manejo de estado, OAuth 2.0.
- **Configuración**: Variables de entorno (`SUPABASE_URL`, `SUPABASE_ANON_KEY`, `JWT_SECRET`).

## Impacto Humano y Empoderamiento Personal
La implementación efectiva de un sistema de autenticación no es solo una tarea técnica; es la base de la **confianza y la privacidad**. Al automatizar el acceso seguro, liberas al usuario de la fricción del registro tradicional y le otorgas el control total sobre su identidad digital. Un sistema "invisible" y seguro empodera al profesional al permitirle enfocarse en el valor que su herramienta ofrece, sin preocuparse por la integridad de sus datos.

## Instrucciones y Pasos detallados que se debe seguir:

### 1. Configuración del Proveedor (Provider Setup)
- Definir el proveedor principal (ej: Supabase Auth).
- Habilitar métodos de acceso: Email/Password, Magic Link y OAuth (Google/GitHub).
- Configurar políticas de seguridad (RLS - Row Level Security) en el backend.

### 2. Implementación del Flow de Registro (Sign Up)
- Crear formulario con validación de complejidad de contraseña (mínimo 8 caracteres, números y símbolos).
- Implementar flujo de confirmación de email para evitar bots.
- Mapear nuevos usuarios a una tabla de `profiles` para metadatos adicionales.

### 3. Implementación del Login e Inicio de Sesión
- Desarrollar la lógica de autenticación asíncrona.
- Gestionar la persistencia de la sesión mediante cookies seguras o `localStorage` (según plataforma).
- Implementar redirección inteligente post-login según el rol del usuario.

### 4. Gestión de Sesión y Cierre (Sign Out)
- Crear endpoint/función de logout que invalide el token local y en el servidor.
- Implementar refresco automático de tokens (Refresh Tokens) para sesiones largas.

## Workflow N8N / Automatización
*Ver archivo `workflow.md` para la implementación técnica en Python, N8N y API.*

## Seguridad y Mejores Prácticas
- 🔒 **No almacenar contraseñas en texto plano**: Usar hashing (Bcrypt/Argon2) a través del proveedor.
- 🛡️ **Prevención CSRF/XSS**: Configurar cabeceras de seguridad y cookies `HttpOnly`.
- 🧪 **Rate Limiting**: Limitar intentos de login por IP para prevenir ataques de fuerza bruta.

## Notas y advertencias
- ⚠️ **Mantenimiento**: Revisar periódicamente las políticas de OAuth (Google/GitHub suelen actualizar sus APIs).

## Changelog
- v1.0 — Versión inicial (Autogenerada)
- v1.1 — Normalización V1.1: Stack Supabase Auth + Sección Empoderamiento Humano.
