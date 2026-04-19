---
title: Prototipado Rápido (Figma), Lógica Condicional y Simulaciones de Alta Fidelidad
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 02. Generación de Contenido
subcategory: Diseño UI/UX
tags: [figma, prototyping, interaction-design, smart-animate, ux-validation, variables, advance-prototyping, design-logic, ia-figma-assist]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 074
---

## 0. Filosofía Human-Centric AI
*Esta habilidad materializa ideas en experiencias tangibles antes de ser construidas, utilizando la tecnología para validar el propósito humano y reducir el desperdicio de esfuerzo creativo.*

**El Rol del Humano:** El Prototipador Maestro debe ser un "Simulador de Realidades Digitales". La IA puede generar pantallas UI, automatizar el auto-layout y sugerir flujos de navegación, pero solo el humano puede imbuir al prototipo de la "fricción" o "fluidez" necesaria para un test de usabilidad honesto, decidir qué nivel de fidelidad es el adecuado para cada fase del proyecto y asegurar que la simulación refleje fielmente el modelo mental del usuario, permitiendo fallar rápido y barato para triunfar con propósito.
**Empoderamiento:** Usamos la tecnología para automatizar la creación de componentes repetitivos y la lógica de variables complejas, permitiendo que el experto se centre en la orquestación de la experiencia y en la captura de insights críticos durante la validación.

---

## 1. Descripción Detallada
El Prototipado Rápido en Figma es la capacidad de crear simulaciones interactivas de alta fidelidad que se comportan como productos reales. No es solo "enlazar pantallas"; es **Ingeniería de la Validación Temprana**. El enfoque v2.0 incorpora la **Prototipación Avanzada con Variables y Lógica Condicional**, donde se pueden simular carritos de compra reales, sistemas de login, estados dinámicos y animaciones quirúrgicas (Smart Animate), permitiendo ahorrar miles de euros en desarrollo al validar la UX completa antes de escribir una sola línea de código.

## 2. Escenarios de Aplicación
- **Validación de Concepto con Stakeholders:** Presentación de ideas "que funcionan" para obtener aprobación de dirección o inversión.
- **Sesiones de User Testing de Alta Fidelidad:** Observación del comportamiento real del usuario ante un sistema que parece final (Maze/Test de guerrilla).
- **Traspaso Técnico (Handoff) Impecable:** Demostración exacta a los desarrolladores de cómo deben ser las transiciones, microinteracciones y lógica de errores.
- **Iteración de Flujos Complejos (SaaS/Fintech):** Prueba de lógica condicional (Ej: "Si el usuario tiene > 100€, muestra X, si no Y") dentro de Figma.
- **Demos de Venta y Preventa:** Creación de versiones personalizadas de la App para clientes específicos en cuestión de horas.

## 3. Requisitos de Implementación
- **Maestría en Figma Pro:** Uso avanzado de Componentes, Variantes, Propiedades de instancia y Auto Layout (Resposividad nativa).
- **Control de Prototipado Avanzado:** Dominio de Variables (Strings, Booleans, Numbers, Colors), Expresiones y Lógica Condicional (`if/else`).
- **Uso Crítico de Smart Animate:** Capacidad de crear transiciones fluidas y naturales calculando jerarquías de nombres de capas.

---

## 4. Diferencial: Enlaces Básicos vs. Prototipado Sistémico v2.0

| Dimensión | Enfoque "Ir de A a B" | Prototipado de Alta Densidad (v2.0) |
| :--- | :--- | :--- |
| **Lógica** | Lineal y rígida. | Condicional y Dinámica (Variables). |
| **Realismo** | Pantallas estáticas. | Datos reales cambiantes en tiempo real. |
| **Animación** | Disolvencias genéricas. | Movimiento coreografiado (Smart Animate). |
| **Componentes** | Piezas sueltas. | Variantes sistémicas e interactivas. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Arquitectura de Componentes Interactivos y Variables
**Objetivo:** Crear la "maquinaria" del prototipo para que sea fácil de escalar.
1.  **Creación de Componentes Vivos:** Define componentes que ya tengan sus estados (Hover, Pressed, Selected) integrados para no repetir enlaces.
2.  **Configuración de Variables de Estado:** Crea variables para el nombre del usuario, el saldo del carrito o el estado del login para una simulación real.

**Prompt Maestro de Dirección de Prototipado:**
```text
Actúa como Master Prototyping Specialist y Especialista en Figma Avanzado. Para el flujo de [FLUJO], realiza el siguiente plan de simulación: 
1. Define los 'Puntos de Interacción' críticos: [Ej: Formulario de pago y confirmación de éxito]. 
2. Diseña la 'Lógica Condicional': ¿Qué variables controlarán el flujo? (Ej: Una variable booleana 'is_logged_in' que redirige a home o login). 
3. Especifica las 'Transiciones Maestras': Uso de Smart Animate con curva 'Ease-in-out' y duración de '300ms' para sensación premium. 
4. Detalla el uso de 'Auto Layout': Asegura que el prototipo se puede testear en un iPhone 14 y en un monitor Desktop sin deformarse. 
5. Protocolo de 'Validación': ¿Cómo recogeremos el feedback del usuario en Figma (comentarios) o vía herramienta externa (Maze)?
```

### Fase 2: Montaje de Flujos, Refinamiento de Animación y Testeo
... (Expansión técnica sobre el uso de 'After Delay' para estados automáticos, la creación de overlays modales persistentes y la preparación del modo 'Preview' para dispositivos móviles mediante Figma Mirror) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de creación de prototipos automatizada.*

1.  **Trigger:** El diseñador termina de definir el User Flow en un diagrama (Sitemap/Miro).
2.  **Nodo de Traducción a Figma IA:** El sistema genera automáticamente el esquema de pantallas y conecta los botones principales basándose en el diagrama de flujo.
3.  **Nodo de Inyección de Librería de Estilos:** IA aplica automáticamente los componentes maestros (botones, menús) del Design System a los bloques placeholder.
4.  **Nodo de Verificación de Enlaces Rotos:** Un bot recorre el prototipo buscando botones sin destino o transiciones incoherentes antes de compartir el enlace.
5.  **Output:** Enlace de prototipo funcional funcional y listo para la primera fase de revisión con el cliente.

---

## 7. Ejemplo Práctico: App de Delivery de Comida
**Reto:** El cliente no entendía cómo funcionaba el "seguimiento en el mapa" mirando imágenes estáticas.
**Acción v2.0:** Se creó un prototipo avanzado con Smart Animate donde el ciclista se mueve realmente por el mapa tras 2 segundos. Se usaron variables para que el usuario pudiera "añadir hamburguesas" y ver cómo subía el precio del carrito en tiempo real.
**Resultado:** El cliente quedó impresionado ("¡Parece real!"). Se detectó que el botón de 'Pagar' era confuso en pantallas pequeñas y se corrigió antes de programar, evitando semanas de retrabajo técnico.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
