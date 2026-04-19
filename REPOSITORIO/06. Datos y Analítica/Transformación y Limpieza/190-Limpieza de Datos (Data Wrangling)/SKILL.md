---
title: Limpieza de Datos & Wrangling (Data Integrity & Quality Mastery)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-18
category: 06. Datos y Analítica
subcategory: Transformación y Limpieza
tags: [data-cleaning, data-wrangling, data-quality, pandas, regex, anomaly-detection, data-normalization, information-integrity, etl-logic, garbage-in-garbage-out]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 190
---

## 0. Filosofía Human-Centric AI
*Esta habilidad garantiza la honestidad y veracidad de cualquier análisis al purificar la información desde su origen, utilizando la tecnología para automatizar la corrección de errores y permitir que el humano trabaje sobre una base de datos íntegra, libre de ruidos y sesgos técnicos que distorsionen la realidad.*

**El Rol del Humano:** El Purificador de Datos debe ser un "Garantes de la Integridad de la Información". La IA puede identificar automáticamente valores nulos (nulls) y proponer métodos de imputación estadística, detectar duplicados complejos mediante algoritmos de similitud de texto (Fuzzy matching) y normalizar formatos de forma masiva en segundos, pero solo el humano puede validar si un dato "atípico" es realmente un error o una señal de mercado crítica, decidir qué criterios éticos rigen el tratamiento de datos incompletos y asegurar que la limpieza no elimine la diversidad y los matices que hacen que los datos reflejen el mundo real.
**Empoderamiento:** Usamos la tecnología para sustituir el caos informativo por la claridad basada en la calidad extrema del dato.

---

## 1. Descripción Detallada
La Limpieza de Datos y Wrangling (v2.0) es la competencia de transformar datos crudos y desordenados en un formato útil y veraz. No es solo "borrar filas vacías"; es **Ingeniería de la Calidad del Dato**. El enfoque v2.0 se centra en el principio "Garbage In, Garbage Out", integrando técnicas avanzadas de manipulación (Pandas/NumPy), limpieza mediante Expresiones Regulares (Regex) y detección proactiva de anomalías estructurales. Abarca el mapeo de fuentes heterogéneas, la unificación de esquemas y la reconstrucción lógica de información faltante, asegurando que el 80% del tiempo invertido en el proceso de datos sea eficiente y productivo.

## 2. Escenarios de Aplicación
- **Unificación de Bases de Datos Multidispositivo:** Consolidación de perfiles de clientes que aparecen duplicados con ligeras variaciones entre el CRM y el E-commerce.
- **Normalización de Formatos de Fecha y Moneda:** Estandarización de registros provenientes de diferentes países con nomenclaturas temporales y financieras dispares.
- **Tratamiento Inteligente de Outliers:** Identificación y corrección de picos de datos absurdos (Ej: Edad 150 años) que arruinarían cualquier modelo estadístico.
- **Limpieza de Texto Masiva (Strings):** Eliminación de caracteres especiales, espacios extra y errores tipográficos en descripciones de productos o comentarios de clientes.
- **Imputación de Datos Faltantes:** Relleno lógico de campos vacíos mediante medias móviles, regresiones o reglas de negocio para no perder registros valiosos.

## 3. Requisitos de Implementación
- **Maestría en Herramientas de 'Data Munging':** Uso fluido de Python (Pandas) o Lenguaje R.
- **Pensamiento Lógico y Sanity Checks:** Capacidad para diseñar pruebas que verifiquen si los datos finales tienen sentido común (Ej: ¿Es posible que el IVA sea mayor que el Total?).
- **Dominio de Expresiones Regulares (Regex):** Habilidad para buscar y sustituir patrones de texto complejos en miles de celdas.
- **Rigurosidad en la Documentación del Proceso:** Registro de todas las transformaciones realizadas para asegurar la trazabilidad y reproducibilidad del análisis.

---

## 4. Diferencial: Limpieza Manual vs. Data Wrangling v2.0

