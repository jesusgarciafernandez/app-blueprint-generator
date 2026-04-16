#!/bin/bash

# ═══════════════════════════════════════════════════════════
#  🛸 App Blueprint Generator — Lanzador macOS
#  Autor: Jesús García Fernández | jesusgarciafernandez.com
# ═══════════════════════════════════════════════════════════

REPO_ROOT=$(dirname "$0")
cd "$REPO_ROOT"

echo "═══════════════════════════════════════════════════════"
echo "  🛸 App Blueprint Generator v1.2.0"
echo "  Autor: Jesús García Fernández"
echo "═══════════════════════════════════════════════════════"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[!] Error: 'python3' no está instalado."
    echo "    Instálalo desde https://www.python.org/ e inténtalo de nuevo."
    read -p "Presiona Enter para cerrar..."
    exit 1
fi

echo "[✓] Python3 encontrado."
echo "[*] Iniciando servidor en http://localhost:5500 ..."
echo "[*] Se abrirá tu navegador automáticamente."
echo "[*] Para detener el servidor, pulsa Ctrl+C."
echo ""

python3 "$REPO_ROOT/REPOSITORIO/00. Sistema/Herramientas/app_generator.py"
