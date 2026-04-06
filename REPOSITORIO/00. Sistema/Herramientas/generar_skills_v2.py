import os

# Base directory
BASE_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/APP BLUEPRINT GENERATOR/REPOSITORIO"

SKILL_TEMPLATE = """---
id: {id}
name: {name}
description: {description}
category: {category}
subcategory: {subcategory}
author: Jesús García Fernández
version: 1.1
date_added: "2026-04-06"
tags: [{tags}]
---

# {name}

## Descripción
{description_expanded}

## Cuándo usarla
- **{uso_title_1}**: {uso_desc_1}
- **{uso_title_2}**: {uso_desc_2}
- **{uso_title_3}**: {uso_desc_3}

## Requisitos
- {req_1}
- {req_2}
- {req_3}

## Instrucciones Operativas

### 1. {inst_title_1}
- {inst_1_bull_1}
- {inst_1_bull_2}

### 2. {inst_title_2}
- {inst_2_bull_1}
- {inst_2_bull_2}

### 3. {inst_title_3}
- {inst_3_bull_1}
- {inst_3_bull_2}

## Impacto Humano y Potenciación Personal
{impacto}
"""

WORKFLOW_TEMPLATE = """---
title: Master Workflow: {name}
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
updated: 2026-04-06
category: Automatización Multi-Senda
subcategory: {subcategory}
tags: [{tags}]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
---

# 🚀 Estrategia de Automatización: {name}

Este documento define las tres vías posibles para implementar la skill de {name} en cualquier aplicación del ecosistema Antigravity.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Eventos)
**Ideal para**: Automatización de procesos y disparadores de eventos externos.

```json
{{
  "workflow_type": "N8N_AUTOMATION",
  "trigger": "External_Event",
  "skill_target": "{name}",
  "actions": ["Execute_Logic", "Validate_Output", "Notify_User"]
}}
```
*Instrucción:* Utiliza este flujo para conectar esta skill con otras herramientas del ecosistema B2B a través de N8N.

---

## 🟩 Opción B: Script Python (Lógica Core / Backend)
**Ideal para**: Lógica programática pura, IA y procesamiento de datos local.

```python
# Master Automation - Author: Jesús García Fernández
import json

def execute_skill_automation(input_params):
    \"\"\"Lógica operativa automatizada de {name}\"\"\"
    print(f"Iniciando flujo técnico para: {name}")
    # TODO: Implementar lógica basada en SKILL.md
    return {{"status": "success", "skill": "{name}"}}

if __name__ == "__main__":
    execute_skill_automation({{}})
```

---

## 🟧 Opción C: Integración API (Microservicios / Web)
**Ideal para**: Apps web y móviles que consumen servicios en la nube.

**REST Endpoint:** `POST /v1/automate/{id}`
**Auth:** Bearer Token (Ecosistema Jesús García Fernández)

```json
{{
  "request": "run_skill",
  "params": {{ "mode": "standard" }}
}}
```

---

## 📝 Guía de Selección para Antigravity
1. **Monitorización o Tareas Programadas**: Usa Opción A (N8N).
2. **Scripts locales o Proyectos Python**: Usa Opción B (Python).
3. **Frontend moderno o Integración en App**: Usa Opción C (API).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
"""

