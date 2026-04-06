@echo off
TITLE Antigravity Skill Watcher - Windows
COLOR 0B

echo ============================================================
echo   ANTIGRAVITY SKILL WATCHER - Windows Edition
echo ============================================================
echo.

:: Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo encontrar 'python' en el sistema.
    echo Asegurate de que Python esta instalado y en el PATH.
    pause
    exit /b
)

:: Obtener la ruta del repositorio (directorio donde esta el .bat)
set REPO_ROOT=%~dp0
cd /d "%REPO_ROOT%"

echo [*] Repositorio: %REPO_ROOT%
echo [*] Iniciando vigilancia automatica...
echo.

:: Ejecutar el script (buscando en la subcarpeta sistema)
python "%REPO_ROOT%REPOSITORIO\00. Sistema\Herramientas\WATCH.py"

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] El vigilante se detuvo inesperadamente.
    pause
)
