---
title: Account Based Marketing (ABM) y Estrategia de Cuentas de Alto Valor
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 01. Marketing Digital
subcategory: Publicidad de Pago (Ads)
tags: [abm, b2b-strategy, account-orchestration, intent-data, precision-marketing, smarketing, ia-b2b]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 035
---

## 0. Filosofía Human-Centric AI
*Esta habilidad asegura que la venta compleja siga siendo un proceso de confianza entre personas, eliminando el ruido innecesario.*

**El Rol del Humano:** El consultor ABM debe ser un estratega de relaciones. La IA identifica las señales de intención de las empresas, pero el humano es el que diseña la propuesta que resuelve el problema político o estratégico de la cuenta objetivo.
**Empoderamiento:** Usamos la tecnología para "rodear" a los decisores de una empresa con mensajes de valor, permitiendo que el equipo de ventas entre en la conversación cuando la confianza ya ha sido sembrada.

---

## 1. Descripción Detallada
Esta habilidad estratégica de marketing B2B está diseñada para maximizar la eficiencia comercial enfocándose exclusivamente en un conjunto de **Cuentas Objetivo (Target Accounts)**. El ABM invierte el embudo tradicional: en lugar de captar volumen, busca precisión milimétrica. El enfoque v2.0 incorpora la **Inteligencia de Intención Predictiva (Intent Data)**, donde la IA detecta cuándo una empresa objetivo está investigando a la competencia para activar automáticamente una campaña de contraste de valor personalizada para sus directivos.

## 2. Escenarios de Aplicación
- **Venta Enterprise Compleja:** Ecosistemas donde deciden 5 o más personas (Comité de Compras).
- **Penetración en Cuentas Estratégicas:** Intentar entrar en empresas del Fortune 500 donde la publicidad masiva no sirve.
- **Estrategias de Expansión (Land & Expand):** Crecer dentro de un cliente actual ofreciendo servicios a otros departamentos.
- **Licitaciones de Alto Valor:** Personalización extrema de la propuesta para ganar contratos públicos o privados críticos.

## 3. Requisitos de Implementación
- **Target Account List (TAL):** Una lista validada de empresas que realmente queremos como clientes.
- **Stack ABM:** Herramientas de publicidad por IP o dominio (LinkedIn, Demandbase o 6sense).
- **Alineación Smarketing:** Comunicación diaria y objetivos compartidos entre Marketing y Ventas.

---

## 4. Diferencial: Marketing B2B Tradicional vs. ABM v2.0

| Dimensión | Inbound / Outbound Clásico | ABM Estratégico (v2.0) |
| :--- | :--- | :--- |
| **Métrica** | Número de Leads (MQLs). | Engagement y Pipeline por Cuenta. |
| **Contenido** | Generalista por industria. | Hiper-personalizado por empresa y cargo. |
| **Canales** | Masivos (SEO/Ads genéricos). | Quirúrgicos (Ads por IP / Direct Mail / LinkedIn). |
| **Relación** | Marketing entrega, Ventas gestiona. | Marketing y Ventas orquestan el viaje juntos. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Identificación y Perfilado de Cuentas (ICP Avanzado)
**Objetivo:** No perder el tiempo con empresas que no pueden pagarnos.
1.  **Define el Perfil de Cliente Ideal:** Facturación, sector, tecnología que ya usan.
2.  **Mapeo del Comité de Compras:** Identifica al Decisor, al Influenciador y al Usuario final.

**Prompt Maestro de ABM:**
```text
Actúa como Estratega de Marketing B2B. Para la cuenta objetivo [EMPRESA_OBJETIVO], analiza su informe anual o web. 
Identifica los 3 retos estratégicos que mencionan. 
Genera 3 ganchos (hooks) de LinkedIn personalizados para el Director de [DEPARTAMENTO] que relacionen nuestro producto con sus retos específicos. 
Sugiere una landing page dinámica que incluya el logo de la empresa objetivo y su industria.
```

### Fase 2: Orquestación Multicanal y Nutrición de Cuenta
... (Expansión técnica sobre el uso de publicidad programática y eventos exclusivos) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de orquestación de cuentas.*

1.  **Trigger:** Una empresa de nuestra TAL visita la página de "Casos de Éxito" 2 veces en un día.
2.  **Nodo de Identificación:** IA reconoce el dominio de la empresa (vía IP o Reverse DNS).
3.  **Nodo de Acción:**
    - Alerta inmediata a Ventas vía Slack: "[EMPRESA] nos está investigando".
    - Activación de campaña de Retargeting en LinkedIn exclusiva para directivos de esa empresa.
4.  **Nodo de Personalización:** Envío automático de una invitación a un webinar técnico específico para su sector.
5.  **Output:** Reunión comercial agendada con un prospecto altamente educado y consciente del valor.

---

## 7. Ejemplo Práctico: Consultoría de Ciberseguridad
**Reto:** Querían vender a los 10 bancos más grandes del país.
**Acción v2.0:** Se creó una campaña ABM que mostraba a los empleados de IT de esos bancos anuncios sobre "Cómo evitar ataques en el sector bancario" citando sus propias tecnologías.
**Resultado:** Consiguieron abrir brecha en 4 de los 10 bancos en menos de 6 meses, con contratos superiores a los 200.000€.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
