---
title: Master Workflow: Notificaciones Multi-Canal (FCM/Resend)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
updated: 2026-04-06
category: 09. Comunicación y Mensajería
subcategory: Push y Email
tags: ["estándar-v1.1", "validado", "notifications", "push", "email", "fcm", "resend"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
---

# 🚀 Estrategia de Automatización: Notificaciones (Omnichannel)

Este documento define las tres vías posibles para implementar la skill de Notificaciones en cualquier aplicación del ecosistema Antigravity, utilizando **Firebase Cloud Messaging (FCM)** y **Resend** como plataformas principales.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Dispatcher)
**Ideal para**: Lógica de envío en cascada, disparadores de marketing o alertas de servidor simplificadas.

```json
{
  "workflow_type": "N8N_AUTOMATION_NOTIFICATIONS",
  "trigger": "Internal_Alert_Webhook",
  "skill_target": "Notificaciones Multi-Canal",
  "actions": [
    {
      "node": "Resend_Email_Node",
      "action": "Send_Transaction_Email",
      "params": ["template_id", "user_email"]
    },
    {
      "node": "Push_Notification_Node",
      "action": "Send_FCM_Push",
      "params": ["fcm_token", "alert_title"]
    }
  ]
}
```
*Instrucción:* Utiliza N8N para construir la lógica de "si falla Email, intenta Push" de manera visual y mantenible.

---

## 🟩 Opción B: Script Python (Lógica Core / FCM & API)
**Ideal para**: Servidores de backend, scripts de monitorización y envío masivo programado.

```python
# Master Automation - Author: Jesús García Fernández
import requests
import os

RESEND_API_KEY = os.environ.get("RESEND_API_KEY")

def send_transactional_email(to_email, subject, html_content):
    """Envía un email profesional mediante Resend API"""
    headers = {"Authorization": f"Bearer {RESEND_API_KEY}", "Content-Type": "application/json"}
    data = {
        "from": "Antigravity <noreply@jesusgarciafernandez.com>",
        "to": [to_email],
        "subject": subject,
        "html": html_content
    }
    response = requests.post("https://api.resend.com/emails", headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    print(send_transactional_email("test@example.com", "Bienvenido!", "<h1>¡Hola!</h1>"))
```

---

## 🟧 Opción C: Integración API (Frontend / Service Worker)
**Ideal para**: Web Apps modernas (Next.js/PWA) que reciben notificaciones Push en tiempo real.

**FCM Push (Frontend implementation):**

```javascript
/* Integración con Firebase Push v1.1 */
import { getMessaging, getToken, onMessage } from "firebase/messaging";

const messaging = getMessaging();

// Pedir permiso y obtener token
Notification.requestPermission().then((permission) => {
  if (permission === 'granted') {
    getToken(messaging, { vapidKey: 'TU_VAPID_KEY' }).then((currentToken) => {
      if (currentToken) {
        console.log('FCM Token:', currentToken);
        // Guardar en tu base de datos (Ej: Supabase)
      }
    });
  }
});

// Escuchar mensajes en primer plano
onMessage(messaging, (payload) => {
  console.log('Mensaje Recibido en Foreground:', payload);
});
```

---

## 📝 Guía de Selección para Antigravity
1. **Campañas de Re-engagement o Alertas Simple**: Usa Opción A (N8N).
2. **Backends de Python o Tareas Programadas**: Usa Opción B (Python).
3. **Apps Web Modernas (In-App Messaging)**: Usa Opción C (JS SDK).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
