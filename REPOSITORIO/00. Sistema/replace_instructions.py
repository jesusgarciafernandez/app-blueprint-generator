import os

# Ruta base
REPO_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/BIBLIOTECA/REPOSITORIO"

OLD_TEXT = "## Instrucciones para Claude\nPasos detallados que Claude debe seguir:"
NEW_TEXT = "## Instrucciones y Pasos detallados que se debe seguir:"

def replace_in_skills():
    count = 0
    # Recorrer todo el REPOSITORIO buscando SKILL.md
    for root, dirs, files in os.walk(REPO_DIR):
        if "SKILL.md" in files:
            file_path = os.path.join(root, "SKILL.md")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if OLD_TEXT in content:
                new_content = content.replace(OLD_TEXT, NEW_TEXT)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                if count % 50 == 0:
                    print(f"Procesados {count} archivos...")

    print(f"Finalizado: Se han actualizado {count} archivos SKILL.md.")

if __name__ == "__main__":
    replace_in_skills()