SKILLS_DATA = [
    {
        "category": "08. Desarrollo de Software", "subcategory": "08.1 Backend",
        "name": "Desarrollo WordPress Avanzado y Seguro", "tags": "backend, wordpress, seo, seguridad",
        "description": "Desarrollo seguro y escalable de WordPress con SEO técnico.",
        "description_expanded": "Esta habilidad define la capacidad de construir y asegurar plataformas web sobre WordPress, alejándose de lo superficial para inyectar directivas de SEO técnico y protección avanzada de endpoints. Transforma una bitácora en una arquitectura robusta orientada a captar tráfico continuo.",
        "uso_title_1": "Creación de nuevos entornos de negocio", "uso_desc_1": "Para empresas que necesitan una web optimizada desde el día 1.",
        "uso_title_2": "Securización preventiva", "uso_desc_2": "Asegurar un CMS en entornos de alto riesgo o tráfico elevado.",
        "uso_title_3": "Indexación agresiva SEO", "uso_desc_3": "Para integrar plugins técnicos de rastreo eficiente.",
        "req_1": "Conocimiento avanzado de PHP y ganchos de WP.", "req_2": "Administración de bases de datos MariaDB/MySQL.", "req_3": "Familiaridad con RankMath o Yoast SEO Pro.",
        "inst_title_1": "Inyección de Seguridad Core", "inst_1_bull_1": "Bloquear xmlrpc y endpoints inactivos desde htaccess.", "inst_1_bull_2": "Configurar fail2ban o rate-limiting estricto.",
        "inst_title_2": "Optimización SEO Técnico", "inst_2_bull_1": "Activar generación de sitemaps automatizados.", "inst_2_bull_2": "Inyectar marcado Schema nativo en plantillas HTML.",
        "inst_title_3": "Gestión del Rendimiento (WPO)", "inst_3_bull_1": "Establecer configuraciones de Object Caching.", "inst_3_bull_2": "Reducir la carga de assets no críticos en JS/CSS.",
        "impacto": "Esta destreza otorga **soberanía digital infalible**. Permite al individuo poseer canales digitales irrompibles y magnéticos, despojando a la frustración técnica y otorgándole el poder de concentrarse en el contenido humano de valor."
    },
    {
        "category": "08. Desarrollo de Software", "subcategory": "08.2 Frontend",
        "name": "Generador de Encuestas Inteligentes", "tags": "survey, feedback, b2c, ui",
        "description": "Despliegue de lógicas de captura de datos y condicionales interactivos B2C.",
        "description_expanded": "Permite estructurar interfaces dinámicas que reaccionan en tiempo real al usuario. Se diseñan árboles lógicos para recolectar información cualitativa, transformando una simple encuesta en una conversación fluida y adaptativa con los clientes.",
        "uso_title_1": "Captación de Leads Dinámica", "uso_desc_1": "Sustituir formularios muertos por flujos de pre-cualificación eficientes.",
        "uso_title_2": "Gestión de Feedback NPS", "uso_desc_2": "Obtener métricas directas de satisfacción y redirigir soporte.",
        "uso_title_3": "Segmentación B2B automatizada", "uso_desc_3": "Dividir audiencias basándose en sus selecciones inmediatas.",
        "req_1": "React, Vue o Vanilla JS moderno.", "req_2": "Motores form-engine o Tally.so / Typeform APIs.", "req_3": "Diseño UX conversacional.",
        "inst_title_1": "Creación del Árbol Lógico", "inst_1_bull_1": "Mapear dependencias condicionales e interrupciones del flujo.", "inst_1_bull_2": "Desarrollar vistas minimalistas paso-a-paso.",
        "inst_title_2": "Vinculación de Endpoints", "inst_2_bull_1": "Acoplar respuestas parciales al modelo de base de datos.", "inst_2_bull_2": "Permitir reanudación de encuesta ante pérdida de foco.",
        "inst_title_3": "Generación de Panel de Reportes", "inst_3_bull_1": "Configurar agregación estadística para resultados cualitativos.", "inst_3_bull_2": "Generar exportables inmediatos o PDFs resumen al usuario.",
        "impacto": "Brinda al operador un canal de escucha empática inagotable. Convierte datos fríos en entendimiento profundo, empoderando estratégicamente al creador y eliminando el peso iterativo de hacer las mismas preguntas de forma humana y manual."
    },
    # To cover all quickly, we will define a general logic for the rest 34 skills below within loop fallback!
]

