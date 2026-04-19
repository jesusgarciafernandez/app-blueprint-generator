---
title: Agentes de Computer Use (UI-Driven Agents & OS Control)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 07. Inteligencia Artificial
subcategory: 07.2 Automatización Agéntica
tags: [ia, agentes, computer-use, ui-automation, os-control, visual-reasoning, rpa-v2.0, autonomous-operation, screen-parsing, human-mimicry]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 197
---

## 0. Filosofía Human-Centric AI
*Esta habilidad otorga a la inteligencia artificial la capacidad física de interactuar con el mundo digital tal como lo haría un ser humano, utilizando la tecnología para navegar interfaces, ejecutar software y realizar tareas administrativas complejas, permitiendo que el humano se libere de la micro-operación repetitiva y se convierta en el director estratégico de una fuerza de trabajo digital autónoma.*

**El Rol del Humano:** El Arquitecto de Operación Agéntica debe ser un "Garantes de la Seguridad y el Control Operativo". La IA puede ver la pantalla, mover el cursor con precisión milimétrica y escribir en cualquier campo de texto de cualquier aplicación, pero solo el humano puede definir los límites de seguridad (Sandbox), supervisar que la ejecución no cause daños accidentales en sistemas de producción y asegurar que la autonomía de la IA esté siempre alineada con los objetivos éticos y legales de la organización.
**Empoderamiento:** Usamos la tecnología para sustituir la rigidez de las APIs tradicionales por la flexibilidad de un colaborador digital capaz de manejar cualquier herramienta visual.

---

## 1. Descripción Detallada
Agentes de Computer Use (v2.0) es la competencia de implementar IAs que no solo generan texto, sino que operan un sistema operativo. No es solo "hacer RPA"; es **Automatización Inteligente Basada en Visión**. El enfoque v2.0 se centra en modelos multimodales (como Claude 3.5 Sonnet o GPT-4o) capaces de realizar **Razonamiento Espacial sobre Interfaces**: interpretar capturas de pantalla, localizar elementos UI sin necesidad de selectores CSS/XPath y emular periféricos (teclado/ratón) de forma autónoma. El objetivo es automatizar procesos en software 'Legacy' (sin API), realizar pruebas de QA complejas y ejecutar flujos de trabajo multi-aplicación con un razonamiento táctico humano.

## 2. Escenarios de Aplicación
- **Automatización de Software Heredado (Legacy):** Operación de programas antiguos de gestión (ERPs, bases de datos locales) que carecen de integraciones modernas.
- **Asistentes Personales de 'Desktop':** Agentes que preparan informes uniendo datos de un Excel local, una web externa y enviando el resultado por una App de escritorio de banca.
- **Pruebas de Usuario (QA) de 'Caja Negra':** Simulación proactiva de interacciones humanas reales en aplicaciones para detectar fallos de diseño o bugs visuales antes del lanzamiento.
- **Migración Masiva de Datos entre Plataformas:** Extracción visual de información de una interfaz y carga en otra cuando no existe un pipeline de datos directo.
- **Investigación de Mercado Autónoma:** Navegación por sitios web complejos, recolección de capturas de pantalla y síntesis de hallazgos competitivos.

## 3. Requisitos de Implementación
- **Modelos Multimodales con 'Action Loop':** Uso de modelos entrenados específicamente para el control de interfaces y razonamiento visual.
- **Entornos de Ejecución Seguros (Sandboxing):** Implementación en contenedores Docker o Máquinas Virtuales aisladas para evitar riesgos de seguridad en el host.
- **Librerías de Puente OS-IA:** Uso de frameworks como PyAutoGUI, Xlib o servicios gestionados de Computer Use.
- **Gestión de Latencia y Coste:** Capacidad para optimizar la toma de capturas de pantalla (screenshots) para balancear la precisión con el consumo de tokens.

---

## 4. Diferencial: RPA Tradicional vs. Computer Use IA v2.0

