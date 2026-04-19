---
title: Auditoría de Accesibilidad Universal y Cumplimiento WCAG (A11y)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 03. Diseño y Creatividad
subcategory: 03.1 Diseño UI/UX
tags: [accesibilidad, wcag, inclusión, ética-digital, diseño-universal, a11y, ia-accessibility, compliance]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 122
---

## 0. Filosofía Human-Centric AI
*Esta habilidad garantiza que el progreso tecnológico no deje a nadie atrás, utilizando la tecnología para derribar barreras y asegurar el acceso universal a la información como un derecho fundamental.*

**El Rol del Humano:** El Auditor de Accesibilidad debe ser un "Garante de la Inclusión". La IA puede detectar errores de contraste, falta de etiquetas Alt y estructuras de encabezado incorrectas a escala masiva, pero solo el humano puede evaluar si el "orden de lectura" tiene sentido lógico, si la navegación por teclado es realmente fluida para una persona con discapacidad motriz y si el lenguaje utilizado es comprensible para personas con diversidad cognitiva.
**Empoderamiento:** Usamos la tecnología para automatizar el cumplimiento técnico, permitiendo que el experto se centre en la experiencia humana real y en la creación de soluciones creativas que mejoren la usabilidad para todos.

---

## 1. Descripción Detallada
La Auditoría de Accesibilidad Universal es el proceso de verificación técnica y funcional de activos digitales bajo las **Pautas de Accesibilidad para el Contenido Web (WCAG 2.1/2.2)**. No es una lista de verificación superficial; es **Ingeniería de la Dignidad Digital**. El enfoque v2.0 incorpora la **Accesibilidad Predictiva vía IA**, donde el sistema analiza el código antes del despliegue para sugerir correcciones semánticas y la implementación de **Atributos ARIA (Accessible Rich Internet Applications)** avanzados que permiten una comunicación perfecta con tecnologías de asistencia.

## 2. Escenarios de Aplicación
- **Cumplimiento Legal y Normativo (EN 301 549 / Sección 508):** Auditorías obligatorias para plataformas públicas y servicios esenciales.
- **Optimización de Conversión (SEO y Usabilidad):** Mejora del posicionamiento orgánico mediante el uso de semántica HTML correcta.
- **Diseño de Productos Inclusivos:** Creación de aplicaciones que funcionan perfectamente para usuarios con discapacidad visual, auditiva, motriz o cognitiva.
- **Auditoría de Documentación Digital:** Asegurar que PDFs, presentaciones y hojas de cálculo sean accesibles para lectores de pantalla.
- **Formación de Equipos de Desarrollo:** Integración de la cultura "Accessibility-First" en el flujo de trabajo de programación.

## 3. Requisitos de Implementación
- **Maestría en WCAG 2.1/2.2 (Niveles A, AA, AAA):** Conocimiento profundo de los 4 principios (Perceptible, Operable, Comprensible, Robusto).
- **Herramientas de Auditoría Técnica:** Axe DevTools, Lighthouse, WAVE y herramientas de inspección de contraste.
- **Uso de Lectores de Pantalla:** Capacidad práctica de navegar con NVDA, JAWS o VoiceOver para validación humana.

---

## 4. Diferencial: Auditoría Automática vs. Certificación Humana v2.0

| Dimensión | Auditoría Automática (Lighthouse) | Certificación A11y (v2.0) |
| :--- | :--- | :--- |
| **Cobertura** | Detecta el 30-40% de los fallos. | Detecta el 100% (Técnico + Funcional). |
| **Contexto** | Valida sintaxis técnica. | Valida sentido semántico y usabilidad real. |
| **Legislación** | Indicador orientativo. | Respaldo para auditorías legales oficiales. |
| **Enfoque** | Corregir errores de código. | Garantizar la experiencia de usuario universal. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Diagnóstico Técnico y de Semántica
**Objetivo:** Eliminar los errores "ruidosos" que bloquean a las máquinas de asistencia.
1.  **Escaneo Semántico:** Verifica que cada elemento interactivo tenga un rol, nombre y valor definido.
2.  **Validación de Contrastes:** Asegura un ratio mínimo de 4.5:1 para texto normal y 3:1 para texto grande.

**Prompt Maestro de Auditoría de Accesibilidad:**
```text
Actúa como un Especialista en Accesibilidad Digital (CPACC). Analiza el panel de usuario [INTERFAZ] basándote en WCAG 2.2 nivel AA. 
1. Realiza una auditoría del orden del foco del teclado: ¿Es lógico y predecible? 
2. Evalúa el uso de colores y texturas: ¿Se transmite información crítica solo mediante el color? 
3. Revisa los formularios: ¿Tienen etiquetas (labels) vinculadas correctamente y mensajes de error accesibles? 
4. Genera una lista de 5 mejoras de código (ARIA) para aumentar la compatibilidad con VoiceOver. 
5. Proporciona una justificación ética y de negocio (ROI) para implementar estos cambios.
```

### Fase 2: Validación Funcional con Usuario Externo (Simulado o Real)
... (Expansión técnica sobre el testeo con lectores de pantalla, la navegación sin ratón y la auditoría de carga cognitiva en interfaces complejas) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de cumplimiento continuo.*

1.  **Trigger:** Se realiza un 'Pull Request' en el repositorio de código.
2.  **Nodo de Auditoría Estática:** La IA escanea el código fuente buscando omisiones de accesibilidad (Alt-tags, Contrastes, Roles).
3.  **Nodo de Reporte de Bloqueo:** Si se detectan fallos de nivel 'Crítico', se bloquea el despliegue y se envía una alerta al equipo de diseño.
4.  **Nodo de Sugerencia de Fix:** El sistema propone el fragmento de código corregido siguiendo las pautas WCAG.
5.  **Output:** Software accesible por defecto, manteniendo el cumplimiento legal y ético de forma automática en cada iteración.

---

## 7. Ejemplo Práctico: Plataforma de Banca Online
**Reto:** Los usuarios invidentes no podían realizar transferencias porque el botón de "Confirmar" no tenía etiqueta de texto.
**Acción v2.0:** Auditoría profunda con VoiceOver. Implementación de una arquitectura de regiones ARIA que guía al usuario paso a paso por el formulario.
**Resultado:** Cero barreras de acceso detectadas en la siguiente auditoría legal. Aumento de la base de usuarios y eliminación de riesgos de demandas por discriminación digital.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
