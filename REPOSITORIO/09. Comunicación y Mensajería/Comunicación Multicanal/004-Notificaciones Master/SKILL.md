---
title: Notificaciones Multi-Canal (Omnichannel Master)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 09. Comunicación y Mensajería
subcategory: Push y Email
tags: ["estándar-v1.1", "validado", "notifications", "push", "email", "sms", "fcm", "resend"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 004-NOTIF
---

## Descripción
Esta skill gestiona la comunicación proactiva con el usuario a través de múltiples canales: Notificaciones Push (Web/Mobile), Email transaccional y SMS/WhatsApp. Su objetivo es mantener al usuario informado en tiempo real, aumentar el engagement y facilitar flujos de trabajo críticos de manera automatizada y personalizada.

## Cuándo usarla
- **Alertas de Sistema**: Notificación de eventos críticos o cambios de estado.
- **Engagement**: Envío de recordatorios, promociones o actualizaciones de contenido.
- **Transaccional**: Confirmaciones de compra, recuperación de contraseñas o facturación.
- **Seguridad**: Alertas de inicio de sesión desde dispositivos nuevos o cambios de MFA.

## Requisitos
- **Stack Recomendado**: Firebase Cloud Messaging (FCM) para Push, Resend o SendGrid para Email, Twilio para SMS/WhatsApp.
- **Herramientas**: Service Workers (para Web Push), SDKs de backend (Node/Python).
- **Variables**: `FCM_SERVER_KEY`, `RESEND_API_KEY`, `TWILIO_SID`, `TWILIO_TOKEN`.

## Impacto Humano y Empoderamiento Personal
La comunicación efectiva y oportuna es el **pulso de la conexión**. Al automatizar las notificaciones, no solo envías información; entregas **tranquilidad y control** al usuario. Una notificación bien diseñada en el momento justo empodera al profesional al evitarle la necesidad de monitorizar manualmente procesos, permitiéndole estar presente en lo que importa mientras su sistema le mantiene al tanto de lo relevante.

## Instrucciones y Pasos detallados que se debe seguir:

### 1. Configuración de Canales y Proveedores
- Configurar el proyecto en Firebase (FCM) y obtener el archivo de credenciales.
- Validar el dominio en el proveedor de Email (ej: Resend) para asegurar entregabilidad alta (SPF/DKIM).
- Integrar APIs de mensajería instantánea si se requiere contacto vía WhatsApp/SMS.

### 2. Gestión de Tokens y Suscripciones
- Capturar y almacenar el `FCM Token` del dispositivo del usuario de forma segura.
- Implementar lógica de renovación de tokens y limpieza de tokens inválidos (stale tokens).
- Permitir que el usuario elija sus preferencias de notificación (Opt-in/Opt-out).

### 3. Orquestación del Envío (Dispatcher)
- Crear una lógica de despacho que elija el mejor canal según la urgencia del mensaje.
- Implementar plantillas dinámicas (Handlebars/JSX) para emails y mensajes.
- Utilizar colas de mensajes (Sytem queues) para evitar cuellos de botella en envíos masivos.

### 4. Monitorización y Análisis
- Trackear tasas de apertura (CTR) y entrega de cada canal.
- Implementar Webhooks de entrega para saber si el mensaje llegó correctamente.
- Ajustar la frecuencia de envío para evitar el spam y la fatiga del usuario.

## Workflow N8N / Automatización
*Ver archivo `workflow.md` para la implementación técnica en Python, N8N y API.*

## Seguridad y Mejores Prácticas
- 🔏 **Protección de Datos**: No incluir información sensible (passwords, tokens) en el cuerpo de una notificación push.
- 🔇 **Quiet Hours**: Implementar lógica para no enviar notificaciones de baja prioridad en horarios de descanso del usuario.
- 🧪 **A/B Testing**: Probar diferentes copies para mejorar el engagement del usuario.

## Notas y advertencias
- ⚠️ **Entregabilidad**: Si envías demasiados emails que los usuarios marquen como spam, tu dominio será penalizado. Siempre cumple con la ley CAN-SPAM.

## Changelog
- v1.0 — Versión inicial (Autogenerada)
- v1.1 — Normalización V1.1: Stack FCM/Resend + Sección Empoderamiento Humano.
