---
title: Gestión de CRM y Gobernanza de Datos (Salesforce & HubSpot Mastery)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 03. Gestión de Leads y CRM
subcategory: Sincronización con CRM
tags: [crm-management, salesforce, hubspot, data-architecture, revops, sales-ops, martech-stack, data-governance]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 132
---

## 0. Filosofía Human-Centric AI
*Esta habilidad orquesta la memoria colectiva de la organización, utilizando la tecnología para asegurar que cada interacción con el cliente sea recordada, valorada y utilizada para construir relaciones de confianza duraderas.*

**El Rol del Humano:** El Administrador de CRM debe ser un "Arquitecto de la Verdad Corporativa". La IA puede ejecutar migraciones de datos massivas, normalizar campos de texto y predecir cuándo una oportunidad está en riesgo, pero solo el humano puede definir los procesos de negocio que realmente aportan valor al equipo comercial, asegurar que la herramienta facilite el trabajo en lugar de ser una carga burocrática, y garantizar la privacidad y ética en el manejo de los datos sensibles de los clientes.
**Empoderamiento:** Usamos la tecnología para centralizar el conocimiento, permitiendo que cualquier miembro del equipo tenga el contexto completo de un cliente en segundos, eliminando silos de información y acelerando el ciclo de cierre de ventas.

---

## 1. Descripción Detallada
La Gestión de CRM es la capacidad estratégica de configurar y optimizar plataformas de relaciones con clientes como la "Fuente Único de Verdad" (SSOT). No es solo "rellenar fichas"; es **Ingeniería de Operaciones de Ingresos (Revenue Operations)**. El enfoque v2.0 incorpora la **Arquitectura de Datos Bidireccional**, donde el CRM está interconectado con el producto, la facturación (Stripe/ERP) y el soporte técnico, permitiendo una visión de 360 grados del cliente mediante workflows dinámicos que automatizan la vida comercial, desde el lead scoring hasta la renovación de contratos.

## 2. Escenarios de Aplicación
- **Implementación y Migración de CRM:** Configuración desde cero o traslado de datos entre plataformas garantizando la integridad.
- **Automatización de Sales Ops:** Diseño de flujos que asignan leads, envían alertas de estancamiento y actualizan el pipeline automáticamente.
- **Saneamiento y Normalización de Datos:** Procesos de "Data Cleansing" para eliminar duplicados y asegurar que la base de datos es fiable para decisiones.
- **Integración del Stack Tecnológico (MarTech):** Conexión del CRM con herramientas de marketing automation, webinars y analítica web.
- **Generación de Business Intelligence:** Diseño de cuadros de mando (Dashboards) que muestran la salud financiera y la velocidad del pipeline en tiempo real.

## 3. Requisitos de Implementación
- **Acceso con Nivel de Administrador:** Permisos para modificar objetos, campos y flujos en Salesforce o HubSpot Suite.
- **Dominio de Lógica Condicional:** Maestría en Salesforce Flow, HubSpot Workflows o herramientas de orquestación externa (n8n/Make).
- **Entendimiento de la Arquitectura de Objetos:** Definición de relaciones entre Contactos, Empresas, Negocios y Objetos Personalizados.
- **Conocimiento Riguroso de GDPR/LOPD:** Implementación de protocolos de consentimiento y derecho al olvido en la base de datos.

---

## 4. Diferencial: Agenda de Contactos vs. Sistema RevOps v2.0

| Dimensión | Enfoque Tradicional (Agenda) | Excelencia CRM (v2.0) |
| :--- | :--- | :--- |
| **Uso** | Libro de direcciones pasivo. | Motor proactivo de automatización comercial. |
| **Conectividad** | Datos aislados y manuales. | Ecosistema interconectado en tiempo real. |
| **Integridad** | Desordenado y con duplicados. | Gobernanza de datos estricta y profesional. |
| **Valor** | Histórico de lo que pasó. | Predictivo de lo que va a pasar (Forecasting). |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Arquitectura de Datos y Mapeo de Procesos
**Objetivo:** Diseñar un sistema que refleje el proceso real de venta de la empresa.
1.  **Definición del Pipeline Maestro:** Establece las etapas exactas del trato (Deal stages) y los requisitos de información para pasar de una a otra.
2.  **Mapeo de Campos Críticos:** ¿Qué datos son obligatorios para que un lead sea considerado cualificado? (Lead Source, LinkedIn, Teléfono).

**Prompt Maestro de Arquitectura CRM:**
```text
Actúa como un Senior CRM Architect y RevOps Consultant certificado en Salesforce/HubSpot. Diseña el ecosistema de datos para [EMPRESA/SECTOR]. 
1. Estructura el Pipeline de Ventas: Define las 7 etapas desde 'Primer Contacto' hasta 'Cerrado Ganado' y qué ocurre en cada fase. 
2. Diseña 3 'Custom Objects' o campos personalizados necesarios para este negocio específico. 
3. Crea la lógica de 5 Workflows críticos: [Alertas de abandono, Asignación de leads round-robin, Notificación de renovación, etc.]. 
4. Establece el protocolo de 'Higiene de Datos': ¿Cómo evitamos duplicados y cómo normalizamos los campos de industria y país? 
5. Propón el 'Dashboard Ejecutivo': Define las 5 métricas que deben estar en la pantalla del CEO todos los lunes.
```

### Fase 2: Implementación, Testing de Flujos y Adopción de Usuario
... (Expansión técnica sobre la validación de integraciones API, la formación del equipo para asegurar el uso correcto de la herramienta y la auditoría de seguridad de accesos) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de sincronización sistémica.*

1.  **Trigger:** Un cambio de estado en una plataforma externa (Ej: Pago completado en Stripe) o una acción manual en el CRM.
2.  **Nodo de Transformación de Datos:** El sistema traduce el input externo al formato del CRM (Mapeo de campos).
3.  **Nodo de Lógica de Negocio:** ¿Es un cliente nuevo o existente? El sistema actualiza el registro correspondiente y dispara las acciones de post-venta.
4.  **Nodo de Verificación de Integridad:** Se comprueba que no hay duplicados y que los campos obligatorios están rellenados antes del commit final.
5.  **Output:** CRM actualizado y "limpio"; notificaciones enviadas a administración y ventas para iniciar la fase de entrega del servicio.

---

## 7. Ejemplo Práctico: Empresa de Servicios de Limpieza Industrial
**Reto:** Perdían el 20% de las renovaciones de contratos anuales porque nadie se acordaba de llamar al cliente un mes antes del vencimiento.
**Acción v2.0:** Se configuró un workflow en el CRM que 45 días antes de la fecha de caducidad creaba un "Deal" de renovación, asignaba una tarea al comercial y enviaba un email automático de cortesía al cliente agendando una revisión técnica.
**Resultado:** La tasa de renovación subió al 98% en el primer año. El equipo administrativo ahorró 10 horas semanales que antes dedicaban a buscar fechas en archivos Excel antiguos.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
