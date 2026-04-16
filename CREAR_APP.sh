#!/bin/bash

# ═══════════════════════════════════════════════════════════
#  🛸 App Blueprint Generator — Lanzador Linux
#  Autor: Jesús García Fernández | jesusgarciafernandez.com
# ═══════════════════════════════════════════════════════════

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo "═══════════════════════════════════════════════════════"
echo "  🛸 App Blueprint Generator v1.2.0"
echo "  Autor: Jesús García Fernández"
echo "═══════════════════════════════════════════════════════"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[!] Error: 'python3' no está instalado."
    echo "    Instálalo con: sudo apt install python3"
    read -p "Presiona Enter para cerrar..."
    exit 1
fi

echo "[✓] Python3 encontrado."
echo "[*] Iniciando servidor en http://localhost:5500 ..."
echo "[*] Se abrirá tu navegador automáticamente."
echo "[*] Para detener el servidor, pulsa Ctrl+C."
echo ""

python3 "$REPO_ROOT/REPOSITORIO/00. Sistema/Herramientas/app_generator.py"

if [ $? -ne 0 ]; then
    echo ""
    echo "[X] El servidor se detuvo inesperadamente."
    read -p "Presiona Enter para cerrar..."
fi
