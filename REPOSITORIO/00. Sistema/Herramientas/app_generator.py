#!/usr/bin/env python3
"""
App Blueprint Generator — Motor Principal
Jesús García Fernández | jesusgarciafernandez.com

Servidor HTTP local que sirve la interfaz del generador,
analiza las skills del repositorio, compone un Blueprint y genera un ZIP listo
para ser interpretado por cualquier IA de codificación.

Cero dependencias externas. Funciona con Python 3.6+.
"""

import os
import re
import json
import zipfile
import shutil
import math
import webbrowser
import threading
import urllib.parse
import traceback
from collections import Counter
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

# Try to import ThreadingHTTPServer (Python 3.7+)
try:
    from http.server import ThreadingHTTPServer
except ImportError:
    import socketserver
    class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
        daemon_threads = True

# ────────────────────────────────────────────────────────────
# CONFIGURACIÓN
# ────────────────────────────────────────────────────────────
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REPO_ROOT = PROJECT_ROOT
SKILLS_DIR = os.path.join(PROJECT_ROOT, "REPOSITORIO")
INDEX_JS_PATH = os.path.join(PROJECT_ROOT, "INDEX.js")
APPS_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "APPS-CREADAS")
TOOLS_DIR = os.path.join(SKILLS_DIR, "00. Sistema", "Herramientas")
PORT = 5500
AUTHOR = "Jesús García Fernández"
AUTHOR_WEB = "jesusgarciafernandez.com"
TOOL_NAME = "App Blueprint Generator"
TOOL_VERSION = "1.2.0"

# ────────────────────────────────────────────────────────────
# STOPWORDS para español e inglés
# ────────────────────────────────────────────────────────────
STOPWORDS_ES = {
    'de', 'la', 'el', 'en', 'y', 'a', 'los', 'del', 'las', 'un', 'por',
    'con', 'una', 'su', 'para', 'es', 'al', 'lo', 'como', 'más', 'pero',
    'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque', 'esta',
    'son', 'entre', 'está', 'cuando', 'muy', 'sin', 'sobre', 'ser', 'también',
    'me', 'hasta', 'hay', 'donde', 'han', 'quien', 'están', 'ese', 'yo',
    'eso', 'ante', 'ellos', 'e', 'nos', 'ni', 'que', 'se', 'no', 'si',
    'todo', 'ella', 'cada', 'desde', 'etc', 'otro', 'otros', 'otra', 'otras',
    'cual', 'puede', 'todos', 'así', 'qué', 'esto', 'algo', 'aquí', 'será'
}
STOPWORDS_EN = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'with', 'by', 'of', 'at', 'from', 'as', 'is', 'it', 'its', 'my', 'your',
    'his', 'her', 'their', 'our', 'this', 'that', 'these', 'those', 'be', 'been'
}
STOPWORDS = STOPWORDS_ES.union(STOPWORDS_EN)


# ────────────────────────────────────────────────────────────
# CARGA DE DATOS DEL REPOSITORIO
# ────────────────────────────────────────────────────────────
def load_skills_data():
    """Carga las skills desde INDEX.js parseando el array JavaScript."""
    if not os.path.exists(INDEX_JS_PATH):
        print(f"[!] INDEX.js no encontrado en {INDEX_JS_PATH}")
        return []

    with open(INDEX_JS_PATH, 'r', encoding='utf-8') as f:
        raw = f.read()

    # Extraer el JSON del archivo .js (formato: const skillsData = [...];)
    match = re.search(r'const\s+skillsData\s*=\s*(\[.*\])\s*;', raw, re.DOTALL)
    if not match:
        print("[!] No se pudo parsear INDEX.js")
        return []

    try:
        skills = json.loads(match.group(1))
        print(f"[✓] Cargadas {len(skills)} skills desde INDEX.js")
        return skills
    except json.JSONDecodeError as e:
        print(f"[!] Error parseando JSON: {e}")
        return []


# ────────────────────────────────────────────────────────────
# MOTOR DE BÚSQUEDA SEMÁNTICA LOCAL (TF-IDF simplificado)
# ────────────────────────────────────────────────────────────
def tokenize(text):
    """Tokeniza un texto en palabras significativas."""
    if not text:
        return []
    text = text.lower()
    text = re.sub(r'[^a-záéíóúüñ0-9\s-]', ' ', text)
    tokens = text.split()
    return [t for t in tokens if t not in STOPWORDS and len(t) > 2]


def compute_tf(tokens):
    """Calcula la frecuencia relativa de cada término."""
    tf = Counter(tokens)
    total = len(tokens)
    if total == 0:
        return {}
    return {k: v / total for k, v in tf.items()}


def compute_idf(corpus_tokens_list):
    """Calcula el IDF (Inverse Document Frequency) del corpus."""
    n_docs = len(corpus_tokens_list)
    if n_docs == 0:
        return {}

    df = Counter()
    for tokens in corpus_tokens_list:
        unique_terms = set(tokens)
        for term in unique_terms:
            df[term] += 1

    return {term: math.log(n_docs / (1 + freq)) for term, freq in df.items()}


def match_skills(query_text, features_text, skills_data, top_n=15):
    """
    Encuentra las skills más relevantes para la descripción del usuario.
    Usa TF-IDF simplificado con bonus por coincidencia en tags y nombre.
    """
    if not skills_data:
        return []

    # Combinar todos los textos del usuario
    user_text = f"{query_text} {features_text}"
    user_tokens = tokenize(user_text)

    if not user_tokens:
        return []

    # Preparar corpus: para cada skill, su texto indexable
    corpus = []
    for skill in skills_data:
        skill_text = f"{skill.get('name', '')} {skill.get('description', '')} " \
                     f"{skill.get('category', '')} {skill.get('subcategory', '')}"

        # Extraer tags del contenido YAML si están disponibles
        content = skill.get('content', '')
        tags_match = re.search(r'tags:\s*\[(.*?)\]', content or '')
        if tags_match:
            skill_text += f" {tags_match.group(1).replace(',', ' ')}"

        corpus.append(tokenize(skill_text))

    # Calcular IDF del corpus
    idf = compute_idf(corpus)
    user_tf = compute_tf(user_tokens)

    # Calcular similitud para cada skill
    scores = []
    for i, skill in enumerate(skills_data):
        skill_tokens = corpus[i]
        skill_tf = compute_tf(skill_tokens)

        # TF-IDF cosine similarity simplificada
        score = 0
        for term in user_tokens:
            if term in skill_tf:
                tf_user = user_tf.get(term, 0)
                tf_skill = skill_tf.get(term, 0)
                idf_val = idf.get(term, 0)
                score += tf_user * tf_skill * (idf_val ** 2)

        # Bonus por coincidencia exacta en nombre
        if query_text and query_text.lower() in skill.get('name', '').lower():
            score *= 1.5

        scores.append((skill, round(score * 100, 2)))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


