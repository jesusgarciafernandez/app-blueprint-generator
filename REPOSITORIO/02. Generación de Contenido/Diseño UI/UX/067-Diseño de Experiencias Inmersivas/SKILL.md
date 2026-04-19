---
title: Diseño de Experiencias Inmersivas (XR), Diseño Espacial y Realidad Extendida
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 02. Generación de Contenido
subcategory: Diseño UI/UX
tags: [augmented-reality, virtual-reality, mixed-reality, spatial-design, immersive-ux, xr, spatial-audio, meta-quest, vision-pro, ia-3d-asset-gen]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 067
---

## 0. Filosofía Human-Centric AI
*Esta habilidad expande la realidad humana hacia nuevas dimensiones digitales, utilizando la tecnología para crear mundos donde la imaginación y la física se funden en una experiencia segura y trascendente.*

**El Rol del Humano:** El Diseñador Inmersivo debe ser un "Arquitecto de Realidades". La IA puede generar mundos 3D complejos, texturas realistas y optimizar el rendimiento de fotogramas, pero solo el humano puede asegurar la ergonomía del movimiento para evitar el mareo (*motion sickness*), decidir dónde colocar la atención del usuario mediante audio espacial y garantizar que la inmersión respete los límites físicos y psicológicos del ser humano, creando entornos que enriquecen la realidad en lugar de sustituirla fríamente.
**Empoderamiento:** Usamos la tecnología para automatizar el modelado de activos y la simulación de físicas, permitiendo que el creativo se centre en la narrativa espacial y en la excelencia de la interacción gestual y sensorial.

---

## 1. Descripción Detallada
El Diseño de Experiencias Inmersivas (XR) es la disciplina que diseña interfaces en espacios tridimensionales. A diferencia del diseño 2D, es **Ingeniería de la Presencia y la Escala**. El enfoque v2.0 incorpora el **Diseño Espacial para Computación Espacial (Vision Pro/Quest 3) y la Interacción Multimodal**, donde se orquestan la mirada, los gestos de las manos y la voz dentro de un entorno que rodea al usuario, garantizando la comodidad ergonómica, la verosimilitud física y una carga cognitiva controlada para una inmersión profunda y productiva.

## 2. Escenarios de Aplicación
- **Simuladores de Entrenamiento Industrial y Médico:** Práctica en entornos de alto riesgo sin peligro real, con feedback háptico y visual extremo.
- **Visualización Arquitectónica y Gemelos Digitales:** Paseos virtuales por proyectos no construidos con escala real 1:1.
- **E-commerce Inmersivo (Spatial Shopping):** Visualización de productos en el propio salón del usuario con oclusión real y sombras dinámicas.
- **Colaboración en Espacios Virtuales (Metaverso corporativo):** Reuniones con avatares fotorrealistas y pizarras espaciales infinitas.
- **Museos y Educación Aumentada:** Superposición de información histórica o científica sobre objetos reales mediante AR.

## 3. Requisitos de Implementación
- **Maestría en Principios de Diseño Espacial:** Conocimiento de FOV (Campo de visión), zonas de confort ergonómico y distancias focales.
- **Dominio de Herramientas de Prototipado XR:** Bezi, ShapesXR o Spline para prototipado rápido; Unity/Unreal para implementación técnica.
- **Entendimiento de la Interacción Natural:** Diseño basado en Gaze (mirada), Gesture (manos) y Voice (voz) sin necesidad de mandos físicos.

---

## 4. Diferencial: Diseño 2D Adaptado vs. Diseño Espacial Nativo v2.0

| Dimensión | Enfoque "Pantalla en el aire" | Diseño Espacial Nativo (v2.0) |
| :--- | :--- | :--- |
| **Interfaz** | Ventanas planas flotando. | Objetos volumétricos e integrados. |
| **Navegación** | Menús de botones habituales. | Interacción gestual y mirada (Gaze). |
| **Contexto** | Aísla al usuario (VR básica). | Mezcla (Vuelve el contenido parte del entorno). |
| **Ergonomía** | Fatiga visual / Cuello cansado. | Diseño basado en el campo de visión natural. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Definición del Canvas Espacial y Zonas de Interacción
**Objetivo:** Organizar el mundo 360º antes de añadir contenido.
1.  **Mapeo de la Zona de Confort:** Define qué elementos van en la "Zona Primaria" (frente al usuario, sin mover el cuello) y cuáles en la "Zona Periférica".
2.  **Establecimiento de la Escala Humana:** Asegura que los objetos se perciben en su tamaño real para evitar la sensación de vértigo o miniatura.

**Prompt Maestro de Dirección de Diseño Inmersivo:**
```text
Actúa como Director Creativo de XR y Arquitecto de Computación Espacial. Para la experiencia [NOMBRE], diseña el siguiente protocolo de inmersión: 
1. Define el 'Modo de Presencia': [VR Total / AR de Superposición / MR Integrada]. 
2. Establece el sistema de 'Locomoción y Navegación': [Ej: Teletransporte por mirada / Movimiento fluido con 'vignetting' para evitar mareos]. 
3. Diseña la 'Interacción Gestual Core': ¿Cómo agarra, escala y lanza objetos el usuario usando solo sus manos (Hand Tracking)? 
4. Documenta el uso del 'Audio Espacial': Cómo usaremos el sonido 3D para guiar al usuario hacia los puntos de interés. 
5. Protocolo de 'Confort y Seguridad': Define los tiempos de descanso recomendados y las mallas de seguridad de límites físicos.
```

### Fase 2: Prototipado Volumétrico, Pulido de Físicas y Validación Háptica
... (Expansión técnica sobre el uso de Shaders para oclusión en AR, la optimización de polígonos para dispositivos móviles XR y la validación de la UX mediante 'Heatmaps' 3D de atención visual) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de generación de mundos inmersivos automatizada.*

1.  **Trigger:** Un arquitecto sube el plano 2D de una nueva oficina en formato CAD.
2.  **Nodo de Extrusión y Texturizado IA:** El sistema convierte automáticamente las líneas en paredes 3D, aplica texturas realistas y coloca luces dinámicas según la orientación solar real.
3.  **Nodo de Auditoría de Ergonomía:** IA recorre virtualmente el espacio y detecta si hay pasillos demasiado estrechos para la escala humana o si la información está fuera del FOV natural.
4.  **Nodo de Generación de Activos XR:** Creación automática de los niveles de detalle (LOD) para que la experiencia fluya a 90 FPS estables.
5.  **Output:** Archivo ejecutable (.apk / .reality) listo para ser visualizado en gafas de realidad mixta inmediatamente.

---

## 7. Ejemplo Práctico: Mantenimiento de Turbinas Eólicas
**Reto:** Los técnicos debían mirar un manual en papel mientras escalaban la turbina, lo cual era peligroso e ineficiente.
**Acción v2.0:** Se diseñó una experiencia de AR para gafas que proyecta las instrucciones paso a paso directamente sobre la pieza que el técnico está mirando, resaltando los tornillos correctos en verde.
**Resultado:** El tiempo de reparación bajó un 40% y los errores críticos de seguridad se redujeron a cero, ya que el técnico siempre tiene las manos libres y la información en su campo visual.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
