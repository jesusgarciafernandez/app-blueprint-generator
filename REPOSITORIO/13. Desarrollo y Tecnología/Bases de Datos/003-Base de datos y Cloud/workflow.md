---
title: Master Workflow: Base de datos y Cloud
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
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
---

# 🚀 Estrategia de Automatización: Base de datos y Cloud (Infraestructura)

Este documento define las tres vías posibles para implementar la skill de Base de datos y Cloud en cualquier aplicación del ecosistema Antigravity, utilizando **Supabase (PostgreSQL)** como plataforma central.

---

## 🟦 Opción A: Flujo N8N (Low-Code / Gestión)
**Ideal para**: Backups remotos, sincronización entre bases y limpieza de datos periódica.

```json
{
  "workflow_type": "N8N_AUTOMATION_DB",
  "trigger": "Scheduled_Backup",
  "skill_target": "Base de datos y Cloud",
  "actions": [
    {
      "node": "Supabase_Node",
      "action": "Select_Rows",
      "params": ["users", "profiles"]
    },
    {
      "node": "Google_Drive_Node",
      "action": "Upload_Backup",
      "params": ["DB_Dump.sql"]
    }
  ]
}
```
*Instrucción:* Utiliza este flujo para automatizar tareas administrativas y de mantenimiento de la base de datos sin escribir código pesado.

---

## 🟩 Opción B: Script Python (Lógica de Datos / ETL)
**Ideal para**: Procesamiento por lotes, migraciones automáticas y análisis local masivo.

```python
# Master Automation - Author: Jesús García Fernández
import pandas as pd
from sqlalchemy import create_client, engine

# Configuración de conexión (Variables Jesús García Fernández)
db_url = "postgresql://user:password@host/dbname"

def perform_data_cleanup():
    """Ejecuta una limpieza de datos en la nube"""
    db_engine = engine.create_engine(db_url)
    df = pd.read_sql("SELECT * FROM profiles WHERE active = false", db_engine)
    print(f"Borrando {len(df)} perfiles inactivos...")
    # Lógica de eliminación...
    return True

if __name__ == "__main__":
    perform_data_cleanup()
```

---

## 🟧 Opción C: Integración API (SQL Serverless / Edge)
**Ideal para**: Aplicaciones web (Frontend) que consumen datos en tiempo real mediante Supabase Client.

**Supabase SDK (SQL Directo):**

```javascript
/* Integración Técnica v1.1 */
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY)

// Insertar datos complejos
async function saveProjectData(project) {
  const { data, error } = await supabase
    .from('projects')
    .insert([
      { title: project.name, description: project.desc, user_id: auth.id }
    ])
}

// Suscripción en tiempo real (Realtime)
const channel = supabase
  .channel('changes')
  .on('postgres_changes', { event: '*', schema: 'public', table: 'messages' }, payload => {
    console.log('Mensaje Recibido!', payload)
  })
  .subscribe()
```

---

## 📝 Guía de Selección para Antigravity
1. **Tareas de Mantenimiento o Reportes**: Usa Opción A (N8N).
2. ** scripts de Limpieza o IA sobre Datos**: Usa Opción B (Python).
3. **App de una Sola Página (SPA) o Colaboración Real-Time**: Usa Opción C (JS Client/Realtime).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