# ────────────────────────────────────────────────────────────
# GENERADORES DE CONTENIDO MARKDOWN
# ────────────────────────────────────────────────────────────
# DICCIONARIO DE TRADUCCIONES PARA BLUEPRINTS (I18N)
# ────────────────────────────────────────────────────────────
BP_I18N = {
    'es': {
        'generated_with': 'Generado con',
        'tool_author': 'Autor de la herramienta',
        'blueprint_title': 'Blueprint',
        'welcome_msg': 'Bienvenido a tu Blueprint profesional. Este paquete contiene todo lo necesario para que una IA de codificación (Claude, ChatGPT, Gemini, Copilot...) construya tu aplicación de forma guiada.',
        'structure_title': 'Estructura del Blueprint',
        'folder': 'Carpeta',
        'content': 'Contenido',
        'folder_vision': 'Visión del proyecto, audiencia y funcionalidades',
        'folder_agents': 'Configuración del equipo de agentes IA',
        'folder_skills': 'Manuales técnicos relevantes del repositorio',
        'folder_arch': 'Stack tecnológico recomendado',
        'folder_rules': 'Líneas rojas, estándares y seguridad',
        'folder_design': 'Guía de estilo visual',
        'how_to_use': 'Cómo Usar',
        'step_1': '1. Abre tu IA de codificación favorita.',
        'step_2': '2. Copia el contenido de `PROMPT_MAESTRO.md` como primer mensaje.',
        'step_3': '3. Adjunta o referencia las carpetas del Blueprint según lo necesites.',
        'step_4': '4. La IA tendrá contexto completo para construir tu app de principio a fin.',
        'footer_generated': 'Generado con',
        'prompt_master_title': 'Prompt Maestro',
        'prompt_copy_msg': 'Copia este prompt como **primer mensaje** en tu IA de codificación favorita.',
        'your_role': 'Tu Rol',
        'role_desc': 'Eres un equipo de desarrollo Senior especializado en **{app_type}**.',
        'mission_desc': 'Tu misión es construir **{app_name}** siguiendo estrictamente los documentos de este Blueprint.',
        'pending_tasks': 'TAREAS PENDIENTES DEL ECOSISTEMA (CRÍTICO)',
        'pending_desc': '{ai_name}, hemos detectado que las siguientes funcionalidades solicitadas por el usuario **NO existían en este repositorio de Skills**: ',
        'pending_obligation': '👉 TU OBLIGACIÓN: ANTES de empezar a escribir el código de la app, COMPLETA Y REDACTA detalladamente los archivos `SKILL.md` y `workflow.md` correspondientes dentro de esas carpetas en el sistema físico. ¡Retroalimenta tu propio ecosistema!',
        'project_desc_title': 'Descripción del Proyecto',
        'no_desc': 'Sin descripción proporcionada.',
        'req_features': 'Funcionalidades Requeridas',
        'no_features': '(No se especificaron funcionalidades)',
        'critical_inst': 'Instrucciones Críticas',
        'inst_1': '1. ANTES de escribir una sola línea de código, lee TODOS los archivos de este Blueprint (y resuelve las Tareas Pendientes si las hay).',
        'inst_2': '2. Presta especial atención a `05_REGLAS/LINEAS_ROJAS.md`.',
        'inst_3': '3. Consulta `03_SKILLS/` para los manuales técnicos que aplican.',
        'inst_4': '4. Sigue el stack de `04_ARQUITECTURA/` salvo que haya una razón técnica para cambiarlo.',
        'inst_5': '5. Aplica la guía visual de `06_DISEÑO/`.',
        'project_sheet': 'Ficha del Proyecto',
        'field': 'Campo',
        'value': 'Valor',
        'name': 'Nombre',
        'type': 'Tipo',
        'language': 'Idioma',
        'audience_title': 'Audiencia y Usuarios',
        'target_public': 'Público Objetivo',
        'sector': 'Sector',
        'considerations': 'Consideraciones',
        'cons_1': '- Adaptar la complejidad de la interfaz al nivel del usuario objetivo.',
        'cons_2': '- Priorizar los flujos más frecuentes del público indicado.',
        'scope_title': 'Funcionalidades y Alcance',
        'main_functions': 'Funciones Principales',
        'external_ints': 'Integraciones Externas',
        'no_ints': '(Sin integraciones especificadas)',
        'agents_team_title': 'Equipo de Agentes IA Recomendado',
        'agents_msg': 'Para desarrollar **{app_name}**, sugerimos este ecosistema:',
        'agent': 'Agente',
        'responsibility': 'Responsabilidad',
        'arch_name': 'Arquitecto',
        'arch_desc': 'Estructura de archivos, DB schema, decisiones técnicas',
        'back_name': 'Backend',
        'back_desc': 'Lógica de negocio, API, autenticación, seguridad',
        'front_name': 'Frontend/UI',
        'front_desc': 'Interfaz, animaciones, responsive design',
        'qa_name': 'QA',
        'qa_desc': 'Tests unitarios, E2E, validación de edge cases',
        'devops_name': 'DevOps',
        'devops_desc': 'CI/CD, despliegue, monitorización',
        'workflow_sugg': 'Flujo de Trabajo Sugerido',
        'wf_1': '1. El **Arquitecto** define la estructura y el stack.',
        'wf_2': '2. El **Backend** implementa la API y la lógica core.',
        'wf_3': '3. El **Frontend** construye la interfaz consumiendo la API.',
        'wf_4': '4. El **QA** valida cada módulo antes de integrarlo.',
        'wf_5': '5. **DevOps** despliega y monitoriza.',
        'skill_assign': 'Asigna cada Skill de la carpeta 03_SKILLS al agente correspondiente.',
        'stack_title': 'Stack Tecnológico Recomendado',
        'layer': 'Capa',
        'technology': 'Tecnología',
        'support_tools': 'Herramientas de Apoyo Recomendadas',
        'arch_principles': 'Principios Arquitectónicos',
        'red_lines_title': 'Líneas Rojas — Lo que NO se debe hacer',
        'red_lines_desc': 'Este documento define las restricciones inquebrantables durante la construcción de **{app_name}**.',
        'security': 'Seguridad',
        'user_data': 'Datos del Usuario',
        'code_quality': 'Calidad del Código',
        'ux_experience': 'Experiencia de Usuario',
        'performance': 'Rendimiento',
        'standards_title': 'Estándares de Desarrollo',
        'naming_conv': 'Nombres y Convenciones',
        'file_struct': 'Estructura de Archivos',
        'documentation_title': 'Documentación',
        'commits_title': 'Commits y Versionado',
        'visual_design_title': 'Diseño Visual',
        'security_guide_title': 'Guía de Seguridad',
        'visual_style_title': 'Guía de Estilo Visual',
        'style_requested': 'Estilo Visual Solicitado',
        'user_refs': 'Referencias del Usuario',
        'no_refs': 'No se proporcionaron referencias específicas.',
        'design_principles': 'Principios de Diseño'
    },
    'en': {
        'generated_with': 'Generated with',
        'tool_author': 'Tool author',
        'blueprint_title': 'Blueprint',
        'welcome_msg': 'Welcome to your professional Blueprint. This package contains everything needed for a coding AI (Claude, ChatGPT, Gemini, Copilot...) to build your application step-by-step.',
        'structure_title': 'Blueprint Structure',
        'folder': 'Folder',
        'content': 'Content',
        'folder_vision': 'Project vision, audience, and features',
        'folder_agents': 'AI agents team configuration',
        'folder_skills': 'Relevant technical manuals from the repository',
        'folder_arch': 'Recommended technology stack',
        'folder_rules': 'Red lines, standards, and security',
        'folder_design': 'Visual style guide',
        'how_to_use': 'How to Use',
        'step_1': '1. Open your favorite coding AI.',
        'step_2': '2. Copy the content of `PROMPT_MAESTRO.md` as the first message.',
        'step_3': '3. Attach or reference the Blueprint folders as needed.',
        'step_4': '4. The AI will have full context to build your app from start to finish.',
        'footer_generated': 'Generated with',
        'prompt_master_title': 'Master Prompt',
        'prompt_copy_msg': 'Copy this prompt as the **first message** in your favorite coding AI.',
        'your_role': 'Your Role',
        'role_desc': 'You are a Senior development team specialized in **{app_type}**.',
        'mission_desc': 'Your mission is to build **{app_name}** strictly following the documents in this Blueprint.',
        'pending_tasks': 'PENDING ECOSYSTEM TASKS (CRITICAL)',
        'pending_desc': '{ai_name}, we have detected that the following features requested by the user **did NOT exist in this Skills repository**:',
        'pending_obligation': '👉 YOUR OBLIGATION: BEFORE you start writing code, COMPLETE AND REDACT in detail the corresponding `SKILL.md` and `workflow.md` files within those folders in the physical system. Feed back your own ecosystem!',
        'project_desc_title': 'Project Description',
        'no_desc': 'No description provided.',
        'req_features': 'Required Features',
        'no_features': '(No features were specified)',
        'critical_inst': 'Critical Instructions',
        'inst_1': '1. BEFORE writing a single line of code, read ALL the files in this Blueprint (and resolve Pending Tasks if any).',
        'inst_2': '2. Pay special attention to `05_REGLAS/LINEAS_ROJAS.md`.',
        'inst_3': '3. Consult `03_SKILLS/` for the applicable technical manuals.',
        'inst_4': '4. Follow the stack in `04_ARQUITECTURA/` unless there is a technical reason to change it.',
        'inst_5': '5. Apply the visual guide in `06_DISEÑO/`.',
        'project_sheet': 'Project Sheet',
        'field': 'Field',
        'value': 'Value',
        'name': 'Name',
        'type': 'Type',
        'language': 'Language',
        'audience_title': 'Audience and Users',
        'target_public': 'Target Audience',
        'sector': 'Sector',
        'considerations': 'Considerations',
        'cons_1': '- Adapt interface complexity to the target user level.',
        'cons_2': '- Prioritize the most frequent flows for the indicated audience.',
        'scope_title': 'Features and Scope',
        'main_functions': 'Main Functions',
        'external_ints': 'External Integrations',
        'no_ints': '(No integrations specified)',
        'agents_team_title': 'Recommended AI Agents Team',
        'agents_msg': 'To develop **{app_name}**, we suggest this ecosystem:',
        'agent': 'Agent',
        'responsibility': 'Responsibility',
        'arch_name': 'Architect',
        'arch_desc': 'File structure, DB schema, technical decisions',
        'back_name': 'Backend',
        'back_desc': 'Business logic, API, authentication, security',
        'front_name': 'Frontend/UI',
        'front_desc': 'Interface, animations, responsive design',
        'qa_name': 'QA',
        'qa_desc': 'Unit tests, E2E, edge case validation',
        'devops_name': 'DevOps',
        'devops_desc': 'CI/CD, deployment, monitoring',
        'workflow_sugg': 'Suggested Workflow',
        'wf_1': '1. The **Architect** defines the structure and stack.',
        'wf_2': '2. The **Backend** implements the API and core logic.',
        'wf_3': '3. The **Frontend** builds the interface consuming the API.',
        'wf_4': '4. The **QA** validates each module before integrating.',
        'wf_5': '5. **DevOps** deploys and monitors.',
        'skill_assign': 'Assign each Skill from the 03_SKILLS folder to the corresponding agent.',
        'stack_title': 'Recommended Technology Stack',
        'layer': 'Layer',
        'technology': 'Technology',
        'support_tools': 'Recommended Support Tools',
        'arch_principles': 'Architectural Principles',
        'red_lines_title': 'Red Lines — What NOT to do',
        'red_lines_desc': 'This document defines the unbreakable restrictions during the construction of **{app_name}**.',
        'security': 'Security',
        'user_data': 'User Data',
        'code_quality': 'Code Quality',
        'ux_experience': 'User Experience',
        'performance': 'Performance',
        'standards_title': 'Development Standards',
        'naming_conv': 'Naming and Conventions',
        'file_struct': 'File Structure',
        'documentation_title': 'Documentation',
        'commits_title': 'Commits and Versioning',
        'visual_design_title': 'Visual Design',
        'security_guide_title': 'Security Guide',
        'visual_style_title': 'Visual Style Guide',
        'style_requested': 'Requested Visual Style',
        'user_refs': 'User References',
        'no_refs': 'No specific references were provided.',
        'design_principles': 'Design Principles'
    },
    'fr': {
        'generated_with': 'Généré avec',
        'tool_author': 'Auteur de l\'outil',
        'blueprint_title': 'Blueprint',
        'welcome_msg': 'Bienvenue dans votre Blueprint professionnel. Ce pack contient tout le nécessaire pour qu\'une IA de codage (Claude, ChatGPT, Gemini, Copilot...) construise votre application de manière guidée.',
        'structure_title': 'Structure du Blueprint',
        'folder': 'Dossier',
        'content': 'Contenu',
        'folder_vision': 'Vision du projet, audience et fonctionnalités',
        'folder_agents': 'Configuration de l\'équipe d\'agents IA',
        'folder_skills': 'Manuels techniques pertinents du dépôt',
        'folder_arch': 'Stack technologique recommandé',
        'folder_rules': 'Lignes rouges, standards et sécurité',
        'folder_design': 'Guide de style visuel',
        'how_to_use': 'Comment Utiliser',
        'step_1': '1. Ouvrez votre IA de codage préférée.',
        'step_2': '2. Copiez le contenu de `PROMPT_MAESTRO.md` comme premier message.',
        'step_3': '3. Joignez ou référencez les dossiers du Blueprint selon vos besoins.',
        'step_4': '4. L\'IA aura le contexte complet pour construire votre application de A à Z.',
        'footer_generated': 'Généré avec',
        'prompt_master_title': 'Prompt Maître',
        'prompt_copy_msg': 'Copiez ce prompt comme **premier message** dans votre IA de codage préférée.',
        'your_role': 'Votre Rôle',
        'role_desc': 'Vous êtes une équipe de développement Senior spécialisée en **{app_type}**.',
        'mission_desc': 'Votre mission est de construire **{app_name}** en suivant strictement les documents de ce Blueprint.',
        'pending_tasks': 'TÂCHES EN ATTENTE DE L\'ÉCOSYSTÈME (CRITIQUE)',
        'pending_desc': 'Antigravity, nous avons détecté que les fonctionnalités suivantes demandées par l\'utilisateur **n\'existaient PAS dans ce dépôt de Skills** :',
        'pending_obligation': '👉 VOTRE OBLIGATION : AVANT de commencer à écrire le code, COMPLÉTEZ ET RÉDIGEZ en détail les fichiers `SKILL.md` et `workflow.md` correspondants dans ces dossiers du système physique. Alimentez votre propre écosystème !',
        'project_desc_title': 'Description du Projet',
        'no_desc': 'Aucune description fournie.',
        'req_features': 'Fonctionnalités Requises',
        'no_features': '(Aucune fonctionnalité spécifiée)',
        'critical_inst': 'Instructions Critiques',
        'inst_1': '1. AVANT d\'écrire une seule ligne de code, lisez TOUS les fichiers de ce Blueprint (et résolvez les Tâches en Attente s\'il y en a).',
        'inst_2': '2. Portez une attention particulière à `05_REGLAS/LINEAS_ROJAS.md`.',
        'inst_3': '3. Consultez `03_SKILLS/` pour les manuels techniques applicables.',
        'inst_4': '4. Suivez le stack dans `04_ARQUITECTURA/` à moins qu\'il n\'y ait une raison technique de changer.',
        'inst_5': '5. Appliquez le guide visuel dans `06_DISEÑO/`.',
        'project_sheet': 'Fiche du Projet',
        'field': 'Champ',
        'value': 'Valeur',
        'name': 'Nom',
        'type': 'Type',
        'language': 'Langue',
        'audience_title': 'Audience et Utilisateurs',
        'target_public': 'Public Cible',
        'sector': 'Secteur',
        'considerations': 'Considérations',
        'cons_1': '- Adapter la complexité de l\'interface au niveau de l\'utilisateur cible.',
        'cons_2': '- Prioriser les flux les plus fréquents pour le public indiqué.',
        'scope_title': 'Fonctionnalités et Portée',
        'main_functions': 'Fonctions Principales',
        'external_ints': 'Intégrations Externes',
        'no_ints': '(Aucune intégration spécifiée)',
        'agents_team_title': 'Équipe d\'Agents IA Recommandée',
        'agents_msg': 'Pour développer **{app_name}**, nous suggérons cet écosystème :',
        'agent': 'Agent',
        'responsibility': 'Responsabilité',
        'arch_name': 'Architecte',
        'arch_desc': 'Structure des fichiers, schéma DB, décisions techniques',
        'back_name': 'Backend',
        'back_desc': 'Logique métier, API, authentification, sécurité',
        'front_name': 'Frontend/UI',
        'front_desc': 'Interface, animations, design responsive',
        'qa_name': 'QA',
        'qa_desc': 'Tests unitaires, E2E, validation des cas limites',
        'devops_name': 'DevOps',
        'devops_desc': 'CI/CD, déploiement, surveillance',
        'workflow_sugg': 'Flux de Travail Suggéré',
        'wf_1': '1. L\'**Architecte** définit la structure et le stack.',
        'wf_2': '2. Le **Backend** implémente l\'API et la logique métier.',
        'wf_3': '3. Le **Frontend** construit l\'interface en consommant l\'API.',
        'wf_4': '4. Le **QA** valide chaque module avant intégration.',
        'wf_5': '5. **DevOps** déploie et surveille.',
        'skill_assign': 'Attribuez chaque Skill du dossier 03_SKILLS à l\'agent correspondant.',
        'stack_title': 'Stack Technologique Recommandé',
        'layer': 'Couche',
        'technology': 'Technologie',
        'support_tools': 'Outils d\'Appui Recommandés',
        'arch_principles': 'Principes Architecturaux',
        'red_lines_title': 'Lignes Rouges — Ce qu\'il NE faut PAS faire',
        'red_lines_desc': 'Ce document définit les restrictions inviolables lors de la construction de **{app_name}**.',
        'security': 'Sécurité',
        'user_data': 'Données Utilisateur',
        'code_quality': 'Qualité du Code',
        'ux_experience': 'Expérience Utilisateur',
        'performance': 'Performance',
        'standards_title': 'Standards de Développement',
        'naming_conv': 'Noms et Conventions',
        'file_struct': 'Structure des Fichiers',
        'documentation_title': 'Documentation',
        'commits_title': 'Commits et Versionnement',
        'visual_design_title': 'Design Visuel',
        'security_guide_title': 'Guide de Sécurité',
        'visual_style_title': 'Guide de Style Visuel',
        'style_requested': 'Style Visuel Demandé',
        'user_refs': 'Références Utilisateur',
        'no_refs': 'Aucune référence spécifique n\'a été fournie.',
        'design_principles': 'Principes de Design'
    },
    'de': {
        'generated_with': 'Generiert mit',
        'tool_author': 'Tool-Autor',
        'blueprint_title': 'Blueprint',
        'welcome_msg': 'Willkommen zu Ihrem professionellen Blueprint. Dieses Paket enthält alles, was eine Coding-KI (Claude, ChatGPT, Gemini, Copilot...) benötigt, um Ihre Anwendung Schritt für Schritt zu erstellen.',
        'structure_title': 'Blueprint-Struktur',
        'folder': 'Ordner',
        'content': 'Inhalt',
        'folder_vision': 'Projektvision, Zielgruppe und Funktionen',
        'folder_agents': 'KI-Agenten-Team Konfiguration',
        'folder_skills': 'Relevante technische Handbücher aus dem Repository',
        'folder_arch': 'Empfohlener Technologie-Stack',
        'folder_rules': 'Rote Linien, Standards und Sicherheit',
        'folder_design': 'Visueller Styleguide',
        'how_to_use': 'Anwendung',
        'step_1': '1. Öffnen Sie Ihre bevorzugte Coding-KI.',
        'step_2': '2. Kopieren Sie den Inhalt von `PROMPT_MAESTRO.md` als erste Nachricht.',
        'step_3': '3. Fügen Sie die Blueprint-Ordner nach Bedarf ein oder referenzieren Sie diese.',
        'step_4': '4. Die KI hat den vollen Kontext, um Ihre App von Anfang bis Ende zu erstellen.',
        'footer_generated': 'Generiert mit',
        'prompt_master_title': 'Master-Prompt',
        'prompt_copy_msg': 'Kopieren Sie diesen Prompt als **erste Nachricht** in Ihre bevorzugte Coding-KI.',
        'your_role': 'Ihre Rolle',
        'role_desc': 'Sie sind ein Senior-Entwicklungsteam, spezialisiert auf **{app_type}**.',
        'mission_desc': 'Ihre Mission ist es, **{app_name}** unter strenger Einhaltung der Dokumente in diesem Blueprint zu erstellen.',
        'pending_tasks': 'AUSSTEHENDE ÖKOSYSTEM-AUFGABEN (KRITISCH)',
        'pending_desc': '{ai_name}, wir haben festgestellt, dass die folgenden vom Benutzer angeforderten Funktionen **NICHT in diesem Skills-Repository existierten**:',
        'pending_obligation': '👉 IHRE VERPFLICHTUNG: BEVOR Sie mit dem Schreiben von Code beginnen, VERVOLLSTÄNDIGEN UND VERFASSEN Sie die entsprechenden `SKILL.md`- und `workflow.md`-Dateien in diesen Ordnern im physischen System detailliert. Geben Sie Rückmeldung an Ihr eigenes Ökosystem!',
        'project_desc_title': 'Projektbeschreibung',
        'no_desc': 'Keine Beschreibung angegeben.',
        'req_features': 'Erforderliche Funktionen',
        'no_features': '(Keine Funktionen angegeben)',
        'critical_inst': 'Kritische Anweisungen',
        'inst_1': '1. BEVOR Sie eine einzige Zeile Code schreiben, lesen Sie ALLE Dateien in diesem Blueprint (und lösen Sie ggf. ausstehende Aufgaben).',
        'inst_2': '2. Achten Sie besonders auf `05_REGLAS/LINEAS_ROJAS.md`.',
        'inst_3': '3. Konsultieren Sie `03_SKILLS/` für die entsprechenden technischen Handbücher.',
        'inst_4': '4. Folgen Sie dem Stack in `04_ARQUITECTURA/`, es sei denn, es gibt einen technischen Grund für eine Änderung.',
        'inst_5': '5. Wenden Sie den visuellen Leitfaden in `06_DISEÑO/` an.',
        'project_sheet': 'Projektblatt',
        'field': 'Feld',
        'value': 'Wert',
        'name': 'Name',
        'type': 'Typ',
        'language': 'Sprache',
        'audience_title': 'Zielgruppe und Benutzer',
        'target_public': 'Zielgruppe',
        'sector': 'Branche',
        'considerations': 'Überlegungen',
        'cons_1': '- Komplexität der Schnittstelle an das Niveau der Zielgruppe anpassen.',
        'cons_2': '- Die häufigsten Abläufe für die angegebene Zielgruppe priorisieren.',
        'scope_title': 'Funktionen und Umfang',
        'main_functions': 'Hauptfunktionen',
        'external_ints': 'Externe Integrationen',
        'no_ints': '(Keine Integrationen angegeben)',
        'agents_team_title': 'Empfohlenes KI-Agenten-Team',
        'agents_msg': 'Zur Entwicklung von **{app_name}** empfehlen wir dieses Ökosystem:',
        'agent': 'Agent',
        'responsibility': 'Verantwortung',
        'arch_name': 'Architekt',
        'arch_desc': 'Dateistruktur, DB-Schema, technische Entscheidungen',
        'back_name': 'Backend',
        'back_desc': 'Geschäftslogik, API, Authentifizierung, Sicherheit',
        'front_name': 'Frontend/UI',
        'front_desc': 'Oberfläche, Animationen, Responsive Design',
        'qa_name': 'QA',
        'qa_desc': 'Unit-Tests, E2E, Validierung von Grenzfällen',
        'devops_name': 'DevOps',
        'devops_desc': 'CI/CD, Deployment, Überwachung',
        'workflow_sugg': 'Vorgeschlagener Workflow',
        'wf_1': '1. Der **Architekt** definiert die Struktur und den Stack.',
        'wf_2': '2. Das **Backend** implementiert die API und die Core-Logik.',
        'wf_3': '3. Das **Frontend** erstellt die Oberfläche und nutzt die API.',
        'wf_4': '4. QA validiert jedes Modul vor der Integration.',
        'wf_5': '5. **DevOps** stellt bereit und überwacht.',
        'skill_assign': 'Weisen Sie jede Skill aus dem Ordner 03_SKILLS dem entsprechenden Agenten zu.',
        'stack_title': 'Empfohlener Technologie-Stack',
        'layer': 'Schicht',
        'technology': 'Technologie',
        'support_tools': 'Empfohlene Support-Tools',
        'arch_principles': 'Architektonische Prinzipien',
        'red_lines_title': 'Rote Linien — Was man NICHT tun sollte',
        'red_lines_desc': 'Dieses Dokument definiert die unumstößlichen Einschränkungen beim Bau von **{app_name}**.',
        'security': 'Sicherheit',
        'user_data': 'Benutzerdaten',
        'code_quality': 'Codequalität',
        'ux_experience': 'Benutzererfahrung',
        'performance': 'Leistung',
        'standards_title': 'Entwicklungsstandards',
        'naming_conv': 'Namensgebung und Konventionen',
        'file_struct': 'Dateistruktur',
        'documentation_title': 'Dokumentation',
        'commits_title': 'Commits und Versionierung',
        'visual_design_title': 'Visuelles Design',
        'security_guide_title': 'Sicherheitsleitfaden',
        'visual_style_title': 'Visueller Styleguide',
        'style_requested': 'Angeforderter visueller Stil',
        'user_refs': 'Benutzerreferenzen',
        'no_refs': 'Es wurden keine spezifischen Referenzen angegeben.',
        'design_principles': 'Designprinzipien'
    },
    'zh': {
        'generated_with': '生成于',
        'tool_author': '工具作者',
        'blueprint_title': '蓝图',
        'welcome_msg': '欢迎使用您的专业蓝图。本包包含了编码 AI（Claude, ChatGPT, Gemini, Copilot...）按步骤构建您的应用程序所需的一切。',
        'structure_title': '蓝图结构',
        'folder': '文件夹',
        'content': '内容',
        'folder_vision': '项目愿景、受众和功能',
        'folder_agents': 'AI 代理团队配置',
        'folder_skills': '存储库中的相关技术手册',
        'folder_arch': '推荐的技术栈',
        'folder_rules': '红线、标准和安全',
        'folder_design': '视觉风格指南',
        'how_to_use': '如何使用',
        'step_1': '1. 打开您喜欢的编码 AI。',
        'step_2': '2. 将 `PROMPT_MAESTRO.md` 的内容作为第一条消息复制。',
        'step_3': '3. 根据需要附加或引用蓝图文件夹。',
        'step_4': '4. AI 将拥有完整的上下文来从头到尾构建您的应用。',
        'footer_generated': '生成于',
        'prompt_master_title': '主提示词',
        'prompt_copy_msg': '在您喜欢的编码 AI 中将此提示词作为**第一条消息**复制。',
        'your_role': '您的角色',
        'role_desc': '您是一个专注于 **{app_type}** 的高级开发团队。',
        'mission_desc': '您的任务是严格遵循本蓝图中的文档来构建 **{app_name}**。',
        'pending_tasks': '待处理生态系统任务（关键）',
        'pending_desc': '{ai_name}，我们检测到用户请求的以下功能**在技能库中不存在**：',
        'pending_obligation': '👉 您的义务：在开始编写代码之前，请详细完成并编写物理系统中这些文件夹内相应的 `SKILL.md` 和 `workflow.md` 文件。反馈您自己的生态系统！',
        'project_desc_title': '项目描述',
        'no_desc': '未提供描述。',
        'req_features': '所需功能',
        'no_features': '（未指定功能）',
        'critical_inst': '关键说明',
        'inst_1': '1. 在编写任何代码之前，请阅读此蓝图中的所有文件（并解决任何待处理任务）。',
        'inst_2': '2. 特别注意 `05_REGLAS/LINEAS_ROJAS.md`。',
        'inst_3': '3. 查阅 `03_SKILLS/` 以获取适用的技术手册。',
        'inst_4': '4. 除非有技术原因需要更改，否则请遵循 `04_ARQUITECTURA/` 中的技术栈。',
        'inst_5': '5. 应用 `06_DISEÑO/` 中的视觉指南。',
        'project_sheet': '项目表',
        'field': '字段',
        'value': '值',
        'name': '名称',
        'type': '类型',
        'language': '语言',
        'audience_title': '受众与用户',
        'target_public': '目标受众',
        'sector': '行业',
        'considerations': '注意事项',
        'cons_1': '- 根据目标用户水平调整界面复杂度。',
        'cons_2': '- 优先处理指定受众常用的流程。',
        'scope_title': '功能与范围',
        'main_functions': '主要功能',
        'external_ints': '外部集成',
        'no_ints': '（未指定集成）',
        'agents_team_title': '推荐的 AI 代理团队',
        'agents_msg': '为了开发 **{app_name}**，我们建议使用以下生态系统：',
        'agent': '代理',
        'responsibility': '职责',
        'arch_name': '架构师',
        'arch_desc': '文件结构、数据库模式、技术决策',
        'back_name': '后端',
        'back_desc': '业务逻辑、API、身份验证、安全',
        'front_name': '前端/UI',
        'front_desc': '界面、动画、响应式设计',
        'qa_name': 'QA',
        'qa_desc': '单元测试、E2E、边界情况验证',
        'devops_name': 'DevOps',
        'devops_desc': 'CI/CD、部署、监控',
        'workflow_sugg': '建议的工作流程',
        'wf_1': '1. **架构师**定义结构和技术栈。',
        'wf_2': '2. **后端**实现 API 和核心逻辑。',
        'wf_3': '3. **前端**构建调用 API 的界面。',
        'wf_4': '4. **QA**在集成前验证每个模块。',
        'wf_5': '5. **DevOps**部署并监控。',
        'skill_assign': '将 03_SKILLS 文件夹中的每项技能分配给相应的代理。',
        'stack_title': '推荐技术栈',
        'layer': '层',
        'technology': '技术',
        'support_tools': '推荐的辅助工具',
        'arch_principles': '架构原则',
        'red_lines_title': '红线 — 不该做的事',
        'red_lines_desc': '此文档定义了在构建 **{app_name}** 期间不可逾越的限制。',
        'security': '安全',
        'user_data': '用户数据',
        'code_quality': '代码质量',
        'ux_experience': '用户体验',
        'performance': '性能',
        'standards_title': '开发标准',
        'naming_conv': '命名与规范',
        'file_struct': '文件结构',
        'documentation_title': '文档',
        'commits_title': '提交与版本控制',
        'visual_design_title': '视觉设计',
        'security_guide_title': '安全指南',
        'visual_style_title': '视觉风格指南',
        'style_requested': '要求的视觉风格',
        'user_refs': '用户参考',
        'no_refs': '未提供具体参考。',
        'design_principles': '设计原则'
    },
    'ja': {
        'generated_with': '生成元',
        'tool_author': 'ツール作成者',
        'blueprint_title': 'ブループリント',
        'welcome_msg': 'プロフェッショナルなブループリントへようこそ。このパッケージには、コーディングAI（Claude, ChatGPT, Gemini, Copilot...）がアプリケーションを段階的に構築するために必要なものがすべて含まれています。',
        'structure_title': 'ブループリントの構造',
        'folder': 'フォルダ',
        'content': '内容',
        'folder_vision': 'プロジェクトのビジョン、対象読者、および機能',
        'folder_agents': 'AIエージェントチームの構成',
        'folder_skills': 'リポジトリからの関連技術マニュアル',
        'folder_arch': '推奨されるテクノロジースタック',
        'folder_rules': 'レッドライン、標準、およびセキュリティ',
        'folder_design': 'ビジュアルスタイルガイド',
        'how_to_use': '使い方',
        'step_1': '1. お好みのコーディングAIを開きます。',
        'step_2': '2. `PROMPT_MAESTRO.md`の内容を最初のメッセージとしてコピーします。',
        'step_3': '3. 必要に応じてブループリントフォルダを添付または参照します。',
        'step_4': '4. AIはアプリを最初から最後まで構築するための完全なコンテキストを持ちます。',
        'footer_generated': '生成元',
        'prompt_master_title': 'マスタープロンプト',
        'prompt_copy_msg': 'お好みのコーディングAIで、このプロンプトを**最初のメッセージ**としてコピーしてください。',
        'your_role': 'あなたの役割',
        'role_desc': 'あなたは**{app_type}**に特化したシニア開発チームです。',
        'mission_desc': 'あなたの使命は、このブループリント内のドキュメントに厳密に従って**{app_name}**を構築することです。',
        'pending_tasks': '保留中のエコシステムタスク（重要）',
        'pending_desc': '{ai_name}、ユーザーが要求した以下の機能が**このスキルリポジトリに存在しない**ことを検出しました：',
        'pending_obligation': '👉 あなたの義務：コードを書き始める前に、物理システム内のそれらのフォルダにある対応する `SKILL.md` と `workflow.md` ファイルを詳細に完成させて記述してください。自身のエコシステムにフィードバックしてください！',
        'project_desc_title': 'プロジェクトの説明',
        'no_desc': '説明なし。',
        'req_features': '必要な機能',
        'no_features': '（機能指定なし）',
        'critical_inst': '重要な指示',
        'inst_1': '1. コードを1行でも書く前に、このブループリントのすべてのファイルを読んでください（保留中のタスクがあれば解決してください）。',
        'inst_2': '2. `05_REGLAS/LINEAS_ROJAS.md`に特に注意してください。',
        'inst_3': '3. 適用される技術マニュアルについては `03_SKILLS/` を参照してください。',
        'inst_4': '4. 技術的な変更理由がない限り、 `04_ARQUITECTURA/` のスタックに従ってください。',
        'inst_5': '5. `06_DISEÑO/` のビジュアルガイドを適用してください。',
        'project_sheet': 'プロジェクトシート',
        'field': '項目',
        'value': '値',
        'name': '名前',
        'type': 'タイプ',
        'language': '言語',
        'audience_title': 'ターゲットとユーザー',
        'target_public': 'ターゲット読者',
        'sector': 'セクター',
        'considerations': '考慮事項',
        'cons_1': '- インターフェースの複雑さをターゲットユーザーのレベルに合わせて調整する。',
        'cons_2': '- 指定されたオーディエンスの最も頻繁なフローを優先する。',
        'scope_title': '機能と範囲',
        'main_functions': '主な機能',
        'external_ints': '外部連携',
        'no_ints': '（連携指定なし）',
        'agents_team_title': '推奨AIエージェントチーム',
        'agents_msg': '**{app_name}**を開発するために、このエコシステムを提案します：',
        'agent': 'エージェント',
        'responsibility': '責任',
        'arch_name': 'アーキテクト',
        'arch_desc': 'ファイル構造、DBスキーマ、技術的決定',
        'back_name': 'バックエンド',
        'back_desc': 'ビジネスロジック、API、認証、セキュリティ',
        'front_name': 'フロントエンド/UI',
        'front_desc': 'インターフェース、アニメーション、レスポンシブデザイン',
        'qa_name': 'QA',
        'qa_desc': 'ユニットテスト、E2E、エッジケースの検証',
        'devops_name': 'DevOps',
        'devops_desc': 'CI/CD、デプロイ、監視',
        'workflow_sugg': '提案されるワークフロー',
        'wf_1': '1. **アーキテクト**が構造とスタックを定義する。',
        'wf_2': '2. **バックエンド**がAPIとコアロジックを実装する。',
        'wf_3': '3. **フロントエンド**がAPIを使用してインターフェースを構築する。',
        'wf_4': '4. **QA**が統合前に各モジュールを検証する。',
        'wf_5': '5. **DevOps**がデプロイと監視を行う。',
        'skill_assign': '03_SKILLSフォルダの各スキルを対応するエージェントに割り当てます。',
        'stack_title': '推奨テクノロジースタック',
        'layer': 'レイヤー',
        'technology': 'テクノロジー',
        'support_tools': '推奨サポートツール',
        'arch_principles': 'アーキテクチャの原則',
        'red_lines_title': 'レッドライン — やってはいけないこと',
        'red_lines_desc': 'このドキュメントは、**{app_name}**の構築中における不可侵の制限を定義します。',
        'security': 'セキュリティ',
        'user_data': 'ユーザーデータ',
        'code_quality': 'コード品質',
        'ux_experience': 'ユーザーエクスペリエンス',
        'performance': 'パフォーマンス',
        'standards_title': '開発標準',
        'naming_conv': '命名と規則',
        'file_struct': 'ファイル構造',
        'documentation_title': 'ドキュメント',
        'commits_title': 'コミットとバージョン管理',
        'visual_design_title': 'ビジュアルデザイン',
        'security_guide_title': 'セキュリティガイド',
        'visual_style_title': 'ビジュアルスタイルガイド',
        'style_requested': '要求されたビジュアルスタイル',
        'user_refs': 'ユーザーリファレンス',
        'no_refs': '具体的なリファレンスは提供されませんでした。',
        'design_principles': 'デザインの原則'
    }
}

