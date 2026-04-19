---
title: Data Engineering (Data Pipelines & Infrastructure Mastery)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 06. Datos y Analítica
subcategory: Transformación y Limpieza
tags: [data-engineering, etl-elt, data-pipelines, data-warehouse, data-lake, orchestration, airflow, medallion-architecture, information-integrity, data-ops]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 189
---

## 0. Filosofía Human-Centric AI
*Esta habilidad construye los cimientos sobre los que descansa toda la inteligencia del negocio al crear tuberías de datos robustas y confiables, utilizando la tecnología para automatizar el flujo de información y permitir que el humano trabaje sobre una "fuente de verdad" íntegra, transparente y siempre disponible para la toma de decisiones.*

**El Rol del Humano:** El Ingeniero de Datos debe ser un "Garantes de la Pureza del Dato". La IA puede automatizar la creación de esquemas de bases de datos, optimizar las consultas SQL complejas para mejorar el rendimiento y predecir fallos en la orquestación de flujos de trabajo (Pipelines), pero solo el humano puede asegurar que el diseño de la arquitectura refleje fielmente las reglas de negocio, decidir cómo priorizar la carga de datos críticos frente a los accesorios, y garantizar que la infraestructura de datos sea resiliente, segura y respete la ética en la gestión de la información privada.
**Empoderamiento:** Usamos la tecnología para sustituir la incertidumbre de los datos aislados por un ecosistema de información unificado y potente.

---

## 1. Descripción Detallada
Data Engineering (v2.0) es la competencia de diseñar, construir y mantener la infraestructura para el procesamiento masivo de datos. No es solo "mover datos"; es **Arquitectura de la Información Fluida**. El enfoque v2.0 se basa en la **Medallion Architecture** (Capas Bronze, Silver, Gold), integrando procesos ETL/ELT, orquestación avanzada (Airflow/Prefect) y gestión de Data Warehouses modernos (BigQuery/Snowflake). El objetivo es transformar datos crudos y sucios en activos de alta calidad, normalizados y listos para ser consumidos por analistas, científicos de datos y modelos de Machine Learning.

## 2. Escenarios de Aplicación
- **Integración de Fuentes Heterogéneas:** Consolidación de datos de CRMs (Salesforce), E-commerce (Shopify) y logs de App en un único Data Lake.
- **Automatización de Limpieza y Normalización:** Creación de pipelines que eliminan duplicados, unifican formatos de fecha y validan esquemas automáticamente.
- **Construcción de Data Warehouses Corporativos:** Diseño de modelos dimensionales (Star Schema) que permiten consultas analíticas ultrarrápidas.
- **Orquestación de Procesos Complejos:** Programación de dependencias entre cientos de tareas de datos para asegurar el orden de ejecución.
- **Implementación de Observabilidad de Datos:** Creación de dashboards de salud de los pipelines y linaje de datos para saber exactamente de dónde viene cada número.

## 3. Requisitos de Implementación
- **Domino Avanzado de SQL:** Capacidad para realizar transformaciones complejas, ventanas (window functions) y CTEs.
- **Programación de Backend Data:** Uso fluido de Python para scripts de integración y manipulación de datos masivos.
- **Experiencia en Herramientas de Orquestación:** Conocimiento de Airflow, Dagster u herramientas de automatización de pipelines equivalentes.
- **Entendimiento de la Infraestructura Cloud:** Habilidad para configurar buckets de almacenamiento, funciones serverless y servicios de procesamiento de datos gestionados.

---

## 4. Diferencial: Procesamiento Manual vs. Data Engineering v2.0

| Dimensión | Enfoque Legacy (Silos) | Data Engineering (v2.0) |
| :--- | :--- | :--- |
| **Fiabilidad** | Alta probabilidad de error humano. | Automatización total con validación (QA). |
| **Escalabilidad** | Se rompe al aumentar el volumen. | Diseñado para crecer de forma elástica. |
| **Integración** | Datos pegados "con parches". | Pipelines integrados y orquestados. |
| **Velocidad** | Los reportes tardan días. | Datos frescos en minutos/segundos. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Diseño de la Arquitectura y Modelado
**Objetivo:** Crear un mapa claro de cómo va a fluir y transformarse el dato.
1.  **Selección del Modelo de Datos:** IA ayuda a elegir entre OBT (One Big Table) o Esquema en Estrella según el motor de consulta.
2.  **Mapeo de Linaje (Lineage):** Definición de la traza del dato desde el origen hasta el Dashboard final.

**Prompt Maestro de Data Engineering:**
```text
Actúa como un Senior Data Engineer y Arquitecto de Pipelines. Diseña el ecosistema de datos para [PROYECTO/EMPRESA]. 
1. Estructura la Medallion Architecture: Define qué trataremos en la capa Bronze (Raw), Silver (Cleaned) y Gold (Business Ready). 
2. Diseña el Pipeline ETL: Describe el flujo desde la extracción vía API de [FUENTE] hasta el almacenamiento en [DATA_WAREHOUSE]. 
3. Configura la Orquestación: Genera el esquema de un DAG de Airflow que maneje reintentos en caso de fallo y avise a Slack si el pipeline se rompe. 
4. Implementa Validaciones de Calidad (Data Quality): ¿Qué tests automatizados (Ej: Not Null, Unique, Range) debemos poner en cada etapa? 
5. Plan de Carga Incremental: ¿Cómo vamos a cargar solo los datos nuevos cada hora para ahorrar costes de computación?
```

### Fase 2: Construcción, Orquestación y Data-Ops
... (Expansión técnica sobre el uso de dbt (Data Build Tool) para transformaciones SQL modulares, la implementación de infraestructuras como código (Terraform) para los servicios de datos y la creación de un sistema de monitorización de la frescura de los datos (Data Freshness) para garantizar que los usuarios siempre ven información actualizada) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de tubería de información.*

1.  **Trigger:** Evento temporal (cron) o llegada de nuevos archivos al sistema de almacenamiento primario.
2.  **Nodo de Extracción (Ingestion):** El sistema lanza un worker de Python que se conecta a las fuentes origen y vuelca los datos en la capa Bronze.
3.  **Nodo de Transformación y QA:** IA revisa el esquema y ejecuta los scripts de limpieza, moviendo los datos validados a la capa Silver.
4.  **Nodo de Agregación de Negocio:** El motor de base de datos ejecuta las vistas Gold que unen tablas y calculan KPIs finales.
5.  **Output:** Tablas Gold listas para el BI; el sistema de orquestación marca el ciclo como "Exitoso" y libera recursos.

---

## 7. Ejemplo Práctico: E-commerce 'FashionFlow'
**Reto:** Tenían los datos de stock en Excel, los de ventas en Shopify y los de marketing en Facebook. Saber el beneficio real de un producto les llevaba 3 días de trabajo manual.
**Action v2.0:** Los ingenieros crearon un pipeline que une las 3 fuentes cada hora en un Data Warehouse en la nube.
**Resultado:** Ahora el equipo de compras sabe el beneficio exacto por SKU en tiempo real. Redujeron el stock inmovilizado un 20% al ver qué productos no tenían rotación rentable inmediatamente.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
