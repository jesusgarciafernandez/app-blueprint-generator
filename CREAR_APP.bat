@echo off
TITLE App Blueprint Generator v1.2.0
COLOR 0B

echo ============================================================
echo   App Blueprint Generator v1.2.0
echo   Autor: Jesus Garcia Fernandez - jesusgarciafernandez.com
echo ============================================================
echo.

:: Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] No se pudo encontrar 'python' en el sistema.
    echo Asegurate de que Python esta instalado y en el PATH.
    echo Descargalo desde https://www.python.org/
    pause
    exit /b
)

:: Obtener la ruta del repositorio
set REPO_ROOT=%~dp0
cd /d "%REPO_ROOT%"

echo [*] Repositorio: %REPO_ROOT%
echo [*] Iniciando servidor en http://localhost:5500 ...
echo [*] Se abrira tu navegador automaticamente.
echo [*] Para detener el servidor, cierra esta ventana o pulsa Ctrl+C.
echo.

python "%REPO_ROOT%REPOSITORIO\00. Sistema\Herramientas\app_generator.py"

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] El servidor se detuvo inesperadamente.
    pause
)
