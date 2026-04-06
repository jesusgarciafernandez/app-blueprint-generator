# 🛸 Guía del App Blueprint Generator

## ¿Qué es el App Blueprint Generator?

Es una herramienta que transforma tu **idea de aplicación** (descrita con tus propias palabras) en un **paquete profesional** listo para que cualquier Inteligencia Artificial construya la app por ti.

No necesitas saber programar. Solo necesitas saber qué quieres.

---

## Requisitos

- **Python 3** instalado en tu ordenador ([descargar aquí](https://www.python.org/))
- **Navegador web** (Chrome, Firefox, Safari o Edge)
- Este repositorio completo descargado en tu equipo

---

## Cómo usarlo (Paso a paso)

### 1. Arranca el generador

Haz **doble clic** en el archivo que corresponda a tu sistema operativo:

| Sistema | Archivo |
|---------|---------|
| macOS | `CREAR_APP.command` |
| Windows | `CREAR_APP.bat` |
| Linux | `CREAR_APP.sh` |

Se abrirá tu navegador automáticamente con la interfaz del generador.

### 2. Describe tu idea (5 pasos sencillos)

1. **Visión**: Dale un nombre a tu app y describe qué hace.
2. **Audiencia**: Indica quién la usará y en qué sector.
3. **Funciones**: Selecciona las funcionalidades que necesitas.
4. **Diseño**: Elige colores y estilo visual.
5. **Generar**: Revisa el resumen y pulsa "Generar Mi Blueprint".

### 3. Descarga tu Blueprint

El sistema generará un archivo ZIP que se guardará automáticamente en la carpeta **`APPS-CREADAS`** dentro del repositorio.

### 4. Abre tu IA y empieza a construir

1. Abre tu herramienta de IA favorita (Antigravity, Cursor, Claude, ChatGPT...)
2. Abre el archivo `PROMPT_INICIAL.md` del ZIP descargado.
3. **Copia todo el texto** y pégalo como tu primer mensaje.
4. ¡La IA empezará a construir tu aplicación!

---

## ¿Qué contiene el Blueprint (ZIP)?

| Carpeta | Contenido |
|---------|-----------|
| `LEEME_PRIMERO.md` | Guía rápida de uso |
| `PROMPT_INICIAL.md` | El primer mensaje para la IA |
| `01_VISION/` | Proyecto, audiencia y funcionalidades |
| `02_AGENTES/` | Roles del equipo IA |
| `03_SKILLS/` | Conocimiento técnico especializado |
| `04_ARQUITECTURA/` | Recomendaciones tecnológicas |
| `05_REGLAS/` | Límites, estándares y seguridad |
| `06_DISEÑO/` | Guía de estilo visual |

---

## Preguntas Frecuentes

### ¿Necesito conexión a internet?
**No.** Todo funciona en local. Solo necesitas internet para cargar las fuentes de la interfaz (Google Fonts), pero funciona igual sin ellas.

### ¿Puedo crear más de un Blueprint?
**Sí.** Puedes crear tantos como quieras. Cada uno se guarda con su propio nombre y fecha.

### ¿Puedo modificar el Blueprint después de crearlo?
**Sí.** Los archivos del ZIP son documentos Markdown (.md) que puedes abrir y editar con cualquier editor de texto.

### ¿Funciona con cualquier IA?
**Sí.** El Blueprint está diseñado para funcionar con Antigravity, Cursor, Claude, ChatGPT y cualquier herramienta que entienda lenguaje natural.

### ¿Qué pasa si el generador crea una skill nueva?
La nueva skill se integra automáticamente en el repositorio (en su categoría correspondiente) y aparecerá en el Explorador de Skills.

---

## Solución de Problemas

| Problema | Solución |
|----------|----------|
| "Servidor offline" | Cierra y vuelve a abrir el archivo `CREAR_APP.*` |
| No se abre el navegador | Abre manualmente `http://localhost:5500` |
| Error de Python | Asegúrate de tener Python 3 instalado: `python3 --version` |
| El ZIP está vacío | Comprueba que el archivo `INDEX.js` existe en la raíz |

---

## Créditos

Diseñado y desarrollado por **Jesús García Fernández** | [jesusgarciafernandez.com](https://jesusgarciafernandez.com)

App Blueprint Generator v1.0 — Ecosistema Antigravity
