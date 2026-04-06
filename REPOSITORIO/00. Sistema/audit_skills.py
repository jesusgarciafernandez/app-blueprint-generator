import os
import json
import re

# Configuración
BASE_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/BIBLIOTECA/REPOSITORIO"
INDEX_FILE = os.path.join(BASE_DIR, "INDEX.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "REQUIRED_OPTIMIZATION.json")

def audit_skill(file_path):
    """
    Analiza un archivo SKILL.md y determina si necesita optimización a v1.1.
    Retorna (True/False, Motivo)
    """
    if not os.path.exists(file_path):
        return True, ["Archivo no encontrado"]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return True, [f"Error de lectura: {str(e)}"]

    reasons = []
    
    # 1. Verificar Versión
    version_match = re.search(r"version:\s*([\d\.]+)", content)
    version = version_match.group(1) if version_match else "0.0"
    if version != "1.1":
        reasons.append(f"Versión obsoleta o ausente ({version})")

    # 2. Verificar Placeholders (puntos vacíos o con guiones solos)
    # Busca líneas que son solo un guion seguido de nada o espacios, o asteriscos
    if re.search(r"^\s*[\-\*]\s*$", content, re.MULTILINE):
        reasons.append("Contiene placeholders vacíos ('- ')")
    
    # Check for empty requirements/steps (multiline check)
    if "## Requisitos\n- \n- " in content or "## Requisitos\n-\n-" in content:
         reasons.append("Sección de Requisitos vacía")
    
    if "## Instrucciones y Pasos detallados que se debe seguir:\n1.  \n2.  " in content:
         reasons.append("Sección de Pasos vacía")

    # 3. Verificar secciones críticas
    critical_sections = [
        "## Instrucciones y Pasos detallados",
        "## Workflow N8N",
        "## Notas y advertencias",
        "## Changelog"
    ]
    for section in critical_sections:
        if section not in content:
            reasons.append(f"Falta sección crítica: {section}")

    # 4. Verificar longitud de descripción
    desc_match = re.search(r"## Descripción\n(.*?)\n##", content, re.DOTALL)
    if desc_match:
        desc_text = desc_match.group(1).strip()
        if len(desc_text.split()) < 10:
            reasons.append("Descripción demasiado breve o genérica")
    else:
        reasons.append("No se pudo extraer o falta la sección de Descripción")

    if reasons:
        return True, reasons
    return False, []

def main():
    if not os.path.exists(INDEX_FILE):
        print(f"Error: No se encuentra {INDEX_FILE}")
        return

    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_data = json.load(f)

    to_optimize = []
    total_scanned = 0

    print("Iniciando auditoría de skills...")

    for item in index_data:
        skill_id = item.get("id")
        skill_path = item.get("path")
        skill_name = item.get("name")
        
        full_path = os.path.join(BASE_DIR, skill_path, "SKILL.md")
        needs_opt, reasons = audit_skill(full_path)
        
        total_scanned += 1
        
        if needs_opt:
            to_optimize.append({
                "id": skill_id,
                "name": skill_name,
                "path": full_path,
                "reasons": reasons
            })

    # Guardar resultados
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            "summary": {
                "total_scanned": total_scanned,
                "needs_optimization": len(to_optimize),
                "optimized": total_scanned - len(to_optimize)
            },
            "tasks": to_optimize
        }, f, indent=2, ensure_ascii=False)

    print(f"Auditoría completada.")
    print(f"Total escaneadas: {total_scanned}")
    print(f"Necesitan optimización: {len(to_optimize)}")
    print(f"Archivo de control generado en: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
