---
title: Base de datos y Cloud (Infraestructura Maestra)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: Bases de Datos
tags: ["estándar-v1.1", "validado", "database", "supabase", "postgresql", "cloud"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 003
---

## Descripción
Esta skill define la arquitectura de datos y la infraestructura en la nube necesaria para soportar aplicaciones escalables. Se centra en el uso de **Supabase (PostgreSQL)** como núcleo de datos, integrando funciones de servidor (Edge Functions) y almacenamiento de archivos (Object Storage). Proporciona las directrices para el diseño de esquemas relacionales, seguridad a nivel de fila (RLS) y optimización de consultas.

## Cuándo usarla
- **Modelado de Datos**: Al inicio de cualquier desarrollo que requiera persistencia de información.
- **Escalabilidad**: Cuando la aplicación necesita manejar grandes volúmenes de datos o concurrencia.
- **Estructura Backend**: Configuración de servicios en la nube sin servidor (Serverless).

## Requisitos
- **Stack Recomendado**: Supabase (PostgreSQL), Firebase Firestore o MongoDB Atlas.
- **Conceptos**: SQL relacional, Migraciones, Índices, Triggers y RLS.
- **Variables**: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`.

## Impacto Humano y Empoderamiento Personal
Tener una base de datos bien estructurada y en la nube es como tener un **segundo cerebro digital** organizado y seguro. Al automatizar la persistencia y escalabilidad, liberas tu mente de la gestión técnica de la infraestructura y te empoderas para tomar decisiones basadas en datos reales. La integridad y disponibilidad de la información son los pilares sobre los que construyes tu libertad profesional y la confianza de tus usuarios.

## Instrucciones y Pasos detallados que se debe seguir:

### 1. Diseño del Esquema (Schema Design)
- Definir entidades principales y sus relaciones (1:1, 1:N, N:M).
- Aplicar normalización para evitar redundancia innecesaria.
- Establecer claves primarias (UUID recomendados) y foráneas.

### 2. Configuración de Seguridad y RLS
- Habilitar Row Level Security (RLS) en todas las tablas sensibles.
- Crear políticas que permitan solo al autor ver/editar sus propios datos.
- Configurar roles de usuario (admin, editor, user).

### 3. Implementación de Funciones y Triggers
- Desarrollar funciones en SQL o Edge Functions (TypeScript) para lógica pesada.
- Configurar triggers para automatizar campos de auditoría (`created_at`, `updated_at`).
- Implementar validaciones complejas de datos a nivel de motor.

### 4. Backup y Monitorización
- Configurar copias de seguridad automáticas diarias.
- Establecer alertas de rendimiento e índices lentos.
- Monitorizar el uso de almacenamiento y cuotas de API.

## Workflow N8N / Automatización
*Ver archivo `workflow.md` para la implementación técnica en Python, N8N y API.*

## Seguridad y Mejores Prácticas
- 🔐 **Principio de Mínimo Privilegio**: No usar el usuario `postgres` para la app; usar roles limitados.
- 📉 **Índices Estratégicos**: Crear índices solo en columnas de búsqueda frecuente para no penalizar inserciones.
- 📦 **Almacenamiento**: Usar Buckets para archivos grandes; nunca guardar binarios directos en SQL.

## Notas y advertencias
- ⚠️ **Cambios de Esquema**: Realizar siempre mediante migraciones versionadas para evitar pérdida de datos en producción.

## Changelog
- v1.0 — Versión inicial (Autogenerada)
- v1.1 — Normalización V1.1: Stack Supabase/PostgreSQL + Sección Empoderamiento Humano.