# ────────────────────────────────────────────────────────────

def generate_leeme(app_name, lang='es'):
    """Genera LEEME_PRIMERO.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🛸 {t['blueprint_title']}: {app_name}

{t['welcome_msg']}

## 📂 {t['structure_title']}

| {t['folder']} | {t['content']} |
|---------|-----------|
| `01_VISION/` | {t['folder_vision']} |
| `02_AGENTES/` | {t['folder_agents']} |
| `03_SKILLS/` | {t['folder_skills']} |
| `04_ARQUITECTURA/` | {t['folder_arch']} |
| `05_REGLAS/` | {t['folder_rules']} |
| `06_DISEÑO/` | {t['folder_design']} |

## 🚀 {t['how_to_use']}

{t['step_1']}
{t['step_2']}
{t['step_3']}
{t['step_4']}

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_prompt_inicial(app_name, app_desc, app_type, features_list, ai_engine='Antigravity', missing_skills=None, lang='es'):
    """Genera PROMPT_MAESTRO.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    features_list = features_list or []
    feats = "\n".join([f"- {f}" for f in features_list]) if features_list else f"- {t['no_features']}"
    
    missing_md = ""
    if missing_skills:
        m_list = "\n".join([f"- {m}" for m in missing_skills])
        pending_desc_formatted = t['pending_desc'].format(ai_name=ai_engine)
        missing_md = f"""
## ⚠️ {t['pending_tasks']}
{pending_desc_formatted}

{m_list}

{t['pending_obligation']}
"""

    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 📝 {t['prompt_master_title']} — {app_name}

