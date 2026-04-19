---
title: Data Mining & Knowledge Discovery (Extracción de Inteligencia de Datos)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 06. Datos y Analítica
subcategory: Ciencia de Datos
tags: [data-mining, knowledge-discovery, pattern-recognition, market-basket-analysis, association-rules, sequence-mining, data-intelligence, crisp-dm, feature-engineering, industrial-analytics]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 179
---

## 0. Filosofía Human-Centric AI
*Esta habilidad transforma los datos crudos en conocimiento accionable al extraer patrones y correlaciones invisibles al ojo humano, utilizando la tecnología para diseccionar grandes volúmenes de información y permitir que el humano comprenda el "porqué" de los comportamientos y anticipe oportunidades estratégicas con base científica.*

**El Rol del Humano:** El Minero de Datos debe ser un "Garantes de la Causalidad Útil". La IA puede ejecutar algoritmos de asociación (Apriori), detectar secuencias de eventos repetitivos y encontrar correlaciones estadísticas sorprendentes en Terabytes de datos, pero solo el humano puede validar si una correlación tiene sentido de negocio, identificar falsos positivos originados por ruidos en los datos y asegurar que el conocimiento extraído se utilice para mejorar la vida de los usuarios y no para explotar sus vulnerabilidades psicológicas mediante técnicas de manipulación algorítmica.
**Empoderamiento:** Usamos la tecnología para sustituir la duda por la certeza basada en la evidencia extraída de la realidad.

---

## 1. Descripción Detallada
La Minería de Datos (v2.0) es la competencia de extraer conocimiento implícito y potencialmente útil desde grandes volúmenes de datos. No es solo "hacer informes"; es **Ingeniería del Descubrimiento de Inteligencia**. El enfoque v2.0 sigue el marco metodológico **CRISP-DM** (Cross-Industry Standard Process for Data Mining), integrando técnicas de asociación (Market Basket Analysis), minería de secuencias y detección de patrones anómalos. El objetivo es pasar del reporte descriptivo (qué pasó) al análisis diagnóstico (por qué pasó) y exploratorio (qué más está pasando y no sabemos).

## 2. Escenarios de Aplicación
- **Análisis de Cesta de la Compra (Market Basket):** Identificación de productos que tienden a comprarse juntos para optimizar el cross-selling y la disposición en tienda/web.
- **Detección de Patrones de Retención y Abandono:** Minería de las secuencias de comportamiento que preceden a la cancelación de una suscripción.
- **Análisis de Secuencias Temporales de Uso:** Comprensión de cómo los usuarios navegan por una App o Software para identificar cuellos de botella u oportunidades.
- **Minería de Texto y Opinión:** Extracción de temas y sentimientos recurrentes en miles de reseñas de clientes o tickets de soporte.
- **Optimización de Procesos Industriales:** Identificación de las variables de entorno que causan micro-defectos de fabricación mediante el análisis de logs de sensores.

## 3. Requisitos de Implementación
- **Domino de la Metodología CRISP-DM:** Entendimiento del negocio, comprensión de datos, preparación, modelado, evaluación y despliegue.
- **Herramientas de Minería y Análisis Profundo:** Uso de Python (Pandas, Mlxtend para asociación) o herramientas especializadas (RapidMiner/KNIME).
- **Capacidad de Gestión de Big Data:** Habilidad para procesar datos que no caben en memoria (Dask, PySpark) si el volumen lo requiere.
- **Pensamiento Estadístico y Crítico:** Capacidad para filtrar el "ruido" y centrarse en patrones con significancia estadística real y valor de negocio.

---

## 4. Diferencial: Reporting Tradicional vs. Data Mining v2.0

| Dimensión | Enfoque Legacy (Reporting) | Data Mining (v2.0) |
| :--- | :--- | :--- |
| **Enfoque** | Confirma lo que ya sabemos (Kpis). | Descubre lo que no sabemos que está ahí. |
| **Naturaleza** | Descriptiva y retrospectiva. | Exploratoria e intuitiva (IA-Augmented). |
| **Relaciones** | Análisis de variables aisladas. | Análisis de asociaciones y secuencias. |
| **Finalidad** | Controlar el negocio. | Innovar y optimizar el negocio. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Entendimiento de Datos y Preparación de la Minería
**Objetivo:** Limpiar el terreno para que los algoritmos de descubrimiento puedan trabajar.
1.  **Auditoría de Calidad de Datos:** IA ayuda a detectar sesgos en la recolección que podrían generar patrones falsos.
2.  **Transformación y Binning:** Conversión de variables continuas en categorías lógicas (Ej: "Gasto alto/medio/bajo") para algoritmos de asociación.

**Prompt Maestro de Data Mining:**
```text
Actúa como un Senior Data Mining Consultant y Senior Data Scientist. Facilita el proceso de descubrimiento de conocimiento para [CONTEXTO_NEGOCIO]. 
1. Define el Objetivo de Minería: ¿Buscamos asociaciones, secuencias o anomalías? 
2. Diseña el Experimento de Asociación: Si aplicamos el algoritmo Apriori a [DATOS], ¿qué umbrales de 'Soporte' (Support) y 'Confianza' (Confidence) establecerías? 
3. Identifica 'Reglas de Oro': Extrae 3 reglas de tipo "Si ocurre A, entonces ocurre B" que tengan un alto interés para la estrategia. 
4. Análisis de Sustancialidad: ¿Estos patrones son estables en el tiempo o han sido fruto de una campaña puntual? 
5. Plan de Acción de Inteligencia: ¿Cómo convertimos el descubrimiento de que [PATRÓN] en una mejora de [PROCESO/VENTAS]?
```

### Fase 2: Modelado de Descubrimiento y Evaluación de Reglas
... (Expansión técnica sobre el uso de algoritmos de minería de reglas de asociación, la validación de la 'Elevación' (Lift) de las reglas encontradas y la integración del conocimiento extraído en el diseño UX/UI o en la lógica de recomendación del producto) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de descubrimiento continuo.*

1.  **Trigger:** Carga semanal de grandes datasets históricos de transacciones o interacciones.
2.  **Nodo de Reducción y Limpieza:** El sistema filtra datos irrelevantes y prepara el formato "transaccional" para la minería.
3.  **Nodo de Ejecución Alogritmo de Minería:** IA busca automáticamente patrones de asociación y secuencias con alta confianza.
4.  **Nodo de Filtrado de Novedad:** El sistema compara los patrones encontrados con los conocidos, resaltando solo los "nuevos" descubrimientos.
5.  **Output:** Informe de "Nuevos Insights de Negocio"; alerta automática al equipo de estrategia si se detecta un cambio brusco en los patrones habituales de los clientes.

---

## 7. Ejemplo Práctico: Supermercado Online 'FreshClick'
**Reto:** Sus promociones de "2x1" no funcionaban. Enviaban cupones de pañales a gente que no los compraba habitualmente.
**Acción v2.0:** Hicieron Data Mining de 2 años de tickets. La IA descubrió que los clientes de "comida orgánica" tenían una alta asociación (Lift) con la compra de "detergentes ecológicos", aunque fueran categorías separadas.
**Resultado:** Hicieron campañas cruzadas. La facturación de detergentes subió un 40% al impactar al nicho de "estilo de vida consciente" identificado por la minería.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