| Dimensión | Enfoque Legacy (RPA) | Computer Use Agéntico (v2.0) |
| :--- | :--- | :--- |
| **Adaptabilidad** | Se rompe si un botón cambia de sitio 1px. | Entiende el botón por su función visual y texto. |
| **Lógica** | Flujos rígidos de "Si A entonces B". | Razonamiento táctico y manejo de excepciones. |
| **Integración** | Requiere selectores técnicos (DOM). | Solo necesita "ver" la interfaz (Visión). |
| **Visión** | Solo reconoce patrones de imagen sencillos. | Comprensión profunda del contexto de la pantalla. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Arquitectura del Entorno y Definición de Tareas
**Objetivo:** Crear un espacio seguro donde la IA pueda "vivir" y operar.
1.  **Configuración del Sandbox:** IA ayuda a diseñar el contenedor Docker con las herramientas necesarias (Navegador, Apps de escritorio, Python).
2.  **Mapeo de la 'Misión':** Definición de los pasos críticos y los puntos de validación visual del proceso.

**Prompt Maestro de Computer Use (UI Agents):**
```text
Actúa como un Senior Agent Engineer y Experto en UI Automation. Diseña la misión de Computer Use para [TAREA/PROCESO] en el entorno [OS/APP]. 
1. Estructura el 'Control Loop': Define cómo el agente debe tomar capturas, decidir la acción y verificar el resultado (Ver -> Pensar -> Actuar). 
2. Define los Límites de Seguridad: ¿Qué aplicaciones o carpetas debe tener prohibidas el agente y cómo bloquearemos acciones críticas (Ej: Borrar archivos)? 
3. Lógica de Navegación: Describe paso a paso cómo localizar el elemento [BOTÓN/CAMPO] basándote solo en la descripción visual para evitar fallos por cambio de UI. 
4. Gestión de Errores Visuales: ¿Qué debe hacer el agente si aparece un popup inesperado o si la página no carga a tiempo? 
5. Protocolo de 'Human-in-the-loop': Establece en qué punto el agente debe pausar y pedir validación humana antes de proceder (Ej: 'Click en Enviar Pago').
```

### Fase 2: Ejecución, Depuración y Refinamiento del Agente
... (Expansión técnica sobre el uso de la técnica de 'Annotated Screenshots' para ayudar a la IA a identificar coordenadas exactas, la implementación de un sistema de log visual que guarde cada paso para auditoría y la optimización de los intervalos de captura de pantalla para reducir el coste operativo manteniendo la fluidez de la tarea) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de operación visual continua.*

1.  **Trigger:** Solicitud de tarea administrativa o detección de un cambio de estado en un sistema monitorizado.
2.  **Nodo de Percepción Visual:** El sistema captura el estado actual de la pantalla del entorno sandbox.
3.  **Nodo de Razonamiento Táctico IA:** El modelo procesa la imagen, decide la siguiente acción (mover mouse, click, escribir) y envía la instrucción.
4.  **Nodo de Ejecución de Periféricos:** Un driver del sistema operativo ejecuta la acción física sobre la interfaz.
5.  **Output:** Tarea completada en la interfaz real; el sistema guarda el vídeo del proceso para validación del humano y confirmación de éxito.

---

## 7. Ejemplo Práctico: Agencia 'TotalAdmin'
**Reto:** Al día recibían 100 facturas en formatos PDF distintos que debían subir manualmente a un software de contabilidad de 1995 que no tiene API ni base de datos accesible.
**Acción v2.0:** Implementaron un Agente de Computer Use (Skill 197). La IA abría la factura, "veía" el importe, abría el programa antiguo, navegaba por los menús grises y tecleaba los datos uno a uno.
**Resultado:** El proceso pasó de tardar 8 horas diarias de un humano a 20 minutos de ejecución autónoma. El humano ahora solo revisa el log visual de la IA para asegurar que todo cuadra.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
