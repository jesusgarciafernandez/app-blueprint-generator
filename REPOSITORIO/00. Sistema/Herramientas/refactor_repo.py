import os
import re
import glob
from datetime import datetime

REPO_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/APP BLUEPRINT GENERATOR/REPOSITORIO"

def get_today():
    return datetime.now().strftime("%Y-%m-%d")

def generate_new_skill_content(idx, skill_name, category, subcategory, old_content):
    # Parse old fields as best as we can
    desc_match = re.search(r'## Descripción\n(.*?)(?:\n##|\Z)', old_content, re.DOTALL)
    descripcion = desc_match.group(1).strip() if desc_match else "Manual operativo v1.1 para la integración y escalabilidad."

    # Parse cuando usarla
    uso_match = re.search(r'## Cuándo usarla\n(.*?)(?:\n##|\Z)', old_content, re.DOTALL)
    uso = uso_match.group(1).strip() if uso_match else "- Escenarios de escalabilidad automatizada.\n- Migración y refactorización técnica continua."

    # Requisitos
    req_match = re.search(r'## Requisitos\n(.*?)(?:\n##|\Z)', old_content, re.DOTALL)
    requisitos = req_match.group(1).strip() if req_match else "- Configuración de base local.\n- Credenciales de acceso."

    # Instrucciones (antiguo nombre "Instrucciones Operativas")
    inst_match = re.search(r'## Instrucciones(?:\sOperativas)?.*\n(.*?)(?:\n##|\Z)', old_content, re.DOTALL | re.IGNORECASE)
    instrucciones = inst_match.group(1).strip() if inst_match else "1. Aplicar estrategia de refactor.\n2. Inyectar configuración base.\n3. Validar arquitectura."

    # Tags
    tags = "['automation', 'antigravity-ops']"
    tags_match = re.search(r'tags:\s*\[(.*?)\]', old_content)
    if tags_match:
        tag_content = tags_match.group(1).strip()
        tags = f"[{tag_content}]"

    skill_id = f"{idx:03d}"

    new_content = f"""---
title: {skill_name}
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: {get_today()}
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
id: {skill_id}
---

## Descripción
{descripcion}

## Cuándo usarla
{uso}

## Requisitos
{requisitos}

## Instrucciones y Pasos detallados que se debe seguir:
{instrucciones}

## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
"""
    return new_content

def refactor():
    print(f"Buscando skills en {REPO_DIR} ...")
    
    # Recoger todas las rutas que contienen un SKILL.md
    skills = []
    for root, dirs, files in os.walk(REPO_DIR):
        if 'SKILL.md' in files:
            skills.append(root)

    # Ordenar alfabéticamente para mantener consistencia
    skills.sort()
    
    contador = 1
    for skill_path in skills:
        rel_path = os.path.relpath(skill_path, REPO_DIR)
        parts = rel_path.split(os.sep)
        
        # Ignorar carpetas del sistema
        if not parts[0].split('.')[0].isdigit():
            continue
            
        category = parts[0]
        # Determinar subcategoría de forma segura
        if len(parts) > 2 and parts[1].split('.')[0].isdigit():
            subcategory = parts[1]
            old_skill_folder = parts[-1]
        else:
            subcategory = "General"
            old_skill_folder = parts[-1]

        # Limpiar el nombre de la carpeta (quitar ID antiguo si existe)
        clean_name = re.sub(r'^\d+-\s*', '', old_skill_folder)
        clean_name = re.sub(r'^\d+\s*-\s*', '', clean_name)
        
        # Crear nuevo nombre de carpeta
        new_folder_name = f"{contador:03d}-{clean_name}"
        
        parent_dir = os.path.dirname(skill_path)
        new_skill_path = os.path.join(parent_dir, new_folder_name)
        
        # Renombrar carpeta
        if skill_path != new_skill_path:
            os.rename(skill_path, new_skill_path)
            print(f"Renombrado: {old_skill_folder} -> {new_folder_name}")
        else:
            new_skill_path = skill_path
            
        # Refactorizar SKILL.md
        skill_md_path = os.path.join(new_skill_path, "SKILL.md")
        with open(skill_md_path, "r", encoding="utf-8") as f:
            old_content = f.read()
            
        new_content = generate_new_skill_content(contador, clean_name, category, subcategory, old_content)
        
        with open(skill_md_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        contador += 1
        
    print(f"Refactorización completa. Total skills procesadas: {contador - 1}")

if __name__ == "__main__":
    refactor()
