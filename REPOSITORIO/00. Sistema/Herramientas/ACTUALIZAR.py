import os
import json
import re

# Configuración del Repositorio (Ruta corregida para subcarpeta Sistema/Herramientas)
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_NAME = "INDEX.js"
GLOBAL_VARIABLE = "skillsData"

ID_PATTERN = re.compile(r'ID:\s*(?:[\'"]?)(\d+)(?:[\'"]?)', re.IGNORECASE)
NAME_PATTERN = re.compile(r'#\s*(?:OPS\s*\d+\s*[|:-]\s*)?(.*)', re.IGNORECASE)

def regenerate_index():
    print(f"Buscando unidades de conocimiento en: {BASE_PATH}...")
    temp_skills = []
    
    # 1. Escaneamos y recolectamos todas las habilidades
    for root, dirs, files in os.walk(BASE_PATH):
        if 'SKILL.md' in files:
            rel_path = os.path.relpath(root, BASE_PATH)
            parts = rel_path.split(os.sep)
            
            # Filtro básico: Debe estar en una carpeta de categoría (00 a 21)
            if not parts[0][0].isdigit():
                continue
            
            temp_skills.append({
                'root': root,
                'rel_path': rel_path,
                'parts': parts
            })

    # 2. Ordenamos alfabéticamente por ruta para que los IDs sean estables
    temp_skills.sort(key=lambda x: x['rel_path'])
    
    skills = []
    for idx, item in enumerate(temp_skills, 1):
        category_raw = item['parts'][0]
        category_clean = re.sub(r'^\d+\.\s*', '', category_raw)
        
        subcategory_raw = item['parts'][1] if len(item['parts']) > 1 else 'General'
        subcategory_clean = re.sub(r'^\d+\.\d+\s*', '', subcategory_raw)
        
        full_path = os.path.join(item['root'], 'SKILL.md')
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read(5000) 
                
                # 1. Intentar extraer título del YAML frontmatter
                title_match = re.search(r'^title:\s*(.*)', content, re.MULTILINE | re.IGNORECASE)
                if title_match:
                    skill_name = title_match.group(1).strip().strip("'").strip('"')
                else:
                    # Fallback: Extraer primer título # (ignorando # Descripción)
                    headers = re.findall(r'^#\s*(?!Descripción)(.*)', content, re.MULTILINE | re.IGNORECASE)
                    if headers:
                        skill_name = headers[0].strip()
                    else:
                        # Fallback final: nombre de la carpeta
                        skill_name = item['parts'][-1]
                
                # Limpiar prefijos residuales
                skill_name = re.sub(r'^(?:OPS|SKILL|ID)\s*[\d\|:-]+\s*', '', skill_name, flags=re.IGNORECASE).strip()
                
                # 2. Intentar extraer ID
                id_match = ID_PATTERN.search(content)
                skill_id = int(id_match.group(1)) if id_match else idx
                
                # 3. Extraer Descripción
                description = "Manual operativo v1.1. Consulta el contenido detallado para más información."
                patterns = [
                    r'\*\*Descripción\*\*:(.*?)(?:\n\n|\n#|$)',
                    r'Descripción\s*(.*?)(?:\n\n|\n#|$)',
                    r'>\s*(.*?)(?:\n\n|\n#|$)'
                ]
                
                for p in patterns:
                    desc_match = re.search(p, content, re.DOTALL | re.IGNORECASE)
                    if desc_match:
                        found_desc = desc_match.group(1).strip()
                        found_desc = re.sub(r'[*#>`-]', '', found_desc).strip()
                        if len(found_desc) > 10:
                            description = found_desc[:200] + ("..." if len(found_desc) > 200 else "")
                            break
                
                # 4. Leer contenido completo para el visor interno
                # Volvemos a leer el archivo entero asegurando UTF-8
                with open(full_path, 'r', encoding='utf-8') as f_full:
                    full_md_content = f_full.read()

                # 5. Intentar leer workflow.md si existe
                workflow_path = os.path.join(item['root'], 'workflow.md')
                workflow_content = ""
                if os.path.exists(workflow_path):
                    try:
                        with open(workflow_path, 'r', encoding='utf-8') as wf:
                            workflow_content = wf.read()
                    except Exception as wf_e:
                        print(f"Error leyendo workflow en {workflow_path}: {wf_e}")

                skills.append({
                    'id': skill_id,
                    'name': skill_name,
                    'category': category_clean,
                    'subcategory': subcategory_clean,
                    'description': description,
                    'content': full_md_content, # Contenido completo para el modal
                    'workflow_content': workflow_content, # Nuevo campo para workflow
                    'path': item['rel_path']
                })
        except Exception as e:
            print(f"Error procesando {full_path}: {e}")

    # Generamos el contenido del archivo .js
    js_content = f"const {GLOBAL_VARIABLE} = {json.dumps(skills, indent=2, ensure_ascii=False)};"
    
    output_path = os.path.join(os.path.dirname(BASE_PATH), FILE_NAME)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"\n¡Éxito! Se han indexado {len(skills)} habilidades.")
    print(f"Archivo actualizado: {output_path}")

if __name__ == "__main__":
    regenerate_index()
