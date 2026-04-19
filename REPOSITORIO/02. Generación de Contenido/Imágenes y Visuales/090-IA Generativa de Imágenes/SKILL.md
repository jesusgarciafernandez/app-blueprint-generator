---
title: IA Generativa de Imágenes, Prompt Engineering Visual y Control Avanzado
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 02. Generación de Contenido
subcategory: Imágenes y Visuales
tags: [gen-ai, midjourney, stable-diffusion, flux, Prompt-Engineering, controlnet, inpainting, lora-training, creative-ops]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 090
---

## 0. Filosofía Human-Centric AI
*Esta habilidad expande la imaginación humana, utilizando la tecnología para visualizar lo imposible con la precisión de un maestro del pincel y la luz.*

**El Rol del Humano:** El artista generativo debe ser un "Director de Síntesis". La IA puede generar millones de píxeles estéticamente perfectos en segundos, pero solo el humano puede definir la intención narrativa, aplicar el criterio ético sobre la autoría, guiar la coherencia visual con el resto de la marca y garantizar que la imagen final no sea solo un ruido algorítmico, sino una pieza de comunicación con alma y propósito.
**Empoderamiento:** Usamos la tecnología para derribar la barrera entre la idea y la visualización, permitiendo que cualquier creativo pueda prototipar mundos, productos y personajes con una velocidad y fidelidad que antes solo estaba al alcance de grandes estudios de producción.

---

## 1. Descripción Detallada
La IA Generativa de Imágenes es el dominio de modelos de difusión (Stable Diffusion, Midjourney, Flux) para crear activos visuales. No es solo "poner un texto"; es **Programación del Imaginario Visual**. El enfoque v2.0 incorpora el **Control Espacial y el Entrenamiento Personalizado (LoRAs)**, donde el usuario no depende del azar, sino que utiliza herramientas como ControlNet para definir poses exactas, inpainting para retoques quirúrgicos y modelos entrenados con su propia cara o productos para asegurar una personalización total y una coherencia de marca irrefutable.

## 2. Escenarios de Aplicación
- **Generación de Activos de Marketing Ad-hoc:** Creación instantánea de escenas de campaña que de otro modo requerirían rodajes costosos.
- **Concept Art y Storyboarding Express:** Visualización de ideas de proyectos antes de invertir en la producción final.
- **Prototipado de Producto y Visualización de Espacios:** Ver cómo quedaría un mueble en una estancia o un packaging en un lineal de tienda.
- **Restauración y Modificación de Imágenes Legacy:** Cambio de caras, fondos o iluminación en fotos existentes preservando la esencia original.
- **Creación de Stock Propio y Exclusivo:** Generación de un banco de imágenes único que ninguna otra marca pueda usar.

## 3. Requisitos de Implementación
- **Dominio de Modelos de Vanguardia:** Midjourney (para estética rápida), Stable Diffusion / ComfyUI (para control profesional total) y Flux.
- **Ingeniería de Prompts Avanzada:** Uso de pesos (weights), semillas (seeds), configuradores de cámara y parámetros de iluminación cinematográfica.
- **Flujo de Trabajo Híbrido:** Capacidad de retocar el resultado de la IA en software de diseño tradicional (Photoshop) para la finalización profesional.

---

## 4. Diferencial: Prompting Básico vs. Ingeniería Visual v2.0

| Dimensión | Enfoque "Slot Machine" (v1.0) | Ingeniería Visual (v2.0) |
| :--- | :--- | :--- |
| **Control** | Basado en la suerte. | ControlNet (Pose/Depth/Canny) y LoRAs. |
| **Coherencia** | Los personajes cambian cada vez. | Referencia de personaje y estilo consistente. |
| **Resolución** | Baja / Artefactada. | Hi-Res Fix y Upscaling de alta fidelidad. |
| **Ética/Legal** | Ignorada. | Modelos entrenados éticamente y transparencia. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Arquitectura del Prompt y Definición de Estilo
**Objetivo:** Comunicar la visión al modelo con precisión técnica.
1.  **Sujeto y Acción:** Describe qué ocurre con claridad.
2.  **Dirección de Arte y Óptica:** Especifica el estilo [Cinematográfico / 3D Render / Fotoanalógica] y la lente (Ej: wide angle 24mm, f/1.8).

**Prompt Maestro de Generación Visual:**
```text
Actúa como Master Prompt Engineer y Director Creativo IA. Genera la imagen para [CONCEPTO] siguiendo esta estructura: 
1. Prompt Principal: [Descripción rica en detalles: sujeto, ropa, fondo, acción]. 
2. Estilo Visual: [Ej: Estética de película de 35mm, grano fino, iluminación lateral suave (Golden Hour)]. 
3. Parámetros Técnicos: [Ej: --ar 16:9 --stylize 250 --v 6.0 --no text, blurry]. 
4. Guía de Reference Image: [Indica si usaremos una imagen de base para mantener la composición]. 
5. Flujo de Refinado: [Inpainting sugerido para corregir manos/rostro si es necesario].
```

### Fase 2: ControlNet, Inpainting y Upscaling de Producción
... (Expansión técnica sobre el uso de ComfyUI para flujos complejos, el entrenamiento de LoRAs de marca y el escalado x4 para impresión en gran formato) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de creación de contenidos visuales masivos.*

1.  **Trigger:** El equipo de redes sociales publica un post sobre un nuevo artículo de blog.
2.  **Nodo de Resumen Visual:** IA extrae los 3 conceptos clave del artículo.
3.  **Nodo de Generación de Imágenes:** Creación automática de 4 opciones de imagen hero que ilustren los conceptos usando el estilo de la marca.
4.  **Nodo de Selección y Upscaling:** El sistema elige la imagen con mayor contraste y la escala a resolución de publicación.
5.  **Output:** Activo visual listo para programar en la suite de redes sociales junto con el texto del post.

---

## 7. Ejemplo Práctico: Agencia de Viajes de Aventura
**Reto:** Necesitaban fotos de gente escalando montañas en Marte para una campaña publicitaria futurista. Un rodaje era imposible.
**Acción v2.0:** Usaron Midjourney para el concepto base y Stable Diffusion con ControlNet para asegurar que el escalador tuviera una pose dinámica realista y ropa con el logo de la agencia (vía LoRA).
**Resultado:** Una campaña visualmente impactante que generó un 300% más de interacciones que sus posts habituales y les posicionó como la marca de viajes más innovadora del mercado.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