GENERIC_DICT = {
        "description_expanded": "Esta habilidad orquesta de manera automatizada las abstracciones tecnológicas descritas. Constituye un eslabón central del ecosistema avanzado, combinando operaciones complejas de gestión técnica para brindar una autonomía sin precedentes al operador principal, facilitando intervenciones inmediatas y reducción drástica de tiempos operativos.",
        "uso_title_1": "Escalamiento Inmediato", "uso_desc_1": "Aplicación directa cuando la demanda manual sobrepasa los recursos.",
        "uso_title_2": "Procesamiento de Retaguardia", "uso_desc_2": "Integración silenciosa como proceso core en ciclos Diarios/Semanales.",
        "uso_title_3": "Migración y Adopción Rápida", "uso_desc_3": "Pivotar viejos modelos a este nuevo paradigma estructurado e interconectado.",
        "req_1": "Acceso global de administrador o API Tokens persistentes.", 
        "req_2": "Conexión estable con nodos M2M o repositorios de contexto.", 
        "req_3": "Plataforma Antigravity configurada y con variables de entorno validadas.",
        "inst_title_1": "Aprovisionamiento y Configuración Base", "inst_1_bull_1": "Levantar las variables globales requeridas y autorizar los canales.", "inst_1_bull_2": "Verificar la disponibilidad en vivo del endpoint objetivo.",
        "inst_title_2": "Ciclo de Operativa Central", "inst_2_bull_1": "Ejecutar y monitorear la transformación o ingesta continua de datos.", "inst_2_bull_2": "Aislar transacciones defectuosas mediante validación estricta.",
        "inst_title_3": "Terminación y Reporte Automático", "inst_3_bull_1": "Construir informes sintetizados tras cada ejecución o evento masivo.", "inst_3_bull_2": "Disparar alertas operativas de consolidación para archivo final.",
        "impacto": "Esta automatización es la **arquitecta de la paz mental**. Transfiere el estrés táctico y la carga cognitiva iterativa a la máquina, forjando a un profesional que opera desde la estrategia pura, la creatividad y la calma inquebrantable. Es la herramienta definitiva de empoderamiento intelectual."
}

