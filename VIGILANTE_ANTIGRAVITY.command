#!/bin/bash

# Script de Vigilancia Antigravity
# Este archivo abre una terminal y monitoriza cambios en las skills.

REPO_ROOT=$(dirname "$0")
cd "$REPO_ROOT"

# Limpieza de logs anteriores
rm -f /tmp/antigravity_watcher.log /tmp/antigravity_watcher.err

# Ejecutar el vigilante de Python
python3 "$REPO_ROOT/REPOSITORIO/00. Sistema/Herramientas/WATCH.py"