> {t['prompt_copy_msg']}

---

## {t['your_role']}
{t['role_desc'].format(app_type=app_type)}
{t['mission_desc'].format(app_name=app_name)}
{missing_md}
## {t['project_desc_title']}
{app_desc or t['no_desc']}

## {t['req_features']}
{feats}

## {t['critical_inst']}
{t['inst_1']}
{t['inst_2']}
{t['inst_3']}
{t['inst_4']}
{t['inst_5']}

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_proyecto(data, lang='es'):
    """Genera 01_VISION/PROYECTO.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 📌 {t['project_sheet']}

| {t['field']} | {t['value']} |
|-------|-------|
| **{t['name']}** | {data.get('app_name', '---')} |
| **{t['type']}** | {data.get('app_type', 'Web App')} |
| **{t['language']}** | {data.get('language', 'Spanish')} |

## {t['project_desc_title']}
{data.get('app_desc', t['no_desc'])}

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_audiencia(data, lang='es'):
    """Genera 01_VISION/AUDIENCIA.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 👥 {t['audience_title']}

| {t['field']} | {t['content']} |
|-------|-------------|
| **{t['target_public']}** | {data.get('user_type', 'General')} |
| **{t['sector']}** | {data.get('sector', '---')} |

## {t['considerations']}
{t['cons_1']}
{t['cons_2']}

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_funcionalidades(data, lang='es'):
    """Genera 01_VISION/FUNCIONALIDADES.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    features = data.get('features') or []
    integrations = data.get('integrations') or []
    features_md = "\n".join([f"- ✅ {f}" for f in features]) if features else f"- {t['no_features']}"
    ints_md = "\n".join([f"- 🔗 {i}" for i in integrations]) if integrations else f"- {t['no_ints']}"
    html = f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# ⚡ {t['scope_title']}

## {t['main_functions']}
{features_md}

## {t['external_ints']}
{ints_md}

"""
    nfrs = data.get('nfrs', '').strip()
    if nfrs:
        html += f"## Requisitos No Funcionales (NFRs)\n{nfrs}\n\n"
        
    schema = data.get('data_schema', '').strip()
    if schema:
        html += f"## Esquema de Datos Inicial\n```sql\n{schema}\n```\n\n"
        
    html += f"""---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""
    return html


def generate_equipo_agentes(data, lang='es'):
    """Genera 02_AGENTES/EQUIPO.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🤖 {t['agents_team_title']}

