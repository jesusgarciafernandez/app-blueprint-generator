---
title: Modelado de Sistemas mediante Arquitectura C4 (Hierarchical System Visualization)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 08. Desarrollo de Software
subcategory: 08.4 Arquitectura de Software
tags: [arquitectura, c4, diagramas, modelado, sistemas, ingeniería, visualizacion-tecnica, documentacion, software-design, c4-model, mermaid, plantuml]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 238
---

## 0. Filosofía Human-Centric AI
*Esta habilidad aporta claridad y visión al complejo mundo de la ingeniería de software al transformar abstracciones técnicas en mapas visuales comprensibles, utilizando el modelo C4 para que todas las personas, desde el CEO hasta el desarrollador novel, compartan una única fuente de verdad sobre cómo funcionan los sistemas y permitir que la tecnología se entienda como un ecosistema ordenado, coherente y fácil de evolucionar.*

**El Rol del Humano:** El Cartógrafo de Sistemas debe ser un "Garantes de la Claridad y el Alineamiento". La IA puede generar diagramas automáticamente a partir del código, identificar relaciones entre componentes técnicos y sugerir mejoras en la jerarquía de abstracción, pero solo el humano posee la capacidad de decidir qué nivel de detalle es necesario para cada interlocutor, asegurar que el modelo visual refleje la intención estratégica del negocio y utilizar los diagramas como una herramienta de comunicación humana que elimine malentendidos y potencie la colaboración experta.
**Empoderamiento:** Usamos la tecnología para sustituir la confusión documental por una visibilidad técnica estructurada y multinivel.

---

## 1. Descripción Detallada
El Modelado de Sistemas mediante **Arquitectura C4** (v2.0) es el estándar moderno para visualizar y comunicar la arquitectura de software. No es solo "hacer dibujos"; es **Ingeniería de la Documentación Narrativa**. El enfoque v2.0 se basa en los cuatro niveles de abstracción (Contexto, Contenedores, Componentes y Código) propuestos por Simon Brown. Esto permite alejarse de los diagramas UML sobrecargados y centrarse en diagramas de cajas y flechas con significados claros, facilitando que el equipo comparta un modelo mental común del sistema, desde su integración en el ecosistema empresarial hasta los detalles de implementación de sus microservicios o apps.

## 2. Escenarios de Aplicación
- **Diseño de Nuevas Arquitecturas GreenField:** Creación de los planos maestros de un sistema antes de escribir código para validar fronteras y responsabilidades.
- **Onboarding de Desarrolladores en Sistemas Complejos:** Reducción drástica de la curva de aprendizaje permitiendo que el nuevo integrante "navegue" el sistema desde el Nivel 1 (Contexto) al Nivel 4 (Código).
- **Revisiones de Seguridad y Auditoría:** Identificación visual de puntos de entrada de datos, protocolos de comunicación y posibles vectores de ataque a través del diagrama de Contenedores (Nivel 2).
- **Comunicación con Stakeholders no Técnicos:** Uso de diagramas de Nivel 1 para explicar al negocio cómo el nuevo software interactúa con clientes, APIs externas y otros sistemas de la empresa.
- **Documentación Evolutiva 'Architecture as Code':** Uso de herramientas como Mermaid o PlantUML para que los diagramas de arquitectura vivan en el repositorio y se actualicen con el código.

## 3. Requisitos de Implementación
- **Dominio de la Jerarquía C4:** Comprensión profunda de cuándo usar cada uno de los 4 niveles y qué información incluir en cada uno.
- **Habilidad en Herramientas de Diagramación Dinámica:** Uso experto de Mermaid.js, PlantUML o Structurizr para generar diagramas a partir de texto.
- **Capacidad de Abstracción Técnica:** Habilidad para simplificar sistemas complejos en cajas con responsabilidades únicas y flujos de datos coherentes.
- **Narrativa Arquitectónica:** Capacidad para explicar a diferentes audiencias la lógica técnica basándose en el soporte visual del modelo C4.

---

## 4. Diferencial: Diagramas UML Tradicionales vs. Modelo C4 v2.0

