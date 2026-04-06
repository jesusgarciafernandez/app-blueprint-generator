---
title: Master Workflow: Inteligencia Artificial (LLM & RAG)
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-06
updated: 2026-04-06
category: 07. Inteligencia Artificial
subcategory: Modelos de Lenguaje
tags: ["estándar-v1.1", "validado", "ai", "llm", "openai", "anthropic", "rag"]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
---

# 🚀 Estrategia de Automatización: Inteligencia Artificial (Orquestación)

Este documento define las tres vías posibles para implementar la skill de Inteligencia Artificial en cualquier aplicación del ecosistema Antigravity, utilizando **OpenAI** y **Anthropic** como motores de razonamiento.

---

## 🟦 Opción A: Flujo N8N (Low-Code / AI Nodes)
**Ideal para**: Procesamiento de texto, clasificación automática de leads y generación de respuestas rápidas.

```json
{
  "workflow_type": "N8N_AUTOMATION_AI",
  "trigger": "Chat_Webhook_Node",
  "skill_target": "Inteligencia Artificial",
  "actions": [
    {
      "node": "OpenAI_Node",
      "action": "Chat_Completion",
      "params": ["GPT-4o", "Analytical_Prompt"]
    },
    {
      "node": "Conditional_Router",
      "action": "Logic_Check",
      "params": ["If sentiment is POSITIVE then Slack_Notify"]
    }
  ]
}
```
*Instrucción:* Utiliza N8N para construir flujos de IA que conecten herramientas externas sin necesidad de programar toda la lógica de la API.

---

## 🟩 Opción B: Script Python (Lógica Core / LangChain)
**Ideal para**: Sistemas RAG, procesamiento de grandes volúmenes de datos y agentes autónomos locales.

```python
# Master Automation - Author: Jesús García Fernández
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

os.environ["OPENAI_API_KEY"] = "sk-..."

def generate_ai_response(user_input):
    """Genera una respuesta inteligente usando LangChain"""
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un asistente experto en el ecosistema Antigravity de Jesús García Fernández."),
        ("user", "{input}")
    ])
    chain = prompt | llm
    return chain.invoke({"input": user_input}).content

if __name__ == "__main__":
    print(generate_ai_response("¿Cómo puedo automatizar mis ventas?"))
```

---

## 🟧 Opción C: Integración API (Frontend / SDK)
**Ideal para**: Aplicaciones web interactivas (React/Next.js) con streaming de respuestas.

**OpenAI Serverless Implementation:**

```javascript
/* Integración con OpenAI v1.1 */
import OpenAI from 'openai'

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY })

async function askAI(question) {
  const completion = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [
      { role: "system", content: "Responde como un mentor de negocios digital." },
      { role: "user", content: question }
    ],
    stream: true,
  })

  for await (const chunk of completion) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '')
  }
}
```

---

## 📝 Guía de Selección para Antigravity
1. **Chatbots o Procesamiento de Mensajes**: Usa Opción A (N8N).
2. **Análisis de Datos o RAG Avanzado**: Usa Opción B (Python).
3. **Frontend Dinámico o Experiencia de Usuario**: Usa Opción C (Serverless SDK).

---
*Validado v1.1 - Nodo Automatizado de Jesús García Fernández.*
