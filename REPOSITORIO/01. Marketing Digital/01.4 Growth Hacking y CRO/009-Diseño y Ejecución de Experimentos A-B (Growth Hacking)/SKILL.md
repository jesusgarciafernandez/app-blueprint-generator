---
title: Diseño y Ejecución de Experimentos A/B (Growth Hacking & CRO)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 01. Marketing Digital
subcategory: 01.4 Growth Hacking y CRO
tags: [ab-testing, cro, growth-hacking, experimentos, analítica, conversión, ia-predictiva]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 009
---

## 0. Filosofía Human-Centric AI
*Esta habilidad mata las opiniones ("HIPPOs") y las sustituye por la verdad de los datos observados.*

**El Rol del Humano:** El consultor Growth debe formular la hipótesis estratégica y decidir qué métrica es vital para el negocio. La IA ayuda a diseñar las variantes y a calcular la probabilidad de éxito.
**Empoderamiento:** La tecnología elimina el sesgo cognitivo humano permitiendo que solo las ideas que realmente funcionan lleguen a la mayoría de los usuarios.

---

## 1. Descripción Detallada
Esta habilidad establece un marco de trabajo riguroso para la toma de decisiones basadas en datos. En lugar de basarse en intuiciones, el profesional utiliza experimentos A/B y multivariantes para comparar versiones de una experiencia (landing pages, flujos de onboarding, micro-copy, CTAs) y determinar cuál produce mejores resultados de manera estadísticamente significativa. El enfoque v2.0 integra el **análisis predictivo** para identificar qué variantes tienen mayor "lift" potencial antes de lanzar el test, ahorrando miles de euros en tráfico desperdiciado.

## 2. Escenarios de Aplicación
- **Optimización de Conversión (CRO):** Reducción de la fricción en formularios de registro o checkouts.
- **Validación de Product-Market Fit:** Prueba de diferentes propuestas de valor en la "header" de una web.
- **Micro-Copy Testing:** Evaluación del impacto emocional de palabras específicas en botones de acción.
- **Flujos de Retención:** Experimentos en las notificaciones push para reducir el churn.

## 3. Requisitos de Implementación
- **Herramientas agnósticas:** GTM, PostHog, VWO o scripts de servidor propios.
- **Muestra Crítica:** Tráfico suficiente (calculador de tamaño de muestra) para evitar falsos positivos.
- **Hipótesis ICE/RICE:** Un sistema de priorización para elegir qué probar primero.

---

## 4. Diferencial: Growth Tradicional vs. IA-Augmented Growth v2.0

| Dimensión | Growth Convencional | IA-Augmented Growth (v2.0) |
| :--- | :--- | :--- |
| **Generación de Hipótesis** | Lluvia de ideas manual. | Generación basada en análisis de mapas de calor y grabaciones vía IA. |
| **Diseño de Variantes** | 1 o 2 variantes manuales. | Múltiples variaciones semánticas y visuales automáticas. |
| **Análisis de Resultados** | Estadísticas p-value lentas. | Análisis Bayesiano con detección temprana de ganadores. |
| **Personalización** | Test único para todos. | Segmentación dinámica del experimento según perfil de usuario. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Formulación de Hipótesis Científica
**Objetivo:** Asegurar que el test tiene un propósito claro.
1.  **Observación:** "Los usuarios abandonan en el paso 2 del formulario".
2.  **Solución Propuesta:** "Reducir los campos del formulario de 5 a 3".
3.  **Resultado Esperado:** "Aumento del 15% en la tasa de envío".

**Prompt de Generación de Hipótesis:**
```text
Actúa como un CRO Senior. Analiza estos datos de navegación [DATOS] e identifica 3 fricciones visibles. 
Genera una hipótesis para cada una usando el formato: "Si cambiamos [X] por [Y], esperamos un aumento del [Z]% porque [RAZÓN PSICOLÓGICA]".
```

### Fase 2: Diseño de Variantes y Setup Técnico
... (Expansión técnica sobre implementación en servidor vs navegador) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Flujo operativo integrable.*

1.  **Trigger:** El dashboard detecta una caída de conversión en una página específica (>10%).
2.  **Nodo de Auditoría:** La IA revisa los cambios recientes en esa página y los compara con el histórico.
3.  **Nodo de Propuesta:** Generación automática de 2 variantes de "gancho" (Headline A/B).
4.  **Nodo de Ejecución:** Inyección de las variantes mediante el gestor de contenidos o A/B framework.
5.  **Nodo de Monitoreo:** Al alcanzar el 95% de confianza, el sistema notifica al usuario para aplicar el cambio permanentemente.

---

## 7. Ejemplo Práctico: SaaS de Facturación
**Reto:** El botón "Pruébalo Gratis" no convertía.
**Experimento v2.0:** Se probó contra "Ver Demo en Vivo" y "Empieza tu ahorro hoy".
**Resultado:** "Ver Demo en Vivo" aumentó la conversión un 42%, indicando que el usuario tenía miedo a la curva de aprendizaje, no al precio.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