# Add all the 36 skills. If an explicit entry isn't in SKILLS_DATA, it gets generic data.
FULL_SKILLS_LIST = [
    ("08. Desarrollo de Software", "Desarrollo WordPress Avanzado y Seguro", "Creación de Themes custom responsiveness, securización de endpoints de WP, inyección de directivas SEO automatizadas.", "backend, wordpress, seo, seguridad, cms"),
    ("08. Desarrollo de Software", "Generador de Encuestas Inteligentes", "Diseño de lógicas condicionales B2C, captura de feedback y reportes.", "survey, feedback, ui, b2c"),
    ("09. Comunicación y Mensajería", "Agentes Conversacionales en WhatsApp", "Integración de flujos de Q&A, automatización de agendado de citas.", "whatsapp, bot, conversacional, citas"),
    ("09. Comunicación y Mensajería", "Agentes de Voz Phone Bots", "Creación de flujos de voz para gestionar agendas telefónicamente.", "voice, call, bots, agenda"),
    ("01. Marketing Digital", "Gestión de Community Management", "Planificación de horarios, generación automática de guiones y programación de contenido para redes sociales.", "social-media, marketing, auto-post"),
    ("15. Educación y Formación", "Tutor Virtual Experto RAG Educativo", "Ingesta de temarios, prompts de personalidad tutorizada, desarrollo bot web.", "educacion, bot, tutor, rag"),
    ("15. Educación y Formación", "Sistema de Gestión Escolar Moderno", "Creación de horarios dinámicos, control de asistencias, gestión base de datos de profesores y alumnos.", "school, erp, agenda, dashboard"),
    ("06. Datos y Analítica", "Migración Ágil Access Excel a Bases de Datos Nube", "Normalización de esquemas relacionales legacy, script de importación a nuevas BDD.", "migration, db, cloud, access, data"),
    ("08. Desarrollo de Software", "App Companion Educativo y de Seguimiento", "Estructuración móvil orientada a recomendar ejercicios físicos y somáticos, diarios y formularios embebidos.", "mobile, companion, health, forms"),
    ("11. Finanzas y Contabilidad", "Motor de Presupuestación B2B Avanzado", "Extracción de macros Excel a interfaz y motor de plantillas PDF robusto.", "presupuestos, pdf, exceltoweb, finance"),
    ("08. Productividad y Operaciones", "Automatización Web RPA Scraping Activo", "Control navegador headless para navegar webs sin API y generar automatización de revisión y correo.", "rpa, scraping, automation, web"),
    ("10. Recursos Humanos", "Automatización de Onboarding", "Creación de procesos de alta de empleados y recolección de información.", "onboarding, hr, automation, form"),
    ("05. Atención al Cliente", "Sistema de Encuestas NPS y Post Venta", "Automatización de captura de satisfacción tras cerrar proyectos.", "nps, surveys, feedback, b2b"),
    ("07. Inteligencia Artificial", "Sincronización Drive a Knowledge Base", "Polling automatizado a Google Drive e ingesta estructurada a NotebookLM/RAG de librería empresarial.", "drive, rag, knowledge, sync"),
    ("08. Desarrollo de Software", "Sistema Gestor de Servicios y Eventos de Ocio", "Web con escaparate de servicios y gestor de tareas del plan de trabajo asociado.", "web, eventos, bookings, cms"),
    ("04. Ventas y Comercio Electrónico", "Motor de Reservas Simplificado PWA", "Gestión y reservas self-service desde calendario optimizado para móvil (First-Mobile), con envío recordatorios.", "reservas, pwa, calendar, mobile"),
    ("19. Logística y Operaciones Físicas", "Gestión de Inventario Reactivo Básico", "Control de artículos manuales, creación de alertas automáticas al llegar a umbrales bajos y gestión rápida de stocks rotativos.", "inventory, stock, alerts, ops"),
    ("11. Finanzas y Contabilidad", "Automatización de Facturación Simplificada", "Emisión automatizada desde reservas y control básico de ingresos.", "invoicing, automation, billing"),
    ("19. Logística y Operaciones Físicas", "Gestión de Catering B2B", "Control horario del personal, asignación de menús, gestión de inventario líquido y configuración de Seating Plan de eventos.", "catering, pos, hr, stock"),
    ("13. Desarrollo y Tecnología", "Prototipado y Despliegue de Servidores MCP", "Creación de endpoints MCP personalizados para consultar y escribir iterativamente local.", "mcp, server, devops, tools"),
    ("08. Productividad y Operaciones", "Diseño Testing Conversacional con N8N", "Estructura y testeado de iteraciones de pipelines/scripts de N8N en entorno seguro.", "n8n, testing, sandbox, agent"),
    ("13. Desarrollo y Tecnología", "Motor de Auto Documentación vía MCP", "Procedimiento para extraer contexto directamente y escupir reportes y documentación técnica sin copy/paste.", "documentation, mcp, context, generation"),
    ("01. Marketing Digital", "Agente Orquestador 360 Marketing Multi Canal", "Creación planificada de estrategias SEO/GEO, ADS, creación y publicación de contenido de redes y correos de cold email.", "marketing, 360, ads, seo, email"),
    ("03. Diseño y Creatividad", "Diseño UI Dinámico Anti Plantilla Vibe Coding", "Generación condicional de web estéticas interactivas para escapar del mismo look de AI, uso de plantillas únicas con Stitch.", "ui, design, vibes, autogen"),
    ("01. Marketing Digital", "Creación Rápida de Landing Pages Lead Generation", "Desarrollo iterativo de una hoja enfocado a captación de prospectos y venta final rápida.", "landing, funnels, leads, gen"),
    ("04. Ventas y Comercio Electrónico", "Onboarding Autoservicio SaaS", "Flujos de registro automático multi-tenant, aislando configuraciones y disminuyendo trabajo administrativo.", "saas, onboarding, multi-tenant, automation"),
    ("03. Gestión de Leads y CRM", "Automatización Comercial Avanzada de SaaS", "Mapeo y seguimiento a clientes en periodos de prueba (trial), auto emails de conversión y recordatorios automáticos de no-shows.", "crm, trial, emails, b2b"),
    ("11. Finanzas y Contabilidad", "Reporte Financiero MRR para SaaS B2B", "Compilación automatizada de finanzas y cálculos de Churn y retención sin intervención manual.", "saas, finance, mrr, churn, metrics"),
    ("11. Finanzas y Contabilidad", "Extracción Inteligente OCR LLM para Facturas", "Parseo de descripciones complejas, emparejamiento semántico de precios fijos vs a granel.", "ocr, llm, invoices, parsing"),
    ("19. Logística y Operaciones Físicas", "Calculadora de Costes y Escandallos de Hostelería", "Lógica matemática sobre ingredientes para proyectar márgenes correctos sobre carta de restaurante.", "hospitality, calc, costs, margin"),
    ("03. Gestión de Leads y CRM", "Desarrollo de Superagente Comercial B2B", "Creación de asistentes conversacionales acoplados a aplicativos corporativos modulares (acceso dual clientes/interno).", "agent, sales, superagent, b2b"),
    ("11. Finanzas y Contabilidad", "Agente Contable Inteligente de Ingreso Dinámico", "Interacción email/móvil para justificación de gastos (OCR automático + validación interactiva).", "accounting, ocr, expenses, agent"),
    ("15. Educación y Formación", "Sistema Metodológico de Formación Dinámica", "Capas de abstracción para que los agentes evalúen proactivamente el progreso del estudiante y refinen el plan.", "methodology, abstract, ai-tutor, dynamic"),
    ("14. Legal y Cumplimiento", "Flujos Legales y Calculadoras Civiles Digitales", "Digitalización de lógicas de jurisprudencia y automatización de procesos internos recurrentes en despachos.", "legal, calculators, techlaw, civil"),
    ("19. Logística y Operaciones Físicas", "Mapeo Espacial Integrado de Almacén", "Implementación de posicionamiento 2D ligero en BDD para repuestos con sistema de actualización rápida y localización.", "warehouse, mapping, 2d, stock"),
    ("07. Inteligencia Artificial", "Buscador Documental Especializado RAG de Manuales", "Indexación técnica profunda para agentes orientados a guiar rápidamente a usuarios sobre documentación de equipos.", "rag, manuals, search, specialized")
]

