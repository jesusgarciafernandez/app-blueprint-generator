---
title: Algoritmos de Recomendación y Sistemas de Personalización Predictiva
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 01. Marketing Digital
subcategory: Publicidad de Pago (Ads)
tags: [recommendation-systems, collaborative-filtering, content-based-filtering, matrix-factorization, personalization, ia-predictiva, clv-optimization, cold-start]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 036
---

## 0. Filosofía Human-Centric AI
*Esta habilidad asegura que la tecnología ayude al usuario a descubrir lo que realmente necesita, eliminando la fatiga de decisión con elegancia y ética.*

**El Rol del Humano:** El consultor de IA aplicada debe actuar como el "Arquitecto de la Experiencia". La IA calcula correlaciones y probabilidades entre productos, pero el humano define las reglas de negocio (ej: no recomendar productos agotados o con baja satisfacción) y asegura que la recomendación sea útil y no intrusiva.
**Empoderamiento:** Usamos los algoritmos para que cada usuario sienta que la plataforma ha sido diseñada exclusivamente para él, aumentando la lealtad y el valor percibido.

---

## 1. Descripción Detallada
Los Sistemas de Recomendación son motores de Inteligencia Artificial diseñados para predecir la preferencia de un usuario por un ítem (producto, contenido o servicio). Son los motores invisibles de gigantes como Amazon, Netflix o TikTok. Esta habilidad abarca tres arquitecturas principales:
1.  **Filtrado Colaborativo:** Basado en la similitud entre usuarios o ítems (Usuarios que compraron X también compraron Y).
2.  **Filtrado Basado en Contenido:** Basado en los atributos de los ítems (Si te gustan las camisas azules, te gustarán otros artículos azules).
3.  **Modelos Híbridos y Deep Learning:** Combinación de ambos para superar problemas como el "Cold Start" (falta de datos iniciales).

El enfoque v2.0 integra el **Análisis de Sentimiento en Tiempo Real**, donde la recomendación se adapta no solo a lo que el usuario compró en el pasado, sino a cómo interactúa hoy (clics rápidos, tiempo de permanencia, tipo de scroll).

## 2. Escenarios de Aplicación
- **Personalización de E-commerce:** Secciones dinámicas de "Completar el look" o "Inspiración para ti".
- **Curaduría de Contenido (Media/SaaS):** Feed de noticias o sugerencias de funciones de la App basadas en el perfil de uso.
- **Email Marketing Predictivo:** Envío de ofertas únicas para cada cliente basadas en su probabilidad de compra.
- **Optimización de Retención:** Sugerencia de contenido de "rescate" cuando se detectan señales de abandono (Churn).

## 3. Requisitos de Implementación
- **Recolección de Eventos (Event Tracking):** Sistema de recolección de datos sobre clics, vistas, carritos y compras.
- **Infraestructura de Datos:** Almacenamiento capaz de procesar matrices de afinidad (ej: BigQuery, MongoDB o bases de datos de grafos).
- **Métricas de Evaluación:** Dominio de KPIs técnicos como Precision@K, Recall@K y métricas de negocio como el aumento de AOV (Average Order Value).

---

## 4. Diferencial: Recomendación Estática vs. Predictiva v2.0

| Dimensión | Lógica Estática (Reglas) | Recomendación Predictiva (v2.0) |
| :--- | :--- | :--- |
| **Origen** | Decidido por el equipo ("Manual"). | Decidido por el algoritmo (Patrón oculto). |
| **Adaptabilidad** | Igual para todos los perfiles similares. | Única y personal para cada usuario individual. |
| **Contexto** | Ignorado o muy básico. | Considera dispositivo, hora, ubicación y sentimiento. |
| **Evolución** | Requiere actualización manual. | Aprende y mejora con cada nueva interacción. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Análisis de Datos y Limpieza de Atributos
**Objetivo:** Preparar el "Cerebro" del recomendador.
1.  **Vectorización de Ítems:** Convierte los atributos de productos en valores numéricos procesables.
2.  **Mapeo de Comportamiento:** Clasifica las acciones del usuario por peso (Comprar > Añadir al carrito > Ver).

**Prompt Maestro de Recomendación:**
```text
Actúa como Especialista en Machine Learning para Marketing. Para el catálogo de productos [CATALOGO], diseña un sistema de recomendación híbrido. 
Propón la lógica de peso para los siguientes eventos: [LISTA_EVENTOS]. 
¿Cómo resolverías el problema del 'Cold Start' para una nueva categoría de productos? 
Genera 3 estrategias de personalización de UI para mostrar estas recomendaciones de forma sutil.
```

### Fase 2: Entrenamiento y Despliegue del Modelo
... (Expansión técnica sobre factorización de matrices y redes neuronales) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de refresco y entrega de recomendaciones.*

1.  **Trigger:** El usuario accede a la Home o ficha de producto.
2.  **Nodo de Consulta:** El sistema envía el ID de usuario y el contexto actual al motor de IA.
3.  **Nodo de Filtrado:** Exclusión automática de ítems ya comprados, sin stock o no aptos por reglas éticas.
4.  **Nodo de Ránking:** El motor devuelve los 5 ítems con mayor puntuación de probabilidad de éxito.
5.  **Output:** Visualización instantánea de los productos recomendados en la interfaz.

---

## 7. Ejemplo Práctico: Tienda de Cosmética Online
**Reto:** Los usuarios siempre compraban lo mismo y no exploraban nuevas líneas.
**Acción v2.0:** Se implementó un motor basado en "Rutinas" que recomendaba el siguiente paso lógico de belleza según su última compra.
**Resultado:** Incremento del 25% en productos por pedido y subida del 15% en la tasa de repetición de compra.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
