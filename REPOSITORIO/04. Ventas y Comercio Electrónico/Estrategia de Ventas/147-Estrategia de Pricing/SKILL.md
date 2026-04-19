---
title: Estrategia de Pricing (Value-Based Revenue Management)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 04. Ventas y Comercio Electrónico
subcategory: Estrategia de Ventas
tags: [pricing-strategy, revenue-optimization, value-based-pricing, psychological-pricing, price-elasticity, marketplace-pricing, dynamic-pricing, subscription-models, net-profit-margin]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 147
---

## 0. Filosofía Human-Centric AI
*Esta habilidad equilibra el valor entregado al cliente con la rentabilidad del negocio, utilizando la tecnología para encontrar el "precio justo" que capture el máximo beneficio sin comprometer la confianza ni la accesibilidad del mercado.*

**El Rol del Humano:** El Arquitecto de Pricing debe ser un "Equilibrista del Valor". La IA puede analizar miles de precios de la competencia en tiempo real, calcular la elasticidad de la demanda según cohortes y sugerir ajustes dinámicos de precios por hora o stock, pero solo el humano puede entender el impacto emocional de un cambio de precio en la lealtad de marca, decidir cuándo mantener un precio estable por ética profesional y asegurar que la estrategia de precios sea transparente, justa y sostenible a largo plazo.
**Empoderamiento:** Usamos la tecnología para sustituir la adivinanza del "cuánto cobrar" por un modelado preciso basado en el valor percibido y la realidad del mercado.

---

## 1. Descripción Detallada
La Estrategia de Pricing es la ciencia de maximizar los ingresos a través del diseño de estructuras de precios inteligentes. No es solo "poner números"; es **Ingeniería del Lucro Estratégico**. El enfoque v2.0 abandona el modelo 'Cost-Plus' (coste + margen) para centrarse en el **Pricing Basado en Valor (Value-Based)** y el **Revenue Management Dinámico**. Utiliza datos de comportamiento para ofrecer diferentes niveles (Tiers) de servicio, empaquetados (Bundles) y disparadores psicológicos que optimizan la conversión y el margen neto, alineando el precio con la disposición a pagar del cliente en cada momento.

## 2. Escenarios de Aplicación
- **Lanzamiento de Productos SaaS o Apps:** Diseño de modelos de suscripción (Freemium, Tiered, Flat-rate) que maximicen el LTV.
- **Optimización de E-commerce con Gran Catálogo:** Ajuste dinámico de precios basado en stock, estacionalidad y precios de la competencia.
- **Estrategias de Skimming (Descremado):** Lanzamiento de productos innovadores a precio alto para capturar el mercado de entusiastas antes de bajarlo.
- **Modelado de Servicios bajo Demanda:** Precios dinámicos (Surge pricing) para equilibrar la oferta y la demanda en tiempo real.
- **Diseño de 'Tiered Pricing' para Empresas (Enterprise):** Creación de niveles de precio complejos que incluyan volumen, SLA y soporte dedicado.

## 3. Requisitos de Implementación
- **Acceso a Datos de Unit Economics Claros:** Conocimiento exacto del CAC, LTV y márgenes de contribución.
- **Herramientas de Benchmarking Automatizado:** Sistemas para monitorizar los precios de la competencia sin intervención manual.
- **Software de Modelado y Simulación:** Capacidad de ejecutar escenarios "What-if" para predecir el impacto de un cambio de precio en la demanda.

---

## 4. Diferencial: Precio Fijo vs. Pricing Estratégico v2.0

| Dimensión | Enfoque Legacy (Precio Fijo) | Pricing Estratégico (v2.0) |
| :--- | :--- | :--- |
| **Lógica** | Costes operativos + % de margen. | Valor percibido y posicionamiento. |
| **Frecuencia** | Se cambia una vez al año. | Dinámico y adaptable al contexto. |
| **Segmentación** | El mismo precio para todos. | Precios por segmento y uso (Usage-based). |
| **Psicología** | Números redondos o aleatorios. | Uso de anclajes, señuelos y sesgos. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Auditoría de Valor y Modelado de Sensibilidad
**Objetivo:** Determinar el techo y el suelo de precio según el mercado.
1.  **Entrevistas de Van Westendorp:** Análisis de la disposición a pagar del cliente (¿A qué precio es caro? ¿A qué precio es una ganga sospechosa?).
2.  **Mapeo de la 'Unidad de Valor':** ¿Por qué paga el usuario realmente? (¿Por usuario, por uso, por éxito?).

**Prompt Maestro de Estrategia de Pricing:**
```text
Actúa como un Senior Revenue Manager y Especialista en Estrategia de Precios. Diseña el modelo de pricing para [PRODUCTO/SERVICIO]. 
1. Define los 3 niveles (Tiers) de precio: [Entry, Growth, Enterprise]. ¿Qué incluye cada uno? 
2. Diseña la estacionalidad de precios: ¿Cómo manejaremos descuentos, Black Friday o subidas por demanda? 
3. Identifica el 'Anclaje Psicológico': ¿Cuál es el precio de referencia que hará que nuestra oferta parezca razonable? 
4. Modela la 'Métrica de Valor': ¿Cobramos por clic, por cuenta, por GB? Justifica por qué es la métrica más justa. 
5. Establece el Protocolo de Subida de Precios: ¿Cómo comunicamos una subida a los clientes actuales para que no se den de baja?
```

### Fase 2: Implementación de Pricing Dinámico y Testeo de Elasticidad
... (Expansión técnica sobre el uso de algoritmos de re-pricing automatizado, el diseño de 'Landing Pages' de pricing con test A/B y el seguimiento del impacto en el margen neto en tiempo real) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de optimización de ingresos.*

1.  **Trigger:** Cambio en el coste de adquisición (CAC), movimiento de precio de la competencia o cambio en el stock/disponibilidad.
2.  **Nodo de Análisis de Elasticidad:** El sistema calcula cómo afectaría un cambio del X% en el precio al volumen de ventas total basado en datos históricos.
3.  **Nodo de Propuesta de Ajuste:** IA sugiere el nuevo precio óptimo para maximizar el margen bruto (Revenue - Costes).
4.  **Nodo de Despliegue de Precios:** Actualización masiva de precios en la web, marketplace o CRM tras la validación humana.
5.  **Output:** Precios optimizados para el máximo beneficio; reporte de impacto en conversion rate y margen neto generado.

---

## 7. Ejemplo Práctico: SaaS de Edición de Vídeo Online
**Reto:** Tenían un precio plano de 20€/mes. Muchos usuarios se quejaban de que era caro para un uso puntual, y los profesionales decían que era demasiado barato (desconfiaban de su potencia).
**Acción v2.0:** Se crearon 3 Tiers: Free (Línea de tiempo limitada), Pro (30€/mes para editores frecuentes) y Pay-per-Render (5€ por vídeo para uso puntual).
**Resultado:** Los ingresos subieron un 60%. Capturaron al usuario ocasional que antes no pagaba y elevaron el ticket de los profesionales que buscaban más potencia, todo sin perder a nadie.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
