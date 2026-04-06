---
title: Master Workflow: Pagos y Suscripciones (Stripe)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
updated: 2026-04-06
category: 04. Ventas y Comercio Electrónico
subcategory: Pagos y Suscripciones
tags: ["estándar-v1.1", "validado", "payments", "stripe", "billing", "webhooks"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
---

# 🚀 Estrategia de Automatización: Pagos y Suscripciones (Fintech)

Este documento define las tres vías posibles para implementar la skill de Pagos y Suscripciones en cualquier aplicación del ecosistema Antigravity, utilizando **Stripe** como motor de pagos líder.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Webhooks)
**Ideal para**: Lógica de suscripción, envío de comprobantes y procesos de recuperación de pagos fallidos (Dunning).

```json
{
  "workflow_type": "N8N_AUTOMATION_PAYMENTS",
  "trigger": "Stripe_Webhook_Node",
  "skill_target": "Pagos y Suscripciones",
  "actions": [
    {
      "node": "Webhook_Event",
      "logic": "If invoice.payment_succeeded then Activate_Service"
    },
    {
      "node": "Email_Node",
      "action": "Send_Receipt",
      "params": ["customer_email", "receipt_url"]
    }
  ]
}
```
*Instrucción:* Utiliza N8N para conectar los eventos de Stripe con tu base de datos y sistemas de notificación de manera visual y rápida.

---

## 🟩 Opción B: Script Python (Lógica Core / Stripe SDK)
**Ideal para**: Scripts de migración masiva de clientes o integración en backends complejos.

```python
# Master Automation - Author: Jesús García Fernández
import os
import stripe

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

def create_checkout_session(customer_id, price_id):
    """Crea una sesión de Checkout segura"""
    try:
        session = stripe.checkout.Session.create(
            customer=customer_id,
            payment_method_types=['card'],
            line_items=[{'price': price_id, 'quantity': 1}],
            mode='subscription',
            success_url='https://tu-app.com/success',
            cancel_url='https://tu-app.com/cancel',
        )
        return session.url
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(create_checkout_session("cus_123", "price_abc"))
```

---

## 🟧 Opción C: Integración API (Frontend / JS SDK)
**Ideal para**: Web Apps que redirigen a Stripe Checkout o usan Stripe Elements.

**Método de Redirección Directa:**

```javascript
/* Integración con Stripe v1.1 */
import { loadStripe } from '@stripe/stripe-js'

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY)

async function handleCheckout() {
  const stripe = await stripePromise
  // Llamar a tu backend para crear la sesión
  const response = await fetch('/api/create-checkout-session', { method: 'POST' })
  const session = await response.json()

  // Redirigir a Stripe Checkout
  const result = await stripe.redirectToCheckout({
    sessionId: session.id,
  })
}
```

---

## 📝 Guía de Selección para Antigravity
1. **Lógica de Facturación Automática o Notificaciones**: Usa Opción A (N8N).
2. **Scripts de Servidor o Microservicios**: Usa Opción B (Python).
3. **Frontend Interactivo o SaaS**: Usa Opción C (Stripe SDK).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
