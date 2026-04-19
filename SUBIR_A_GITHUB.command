#!/bin/zsh

# Script para Sincronizar Cambios con GitHub
# Autor: App Blueprint Generator (Jesús García Fernández)

# Cambiar al directorio del script
cd "$(dirname "$0")"

echo "==========================================="
echo "   Sincronizando con GitHub (App Blueprint Generator)   "
echo "==========================================="

# 1. Añadir todos los cambios (especialmente nuevas Skills)
echo "1. Preparando archivos..."
git add .

# 2. Confirmar cambios con fecha y hora
FECHA=$(date '+%Y-%m-%d %H:%M:%S')
echo "2. Guardando cambios locally ($FECHA)..."
git commit -m "Actualizacion de Skills y mejoras: $FECHA"

# 3. Subir a GitHub
echo "3. Subiendo a GitHub..."
git push origin main

echo "==========================================="
echo "   Sincronización Completada con Éxito.   "
echo "==========================================="

# Mantener la ventana abierta unos segundos para ver el resultado
sleep 3
