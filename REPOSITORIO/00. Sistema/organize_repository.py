import os
import json
import re
import unicodedata
from datetime import datetime

# Rutas base
BASE_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/BIBLIOTECA"
REPO_DIR = os.path.join(BASE_DIR, "REPOSITORIO")
STRUCTURE_FILE = os.path.join(REPO_DIR, "ESTRUCTURA.md")
TEMPLATE_FILE = os.path.join(REPO_DIR, "skill_template.md")
METADATA_PATTERN = "skill_metadata_"
INDEX_FILE = os.path.join(REPO_DIR, "INDEX.json")

def normalize(text):
    return unicodedata.normalize('NFC', text).strip()

def safe_name(name):
    """Limpia el nombre para ser usado en carpetas."""
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def get_taxonomy():
    """Lee ESTRUCTURA.md y devuelve un mapeo {NombreCat: NumeroCat}."""
    mapping = {}
    if not os.path.exists(STRUCTURE_FILE):
        return mapping
        
    with open(STRUCTURE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Busca patrones tipo "## 1. Marketing Digital"
    cats = re.findall(r"## (\d+)\. (.+)", content)
    for num, name in cats:
        mapping[normalize(name)] = num.strip().zfill(2)
    return mapping

def load_template():
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def organize():
    taxonomy = get_taxonomy()
    metadata_files = [f for f in os.listdir(REPO_DIR) if f.startswith(METADATA_PATTERN) and f.endswith(".json")]
    
    if not metadata_files:
        if os.path.exists(os.path.join(REPO_DIR, "skill_metadata.json")):
            metadata_files = ["skill_metadata.json"]
        else:
            print("Error: No metadata files found.")
            return

    template_str = load_template()
    index_data = []

    for m_file in sorted(metadata_files):
        with open(os.path.join(REPO_DIR, m_file), 'r', encoding='utf-8') as f:
            skills_data = json.load(f)
        
        print(f"Procesando {m_file}...")

        for skill in skills_data:
            name = skill['name']
            cat = normalize(skill['category'])
            sub = skill['subcategory']
            desc = skill['description']
            tags = skill.get('tags', [])
            
            # Buscar número de categoría
            cat_num = taxonomy.get(cat, "99") # 99 si no está mapeada
            cat_folder_name = f"{cat_num}. {cat}"
            
            # Ruta física
            sub_path = os.path.join(REPO_DIR, cat_folder_name, sub)
            skill_folder = os.path.join(sub_path, safe_name(name))
            
            os.makedirs(skill_folder, exist_ok=True)
            
            # Crear SKILL.md
            skill_file = os.path.join(skill_folder, "SKILL.md")
            skill_content = template_str.replace("{{TITLE}}", name)\
                                        .replace("{{DATE}}", datetime.now().strftime("%Y-%m-%d"))\
                                        .replace("{{CATEGORY}}", cat)\
                                        .replace("{{SUBCATEGORY}}", sub)\
                                        .replace("{{TAGS}}", str(tags))\
                                        .replace("{{DESCRIPTION}}", desc)\
                                        .replace("{{N8N_DESC}}", f"Automatización para {name}")
            
            with open(skill_file, 'w', encoding='utf-8') as f:
                f.write(skill_content)
                
            # Workflow placeholder
            workflow_file = os.path.join(skill_folder, "workflow.json")
            if not os.path.exists(workflow_file):
                with open(workflow_file, 'w', encoding='utf-8') as f:
                    json.dump({"name": name, "nodes": [], "connections": {}}, f, indent=2)

            # Índice
            index_data.append({
                "id": skill.get("id"),
                "name": name,
                "category": cat,
                "subcategory": sub,
                "description": desc,
                "path": os.path.relpath(skill_folder, REPO_DIR)
            })

    # Guardar INDEX.json
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    print(f"Finalizado: {len(index_data)} skills organizados en {REPO_DIR}")

if __name__ == "__main__":
    organize()