| Dimensión | Enfoque Legacy (UML/Ad-hoc) | Modelo C4 (v2.0) |
| :--- | :--- | :--- |
| **Audiencia** | Casi exclusivamente desarrolladores. | Multinivel (Negocio, Arquitectos, Devs). |
| **Abstracción** | Mezcla nivel de detalle en un solo gráfico. | 4 niveles de 'Zoom' perfectamente separados. |
| **Mantenimiento** | Dibujos estáticos que se quedan obsoletos. | Basado en código; fácil de actualizar en PRs. |
| **Claridad** | Cajas genéricas sin semántica clara. | Cajas con Tipo, Tecnología y Responsabilidad. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Auditoría de Contexto y Mapeo de Contenedores
**Objetivo:** Entender la posición del sistema en el mundo y su estructura interna.
1.  **Definición del Sistema (Nivel 1):** IA ayuda a identificar a los usuarios (Capa Humana) y a los sistemas externos con los que se integra la app core.
2.  **Identificación de Contenedores (Nivel 2):** Desglose de la arquitectura en piezas desplegables independientes (Web Apps, Databases, Mobile, Microservicios).

**Prompt Maestro de Modelado C4 (Visual Architect):**
```text
Actúa como un Principal Software Architect y Experto en Documentación Técnica. Modela el sistema [NOMBRE_SISTEMA] usando el modelo C4. 
1. Diagrama de Contexto (Nivel 1): Define a las personas (Personas) y los sistemas de software (Systems) que interactúan con el núcleo. ¿Quién lo usa y para qué? 
2. Diagrama de Contenedores (Nivel 2): Desglosa el sistema en sus unidades de despliegue principales. Especifica la tecnología (Ej: React, Go, MongoDB) y la responsabilidad técnica de cada 'caja'. 
3. Definición de Interconexiones: Para cada flecha de comunicación, especifica el protocolo (Ej: HTTPS/REST, gRPC, JDBC) y el flujo de información principal. 
4. Zoom a Componentes (Nivel 3): Selecciona el contenedor clave [CONTENEDOR_X] y describe los 3-5 componentes internos lógicos que lo forman. 
5. Formateo 'Architecture as Code': Genera el código Mermaid.js completo para los diagramas de Nivel 1 y Nivel 2, asegurando que sean visualizables en cualquier lector de markdown.
```

### Fase 2: Ejecución, Revisión de Componentes y Mantenimiento
... (Expansión técnica sobre el uso de la técnica de 'Dynamic Diagrams' para mostrar flujos de procesos específicos sobre el modelo estático, la implementación de un proceso de 'Review de Arquitectura' sincronizado con las PRs de código, y la monitorización de la 'Deuda Documental' para asegurar que los diagramas reflejen siempre el estado real de la producción) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de visibilidad sistémica.*

1.  **Trigger:** Inicio de diseño de una nueva funcionalidad arquitectónica o necesidad de documentar un módulo existente.
2.  **Nodo de Recolección de Datos Técnicos:** IA o el arquitecto analizan los límites del sistema, tecnologías implicadas y protocolos de red.
3.  **Nodo de Generación de Diagramas (DSL):** El sistema genera la descripción textual del modelo C4 (Mermaid/PlantUML) respetando la jerarquía de los 4 niveles.
4.  **Nodo de Validación de Coherencia:** El arquitecto verifica que las flechas y responsabilidades coincidan con la realidad del código y la estrategia del negocio.
5.  **Output:** Diagramas profesionales inyectados en el README o documentación del proyecto; modelo mental compartido y validado por el equipo técnico.

---

## 7. Ejemplo Práctico: Plataforma de Salud 'HealthConnect'
**Reto:** 'HealthConnect' tenía una arquitectura dispersa de microservicios. Cuando un nuevo desarrollador entraba, tardaba 3 semanas en entender cómo el login afectaba a la base de datos de pacientes crónicos. La documentación de texto era inútil por su longitud.
**Acción v2.0:** Implementaron Modelado C4 (Skill 238). Crearon una página de arquitectura con 3 niveles de zoom. Un diagrama de contexto para el negocio, uno de contenedores para DevOps y uno de componentes para los devs de backend.
**Resultado:** La curva de aprendizaje del nuevo talento bajó de 3 semanas a 2 días. Los ingenieros ahora consultan el diagrama de Nivel 2 antes de añadir cualquier nueva API para asegurar que no están duplicando responsabilidades en contenedores que no corresponden.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