{t['agents_msg'].format(app_name=data.get('app_name', 'la aplicación'))}

| {t['agent']} | {t['responsibility']} |
|--------|----------------|
| 🏗️ **{t['arch_name']}** | {t['arch_desc']} |
| ⚙️ **{t['back_name']}** | {t['back_desc']} |
| 🎨 **{t['front_name']}** | {t['front_desc']} |
| 🧪 **{t['qa_name']}** | {t['qa_desc']} |
| 📦 **{t['devops_name']}** | {t['devops_desc']} |

## {t['workflow_sugg']}
{t['wf_1']}
{t['wf_2']}
{t['wf_3']}
{t['wf_4']}
{t['wf_5']}

---
*{t['skill_assign']}*
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_stack_tecnologico(data, lang='es'):
    """Genera 04_ARQUITECTURA/STACK_TECNOLOGICO.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    app_type = data.get('app_type', 'Web App')

    if 'Móvil' in app_type or 'Mobile' in app_type:
        stack = {
            'frontend': 'React Native / Expo',
            'backend': 'Node.js (Express) o Python (FastAPI)',
            'database': 'PostgreSQL (Supabase) o Firebase',
            'hosting': 'App Store + Play Store / Expo EAS'
        }
    elif 'Desktop' in app_type or 'Escritorio' in app_type:
        stack = {
            'frontend': 'Electron / Tauri con React o Vue',
            'backend': 'Node.js integrado o Python',
            'database': 'SQLite (local) o PostgreSQL',
            'hosting': 'GitHub Releases / distribución directa'
        }
    else:
        stack = {
            'frontend': 'Next.js 14+ / React / TailwindCSS',
            'backend': 'Next.js API Routes o Python (FastAPI)',
            'database': 'PostgreSQL (Supabase) o MongoDB (Atlas)',
            'hosting': 'Vercel / Netlify / Railway'
        }

    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🛠️ {t['stack_title']}

| {t['layer']} | {t['technology']} |
|------|-----------|
| **Frontend** | {stack['frontend']} |
| **Backend / API** | {stack['backend']} |
| **Base de Datos** | {stack['database']} |
| **Hosting / Deploy** | {stack['hosting']} |

## {t['support_tools']}
- **Control de versiones**: Git + GitHub/GitLab
- **Testing**: Jest (JS) / Pytest (Python)
- **Linting**: ESLint (JS) / Black + Flake8 (Python)

## {t['arch_principles']}
1. **Separación de responsabilidades**: Frontend, Backend y Base de Datos independientes.
2. **API-First**: Diseñar la API antes de construir la interfaz.
3. **Mobile-First**: Diseñar primero para pantallas pequeñas y escalar.
4. **Seguridad desde el diseño**: No añadir seguridad al final; integrarla desde el inicio.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_lineas_rojas(data, lang='es'):
    """Genera 05_REGLAS/LINEAS_ROJAS.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    app_name = data.get('app_name', 'la aplicación')
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🚫 {t['red_lines_title']}

{t['red_lines_desc'].format(app_name=app_name)}

## 1. {t['security']}
- ❌ **NUNCA** almacenar contraseñas en texto plano.
- ❌ **NUNCA** exponer claves API, tokens o secretos en el código fuente.
- ❌ **NUNCA** desactivar la validación de datos de entrada del usuario.
- ❌ **NUNCA** confiar en datos enviados desde el cliente sin validarlos en el servidor.

## 2. {t['user_data']}
- ❌ **NUNCA** recopilar datos personales innecesarios.
- ❌ **NUNCA** compartir datos de usuarios con terceros sin consentimiento.
- ❌ **NUNCA** almacenar datos sensibles sin cifrado.

## 3. {t['code_quality']}
- ❌ **NUNCA** dejar código comentado ("por si acaso") en la versión final.
- ❌ **NUNCA** usar valores "hardcodeados" que deberían ser configurables.
- ❌ **NUNCA** ignorar errores silenciosamente (catch vacío).
- ❌ **NUNCA** crear funciones de más de 50 líneas sin dividirlas.

## 4. {t['ux_experience']}
- ❌ **NUNCA** mostrar errores técnicos al usuario final.
- ❌ **NUNCA** dejar la interfaz sin estado de carga durante operaciones lentas.
- ❌ **NUNCA** eliminar datos sin confirmación del usuario.

## 5. {t['performance']}
- ❌ **NUNCA** cargar todos los datos a la vez si hay más de 100 registros.
- ❌ **NUNCA** hacer peticiones al servidor innecesarias o duplicadas.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_estandares(data, lang='es'):
    """Genera 05_REGLAS/ESTANDARES.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 📏 {t['standards_title']}

## {t['naming_conv']}
- **Archivos**: `snake_case` para scripts, `PascalCase` para componentes.
- **Variables**: `camelCase` en JavaScript, `snake_case` en Python.
- **Constantes**: `UPPER_SNAKE_CASE`.
- **Funciones**: Nombres descriptivos que expliquen QUÉ hacen, no CÓMO lo hacen.

## {t['file_struct']}
- Agrupar por funcionalidad, no por tipo de archivo.
- Cada módulo en su propia carpeta con su propio README si es complejo.
- Los archivos de configuración van en la raíz del proyecto.

## {t['documentation_title']}
- Toda función pública debe tener un comentario que explique su propósito.
- El README principal debe explicar cómo instalar y ejecutar el proyecto.
- Los endpoints de API deben estar documentados con ejemplos.

## {t['commits_title']}
- Mensajes de commit descriptivos: `feat: añadir login`, `fix: corregir cálculo`.
- Una funcionalidad por commit. No mezclar cambios no relacionados.

## {t['visual_design_title']}
- Colores: {data.get('primary_color', '#3b82f6')} (primario), paleta coherente.
- Tipografía: moderna y legible.
- Componentes reutilizables con estilos consistentes.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_seguridad(lang='es'):
    """Genera 05_REGLAS/SEGURIDAD.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🔒 {t['security_guide_title']}

## Autenticación
- Implementar OAuth 2.0 o JWT para gestión de sesiones.
- Forzar contraseñas fuertes (mínimo 8 caracteres, mayúscula, número, símbolo).
- Rate-limiting en endpoints de login (máx. 5 intentos / minuto).

## Protección de Datos
- Cifrado en tránsito: TLS 1.3 obligatorio.
- Cifrado en reposo para datos sensibles.
- Sanitización de todas las entradas del usuario (prevenir XSS, SQL injection).

## API
- Validación estricta de JSON Schema en cada endpoint.
- CORS configurado solo para dominios de confianza.
- Tokens con expiración corta y refresh tokens.

## Infraestructura
- Variables de entorno para todos los secretos (nunca en código).
- Logs de acceso y auditoría.
- Backups automáticos de base de datos.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_diseno(data, lang='es'):
    """Genera 06_DISEÑO/ESTILO_VISUAL.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🎨 {t['visual_style_title']}

## Paleta de Colores
| Rol | Color |
|-----|-------|
| **Primario** | `{data.get('primary_color', '#3b82f6')}` |
| **Secundario** | `{data.get('secondary_color', '#8b5cf6')}` |
| **Fondo** | `{data.get('bg_color', '#ffffff')}` |

## {t['style_requested']}
**{data.get('visual_style', 'Moderno y limpio')}**

## {t['user_refs']}
{data.get('visual_reference', t['no_refs'])}

## {t['design_principles']}
1. **Consistencia**: Usar los mismos componentes y espaciados en toda la app.
2. **Jerarquía visual**: El ojo debe saber dónde mirar primero.
3. **Responsive**: Funcionar perfectamente en móvil, tablet y escritorio.
4. **Accesibilidad**: Contraste suficiente, textos legibles, navegación por teclado.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_reglas_workspace(data, lang='es'):
    """Genera 05_REGLAS/WORKSPACE.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🏢 Reglas Específicas del Área de Trabajo (Workspace)