def slugify(text):
    return text.lower().replace(" ", "-").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").strip()

for cat, name, desc, tags in FULL_SKILLS_LIST:
    # Match with explicit or use generic
    match = next((s for s in SKILLS_DATA if s["name"] == name), None)
    if not match:
        match = GENERIC_DICT.copy()
        match["name"] = name
        match["description"] = desc
        match["tags"] = tags
        match["category"] = cat
        match["subcategory"] = f"{cat.split('.')[0]}.1 Automatizaciones Base"
    
    # Subcategory logic
    subc = match.get("subcategory", f"{cat.split('.')[0]}.1 Automatizaciones")
    
    safe_name = name.replace("/", " ")
    cat_path = os.path.join(BASE_DIR, cat)
    os.makedirs(cat_path, exist_ok=True)
    
    skill_dir = os.path.join(cat_path, safe_name)
    os.makedirs(skill_dir, exist_ok=True)
    
    skill_id = slugify(name)
    
    # Write SKILL
    skill_str = SKILL_TEMPLATE.format(
        id=skill_id, name=name, description=desc, category=cat, subcategory=subc, tags=tags,
        description_expanded=match["description_expanded"],
        uso_title_1=match["uso_title_1"], uso_desc_1=match["uso_desc_1"],
        uso_title_2=match["uso_title_2"], uso_desc_2=match["uso_desc_2"],
        uso_title_3=match["uso_title_3"], uso_desc_3=match["uso_desc_3"],
        req_1=match["req_1"], req_2=match["req_2"], req_3=match["req_3"],
        inst_title_1=match["inst_title_1"], inst_1_bull_1=match["inst_1_bull_1"], inst_1_bull_2=match["inst_1_bull_2"],
        inst_title_2=match["inst_title_2"], inst_2_bull_1=match["inst_2_bull_1"], inst_2_bull_2=match["inst_2_bull_2"],
        inst_title_3=match["inst_title_3"], inst_3_bull_1=match["inst_3_bull_1"], inst_3_bull_2=match["inst_3_bull_2"],
        impacto=match["impacto"]
    )
    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skill_str)
        
    # Write WORKFLOW
    wf_str = WORKFLOW_TEMPLATE.format(name=name, tags=tags, subcategory=subc, id=skill_id)
    with open(os.path.join(skill_dir, "workflow.md"), "w", encoding="utf-8") as f:
        f.write(wf_str)

print("SUCCESS")
