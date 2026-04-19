---
title: Diseño de Experiencias Web 3D Inmersivas (Three.js / Spline)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 03. Diseño y Creatividad
subcategory: 03.1 Diseño UI/UX
tags: [3d-web, webgl, three-js, spline, immersive-ux, interactive-3d, react-three-fiber, performance-ops, visual-storytelling]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 123
---

## 0. Filosofía Human-Centric AI
*Esta habilidad rompe la bidimensionalidad de la pantalla para crear espacios digitales que respetan la percepción espacial humana, utilizando la tecnología para generar asombro y claridad.*

**El Rol del Humano:** El Diseñador Inmersivo debe ser un "Arquitecto de la Sensación Virtual". La IA puede optimizar mallas de polígonos, sugerir configuraciones de iluminación física y generar texturas procedurales, pero solo el humano puede decidir el ritmo de la cámara que evita el mareo, asegurar que el 3D sirva a una función narrativa y no sea un simple adorno, y garantizar que la interactividad sea intuitiva y no una barrera de entrada.
**Empoderamiento:** Usamos la tecnología para llevar el realismo del mundo físico al navegador, permitiendo que las marcas muestren sus productos con una profundidad y detalle imposibles en el 2D tradicional.

---

## 1. Descripción Detallada
El Diseño de Experiencias Web 3D Inmersivas es la capacidad de integrar gráficos tridimensionales interactivos en entornos web mediante WebGL. No se trata solo de "poner un objeto 3D"; es **Ingeniería Espacial para Navegadores**. El enfoque v2.0 incorpora el **Diseño Sensible al Rendimiento (Performance-First Design)**, utilizando herramientas como Spline para la creación ágil y Three.js (vía React Three Fiber) para una integración profunda en la lógica de la aplicación, asegurando experiencias de 60 FPS incluso en dispositivos móviles mediante la optimización de shaders y el bakeado de luces dinámicas.

## 2. Escenarios de Aplicación
- **Configuradores de Producto en Tiempo Real:** Personalización de calzado, mobiliario o electrónica con visualización instantánea.
- **Micro-sitios Interactivos de Storytelling:** Narrativas de marca donde el usuario "viaja" por una escena 3D mientras hace scroll.
- **Visualización de Datos Complejos:** Gráficos 3D que permiten al usuario rotar y profundizar en dimensiones de datos masivos.
- **Entornos para Metaverso y WebXR:** Espacios sociales y comerciales accesibles directamente desde el navegador con o sin cascos VR.
- **Landing Pages Hero-Inmersivas:** Primeras impresiones de alto impacto que diferencian una marca premium de su competencia.

## 3. Requisitos de Implementación
- **Flujo de Trabajo Digital:** Domino de Spline (para diseño visual) y Blender (para modelado avanzado y texturizado PBR).
- **Stack Técnico de Referencia:** Three.js, React Three Fiber, Drei, y conocimientos de GLSL (Shaders) básicos.
- **Comprensión de la GPU del Navegador:** Optimización de draw calls, recuento de polígonos (Low-poly) y compresión Draco/Ktx2.

---

## 4. Diferencial: Visualización 2D vs. Experiencia Inmersiva 3D v2.0

| Dimensión | Enfoque Plano (2D) | Experiencia Inmersiva (v2.0) |
| :--- | :--- | :--- |
| **Interacción** | Clics y Scrolls lineales. | Rotación, Zoom y Exploración Espacial. |
| **Tiempo Real** | Imágenes estáticas / Vídeos. | Renderizado dinámico que reacciona al usuario. |
| **Peso y Carga** | Activos de imagen pesados. | Geometría optimizada con carga progresiva. |
| **Impacto** | Familiar / Estándar. | Memorable / Wow-factor / Premium. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Planificación Espacial y Modelado Optimizado
**Objetivo:** Crear una escena visualmente potente pero técnicamente ligera.
1.  **Block-out inicial:** Define la jerarquía visual de la escena en Spline o Blender antes de entrar en detalle.
2.  **Optimización Estructural:** Asegura que todos los modelos tengan un recuento de polígonos mínimo (Retopología) y utiliza atlas de texturas para reducir peticiones al servidor.

**Prompt Maestro de Dirección de Escena 3D:**
```text
Actúa como un Senior 3D Web Artist experto en Spline y Three.js. Diseña la escena para [CONCEPTO/PROYECTO]. 
1. Define el esquema de iluminación: [Soft Ambient / Hard Contrast / Studio Setup] con uso de sombras horneadas (Baked Shadows) para rendimiento. 
2. Describe los 3 puntos de interactividad (Events): [Hover, Click, Scroll-target] y cómo afectan a la cámara o a los objetos. 
3. Especifica los materiales PBR sugeridos para que el [OBJETO] se vea realista (Rugosidad, Metalicidad, Transparencia). 
4. Detalla el protocolo de carga: ¿Cómo mostraremos un 'Placeholder' o 'Loader' mientras se descarga el activo GLB?
```

### Fase 2: Integración de Código y Animación Interactiva
... (Expansión técnica sobre el uso de UseFrame para animaciones, el control de cámaras con OrbitControls o ScrollControls, y el post-procesamiento visual en el navegador -Bloom, DOF, etc.-) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de entrega de activos tridimensionales.*

1.  **Trigger:** El usuario accede a una URL de producto detallado.
2.  **Nodo de Detección de Capacidad:** El sistema analiza si el navegador soporta WebGL y la potencia de la GPU del dispositivo.
3.  **Nodo de Carga Adaptativa:** IA decide enviar el modelo High-poly (Desktop) o Low-poly (Mobile) para asegurar la fluidez de la experiencia.
4.  **Nodo de Sincronización de Estado:** El estado del componente 3D (Ej: Color seleccionado) se comunica instantáneamente al carrito de compra o base de datos.
5.  **Output:** Experiencia 3D fluida cargada; el sistema registra qué ángulos de visión prefiere el usuario para optimizar las futuras tomas de producto.

---

## 7. Ejemplo Práctico: Marca de Relojes de Lujo
**Reto:** Los clientes no apreciaban la complejidad del mecanismo interno del reloj mediante fotos.
**Acción v2.0:** Se integró un modelo 3D en la Home que permitía "entrar" dentro del reloj haciendo scroll. Al llegar a ciertas piezas, la cámara se detenía y mostraba una nota técnica.
**Resultado:** El tiempo de estancia en la web subió de 1 minuto a 4 minutos de media. Las ventas online directas aumentaron un 25% gracias a la transparencia y el detalle visual del producto.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
