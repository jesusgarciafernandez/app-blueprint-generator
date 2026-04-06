---
title: Master Workflow: Registro e Inicio de sesión
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
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
---

# 🚀 Estrategia de Automatización: Registro e Inicio de sesión (Autenticación)

Este documento define las tres vías posibles para implementar la skill de Registro e Inicio de sesión en cualquier aplicación del ecosistema Antigravity, utilizando **Supabase Auth** como estándar de oro.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Eventos)
**Ideal para**: Automatización de procesos post-registro (bienvenida, CRMs, auditoría).

```json
{
  "workflow_type": "N8N_AUTOMATION_AUTH",
  "trigger": "Post_SignUp_Webhook",
  "skill_target": "Registro e Inicio de sesión",
  "actions": [
    {
      "node": "Supabase_Node",
      "action": "On_Auth_Change",
      "logic": "Send_Welcome_Email_Resend"
    },
    {
      "node": "Database_Sync",
      "action": "Sync_User_to_CRM",
      "params": ["email", "user_id"]
    }
  ]
}
```
*Instrucción:* Utiliza este flujo para disparar automatizaciones cada vez que un nuevo usuario se registra o inicia sesión en la plataforma.

---

## 🟩 Opción B: Script Python (Lógica Core / Backend)
**Ideal para**: Apps de escritorio, CLI o servicios personalizados que requieren auth directa.

```python
# Master Automation - Author: Jesús García Fernández
import os
from supabase import create_client, Client

# Configuración de variables de entorno
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

def sign_up_user(email, password):
    """Registra un nuevo usuario en Supabase"""
    res = supabase.auth.sign_up({"email": email, "password": password})
    return res

def sign_in_user(email, password):
    """Inicia sesión y devuelve el token JWT"""
    res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return res

if __name__ == "__main__":
    option = input("1. Registrar / 2. Login: ")
    email = input("Email: ")
    password = input("Password: ")
    if option == '1':
        print(sign_up_user(email, password))
    else:
        print(sign_in_user(email, password))
```

---

## 🟧 Opción C: Integración API (Frontend / SDK)
**Ideal para**: Web Apps (Next.js / Vite) conectadas al ecosistema Jesús García Fernández.

**SDK Method (JS):** `@supabase/supabase-js`

```javascript
/* Implementación en Frontend v1.1 */
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY)

// Login con Google
async function signInWithGoogle() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: 'https://tu-app.com/dashboard'
    }
  })
}

// Registro simple
async function signUp(email, password) {
  const { user, error } = await supabase.auth.signUp({
    email: email,
    password: password,
  })
}
```

---

## 📝 Guía de Selección para Antigravity
1. **Lógica de Bienvenida o Webhooks**: Usa Opción A (N8N).
2. **Scripts locales o Microservicios Python**: Usa Opción B (Python).
3. **Plataforma Web (SaaS) o Mobile**: Usa Opción C (JS SDK / Native SDK).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
