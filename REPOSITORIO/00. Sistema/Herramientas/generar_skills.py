import os

SKILLS = [
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

BASE_DIR = "/Volumes/TC/0 - DESARROLLO PROTOTIPOS/APP BLUEPRINT GENERATOR/REPOSITORIO"

SKILL_TEMPLATE = """---
id: {id}
name: {name}
description: {description}
category: {category}
author: Antigravity System
version: 1.1
date_added: "2026-04-06"
tags: [{tags}]
---

# {name}

## Descripción
Esta habilidad define la capacidad técnica para implementar soluciones orientadas a los requerimientos descritos, asegurando que la tecnología trabaje al servicio del bienestar organizativo y el control eficiente.

## Instrucciones Operativas y Flujo
{description}

## Impacto Humano y Potenciación Personal
Potencia profesionalmente al operador al delegar la complejidad técnica al proceso automatizado o guiado. Esto erradica la carga cognitiva manual y aumenta el grado de tranquilidad y dominio técnico del sistema por parte del individuo, garantizando resultados profesionales y permitiendo el enfoque en la estrategia humana de alto nivel.
"""

WORKFLOW_TEMPLATE = """---
title: Master Workflow: {name}
version: 1.1
author: Antigravity System
created: 2026-04-06
updated: 2026-04-06
category: Automatización Multi-Senda
tags: [{tags}]

license: CC BY-NC 4.0
notice: >
  Esta skill es generada automáticamente para el stack Antigravity.
---

# 🚀 Estrategia de Automatización: {name}

Este documento define las vías posibles para implementar la skill en cualquier aplicación del ecosistema Antigravity.

---

## 🟦 Opción A: Flujo N8N / Automatización Reactiva

```json
{{
  "workflow_type": "N8N_AUTOMATION",
  "trigger": "User_Request_or_Event",
  "skill_target": "{name}",
  "actions": ["Execute_Logic", "Validate_Output"]
}}
```
*Instrucción:* Utiliza este flujo para desencadenar {description}

---

## 🟩 Opción B: Scripting Python Core

```python
# Lógica Core Automatizada
def execute_skill_automation(input_params):
    print(f"Ejecutando: {name}")
    # Objetivo: {description}
    return {{"status": "success", "skill": "{name}"}}

if __name__ == "__main__":
    execute_skill_automation({{}})
```

---

## 🟧 Opción C: Integración Interfaz / API Rest

**Endpoint sugerido:** `POST /v1/automate/{id}`
**Carga útil interactiva:** Interfaz modular acoplada.

---
*Validado v1.1 - Sistema Antigravity.*
"""

def slugify(text):
    return text.lower().replace(" ", "-").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").strip()

report_links = []

for category, name, desc, tags in SKILLS:
    safe_name = name.replace("/", " ")
    cat_path = os.path.join(BASE_DIR, category)
    os.makedirs(cat_path, exist_ok=True)
    
    skill_dir = os.path.join(cat_path, safe_name)
    os.makedirs(skill_dir, exist_ok=True)
    
    skill_id = slugify(name)
    
    # Generate SKILL.md
    skill_content = SKILL_TEMPLATE.format(id=skill_id, name=name, description=desc, category=category, tags=tags)
    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skill_content)
        
    # Generate workflow.md
    workflow_content = WORKFLOW_TEMPLATE.format(id=skill_id, name=name, description=desc, category=category, tags=tags)
    with open(os.path.join(skill_dir, "workflow.md"), "w", encoding="utf-8") as f:
        f.write(workflow_content)
        
    report_links.append(f"- **{category}** / [{name}](file://{skill_dir.replace(' ','%20')})")

with open("/tmp/links_report.md", "w") as f:
    f.write("\\n".join(report_links))

print("SUCCESS")
