import os
import re
from datetime import datetime

# Configuración del REPOSITORIO
BASE_PATH = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/BIBLIOTECA/REPOSITORIO"

def extract_metadata(content):
    """Extrae metadata YAML del SKILL.md de forma robusta"""
    match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not match: return None
    
    metadata = {}
    yaml_block = match.group(1)
    # Regex para capturar llave: valor, incluso con comillas
    lines = yaml_block.split('\n')
    for line in lines:
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip().strip("'").strip('"')
            metadata[key] = val
    
    # Captura del aviso legal (notice) multilínea
    notice_match = re.search(r'notice:\s*>\s*(.*?)(?=\n[a-z_]+:|\Z)', yaml_block, re.DOTALL)
    if notice_match:
        metadata['notice'] = notice_match.group(1).replace('\n  ', '\n').strip()
    else:
        metadata['notice'] = "Esta skill es de autoría original de Jesús García Fernández."
        
    return metadata

def generate_workflow_md(meta, skill_content=""):
    """Genera el contenido del workflow.md basado en la metadata de la skill"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Intentar obtener el título de forma robusta
    title = meta.get('title') or meta.get('name')
    
    if not title and skill_content:
        # Fallback: Extraer el primer H1 del contenido
        h1_match = re.search(r'^#\s*(.*)', skill_content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
    
    if not title:
        title = 'Sin Título'

    # Limpiar posibles prefijos estéticos del título
    title = re.sub(r'^(?:OPS|SKILL|ID)\s*[\d\|:-]+\s*', '', title, flags=re.IGNORECASE).strip()

    author = meta.get('author', 'Jesús García Fernández')
    website = meta.get('website', 'jesusgarciafernandez.com')
    sub = meta.get('subcategory', 'General')
    tags = meta.get('tags', '[]')
    license = meta.get('license', 'CC BY-NC 4.0')
    lic_url = meta.get('license_url', 'https://creativecommons.org/licenses/by-nc/4.0/')
    notice = meta.get('notice', "Esta skill es de autoría original de Jesús García Fernández.")

    return f"""---
title: Master Workflow: {title}
version: 1.1
author: {author}
website: {website}
created: {today}
updated: {today}
category: Automatización Multi-Senda
subcategory: {sub}
tags: {tags}

license: {license}
license_url: {lic_url}
notice: >
  {notice}
---

# 🚀 Estrategia de Automatización: {title}

Este documento define las tres vías posibles para implementar la skill de {title} en cualquier aplicación del ecosistema Antigravity.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Eventos)
**Ideal para**: Automatización de procesos y disparadores de eventos externos.

```json
{{
  "workflow_type": "N8N_AUTOMATION",
  "trigger": "External_Event",
  "skill_target": "{title}",
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
    \"\"\"Lógica operativa automatizada de {title}\"\"\"
    print(f"Iniciando flujo técnico para: {title}")
    # TODO: Implementar lógica basada en SKILL.md
    return {{"status": "success", "skill": "{title}"}}

if __name__ == "__main__":
    execute_skill_automation({{}})
```

---

## 🟧 Opción C: Integración API (Microservicios / Web)
**Ideal para**: Apps web y móviles que consumen servicios en la nube.

**REST Endpoint:** `POST /v1/automate/{title.lower().replace(' ', '-')}`
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

def process_directory(target_category=None):
    """Recorre el repositorio y genera los workflows"""
    processed_count = 0
    deleted_json_count = 0
    
    # Si se pasa una categoría, solo buscamos en esa carpeta
    search_path = os.path.join(BASE_PATH, target_category) if target_category else BASE_PATH
    
    print(f"🔍 Iniciando escaneo en: {search_path}")
    
    for root, dirs, files in os.walk(search_path):
        if "SKILL.md" in files:
            skill_path = os.path.join(root, "SKILL.md")
            wf_md_path = os.path.join(root, "workflow.md")
            wf_json_path = os.path.join(root, "workflow.json")
            
            try:
                # 1. Leer SKILL.md y extraer metadata
                with open(skill_path, 'r', encoding='utf-8') as f:
                    skill_content = f.read()
                    meta = extract_metadata(skill_content)
                
                if not meta:
                    print(f"⚠️ Metadata no encontrada en: {skill_path}")
                    # Aún así intentamos generar con el contenido si existe
                    meta = {} 
                
                # 2. Generar el nuevo workflow.md
                with open(wf_md_path, 'w', encoding='utf-8') as f:
                    f.write(generate_workflow_md(meta, skill_content))
                processed_count += 1
                
                # 3. Eliminar el workflow.json si existe
                if os.path.exists(wf_json_path):
                    os.remove(wf_json_path)
                    deleted_json_count += 1
                    
            except Exception as e:
                print(f"❌ Error procesando {root}: {e}")

    print("\n--- RESUMEN DE EJECUCIÓN ---")
    print(f"✅ Archivos workflow.md creados: {processed_count}")
    print(f"🗑️ Archivos workflow.json eliminados: {deleted_json_count}")
    print("----------------------------\n")

if __name__ == "__main__":
    # Para la primera prueba, definimos una categoría específica
    # Cambiar a None para ejecución global
    TEST_CATEGORY = None # Procesa todo el REPOSITORIO
    process_directory(TEST_CATEGORY)
