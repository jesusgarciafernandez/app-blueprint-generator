---
title: Análisis de Gráficos (Network Analysis)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 06. Datos y Analítica
subcategory: General
tags: ['graph-analytics', 'network-science', 'centrality', 'community-detection', 'neo4j', 'networkx', 'graph-databases', 'fraud-rings']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 177
---

## Descripción
Habilidad de análisis de datos centrada en el estudio de las relaciones y conexiones entre entidades (nodos) representadas como aristas (links). El Análisis de Gráficos permite comprender sistemas complejos donde la estructura de las conexiones es tan importante como el dato individual. Desde identificar el "influencer" real en una red social hasta detectar anillos de fraude en seguros donde varios siniestros comparten el mismo número de teléfono o dirección, esta skill utiliza la teoría de redes para extraer inteligencia que las bases de datos tradicionales no pueden ver.

## Cuándo usarla
Escenarios que activan esta skill:
- En Ciberseguridad para mapear la propagación de un virus por la red y encontrar los nodos críticos de infección.
- Para detectar fraude organizado (Fraud Rings) en banca analizando conexiones indirectas entre cuentas aparentemente no relacionadas.
- En Marketing para identificar comunidades de usuarios y entender cómo fluye la información o la influencia de marca.
- Para optimizar infraestructuras físicas (redes eléctricas, tuberías de agua) mediante el análisis de vulnerabilidad de nodos.
- En sistemas de recomendación para encontrar productos que "suelen viajar juntos" en grafos de compra.

## Requisitos
- Dominio de librerías de grafos (NetworkX, igraph, PyG).
- Conocimiento de bases de datos de grafos (Neo4j, AWS Neptune, Memgraph) y lenguaje Cypher.
- Comprensión de métricas de centralidad (Degree, Betweenness, PageRank, Eigenvector).
- Experiencia en algoritmos de detección de comunidades (Louvain, Leiden).
- Habilidad para visualizar redes complejas (Gephi, Cytoscape).

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