Este documento define la normativa operativa y restricciones del entorno de trabajo lógico y físico.

## Estructura de Trabajo
1. **Directorio Base**: Todos los desarrollos deberán localizarse en el directorio raíz establecido por el entorno del usuario.
2. **Archivos Temporales**: Cualquier recurso o archivo temporal deberá guardarse en un directorio explícito (ej `tmp/` o `.cache/`) que se encuentre ignorado en el control de versiones.
3. **No Interferencia**: No se deben crear, modificar ni eliminar archivos fuera del repositorio activo del proyecto, a menos que conste explícitamente en los *Prompts*.

## Políticas de Ejecución
- Se debe respetar obligatoriamente cualquier flujo de confirmación.
- Los cambios estructucturales (Bases de datos, variables de entorno que borren claves previas) tienen que ser notificados y explicados antes de ejecutarse masivamente.

## Entorno Local vs Producción
- NUNCA sobreescribir las variables globales del sistema (Host).
- Los archivos `.env` solo tendrán referencias vacías si han de subirse a repositorios; las credenciales se manejan offline o con secretos en plataformas de CI/CD.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_workflow_tree(data, lang='es'):
    """Genera 05_REGLAS/WORK_FLOW_TREE.md."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    return f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🌳 Work Flow Tree del Área de Trabajo (Workspace)

El Work Flow Tree representa y unifica la visión del ciclo de desarrollo. Define el marco operativo y el layout esperado del proyecto.

```text
📁 PROYECTO RAIZ (Workspace)
 ├── 📄 README.md                (Contexto global y entrada)
 ├── 📄 docker-compose.yml       (SI APLICA: Entorno contenedorizado)
 ├── 📁 .github/ / .gitlab/      (CI/CD, flujos de versiones)
 ├── 📁 src/                     (Código fuente principal y lógica)
 │    ├── 📁 core/               (Núcleo del negocio, reglas y modelos)
 │    ├── 📁 api/                (Rutas / Endpoints)
 │    ├── 📁 ui/                 (Componentes UI y Frontales)
 │    └── 📁 utils/              (Funciones de utilidad compartidas)
 ├── 📁 tests/                   (Pruebas / Verificaciones)
 ├── 📁 docs/                    (Manuales, guías y descripciones ext.)
 └── 📁 data/                    (Archivos estáticos o temporales .gitignore)
```

## Flujo por Etapas
1. **Preparación (Blueprint)**: Revisión de variables y requerimientos funcionales y técnicos.
2. **Desarrollo Base (Core & API)**: Implementación de la lógica inicial y estructuras DB.
3. **Desarrollo Visual (UI)**: Acoplamiento de Front y Back de acuerdo al Work Flow definido.
4. **Validación Exhaustiva (TEST)**: Desplegar pruebas preventivas.
5. **Entrega/Build**: Creación de entregable final o script automatizado de salida.

---
*{t['footer_generated']} {TOOL_NAME} v{TOOL_VERSION} | {AUTHOR} — {AUTHOR_WEB}*
"""


def generate_detalle_agentes(data, lang='es'):
    """Devuelve un diccionario con los nombres de agente y su contenido markdown detallado."""
    t = BP_I18N.get(lang, BP_I18N['es'])
    app_name = data.get('app_name', 'la aplicación')
    agentes = {}
    
    agentes["01_Arquitecto_IA.md"] = f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🏗️ Arquitecto IA

## Descripción Detallada
El **Arquitecto IA** es el responsable de la visión global y estructural del proyecto "{app_name}". Analiza el requerimiento de negocio y toma las decisiones pertinentes a alto nivel acerca de integraciones, escalabilidad, seguridad y fiabilidad, sentando las bases fundacionales de toda la infraestructura y diseño.

## Responsabilidades
- **Rol principal:** Construir el diagrama maestro y validar que ningún subsistema falle estructuralmente.
- Diseñar y delimitar responsabilidades de cada componente del código.
- Identificar puntos de fricción, dependencias críticas o limitantes de la base tecnológica establecida en este Blueprint.
- Auditar y unificar al resto del equipo IA.

## Entregables
- Esquemas lógicos y de datos.
- Elección de patrones arquitectónicos a seguir de forma transversal en toda la app.
"""

    agentes["02_Desarrollador_Backend_IA.md"] = f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# ⚙️ Desarrollador Backend IA

## Descripción Detallada
El **Desarrollador Backend IA** construye el cerebro lógico, el almacenamiento de datos, y los conectores API que harán posible el funcionamiento técnico de "{app_name}". Es el "motor" del proyecto bajo la supervisión de la Arquitectura escogida.

## Responsabilidades
- **Rol principal:** Escribir y validar la lógica back-end, asegurar la estructura en la persistencia de los datos.
- Controlar el sistema de Autenticación, JWT, roles y permisos correspondientes.
- Integrar APIs y servicios de terceros.
- Optimizar cálculos y garantizar una velocidad de respuesta eficaz (performance server).

## Entregables
- Tablas y Controladores (Modelos y Queries de DB).
- Endpoints (REST, GraphQL) finalizados y documentados.
- Lógica de sincronización.
"""

    agentes["03_Desarrollador_Frontend_IA.md"] = f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🎨 Desarrollador Frontend IA

## Descripción Detallada
El **Desarrollador Frontend IA** crea la magia visual y la interacción humana de la aplicación. Su finalidad es dar vida al "diseño y estilo visual" ya estipulados de "{app_name}" y conectar las vistas con el servidor (Backend).

## Responsabilidades
- **Rol principal:** Plasmar el Look & Feel de la app asegurando una correcta Experiencia y Uso (UI/UX).
- Revestir el estado de la aplicación mediante la maquetación.
- Manejar adecuadamente errores frontales, estados de espera (loading spinners) para que la sensación tecnológica sea fluida.
- Cumplir reglas de accesibilidad, coherencia de color y uso en dispositivos variados (Responsive).

## Entregables
- Vistas completas interactuables.
- Código reutilizable visual a base de componentes (React, Vue, HTML puro o nativos).
- Integración Frontend-Backend transparente para el usuario.
"""

    agentes["04_Ingeniero_QA_IA.md"] = f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 🧪 Ingeniero QA IA

## Descripción Detallada
El **Ingeniero QA (Quality Assurance) IA** es el sabueso y red de seguridad vital del flujo. Rastrea minuciosamente todo lo que el Frontend y el Backend unieron a fin de prevenir fallas o malas prácticas en el proyecto "{app_name}".

## Responsabilidades
- **Rol principal:** Buscar agresivamente vulnerabilidades de código o lógicas (edge cases no prevenidos).
- Revisar que se cumplan todas las *Líneas Rojas* dictadas para el proyecto globalmente.
- Configurar y proponer suites de testing (Unitarias, Integración, mock tools).

## Entregables
- Scripts de validación o pruebas.
- Reporte cruzado de vulnerabilidades solucionables y revisiones de seguridad críticas.
"""

    agentes["05_Ingeniero_DevOps_IA.md"] = f"""---
{t['generated_with']}: {TOOL_NAME}
{t['tool_author']}: {AUTHOR}
---

# 📦 Ingeniero DevOps IA

## Descripción Detallada
El **Ingeniero DevOps IA** es quien agarra el conjunto de código estandarizado y funcional y le abre la puerta del mundo exterior. Automatiza infraestructuras y procesos de integración post-desarrollo.

## Responsabilidades
- **Rol principal:** Asegurar que "{app_name}" pueda construirse (Build) y pueda lanzarse limpiamente en su entorno meta (Producción / LocalHost global).
- Estructurar entornos dockerizados o scripts de despliegue si han sido solicitados.
- Dictar y organizar la integración continua en variables o dependencias finales en un `package.json` o `requirements.txt`.

## Entregables
- Configuraciones listas y limpias (Dockerfile, dependencias puras).
- Paso final de despliegue garantizado.
"""

    return agentes


# ────────────────────────────────────────────────────────────
# SISTEMA MULTI-AGENTE (MAS)
# ────────────────────────────────────────────────────────────
def get_mas_content(complexity):
    """Devuelve un diccionario con el contenido MAS según la complejidad seleccionada."""
    mas_content = {}
    
    if complexity == 'classic':
        return mas_content
        
    if complexity in ['copilot', 'autonomous_mas']:
        mas_content['PROTOCOLOS_MCP_Y_HERRAMIENTAS'] = """# 🛠 Protocolos MCP y Uso de Herramientas
## Regla de Menor Privilegio (PoLP)
- Los agentes (o el asistente único) SOLO pueden solicitar ejecución de herramientas si es estrictamente necesario para cumplir el paso actual.
- Prohibición de bucles de herramientas: Si una API falla 2 veces por timeout o input inválido, se debe emitir un _fallback_ al usuario o al log, no reintentar infinitamente.
## Límite de Contexto (Context Window)
- Cada respuesta generada tras llamar a múltiples herramientas debe ser condensada. Nunca devolver los JSON crudos íntegros en el razonamiento interno, solo la inferencia útil.
"""
        mas_content['GUARDRAILS_Y_QA'] = """# 🛡️ Guardrails y QA
## Anti-Alucinación
- Si una librería, puerto o Endpoint no ha sido provisto como contexto en este blueprint o mediante herramientas de búsqueda en vivo, SE PROHÍBE su invención.
- Confirmación explícita: Si hay duda arquitectónica bloqueante, emitir "USER_QUERY" y pausar.
"""

    if complexity == 'autonomous_mas':
        mas_content['MEMORIA_MAS'] = """# 🧠 Gestión de Memoria y Contexto
## Memoria de Trabajo (Working Memory)
- Se limitará al contexto de la Tarea/Skill actual. Cuando el superagente delega a un subagente, SOLO le transfiere este blueprint y el prompt de tarea, no el historial completo de chat.
## Memoria Episódica (Episodic Memory)
- Obligatorio uso de base de datos vectorial o dumps iterativos en `scratch_pad.md` para recordar decisiones tomadas en iteraciones anteriores. Antes de ejecutar cambios estructurales, el agente DEBE leer la memoria episódica.
"""
        mas_content['COMUNICACION_Y_OBSERVABILIDAD'] = """# 📡 Comunicación y Trazabilidad (Message Broker)
## Inter-Agente
- Los mensajes entre agentes deben ser estructurados: `[SENDER: Agente_X] -> [RECEIVER: Agente_Y] | [INTENT: Code_Review]`.
- No se permiten comunicaciones circulares sin un árbitro (Superagente).
## Observabilidad (Logs)
- Todo output de subagente debe llevar adjunto un árbol de decisiones simple de por qué resolvió así la tarea.
"""
        
    return mas_content

