---
title: Auditoría de Diseño, Gestión de Deuda UX y Control de Calidad Visual
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 02. Generación de Contenido
subcategory: Diseño UI/UX
tags: [design-audit, consistency, ux-debt, visual-inventory, quality-assurance, design-system, accessibility, scalability, ia-design-audit]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 057
---

## 0. Filosofía Human-Centric AI
*Esta habilidad garantiza la honestidad visual y la integridad del diseño, utilizando la tecnología para diagnosticar y sanar las inconsistencias que degradan la experiencia humana.*

**El Rol del Humano:** El auditor de diseño debe ser un "Detective de la Excelencia". La IA puede escanear miles de pantallas buscando valores de color fuera de rango o botones sin alineación matemática, pero solo el humano puede evaluar si la "sensación" de la marca se mantiene en un flujo complejo, decidir qué deuda técnica es prioritaria para el confort del usuario y asegurar que el sistema no solo sea correcto, sino que transmita la calidad y la confianza que una relación humana requiere.
**Empoderamiento:** Usamos la tecnología para automatizar la recopilación de activos y realizar comparativas de regresión visual masivas, permitiendo que el experto se centre en la estrategia de unificación y en la toma de decisiones sobre la arquitectura del sistema de diseño.

---

## 1. Descripción Detallada
La Auditoría de Diseño es una inspección técnica profunda del estado visual y funcional de un producto. No es solo "mirar qué está feo"; es **Ingeniería del Saneamiento UX**. El enfoque v2.0 incorpora la **Gestión Proactiva de la Deuda UX y la Auditoría de Escalabilidad**, donde se analizan las inconsistencias tipográficas, el uso errático del color, la fragmentación de componentes y la falta de accesibilidad, generando un inventario crítico y un plan de acción (Roadmap de Saneamiento) que unifica la experiencia y mejora la eficiencia del equipo de producto.

## 2. Escenarios de Aplicación
- **Integración en Proyectos Maduros y Fragmentados:** Unificación de un producto que ha crecido de forma desorganizada en diferentes manos.
- **Pre-fase de Rediseño Integral (Re-branding):** Diagnóstico preciso del punto de partida para no repetir errores históricos.
- **Control de Calidad tras Lanzamientos de Alta Presión:** Verificación de que la implementación en código respeta fielmente los estándares del Design System.
- **Auditoría Periódica de Consistencia:** Revisión semestral para asegurar que la "entropía de diseño" no está degradando la marca.
- **Auditoría de Accesibilidad Legal (WCAG):** Verificación técnica de cumplimiento de normativas de inclusión para evitar riesgos legales.

## 3. Requisitos de Implementación
- **Maestría en Fundamentos de Diseño Visual:** Ojo entrenado para detectar falta de alineación, jerarquía débil o uso inconsistente de tokens de color.
- **Dominio de Herramientas de Inspección Técnica:** Chrome DevTools, Figma Dev Mode y herramientas de auditoría automática (Lighthouse, Axe).
- **Capacidad de Documentación de Deuda Técnica:** Habilidad para categorizar errores por impacto (Usuario) y esfuerzo (Desarrollo).

---

## 4. Diferencial: Feedback Subjetivo vs. Auditoría Técnica Profesional v2.0

| Dimensión | Enfoque "Me parece que..." | Auditoría de Alta Densidad (v2.0) |
| :--- | :--- | :--- |
| **Evidencia** | Opinión personal. | Capturas, datos de código y cumplimiento de normas. |
| **Alcance** | Visual / Superficial. | Sistémico (Componentes, Tokens, Código, UX). |
| **Documentación** | Reunión breve. | Reporte detallado con Inventario de Inconsistencias. |
| **Resultado** | "Hay que arreglarlo". | Plan de acción priorizado por Severidad e Impacto. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Inventario Visual y Muestreo de Pantallas Críticas
**Objetivo:** Obtener una visión real y cruda del estado actual del sistema.
1.  **Extracción de Componentes:** Captura todos los tipos de botones, formularios y tipografías que conviven hoy en la Web/App.
2.  **Identificación de Patrones Rotos:** Detecta dónde se están usando 3 tonos de azul diferentes para el mismo tipo de acción.

**Prompt Maestro de Dirección de Auditoría de Diseño:**
```text
Actúa como Auditor de Diseño Senior y Especialist en Quality Assurance (QA) Visual. Para el producto [NOMBRE], realiza el siguiente diagnóstico técnico: 
1. Realiza un 'Inventario de Inconsistencias' en: Tipografía (fuentes y escalas), Color (uso de paleta), y Espaciado (grids y márgenes). 
2. Clasifica cada hallazgo en: [Inconsistencia Visual / Error de Usabilidad / Falta de Accesibilidad]. 
3. Asigna un Nivel de Impacto: [Bajo / Medio / Crítico] basado en cuánto afecta a la tarea principal del usuario. 
4. Propón la 'Normalización' de cada grupo de errores: [Ej: Sustituir todos los botones flotantes por el componente oficial del Design System v2]. 
5. Resume la 'Deuda UX' estimada en horas de diseño/desarrollo para alcanzar la coherencia total.
```

### Fase 2: Análisis de Accesibilidad, Evaluación de Código y Reporte Final
... (Expansión técnica sobre el check de contraste WCAG 2.1, la verificación de la semántica HTML de los componentes y la redacción del reporte ejecutivo de 'Estado del Diseño' para stakeholders) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de control de calidad visual automatizada.*

1.  **Trigger:** El equipo de desarrollo realiza un 'Pull Request' con cambios en el CSS/Tokens de la interfaz.
2.  **Nodo de Comparativa de Regresión Visual:** IA compara píxel a píxel las nuevas pantallas con la versión maestra aprobada.
3.  **Nodo de Detección de Colores Fuera de Paleta:** El sistema avisa si se han introducido códigos HEX que no pertenecen al manual de marca.
4.  **Nodo de Generación de Alerta de Consistencia:** El sistema bloquea el despliegue si detecta que un componente core (ej. Botón Primary) ha cambiado su radio de borde sin autorización.
5.  **Output:** Informe automático de "Pase/Fallo" de diseño enviado al equipo de QA antes de salir a producción.

---

## 7. Ejemplo Práctico: Plataforma de Educación Online
**Reto:** Después de 3 años, la web tenía 5 tipos de menús diferentes y el 40% de los botones eran inaccesibles (poco contraste).
**Acción v2.0:** Se realizó una auditoría de diseño integral que identificó 200 puntos de inconsistencia. Se documentó todo en un muro de Miro y se priorizaron las correcciones de mayor impacto en la conversión.
**Resultado:** Al unificar el diseño bajo un solo estándar coherente, las llamadas a atención al cliente por "no encuentro el curso" bajaron un 30% y la velocidad de carga mejoró al limpiar el CSS redundante.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
