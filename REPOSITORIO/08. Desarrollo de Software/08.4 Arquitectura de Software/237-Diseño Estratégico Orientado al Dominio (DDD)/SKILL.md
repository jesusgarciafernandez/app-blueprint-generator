---
title: Diseño Estratégico Orientado al Dominio (Domain-Driven Design / DDD)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 08. Desarrollo de Software
subcategory: 08.4 Arquitectura de Software
tags: [ddd, arquitectura, dominio, lenguaje-ubicuo, modelado, estrategia, bounded-context, event-storming, ubiquitous-language, aggregates, value-objects, strategic-design]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 237
---

## 0. Filosofía Human-Centric AI
*Esta habilidad alinea el lenguaje de las personas con el lenguaje de las máquinas, utilizando el Diseño Orientado al Dominio (DDD) para que el software sea un reflejo fiel de la realidad del negocio y permitir que el humano hable y construya tecnología en sus propios términos, reduciendo la brecha entre la ambición estratégica y la ejecución técnica.*

**El Rol del Humano:** El Arquitecto del Lenguaje Ubicuo debe ser un "Garantes del Sentido y la Coherencia". La IA puede sugerir estructuras de objetos, identificar fronteras lógicas preliminares y generar plantillas de código basadas en modelos de dominio, pero solo el humano posee la capacidad de extraer los matices sutiles de la operativa real a través del diálogo con expertos, decidir los límites de los contextos acotados que definen la organización y asegurar que la tecnología no sea un fin en sí misma, sino un vehículo transparente para resolver los problemas del negocio.
**Empoderamiento:** Usamos la tecnología para sustituir la confusión técnica por una arquitectura basada en el lenguaje y la realidad humana.

---

## 1. Descripción Detallada
El Diseño Estratégico Orientado al Dominio o **DDD** (v2.0) es la metodología definitiva para gestionar la complejidad en proyectos de software de gran escala. No es solo "organizar carpetas"; es **Ingeniería del Modelo de Negocio Sintético**. El enfoque v2.0 se centra en el **Lenguaje Ubicuo y los Contextos Acotados (Bounded Contexts)**: la creación de un idioma común entre expertos de negocio y desarrolladores que se refleja directamente en el código. Abarca el uso de patrones estratégicos (Context Mapping) para definir cómo se comunican las diferentes áreas de la empresa y patrones tácticos (Aggregates, Entities, Value Objects) para asegurar la integridad de la lógica de negocio en cada módulo independiente.

## 2. Escenarios de Aplicación
- **Modelado de Sistemas Transaccionales Complejos:** Diseño de plataformas de banca o logística donde un término como "Pedido" puede tener significados diferentes para Ventas, Almacén y Contabilidad.
- **Transición a Arquitecturas de Microservicios:** Uso de DDD para encontrar las "costuras" naturales del sistema y dividir el monolito en servicios independientes basados en funciones de negocio reales.
- **Proyectos de Larga Duración y Alta Rotación:** Creación de un código base que se explica a sí mismo a través de su lenguaje, facilitando que nuevos ingenieros entiendan el negocio leyendo el código.
- **Refactorización de 'Big Ball of Mud':** Técnica para limpiar sistemas donde la lógica está mezclada, aislando el núcleo de negocio (Domain Core) de los detalles de infraestructura.
- **Sesiones de Event Storming:** Facilitación de talleres visuales donde negocio e IT mapean el flujo de eventos de la empresa para descubrir el modelo de dominio oculto.

## 3. Requisitos de Implementación
- **Dominio de Patrones Estratégicos:** Capacidad para diseñar el 'Context Map' de una organización y establecer relaciones (Upstream/Downstream).
- **Habilidad en Patrones Tácticos:** Implementación técnica de Aggregates profundos, Repositories, Domain Services y Value Objects inmutables.
- **Facilitación de Talleres de Modelado:** Uso de técnicas de 'Event Storming' o 'Domain Storytelling' para extraer conocimiento de los expertos.
- **Comunicación Transversal:** Habilidad para negociar términos y definiciones con directivos, operativos y desarrolladores simultáneamente.

---

## 4. Diferencial: Arquitectura por Capas vs. Domain-Driven Design v2.0

