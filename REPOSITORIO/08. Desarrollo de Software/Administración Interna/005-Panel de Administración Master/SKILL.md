---
title: Panel de Administración (Backoffice Master)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 08. Desarrollo de Software
subcategory: Administración Interna
tags: ["estándar-v1.1", "validado", "admin", "dashboard", "nextjs", "metrics"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 005-ADMIN
---

## Descripción
Esta skill permite construir la "torre de control" de cualquier aplicación: el Panel de Administración o Backoffice. Proporciona las herramientas para gestionar usuarios, monitorizar métricas críticas (KPIs), visualizar datos mediante gráficos interactivos y realizar tareas operativas internas (CRUD) de manera eficiente y segura.

## Cuándo usarla
- **Gestión Interna**: Para que el equipo operativo gestione pedidos, usuarios o contenido.
- **Analytics**: Visualización de rendimiento del negocio en tiempo real.
- **Control de Acceso**: Interfaz para gestionar roles y permisos de la plataforma.
- **Auditoría**: Revisión de logs y eventos del sistema.

## Requisitos
- **Stack Recomendado**: Next.js (App Router), Shadcn UI, TanStack Table, Recharts o Chart.js.
- **Conceptos**: Server Components, Client Components, Server Actions para CRUD.
- **Seguridad**: Middleware para protección de rutas de administración (`/admin/*`).

## Impacto Humano y Empoderamiento Personal
Un panel de administración no es solo un conjunto de tablas; es la **claridad operativa**. Al automatizar la visualización de datos complejos, transformas el caos de la información en **decisiones estratégicas**. Esta herramienta empodera al profesional al darle una visión de 360 grados de su proyecto, permitiéndole identificar cuellos de botella y oportunidades de crecimiento sin depender de programadores para cada informe o cambio manual.

## Instrucciones y Pasos detallados que se debe seguir:

### 1. Estructura de Navegación y UI
- Diseñar un Layout con Sidebar persistente y Header de estado.
- Utilizar componentes de UI consistentes (Shadcn UI) para tablas, botones y modals.
- Implementar modo oscuro/claro para mejorar la salud visual en jornadas largas.

### 2. Gestión de Datos (Data Tables)
- Implementar tablas con filtrado, ordenamiento y paginación en el servidor (TanStack Table).
- Crear flujos de edición (Modals o páginas dedicadas) con validación de formularios (Zod/React Hook Form).
- Implementar acciones en lote (Bulk actions) para mejorar la productividad.

### 3. Visualización de Métricas (Dashboards)
- Identificar los 4-5 KPIs principales y presentarlos mediante "Stat Cards" con tendencia.
- Implementar gráficos de línea/barra interactivos para ver la evolución temporal (Recharts).
- Conectar los gráficos directamente a la base de datos (Supabase) con caché inteligente.

### 4. Seguridad de Administración (Gatekeeping)
- Implementar un nivel de acceso "Role: Admin" verificado mediante Middleware.
- Crear logs de actividad para saber quién hizo qué cambio en el panel.
- Habilitar autenticación de dos factores (2FA) obligatoria para entrar al backoffice.

## Workflow N8N / Automatización
*Ver archivo `workflow.md` para la implementación técnica en Python, N8N y API.*

## Seguridad y Mejores Prácticas
- 🛡️ **Prevención de Exposición**: Nunca exponer datos de usuarios finales que no sean necesarios para la operativa.
- 📉 **Optimización de Queries**: Usar vistas de PostgreSQL para agregaciones pesadas en lugar de procesar todo en JS.
- 🧪 **Testing**: Verificar que las rutas de admin son inaccesibles para usuarios estándar.

## Notas y advertencias
- ⚠️ **Rendimiento**: Un panel cargado de gráficos puede ser lento. Utiliza carga diferida (Suspense) para las métricas más pesadas.

## Changelog
- v1.0 — Versión inicial (Autogenerada)
- v1.1 — Normalización V1.1: Stack Next.js/Shadcn + Sección Empoderamiento Humano.