| Dimensión | Enfoque Legacy (Manual/Excel) | Data Wrangling (v2.0) |
| :--- | :--- | :--- |
| **Escalabilidad** | Inviable para más de mil filas. | Procesa millones de registros en segundos por código. |
| **Reproducibilidad** | Imposible saber qué se borró y por qué. | El código es la bitácora exacta de cada cambio. |
| **Fiabilidad** | Muy alta probabilidad de error al "arrastrar". | Basada en lógica determinista y tests de QA. |
| **Complejidad** | Limitada a filtros simples. | Permite transformaciones profundas y anidadas. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Auditoría de Suciedad y Mapeo de Transformación
**Objetivo:** Identificar dónde y cómo están rotos los datos.
1.  **Análisis de Perfilado (Profiling):** IA ayuda a detectar el porcentaje de nulos, la distribución de valores y la presencia de caracteres extraños en cada columna.
2.  **Definición de Reglas de Limpieza:** Creación de un diccionario de transformaciones (Ej: "Columna A debe ser siempre Minúscula y tipo INTEGER").

**Prompt Maestro de Data Wrangling (Limpieza de Datos):**
```text
Actúa como un Senior Data Curator y Experto en Data Wrangling. Facilita el proceso de purificación del dataset [NOMBRE_DATASET]. 
1. Realiza el Diagnóstico de Calidad: Identifica nulos, duplicados y outliers en [COLUMNAS_CLAVE]. 
2. Diseña el Pipeline de Limpieza: Genera el script en Python (Pandas) para estandarizar los formatos de fecha, eliminar espacios en blanco y unificar la columna de [VARIABLE] bajo la norma [ESTÁNDAR]. 
3. Lógica de Imputación: Si faltan datos en la columna [X], ¿qué método estadístico sugieres para rellenarlos sin sesgar el resultado final? 
4. Filtro de Sanidad (Consistency Check): Diseña 3 reglas lógicas que los datos finales deban cumplir para ser considerados 'Válidos para Producción'. 
5. Reporte de 'Limpieza Realizada': Genera un resumen de cuántos registros han sido modificados o eliminados y cuál es la nueva 'tasa de confianza' del dato.
```

### Fase 2: Ejecución, Validación y QA del Dato
... (Expansión técnica sobre el uso de la técnica de 'Fuzzy Matching' para unir nombres similares, la implementación de scripts de deduplicación basados en identificadores únicos cruzados y la creación de un dataset final 'Tidy Data' donde cada variable sea una columna y cada observación una fila independiente) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de purificación continua.*

1.  **Trigger:** Ingesta de nuevos datos crudos desde una fuente externa (API, CSV, DB).
2.  **Nodo de Perfilado Automático:** El sistema analiza la calidad inicial y detecta si el dataset está por debajo del umbral de limpieza aceptable.
3.  **Nodo de Transformación por Código:** IA ejecuta el pipeline de limpieza predefinido (Deduplicación -> Formateo -> Imputación).
4.  **Nodo de Validación Final:** Un proceso de QA verifica que las reglas de sanidad se cumplen (Ej: No hay precios negativos).
5.  **Output:** Datos íntegros volcados al Data Warehouse; notificación al equipo de analítica de que los nuevos datos están listos y limpios.

---

## 7. Ejemplo Práctico: Retailer 'ShopGlobal'
**Reto:** Tenían 50.000 clientes duplicados porque unos se registraban como "J. Perez", otros como "Juan Perez" y otros con el email en mayúsculas.
**Acción v2.0:** Aplicaron un pipeline de Data Wrangling con limpieza de texto y Fuzzy Matching. La IA detectó que el 30% de sus "clientes" eran en realidad las mismas personas con diferentes registros.
**Resultado:** Unificaron la base de datos de clientes. Ahorraron miles de euros en envíos de marketing duplicados y pudieron por primera vez calcular el Life Time Value (LTV) real de sus usuarios.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