| Dimensión | Enfoque Legacy (Data-Driven) | DDD Estratégico (v2.0) |
| :--- | :--- | :--- |
| **Inicio** | Empieza por la Base de Datos. | Empieza por el Modelo de Negocio. |
| **Lenguaje** | Términos técnicos (DAO, Controller). | Términos de negocio (Invoice, Route). |
| **Fronteras** | Definidas por la tecnología. | Definidas por contextos de negocio. |
| **Complejidad** | Se acumula en funciones gigantes. | Se distribuye en objetos con significado. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Descubrimiento del Dominio y Bounded Contexts
**Objetivo:** Entender el negocio antes de tocar una sola línea de código.
1.  **Auditoría de Lenguaje:** IA ayuda a extraer los términos clave de los documentos de negocio y proponer un glosario de 'Lenguaje Ubicuo'.
2.  **Mapeo de Contextos (Strategic Design):** Identificación de las áreas con responsabilidades independientes dentro de la organización.

**Prompt Maestro de Modelado DDD (Domain Architect):**
```text
Actúa como un Senior Software Architect y Experto en Domain-Driven Design. Diseña el modelo estratégico para el dominio: [DESCRIPCIÓN_NEGOCIO]. 
1. Identificación de Bounded Contexts: Define al menos 3 contextos independientes (Ej: Catálogo, Pedidos, Envios) y justifica sus fronteras. 
2. Glosario de Lenguaje Ubicuo: Lista los 5 términos más importantes para este negocio y define qué significan exactamente en el contexto del software. 
3. Diseño de Agregados Tácticos: Para el contexto [CONTEXTO_X], identifica el 'Aggregate Root' y los 'Value Objects' que garantizan la integridad de la regla de negocio. 
4. Mapa de Contextos (Context Map): Describe cómo se comunicarán los contextos entre sí (Ej: Notificaciones vía Eventos, Llamadas síncronas con ACL - Anti-Corruption Layer). 
5. Taller de Event Storming: Diseña la agenda de una sesión para descubrir los eventos de dominio clave que disparan cambios en el sistema.
```

### Fase 2: Implementación Táctica y Refinamiento
... (Expansión técnica sobre el uso de la técnica de 'Dependency Inversion' para proteger el dominio de la base de datos, la implementación de un proceso de 'Domain Validation' donde los objetos no pueden crearse en un estado inválido, y la monitorización de la 'Fidelidad del Modelo' para asegurar que el código sigue siendo un reflejo exacto de los cambios en los procesos de negocio reales) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de alineamiento organizacional.*

1.  **Trigger:** Necesidad de implementar una nueva funcionalidad de negocio compleja o modificar un proceso existente.
2.  **Nodo de Traducción de Conceptos:** IA ayuda a traducir los requerimientos del experto en cambios específicos sobre el modelo de dominio y el lenguaje ubicuo.
3.  **Nodo de Validación de Fronteras:** El sistema verifica que la nueva funcionalidad pertenezca al 'Bounded Context' correcto y no ensucie otros módulos.
4.  **Nodo de Implementación Táctica:** Se codifican los cambios en las Entidades y Agregados, protegiendo las reglas de negocio mediante tests de dominio puros.
5.  **Output:** Software funcional que habla el idioma del negocio; documentación arquitectónica actualizada según la evolución del modelo de dominio.

---

## 7. Ejemplo Práctico: Operador Logístico 'GlobalShip'
**Reto:** En 'GlobalShip', la palabra "Envío" significaba cosas distintas para el camionero, el contable y el cliente. El código era una maraña de ifs para intentar contentar a todos, lo que hacía que cualquier cambio tardara meses.
**Acción v2.0:** Implementaron DDD (Skill 237). Crearon tres contextos claros: *Operaciones* (enfocado en rutas), *Facturación* (enfocado en costes) y *Customer Experience* (enfocado en tracking). Usaron una capa de traducción (ACL) para que se comunicaran.
**Resultado:** La velocidad de desarrollo aumentó un 300%. Los errores de facturación desaparecieron porque el código de facturación ya no dependía de los cambios en las rutas de los camiones. El negocio y el software finalmente hablaban el mismo idioma.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
