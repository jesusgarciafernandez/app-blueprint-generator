#!/bin/bash

# Script de Vigilancia Antigravity para Linux
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_ROOT"

echo "============================================================"
echo "  ANTIGRAVITY SKILL WATCHER - Linux Edition"
echo "============================================================"
echo.

# Verificar si Python esta instalado
if ! command -v python3 &> /dev/null
then
    echo "[!] Error: 'python3' no se encuentra instalado en el sistema."
    exit 1
fi

echo "[*] Directorio: $REPO_ROOT"
echo "[*] Iniciando vigilancia automatica..."
echo.

# Ejecutar el script (buscando en la subcarpeta sistema)
python3 "$REPO_ROOT/REPOSITORIO/00. Sistema/Herramientas/WATCH.py"

if [ $? -ne 0 ]; then
    echo.
    echo "[X] El vigilante se detuvo inesperadamente."
    read -p "Presiona Enter para cerrar..."
fi
