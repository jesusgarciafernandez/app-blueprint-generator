---
title: Pagos y Suscripciones (Stripe Master)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 04. Ventas y Comercio Electrónico
subcategory: Pagos y Suscripciones
tags: ["estándar-v1.1", "validado", "payments", "stripe", "saas", "billing"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 159-P
---

## Descripción
Esta skill implementa la gestión integral de transacciones monetarias y modelos de suscripción recurrente en aplicaciones digitales. Utiliza **Stripe** como motor principal, cubriendo la creación de productos, planes de precios, gestión de clientes, portales de autoservicio para el usuario y el manejo de eventos asíncronos mediante Webhooks para mantener la integridad del negocio.

## Cuándo usarla
- **Modelos SaaS**: Para gestionar suscripciones mensuales/anuales y upgrades.
- **E-commerce**: Para procesar pagos únicos de productos físicos o digitales.
- **Acceso Premium**: Control de acceso a funcionalidades basado en el estado del pago.

## Requisitos
- **Stack Recomendado**: Stripe SDK (Python/Node.js), Stripe CLI para pruebas de Webhooks.
- **Conceptos**: API Key (Secret/Publishable), Webhook Signatures, Checkout Sessions.
- **Variables**: `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`.

## Impacto Humano y Empoderamiento Personal
La monetización automatizada es la llave de la **independencia profesional**. Al implementar un sistema de pagos que funciona por ti las 24 horas, transformas tu valor en un flujo de ingresos constante sin intervención manual. Esto te empodera para centrarte en la creación de valor real y en tu propósito, automatizando la parte más crítica del negocio: la generación de recursos económicos de manera ética y segura.

## Instrucciones y Pasos detallados que se debe seguir:

### 1. Configuración de Productos y Precios
- Definir el catálogo en el Dashboard de Stripe (Precios recurrentes vs Únicos).
- Obtener los `price_id` necesarios para la integración.
- Configurar el portal de cliente (Customer Portal) para que los usuarios gestionen sus planes solos (Self-Service Onboarding).

### 2. Implementación de Stripe Checkout
- Crear sesiones de pago (Checkout Sessions) seguras desde el servidor.
- Manejar redirecciones de éxito (`success_url`) y cancelación (`cancel_url`).
- Validar la integridad del carrito antes de lanzar la sesión de pago.

### 3. Gestión de Webhooks (Lógica de Servidor)
- Implementar un endpoint `/api/webhooks` que escuche eventos de Stripe.
- Validar la firma de Stripe (`Stripe-Signature`) para evitar fraudes.
- Acciones clave: `checkout.session.completed` (Activar servicio), `customer.subscription.deleted` (Desactivar servicio).

### 4. Seguridad y Cumplimiento (PCI)
- Nunca tocar datos de tarjetas directamente en tu servidor (Usar Stripe Elements / Checkout).
- Implementar 3D Secure (SCA) obligatorio para cumplimiento europeo.
- Registrar log de transacciones para auditoría interna.

## Workflow N8N / Automatización
*Ver archivo `workflow.md` para la implementación técnica en Python, N8N y API.*

## Seguridad y Mejores Prácticas
- 🔐 **Secret Keys**: Nunca exponer `STRIPE_SECRET_KEY` en el frontend.
- 🧪 **Test Mode**: Usar tarjetas de prueba (4242...) de Stripe antes de pasar a producción.
- 🧾 **Facturación**: Automatizar el envío de facturas mediante Stripe Billing para profesionalizar el proceso.

## Notas y advertencias
- ⚠️ **Webhooks**: Siempre usar un sistema de reintentos o verificar que el webhook ha sido procesado antes de completar la lógica.

## Changelog
- v1.0 — Versión inicial (Autogenerada)
- v1.1 — Normalización V1.1: Stack Stripe + Sección Empoderamiento Humano.
