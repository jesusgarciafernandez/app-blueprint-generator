import os
import time
import subprocess
import sys

# Configuración
# Base es subcarpeta Sistema/Herramientas/ -> Subir 2 niveles para REPOSITORIO
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT_UPDATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ACTUALIZAR.py")
POLL_INTERVAL = 2
DEBOUNCE_TIME = 1.5

def notify(title, text):
    """Lanza una notificación nativa según el sistema operativo"""
    try:
        platform = sys.platform
        if platform == "darwin": # macOS
            os.system(f'osascript -e \'display notification "{text}" with title "{title}"\'')
        elif platform == "win32": # Windows
            ps_cmd = f'[reflection.assembly]::loadwithpartialname("System.Windows.Forms"); [reflection.assembly]::loadwithpartialname("System.Drawing"); $notify = new-object system.windows.forms.notifyicon; $notify.icon = [system.drawing.systemicons]::Information; $notify.visible = $true; $notify.showballoontext(5000, "{title}", "{text}", [system.windows.forms.tooltipicon]::Info)'
            subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True)
        elif platform.startswith("linux"): # Linux
            subprocess.run(["notify-send", title, text], capture_output=True)
    except Exception as e:
        # Fallback silencioso si falla la notificación
        print(f"[*] Notificación: {title} - {text}")

def get_md_mtimes(root_dir):
    mtimes = {}
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                try:
                    mtimes[path] = os.path.getmtime(path)
                except OSError:
                    pass
    return mtimes

def main():
    print("="*60)
    print(" 👁️  ANTIGRAVITY SKILL WATCHER v1.2")
    print("="*60)
    print(f"[*] Carpeta: {REPO_ROOT}")
    print("[*] Estado: VIGILANDO (Deja esta ventana abierta para auto-sync)")
    print("="*60)
    
    last_mtimes = get_md_mtimes(REPO_ROOT)
    
    try:
        while True:
            time.sleep(POLL_INTERVAL)
            current_mtimes = get_md_mtimes(REPO_ROOT)
            
            if current_mtimes != last_mtimes:
                time.sleep(DEBOUNCE_TIME)
                print(f"\n[!] {time.strftime('%H:%M:%S')} - Cambio detectado. Sincronizando...")
                
                try:
                    subprocess.run([sys.executable, SCRIPT_UPDATE], check=True)
                    print(f"[√] ÉXITO: Explorador actualizado.")
                    notify("Antigravity Explorer", "✅ Índice de Skills actualizado automáticamente.")
                except subprocess.CalledProcessError as e:
                    print(f"[X] ERROR: {e}")
                    notify("Antigravity Explorer", "❌ Error al sincronizar skills.")
                
                last_mtimes = current_mtimes
                
    except KeyboardInterrupt:
        print("\n[*] Vigilante detenido.")

if __name__ == "__main__":
    main()
