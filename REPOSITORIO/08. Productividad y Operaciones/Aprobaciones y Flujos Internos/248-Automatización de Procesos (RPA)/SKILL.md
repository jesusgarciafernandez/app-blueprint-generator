---
title: Automatización Robótica de Procesos (RPA & Industrial Automation)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 08. Productividad y Operaciones
subcategory: Aprobaciones y Flujos Internos
tags: [rpa, automation, uipath, power-automate, workflow-efficiency, bot-training, optical-character-recognition, digital-twins, legacy-integration, process-mining, efficiency-boost, operational-excellence]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 248
---

## 0. Filosofía Human-Centric AI
*Esta habilidad otorga la capacidad de emular digitalmente la acción humana para liberar a las personas de la esclavitud de las interfaces rígidas y obsoletas, utilizando robots de software (RPA) para navegar por sistemas legacy y realizar tareas mecánicas con una precisión infalible, permitiendo que el humano recupere su rol como decisor estratégico y creativo en un ecosistema tecnológico sin barreras.*

**El Rol del Humano:** El Diseñador de Robots e Inteligencia Operativa debe ser un "Garantes de la Calidad y la Supervisión". La IA y los bots de RPA pueden rellenar miles de formularios en sistemas antiguos, extraer datos de facturas mediante OCR con un 99% de acierto y orquestar flujos de trabajo multietapa sin descanso, pero solo el humano posee la intuición para manejar excepciones complejas que requieren juicio moral o contextual, asegurar que la automatización no perpetúe procesos ineficientes, y liderar la transición hacia una cultura operativa donde el humano y el robot colaboren en armonía.
**Empoderamiento:** Usamos la tecnología para sustituir la entrada de datos manual por una fuerza de trabajo digital incansable y precisa.

---

## 1. Descripción Detallada
La Automatización Robótica de Procesos o **RPA** (v2.0) es la competencia de desarrollar agentes de software que interactúan con las interfaces de usuario (UI) tal como lo haría un humano. No es solo "hacer un macro"; es **Ingeniería de la Emulación Humana Digital**. El enfoque v2.0 se centra en la **Integración de Sistemas sin API**: el uso de herramientas líderes (UiPath, Power Automate) para automatizar procesos en software legacy, entornos de escritorio y webs complejas. Abarca el procesamiento inteligente de documentos (IDP) mediante OCR, la gestión de colas de robots y la resolución avanzada de errores para asegurar que la operativa del negocio nunca se detenga ante aplicaciones cerradas u obsoletas.

## 2. Escenarios de Aplicación
- **Automatización de Finanzas y Conciliación Bancaria:** Descarga automática de extractos de múltiples bancos y su cotejo contra el sistema contable interno o ERP.
- **Procesamiento Masivo de Facturas y Albaranes:** Extracción de datos mediante visión artificial (OCR) y su introducción automática en el portal de gestión documental o gubernamental.
- **Migración de Datos entre Sistemas Legacy:** Transferencia de miles de registros de un software antiguo sin API a uno moderno, simulando el copiado y pegado humano a gran velocidad.
- **Gestión de Recursos Humanos y Alta de Empleados:** Creación automática de perfiles en el sistema de nóminas, correo electrónico, accesos físicos y herramientas de comunicación.
- **Auditoría y Reporte Operativo Masivo:** Recolección de datos de múltiples portales web protegidos para generar cuadros de mando de negocio actualizados cada hora.

## 3. Requisitos de Implementación
- **Domino de Plataformas RPA de Grado Industrial:** Manejo experto de UiPath (Enterprise), Microsoft Power Automate Desktop o Automation Anywhere.
- **Habilidad en Selectores y Visión de Interfaz:** Capacidad para identificar elementos en pantalla (Selectores de Windows, SAP, Web) que sean resistentes a cambios de resolución o diseño.
- **Capacidad de Análisis de Procesos (Process Mining):** Habilidad para desglosar una tarea humana en pasos lógicos atomizados y predecibles para el bot.
- **Gestión de la Continuidad y Excepciones:** Diseño de flujos que sepan qué hacer si una ventana no aparece, una web tarda en cargar o los datos de entrada son incorrectos.

---

## 4. Diferencial: Automatización API vs. RPA Estratégico v2.0