# ────────────────────────────────────────────────────────────
# COMPOSITOR DEL BLUEPRINT (genera el ZIP)
# ────────────────────────────────────────────────────────────
def _build_antigravity_format(zf, data, matched_skills, lang, app_name, features_list, ai_engine):
    # Raíz del ZIP
    zf.writestr("LEEME_PRIMERO.md", generate_leeme(app_name, lang))
    zf.writestr("PROMPT_MAESTRO.md", generate_prompt_inicial(
        app_name,
        data.get('app_desc', ''),
        data.get('app_type', 'Web App'),
        features_list,
        ai_engine,
        data.get('missing_skills'),
        lang
    ))

    # 01_VISION
    zf.writestr("01_VISION/PROYECTO.md", generate_proyecto(data, lang))
    zf.writestr("01_VISION/AUDIENCIA.md", generate_audiencia(data, lang))
    zf.writestr("01_VISION/FUNCIONALIDADES.md", generate_funcionalidades(data, lang))

    # 02_AGENTES
    zf.writestr("02_AGENTES/EQUIPO.md", generate_equipo_agentes(data, lang))

    # 03_SKILLS — Incluir las skills seleccionadas
    for skill_info in matched_skills:
        skill = skill_info[0] if isinstance(skill_info, tuple) else skill_info
        skill_name = skill.get('name', 'Skill')
        folder_name = re.sub(r'[^\w\s-]', '', skill_name).strip().replace(' ', '_')[:50]
        skill_path_prefix = f"03_SKILLS/{folder_name}/"

        # SKILL.md
        content = skill.get('content', '')
        if content:
            zf.writestr(f"{skill_path_prefix}SKILL.md", content)

        # workflow.md
        wf_content = skill.get('workflow_content', '')
        if wf_content:
            zf.writestr(f"{skill_path_prefix}workflow.md", wf_content)

    # 04_ARQUITECTURA
    zf.writestr("04_ARQUITECTURA/STACK_TECNOLOGICO.md", generate_stack_tecnologico(data, lang))

    # 07_SISTEMA_MAS (Opcional según complejidad)
    ai_complexity = data.get('ai_complexity', 'classic')
    mas_content = get_mas_content(ai_complexity)
    if mas_content:
        for title, content in mas_content.items():
            zf.writestr(f"07_SISTEMA_MAS/{title}.md", content)

    # 05_REGLAS
    zf.writestr("05_REGLAS/LINEAS_ROJAS.md", generate_lineas_rojas(data, lang))
    zf.writestr("05_REGLAS/ESTANDARES.md", generate_estandares(data, lang))
    zf.writestr("05_REGLAS/SEGURIDAD.md", generate_seguridad(lang))
    zf.writestr("05_REGLAS/WORKSPACE.md", generate_reglas_workspace(data, lang))
    zf.writestr("05_REGLAS/WORK_FLOW_TREE.md", generate_workflow_tree(data, lang))

    # 06_DISEÑO
    zf.writestr("06_DISEÑO/ESTILO_VISUAL.md", generate_diseno(data, lang))
    
    # AGENTES DETALLADOS
    detalles_agentes = generate_detalle_agentes(data, lang)
    for filename, content in detalles_agentes.items():
        zf.writestr(f"02_AGENTES/AGENTES_INDIVIDUALES/{filename}", content)

    # ARCHIVO DE METADATOS .antigravity
    zf.writestr(".antigravity", json.dumps(data, indent=2, ensure_ascii=False))

def _build_claude_xml_format(zf, data, matched_skills, lang, app_name, features_list, ai_engine):
    xml_content = f'<project name="{app_name}">\n'
    xml_content += f"  <vision>\n{generate_proyecto(data, lang)}\n</vision>\n"
    xml_content += f"  <audience>\n{generate_audiencia(data, lang)}\n</audience>\n"
    xml_content += f"  <features>\n{generate_funcionalidades(data, lang)}\n</features>\n"
    xml_content += f"  <architecture>\n{generate_stack_tecnologico(data, lang)}\n</architecture>\n"
    xml_content += f"  <rules>\n{generate_lineas_rojas(data, lang)}\n{generate_estandares(data, lang)}\n{generate_seguridad(lang)}\n</rules>\n"
    xml_content += f"  <design>\n{generate_diseno(data, lang)}\n</design>\n"
    
    ai_complexity = data.get('ai_complexity', 'classic')
    mas_content = get_mas_content(ai_complexity)
    if mas_content:
        xml_content += f"  <mas_architecture>\n"
        for title, content in mas_content.items():
            safe_tag = title.lower()
            xml_content += f"    <{safe_tag}>\n<![CDATA[\n{content}\n]]>\n    </{safe_tag}>\n"
        xml_content += f"  </mas_architecture>\n"
        
    xml_content += f"  <skills>\n"
    for skill_info in matched_skills:
        skill = skill_info[0] if isinstance(skill_info, tuple) else skill_info
        xml_content += f'    <skill name="{skill.get("name", "")}">\n'
        xml_content += f"      <content><![CDATA[{skill.get('content', '')}]]></content>\n"
        xml_content += f"      <workflow><![CDATA[{skill.get('workflow_content', '')}]]></workflow>\n"
        xml_content += f"    </skill>\n"
    xml_content += f"  </skills>\n"
    xml_content += f"</project>"
    
    zf.writestr(f"{app_name}_context.xml", xml_content)
    
    # Archivo de configuración/metadatos .claude
    claude_config = {
        "project_name": app_name,
        "context_file": f"{app_name}_context.xml",
        "description": data.get('app_desc', ''),
        "ai_engine": ai_engine
    }
    zf.writestr(".claude", json.dumps(claude_config, indent=2, ensure_ascii=False))

    zf.writestr("PROMPT_MAESTRO.md", generate_prompt_inicial(
        app_name,
        data.get('app_desc', ''),
        data.get('app_type', 'Web App'),
        features_list,
        ai_engine,
        data.get('missing_skills'),
        lang
    ) + "\n\n**INSTRUCCIÓN:** Pasa el archivo XML adjunto como contexto inicial.")

def _build_cursor_rules_format(zf, data, matched_skills, lang, app_name, features_list, ai_engine):
    rules_content = f"# Contexto del Proyecto: {app_name}\n\n"
    rules_content += generate_proyecto(data, lang) + "\n\n"
    rules_content += generate_funcionalidades(data, lang) + "\n\n"
    rules_content += "## Tecnologías\n" + generate_stack_tecnologico(data, lang) + "\n\n"
    rules_content += "## Reglas y Líneas Rojas\n" + generate_lineas_rojas(data, lang) + "\n" + generate_estandares(data, lang) + "\n\n"
    rules_content += "## Diseño\n" + generate_diseno(data, lang) + "\n\n"
    
    ai_complexity = data.get('ai_complexity', 'classic')
    mas_content = get_mas_content(ai_complexity)
    if mas_content:
        rules_content += "# 🤖 ARQUITECTURA MULTI-AGENTE (MAS) Y RESILIENCIA\n\n"
        for title, content in mas_content.items():
            rules_content += f"{content}\n\n"
    
    filename = ".windsurfrules" if ai_engine == "Windsurf" else ".cursorrules"
    zf.writestr(filename, rules_content)
    
    zf.writestr("PROMPT_MAESTRO.md", generate_prompt_inicial(
        app_name,
        data.get('app_desc', ''),
        data.get('app_type', 'Web App'),
        features_list,
        ai_engine,
        data.get('missing_skills'),
        lang
    ))

def compose_blueprint(data, matched_skills):
    """Compone el Blueprint completo y genera el archivo ZIP usando el Factory Pattern."""
    lang = data.get('ui_lang', 'es')
    app_name = data.get('app_name', 'MiApp')
    ai_engine = data.get('ai_engine', 'Antigravity')
    safe_name = re.sub(r'[^\w\s-]', '', app_name).strip().replace(' ', '_')
    safe_engine = re.sub(r'[^\w\s-]', '', ai_engine).strip()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M')
    zip_filename = f"{safe_name}_{safe_engine}_Blueprint_{timestamp}.zip"

    # Asegurar que existe la carpeta de salida
    os.makedirs(APPS_OUTPUT_DIR, exist_ok=True)
    zip_path = os.path.join(APPS_OUTPUT_DIR, zip_filename)

    features_list = data.get('features') or []

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        if ai_engine == 'Claude':
            _build_claude_xml_format(zf, data, matched_skills, lang, app_name, features_list, ai_engine)
        elif ai_engine in ['Cursor', 'Windsurf']:
            _build_cursor_rules_format(zf, data, matched_skills, lang, app_name, features_list, ai_engine)
        else:
            # Default fallback format (Antigravity/Genérico)
            _build_antigravity_format(zf, data, matched_skills, lang, app_name, features_list, ai_engine)

    print(f"[✓] Blueprint generado ({lang} - {ai_engine}): {zip_path}")
    return zip_filename, zip_path


# ────────────────────────────────────────────────────────────
# ACTUALIZACIÓN DEL ÍNDICE
# ────────────────────────────────────────────────────────────
import subprocess

def update_index():
    """Regenerar INDEX.js ejecutando ACTUALIZAR.py"""
    try:
        script_path = os.path.join(TOOLS_DIR, "ACTUALIZAR.py")
        print(f"[*] Ejecutando: python3 \"{script_path}\"")
        subprocess.run(["python3", script_path], check=True)
        print("[✓] INDEX.js regenerado automáticamente.")
    except Exception as e:
        print(f"[!] Error regenerando INDEX.js: {e}")

