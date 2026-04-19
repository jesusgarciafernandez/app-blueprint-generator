---
title: Creación Rápida de Landing Pages de Alta Conversión
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 01. Marketing Digital
subcategory: Generación de Leads
tags: [landing, funnels, leads, conversion-rate, ia-design, copywriting]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 013
---

## 0. Filosofía Human-Centric AI
*Esta habilidad permite que el humano se enfoque en la propuesta de valor, mientras la IA construye el andamiaje técnico y visual.*

**El Rol del Humano:** El consultor debe definir la "Oferta Irresistible". La IA genera la estructura, el copy persuasivo y el diseño preliminar, pero el humano valida que la promesa de marca sea auténtica y ética.
**Empoderamiento:** Democratizamos el diseño de alto nivel. Ya no necesitas un equipo de 3 personas para lanzar una landing efectiva hoy mismo.

---

## 1. Descripción Detallada
Esta habilidad automatiza la creación de páginas de aterrizaje (Landing Pages) optimizadas para la captura de leads. No se trata simplemente de "hacer una web", sino de construir un embudo de conversión que use principios de neuro-marketing y jerarquía visual. El enfoque v2.0 utiliza el **análisis de eye-tracking predictivo** para colocar los elementos clave (CTA, beneficios, pruebas sociales) donde el usuario es más propenso a mirar. Genera no solo el código (HTML/CSS/Tailwind), sino también el copy persuasivo basado en marcos como AIDA o PAS.

## 2. Escenarios de Aplicación
- **Validación de MVPs:** Creación de una landing de preventa para medir el interés del mercado en 24 horas.
- **Campañas de Pago (Ads):** Generación de landings específicas para cada ángulo de venta (Skill 008) para mejorar la relevancia y el Quality Score.
- **Lead Magnets:** Configuración rápida de páginas para descarga de guías, webinars o casos de estudio.
- **Micro-segmentación:** Creación de versiones personalizadas de una landing según el sector o industria del visitante.

## 3. Requisitos de Implementación
- **Framework de Estilado:** Tailwind CSS (recomendado por velocidad y limpieza).
- **Hosting/CDN:** Vercel, Netlify o servidor con soporte para despliegue rápido.
- **Motor de Copy:** Acceso a LLM configurado con el contexto de marca.

---

## 4. Diferencial: Diseño Web Tradicional vs. IA-Generated Landings v2.0

| Dimensión | Enfoque Tradicional | IA-Generated Landing (v2.0) |
| :--- | :--- | :--- |
| **Tiempo de Entrega** | 3-7 días (Diseño + Maquetación). | < 15 minutos (Estructura y Copy). |
| **Copywriting** | Generalista o manual. | Persuasivo, basado en psicología de ventas. |
| **Optimización Movil** | Revisión manual. | Mobile-First por defecto, optimizado para carga < 1s. |
| **Mantenimiento** | Edición manual de código. | Iteración rápida basada en métricas de conversión. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Ingeniería de Oferta y Estructura
**Objetivo:** Definir qué vamos a vender y cómo lo vamos a organizar.
1.  **Define el Core:** ¿Qué problema resuelve el producto? ¿Cuál es el beneficio principal?
2.  **Mapeo de Secciones:** Header (Hero), Problema, Solución, Cómo funciona, Testimonios, FAQ, CTA.

**Prompt de Arquitectura de Landing:**
```text
Actúa como Experto en CRO y Diseño de Landings. 
Para el producto [PRODUCTO], genera la estructura detallada de una landing page optimizada para conversión. 
Incluye el H1 sugerido, los beneficios clave y la estructura del formulario de captura. 
Formatea el resultado para que sea fácil de maquetar con Tailwind CSS.
```

### Fase 2: Maquetación y Despliegue Express
... (Expansión técnica sobre inyección de componentes y validación de velocidad) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica integrable en cualquier constructor o pipeline de desarrollo.*

1.  **Trigger:** Recepción de un nuevo Brief de Producto (Skill 012).
2.  **Nodo de Redacción:** Generación automática de los textos de la landing basados en la Fase 1.
3.  **Nodo de Composición:** Selección de los componentes visuales adecuados (Dark mode, Glassmorphism, etc.).
4.  **Nodo de Despliegue:** Inyección del código en el servidor de staging para revisión.
5.  **Output:** URL temporal lista para validación humana y posterior lanzamiento.

---

## 7. Ejemplo Práctico: Agencia de Seguros
**Reto:** Necesitaban landings específicas para 10 nichos distintos (autónomos, familias, pymes...).
**Acción v2.0:** Se generaron 10 versiones de copy e imágenes personalizadas en una mañana usando esta Skill.
**Resultado:** Incremento del 30% en la tasa de conversión al hablarle directamente a cada perfil.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