| Dimensión | Automatización API (Moderna) | RPA Estratégico (v2.0) |
| :--- | :--- | :--- |
| **Punto de Contacto** | Protocolos invisibles (JSON/HTTP). | Interfaz de Usuario (UI/Botones/Campos). |
| **Compatibilidad** | Solo sistemas modernos con API. | Universal; funciona con cualquier software visible. |
| **Velocidad de Despliegue** | Requiere desarrollo técnico profundo. | Rápido; emula lo que el humano hace hoy. |
| **Mantenimiento** | Muy estable; las APIs cambian poco. | Sensible a cambios de UI, pero muy flexible. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Auditoría de Procesos y Selección de Candidatos RPA
**Objetivo:** Elegir procesos con alto retorno de inversión (ROI) y baja complejidad de excepción.
1.  **Cálculo de Viabilidad (RPA Assessment):** IA ayuda a evaluar qué procesos son aptos basándose en el volumen de transacciones y la estabilidad de la interfaz.
2.  **Diseño del PDD (Process Definition Document):** Documentación paso a paso de la tarea humana actual antes de ser automatizada.

**Prompt Maestro de Arquitectura RPA (Bot Architect):**
```text
Actúa como un Senior RPA Solutions Architect y Experto en Excelencia Operativa. Diseña la solución robótica para el proceso: [NOMBRE_PROCESO]. 
1. Mapeo de Interacciones de UI: Describe la secuencia de clics, escritura y lecturas en las aplicaciones [APP_1] y [APP_2]. 
2. Estrategia de Selectores Robustos: ¿Cómo identificaremos el botón de 'Guardar' para que el bot no se pierda si la ventana cambia de tamaño o posición? 
3. Implementación de OCR Inteligente: Si el proceso incluye documentos PDF, define cómo extraeremos los campos [CAMPOS_DIGNÓSTICO] con alta confianza. 
4. Lógica de Gestión de Errores (Error Handler): Diseña el flujo de recuperación (Retry Scope) si la aplicación [APP_X] se congela o da un timeout. 
5. Protocolo de Escalado Humano: ¿Bajo qué condiciones específicas (BUSINESS EXCEPTIONS) el bot debe detenerse y enviar el caso a una persona para su revisión manual?
```

### Fase 2: Ejecución, Pruebas en Entorno de Usuario y Despliegue
... (Expansión técnica sobre el uso de la técnica de 'Headless Bots' para ahorrar recursos, la implementación de un proceso de 'Robot Queuing' para gestionar cargas de trabajo masivas, y la monitorización de la 'Tasa de Éxito de Transacciones' para optimizar la lógica del bot continuamente) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de fuerza digital.*

1.  **Trigger:** Disparo por tiempo, llegada de un nuevo archivo a una carpeta o una señal de un sistema externo.
2.  **Nodo de Inicialización de Robot:** El sistema arranca el bot, abre las aplicaciones necesarias y se loguea con credenciales seguras de tipo 'Robot Account'.
3.  **Nodo de Ejecución de Tarea (Core Logic):** El bot navega por la UI, realiza las acciones programadas (Extract/Write/Click) y gestiona los datos.
4.  **Nodo de Verificación de Resultado:** El sistema comprueba si el objetivo se cumplió (Ej: ¿Apareció el mensaje 'Guardado con éxito'?).
5.  **Output:** Proceso completado; reporte de transacciones generado; humano notificado si hubo excepciones; aplicaciones cerradas de forma limpia.

---

## 7. Ejemplo Práctico: Logística 'TransGlobal'
**Reto:** 'TransGlobal' tenía a 5 personas dedicadas exclusivamente a mirar las webs de 50 navieras diferentes para actualizar el estado de sus contenedores en su sistema interno de gestión (ERP de 1995 sin API). Los datos siempre tenían 24 horas de retraso.
**Acción v2.0:** Implementaron Skill 248. Desarrollaron un robot de RPA que se loguea en cada naviera cada hora, busca los contenedores activos, extrae la fecha de entrega y la escribe directamente en el ERP antiguo.
**Resultado:** Los 5 empleados ahora se dedican a la atención al cliente y ventas. El retraso de la información bajó de 24 horas a 30 minutos. El error humano en la transcripción de números de serie desapareció por completo.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
