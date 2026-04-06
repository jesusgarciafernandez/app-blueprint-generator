import os
import re
from datetime import datetime

REPO_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/APP BLUEPRINT GENERATOR/REPOSITORIO"

WORKFLOW_TEMPLATE = """---
title: Master Workflow: {name}
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: {today}
updated: {today}
category: {category}
subcategory: {subcategory}
tags: {tags}

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
Permitido su uso personal y educativo citando la fuente.
Prohibida su venta, redistribución comercial o modificación
sin autorización expresa del autor.
---

# 🚀 Estrategia de Automatización: {name}

Este documento define las tres vías posibles para implementar la skill de {name} en cualquier aplicación del ecosistema Antigravity.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Eventos)
**Ideal para**: Automatización de procesos y disparadores de eventos externos.

```json
{{
  "workflow_type": "N8N_AUTOMATION",
  "trigger": "External_Event",
  "skill_target": "{name}",
  "actions": ["Execute_Logic", "Validate_Output", "Notify_User"]
}}
```
*Instrucción:* Utiliza este flujo para conectar esta skill con otras herramientas (Slack, CRMs, DBs) a través de N8N.

---

## 🟩 Opción B: Script Python (Lógica Core / Backend)
**Ideal para**: Lógica programática pura, IA y procesamiento de datos local.

```python
# Master Automation - Author: Jesús García Fernández
import json

def execute_skill_automation(input_params):
    \"\"\"Lógica operativa automatizada de {name}\"\"\"
    print(f"Iniciando flujo técnico para: {name}")
    # TODO: Implementar lógica basada en SKILL.md
    return {{"status": "success", "skill": "{name}"}}

if __name__ == "__main__":
    execute_skill_automation({{}})
```

---

## 🟧 Opción C: Integración API (Microservicios / Web)
**Ideal para**: Apps web y móviles que consumen servicios en la nube.

**REST Endpoint:** `POST /v1/automate/{skill_id}`
**Auth:** Bearer Token (Ecosistema Jesús García Fernández)

```json
{{
  "request": "run_skill",
  "params": {{ "mode": "standard" }}
}}
```

---

## 📝 Guía de Selección para Antigravity
1. **Monitorización o Tareas Programadas**: Usa Opción A (N8N).
2. **Scripts locales o Proyectos Python**: Usa Opción B (Python).
3. **Frontend moderno o Integración en App**: Usa Opción C (API).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
"""

def extract_yaml_field(content, field_name, default=""):
    """Extracts a simple scalar field from YAML frontmatter using regex."""
    pattern = re.compile(rf"^{field_name}:\s*(.*?)\s*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(content)
    if match:
        val = match.group(1).strip()
        # remove surrounding quotes if any
        if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            val = val[1:-1]
        return val
    return default

def get_today():
    return datetime.now().strftime("%Y-%m-%d")

def refactor_workflows():
    print(f"Buscando skills en {REPO_DIR} ...")
    today = get_today()
    contador = 0
    
    for root, dirs, files in os.walk(REPO_DIR):
        if 'SKILL.md' in files:
            skill_md_path = os.path.join(root, 'SKILL.md')
            workflow_path = os.path.join(root, 'workflow.md')
            
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extraer campos
            name = extract_yaml_field(content, "title") or extract_yaml_field(content, "name", "Skill Sin Título")
            category = extract_yaml_field(content, "category", "Sin Categoría")
            subcategory = extract_yaml_field(content, "subcategory", "General")
            skill_id = extract_yaml_field(content, "id", "unknown-skill")
            
            # Extraer tags especial (puede tener array sintax)
            tags_match = re.search(r'^tags:\s*(\[.*?\])', content, re.MULTILINE | re.IGNORECASE)
            tags = tags_match.group(1).strip() if tags_match else "['automatización']"

            # Generar contenido
            new_wf_content = WORKFLOW_TEMPLATE.format(
                name=name,
                today=today,
                category=category,
                subcategory=subcategory,
                tags=tags,
                skill_id=skill_id
            )
            
            with open(workflow_path, 'w', encoding='utf-8') as f:
                f.write(new_wf_content)
                
            contador += 1

    print(f"Se estructuraron {contador} archivos workflow.md exitosamente.")

if __name__ == "__main__":
    refactor_workflows()
