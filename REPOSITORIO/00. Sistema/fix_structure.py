import os
import re
import shutil
import unicodedata

# Rutas base
BASE_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/BIBLIOTECA"
REPO_DIR = os.path.join(BASE_DIR, "REPOSITORIO")
STRUCTURE_FILE = os.path.join(REPO_DIR, "ESTRUCTURA.md")

def normalize(text):
    return unicodedata.normalize('NFC', text).strip()

def get_mapping():
    """Lee ESTRUCTURA.md y devuelve un mapeo {Nombre: Número}."""
    mapping = {}
    with open(STRUCTURE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Busca patrones tipo "## 1. Marketing Digital"
    cats = re.findall(r"## (\d+)\. (.+)", content)
    for num, name in cats:
        mapping[normalize(name)] = num.strip().zfill(2)
    return mapping

def fix():
    mapping = get_mapping()
    print("Mapeo cargado (NFC):", list(mapping.keys()))
    
    # Recorrer carpetas en REPOSITORIO/
    folders = [d for d in os.listdir(REPO_DIR) if os.path.isdir(os.path.join(REPO_DIR, d))]
    
    for folder in folders:
        # Extraer el nombre de la categoría del nombre actual de la carpeta
        # Caso 1: XX. Nombre
        # Caso 2: 123. Nombre
        # Caso 3: Nombre (sin prefijo)
        folder_norm = normalize(folder)
        match = re.search(r"(?:XX\.|\d+\.)?\s*(.+)", folder_norm)
        if not match:
            continue
            
        cat_name = match.group(1).strip()
        
        if cat_name in mapping:
            correct_prefix = mapping[cat_name]
            correct_name = f"{correct_prefix}. {cat_name}"
            
            old_path = os.path.join(REPO_DIR, folder)
            new_path = os.path.join(REPO_DIR, correct_name)
            
            # Normalizar nombres para comparación final
            if normalize(folder) != normalize(correct_name):
                if os.path.exists(new_path):
                    print(f"Combinando {folder} -> {correct_name}...")
                    # Mover subcarpetas una a una
                    for sub in os.listdir(old_path):
                        src = os.path.join(old_path, sub)
                        dst = os.path.join(new_path, sub)
                        if os.path.exists(dst):
                            # Si es una carpeta de skill, mover sus contenidos internamente
                            if os.path.isdir(src):
                                for item in os.listdir(src):
                                    shutil.move(os.path.join(src, item), os.path.join(dst, item))
                                try: os.rmdir(src)
                                except: pass
                        else:
                            shutil.move(src, dst)
                    try: os.rmdir(old_path)
                    except: pass
                else:
                    print(f"Renombrando {folder} -> {correct_name}...")
                    os.rename(old_path, new_path)
        else:
            print(f"Omitiendo carpeta no mapeada: {folder}")

if __name__ == "__main__":
    fix()
