import json
import os
import sys

# Ruta al INDEX.json
BASE_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/BIBLIOTECA"
INDEX_FILE = os.path.join(BASE_DIR, "REPOSITORIO", "INDEX.json")

def search(query):
    if not os.path.exists(INDEX_FILE):
        return "Error: INDEX.json no encontrado."
    
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    query = query.lower()
    results = []
    
    for item in data:
        if query in item['name'].lower() or query in item['description'].lower() or query in item['subcategory'].lower():
            results.append(item)
            
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 search_skill.py <término_de_búsqueda>")
    else:
        results = search(sys.argv[1])
        if isinstance(results, str):
            print(results)
        elif not results:
            print("No se encontraron skills que coincidan.")
        else:
            print(json.dumps(results, indent=2, ensure_ascii=False))
