---
title: Master Workflow: Gestión de Reviews y Reseñas
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
updated: 2026-04-06
category: 05. Atención al Cliente
subcategory: General
tags: ['review-management', 'online-reputation', 'google-business-profile', 'trustpilot', 'customer-feedback', 'local-seo', 'reputation-marketing', 'social-proof']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
Permitido su uso personal y educativo citando la fuente.
Prohibida su venta, redistribución comercial o modificación
sin autorización expresa del autor.
---

# 🚀 Estrategia de Automatización: Gestión de Reviews y Reseñas

Este documento define las tres vías posibles para implementar la skill de Gestión de Reviews y Reseñas en cualquier aplicación del ecosistema Antigravity.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Eventos)
**Ideal para**: Automatización de procesos y disparadores de eventos externos.

```json
{
  "workflow_type": "N8N_AUTOMATION",
  "trigger": "External_Event",
  "skill_target": "Gestión de Reviews y Reseñas",
  "actions": ["Execute_Logic", "Validate_Output", "Notify_User"]
}
```
*Instrucción:* Utiliza este flujo para conectar esta skill con otras herramientas (Slack, CRMs, DBs) a través de N8N.

---

## 🟩 Opción B: Script Python (Lógica Core / Backend)
**Ideal para**: Lógica programática pura, IA y procesamiento de datos local.

```python
# Master Automation - Author: Jesús García Fernández
import json

def execute_skill_automation(input_params):
    """Lógica operativa automatizada de Gestión de Reviews y Reseñas"""
    print(f"Iniciando flujo técnico para: Gestión de Reviews y Reseñas")
    # TODO: Implementar lógica basada en SKILL.md
    return {"status": "success", "skill": "Gestión de Reviews y Reseñas"}

if __name__ == "__main__":
    execute_skill_automation({})
```

---

## 🟧 Opción C: Integración API (Microservicios / Web)
**Ideal para**: Apps web y móviles que consumen servicios en la nube.

**REST Endpoint:** `POST /v1/automate/169`
**Auth:** Bearer Token (Ecosistema Jesús García Fernández)

```json
{
  "request": "run_skill",
  "params": { "mode": "standard" }
}
```

---

## 📝 Guía de Selección para Antigravity
1. **Monitorización o Tareas Programadas**: Usa Opción A (N8N).
2. **Scripts locales o Proyectos Python**: Usa Opción B (Python).
3. **Frontend moderno o Integración en App**: Usa Opción C (API).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