# ────────────────────────────────────────────────────────────
# CREACIÓN DE NUEVAS SKILLS
# ────────────────────────────────────────────────────────────
def create_incubator_skill(feature_name):
    """Crea una skill fantasma en incubadora para que Antigravity la rellene después."""
    category = "00. Skills en Incubación"
    subcategory = "Autogeneradas"
    description = f"Manual técnico pendiente para la funcionalidad: {feature_name}."
    
    today = datetime.now().strftime('%Y-%m-%d')
    folder_name = re.sub(r'[^\w\s\-áéíóúüñÁÉÍÓÚÜÑ()]', '', feature_name).strip()
    if not folder_name:
        folder_name = "skill_nueva_" + str(int(datetime.now().timestamp()))
        
    skill_dir = os.path.join(SKILLS_DIR, category, subcategory, folder_name)
    os.makedirs(skill_dir, exist_ok=True)
    
    skill_id = folder_name.lower().replace(' ', '-')
    skill_id = re.sub(r'[^a-záéíóúüñ0-9\-]', '', skill_id)
    
    skill_content = f"""---
title: {feature_name}
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: {today}
updated: {today}
category: {category}
subcategory: {subcategory}
tags: ['autogenerada', 'pendiente']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: {skill_id}
---

## Descripción
{description}

## Cuándo usarla
- Aplicable cuando es necesario integrar {feature_name}.

## Requisitos
- Revisión manual por Antigravity pendiente.

## Instrucciones y Pasos detallados que se debe seguir:
1. Analizar los requisitos del proyecto.
2. Implementar siguiendo las mejores prácticas.
(Antigravity: Rellenar con los detalles de implementación necesarios para {feature_name})

## Workflow N8N
Referencia al archivo `workflow.json` o script correspondiente.

## Notas y advertencias
- ⚠️ **AVISO PARA ANTIGRAVITY (AGENTE IA)**: Esta Skill ha sido creada de forma proactiva por el App Blueprint Generator. La IA debe rellenar los apartados omitidos.

## Changelog
- v1.0 — Borrador inicial
- v1.1 — Generación y encolado automático
"""
    workflow_content = f"""---
title: Master Workflow: {{feature_name}}
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: {{today}}
updated: {{today}}
category: {{category}}
subcategory: {{subcategory}}
tags: ['autogenerada']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
Permitido su uso personal y educativo citando la fuente.
Prohibida su venta, redistribución comercial o modificación
sin autorización expresa del autor.
---

# 🚀 Estrategia de Automatización: {{feature_name}}

Este documento define las tres vías posibles para implementar la skill de {{feature_name}} en cualquier aplicación del ecosistema Antigravity.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Eventos)
**Ideal para**: Automatización de procesos y disparadores de eventos externos.

```json
{{
  "workflow_type": "N8N_AUTOMATION",
  "trigger": "External_Event",
  "skill_target": "{feature_name}",
  "actions": ["Execute_Logic", "Validate_Output", "Notify_User"]
}}
```
*Instrucción:* Utiliza este flujo para conectar esta skill con otras herramientas (Slack, CRMs, DBs) a través de N8N.

---

## 🟩 Opción B: Script Python (Lógica Core / Backend)
**Ideal para**: Lógica programática pura, IA y procesamiento de datos local.

```python
# Master Automation - Author: Jesús García Fernández
import json

def execute_skill_automation(input_params):
    \"\"\"Lógica operativa automatizada de {feature_name}\"\"\"
    print(f"Iniciando flujo técnico para: {feature_name}")
    # TODO: Implementar lógica basada en SKILL.md
    return {{"status": "success", "skill": "{feature_name}"}}

if __name__ == "__main__":
    execute_skill_automation({{}})
```

---

## 🟧 Opción C: Integración API (Microservicios / Web)
**Ideal para**: Apps web y móviles que consumen servicios en la nube.

**REST Endpoint:** `POST /v1/automate/{skill_id}`
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
    
    with open(os.path.join(skill_dir, "SKILL.md"), 'w', encoding='utf-8') as f:
        f.write(skill_content)
    with open(os.path.join(skill_dir, "workflow.md"), 'w', encoding='utf-8') as f:
        f.write(workflow_content)
        
    print(f"[+] Skill Incubadora creada en: {skill_dir}")
    return {
        'id': skill_id,
        'name': feature_name,
        'description': description,
        'category': category,
        'subcategory': subcategory,
        'has_workflow': True
    }


def create_new_skill(skill_data):
    """Crea una nueva skill en el repositorio siguiendo el estándar v1.1."""
    title = skill_data.get('title', 'Nueva Skill')
    category = skill_data.get('category', '07. Inteligencia Artificial')
    subcategory = skill_data.get('subcategory', 'General')
    description = skill_data.get('description', 'Skill generada automáticamente.')
    tags = skill_data.get('tags', [])

    today = datetime.now().strftime('%Y-%m-%d')
    folder_name = re.sub(r'[^\w\s\-áéíóúüñÁÉÍÓÚÜÑ()]', '', title).strip()
    skill_dir = os.path.join(SKILLS_DIR, category, subcategory, folder_name)

    os.makedirs(skill_dir, exist_ok=True)

    tags_str = json.dumps(tags, ensure_ascii=False) if isinstance(tags, list) else f"[{tags}]"
    skill_id = title.lower().replace(' ', '-')
    skill_id = re.sub(r'[^a-záéíóúüñ0-9\-]', '', skill_id)

    skill_content = f"""---
title: {title}
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: {today}
updated: {today}
category: {category}
subcategory: {subcategory}
tags: {tags_str}

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: {skill_id}
---

## Descripción
{description}

## Cuándo usarla
- Aplicación de desarrollo o escenario de uso.

## Requisitos
- Dependencias o configuraciones previas necesarias.

## Instrucciones y Pasos detallados que se debe seguir:
1. Analizar los requisitos del proyecto.
2. Implementar siguiendo las mejores prácticas del sector.
3. Validar el resultado con pruebas funcionales.

## Workflow N8N
Referencia al archivo `workflow.json` incluido.

## Notas y advertencias
- ⚠️ Requiere adaptación final para producción.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Aplicación estándar
"""

    skill_path = os.path.join(skill_dir, "SKILL.md")
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(skill_content)

    return {
        'id': skill_id,
        'name': title,
        'category': category,
        'subcategory': subcategory,
        'path': skill_path
    }


# ────────────────────────────────────────────────────────────
# HANDLER HTTP
# ────────────────────────────────────────────────────────────
class BlueprintHandler(BaseHTTPRequestHandler):
    """Servidor HTTP para la interfaz del Blueprint Generator."""
    skills_data = []

    def log_message(self, format, *args):
        """Reduce el ruido en los logs."""
        # Solo mostrar errores, no cada petición GET
        if args and '404' in str(args[0]):
            print(f"[HTTP] {args[0]}" if args else "")

    def _send_json(self, data, status=200):
        """Envía una respuesta JSON con CORS."""
        try:
            self.send_response(status)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        except Exception as e:
            print(f"[!] Error enviando JSON: {e}")

    def _send_file(self, filepath, content_type):
        """Envía un archivo estático."""
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "Archivo no encontrado")

    def do_OPTIONS(self):
        """Maneja preflight CORS."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        """Maneja peticiones GET."""
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/' or path == '/index.html':
            self._send_file(os.path.join(PROJECT_ROOT, "GENERADOR.html"), 'text/html')

        elif path == '/api/status':
            self._send_json({
                'status': 'online',
                'skills_count': len(self.skills_data),
                'tool': TOOL_NAME,
                'version': TOOL_VERSION
            })

        elif path == '/api/categories':
            cats = {}
            for s in self.skills_data:
                cat = s.get('category', 'Otros')
                sub = s.get('subcategory', 'General')
                if cat not in cats:
                    cats[cat] = {'total': 0, 'subcategories': []}
                cats[cat]['total'] += 1
                if sub not in cats[cat]['subcategories']:
                    cats[cat]['subcategories'].append(sub)
            self._send_json(cats)

        elif path.startswith('/api/download/'):
            filename = urllib.parse.unquote(path.split('/api/download/')[1])
            zip_path = os.path.join(APPS_OUTPUT_DIR, filename)
            if os.path.exists(zip_path):
                self.send_response(200)
                self.send_header('Content-Type', 'application/zip')
                self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                with open(zip_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "ZIP no encontrado")

        else:
            # Intentar servir archivos estáticos del directorio raíz
            # IMPORTANTE: Descodificar el path de la URL para manejar espacios y caracteres especiales
            clean_path = urllib.parse.unquote(path.lstrip('/'))
            file_path = os.path.join(REPO_ROOT, clean_path)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                ext = os.path.splitext(file_path)[1].lower()
                content_types = {
                    '.html': 'text/html', '.js': 'application/javascript',
                    '.css': 'text/css', '.png': 'image/png',
                    '.jpg': 'image/jpeg', '.svg': 'image/svg+xml',
                    '.json': 'application/json', '.md': 'text/markdown; charset=utf-8'
                }
                ct = content_types.get(ext, 'application/octet-stream')
                
                # Para archivos markdown, forzar descarga y asegurar UTF-8
                if ext == '.md':
                    filename = os.path.basename(file_path)
                    self.send_response(200)
                    self.send_header('Content-Type', ct)
                    self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Content-Length', str(os.path.getsize(file_path)))
                    self.end_headers()
                    with open(file_path, 'rb') as f:
                        self.wfile.write(f.read())
                else:
                    self._send_file(file_path, ct)
            else:
                self.send_error(404)

    def do_POST(self):
        """Maneja peticiones POST."""
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self._send_json({'error': 'JSON inválido'}, 400)
            return

        try:
            if path == '/api/analyze':
                print(f"[*] Analizando skills para: {data.get('app_name', '?')}")
                # Buscar skills relevantes
                query = (data.get('app_desc', '') or '') + ' ' + (data.get('app_name', '') or '')
                features = ' '.join(data.get('features') or [])
                results = match_skills(query, features, self.skills_data)

                self._send_json({
                    'matched_skills': [
                        {
                            'id': s[0].get('id'),
                            'name': s[0].get('name'),
                            'category': s[0].get('category'),
                            'subcategory': s[0].get('subcategory'),
                            'description': s[0].get('description'),
                            'relevance': s[1],
                            'has_workflow': bool(s[0].get('workflow_content'))
                        }
                        for s in results
                    ],
                    'total_skills_searched': len(self.skills_data)
                })

            elif path == '/api/generate':
                print(f"[*] Generando Blueprint para: {data.get('app_name', '?')}")
                # Generar el Blueprint ZIP
                selected_ids = data.get('selected_skill_ids') or []
                
                # Normalizar IDs: pueden venir como int o string
                selected_ids_str = [str(sid) for sid in selected_ids]
                
                matched = [s for s in self.skills_data if str(s.get('id', '')) in selected_ids_str]
                print(f"[*] Skills seleccionadas: {len(matched)} de {len(selected_ids)} IDs")

                # Incluir como tupla (skill, score) para compatibilidad
                matched_tuples = [(s, 100) for s in matched]

                # PROACTIVIDAD: Generar missing_skills como borradores para la IA
                missing_skills_list = data.get('missing_skills') or []
                index_needs_update = False
                if missing_skills_list:
                    print(f"[*] Detectadas {len(missing_skills_list)} skills faltantes. Generando proactivamente...")
                    for feature_name in missing_skills_list:
                        new_skill_dict = create_incubator_skill(feature_name)
                        matched_tuples.append((new_skill_dict, 100))
                        index_needs_update = True
                        
                if index_needs_update:
                    update_index()
                    # Recargar en memoria para que aparezcan en futuras peticiones sin reiniciar servidor
                    BlueprintHandler.skills_data = load_skills_data()

                zip_filename, zip_path = compose_blueprint(data, matched_tuples)

                self._send_json({
                    'success': True,
                    'filename': zip_filename,
                    'download_url': f'/api/download/{urllib.parse.quote(zip_filename)}',
                    'skills_included': len(matched) + len(missing_skills_list),
                    'path': zip_path
                })

            elif path == '/api/create-skill':
                # Crear nueva skill
                result = create_new_skill(data)
                update_index()
                BlueprintHandler.skills_data = load_skills_data()
                self._send_json({
                    'success': True,
                    'skill': result
                })

            else:
                self._send_json({'error': 'Endpoint no encontrado'}, 404)

        except Exception as e:
            print(f"\n[!!] ERROR CRÍTICO en {path}:")
            traceback.print_exc()
            print()
            try:
                self._send_json({'error': str(e), 'success': False}, 500)
            except Exception:
                print("[!!] No se pudo enviar respuesta de error al cliente")


def start_server():
    """Inicia el servidor HTTP."""
    # Cargar datos
    BlueprintHandler.skills_data = load_skills_data()

    server = ThreadingHTTPServer(('', PORT), BlueprintHandler)
    print(f"\n{'='*60}")
    print(f"  🛸 {TOOL_NAME} v{TOOL_VERSION}")
    print(f"  Autor: {AUTHOR} | {AUTHOR_WEB}")
    print(f"{'='*60}")
    print(f"  Servidor activo en: http://localhost:{PORT}")
    print(f"  Skills cargadas: {len(BlueprintHandler.skills_data)}")
    print(f"  Carpeta de salida: {APPS_OUTPUT_DIR}")
    print(f"{'='*60}")
    print(f"  Presiona Ctrl+C para detener el servidor.\n")

    # Abrir navegador automáticamente
    threading.Timer(1.5, lambda: webbrowser.open(f'http://localhost:{PORT}')).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Servidor detenido.")
        server.server_close()


if __name__ == "__main__":
    start_server()
