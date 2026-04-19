---
title: Sistema de Encuestas NPS y Post-venta (Automated Feedback Loops)
version: 2.0
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-17
category: 05. Atención al Cliente
subcategory: General
tags: [nps-system, post-sale-feedback, customer-satisfaction, automated-surveys, transactional-feedback, customer-advocacy, feedback-orchestration, data-driven-service, brand-loyalty]

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 171
---

## 0. Filosofía Human-Centric AI
*Esta habilidad establece un diálogo sistemático y honesto con el cliente tras cada interacción crítica, utilizando la tecnología para capturar el sentimiento real y asegurar que la voz del usuario sea el motor que guíe la evolución del servicio y el compromiso ético de la marca.*

**El Rol del Humano:** El Analista de Experiencia debe ser un "Garantes de la Escucha". La IA puede automatizar el envío de encuestas via multicanal (Email, SMS, In-app), clasificar las respuestas abiertas por temática y generar informes de tendencia de NPS al instante, pero solo el humano puede llamar a un "Detractor" (usuario insatisfecho) para entender la raíz emocional de su descontento, decidir qué cambios estructurales en el servicio son necesarios a pesar de que los datos parezcan aceptables, y asegurar que la marca actúe con humildad y rapidez ante las sugerencias de mejora de sus clientes.
**Empoderamiento:** Usamos la tecnología para sustituir la suposición por la certeza basada en la opinión directa y cuantificada del cliente.

---

## 1. Descripción Detallada
El Sistema de Encuestas NPS y Post-venta (v2.0) es la infraestructura técnica para medir la lealtad y satisfacción del cliente de forma automatizada y escalable. No es solo "mandar una pregunta"; es **Orquestación de Ciclos de Feedback**. El enfoque v2.0 se centra en el **Net Promoter Score (NPS)** como métrica de lealtad a largo plazo, combinada con encuestas transaccionales de post-venta para medir la efectividad de interacciones específicas. Integra el cierre del ciclo de feedback ("Closing the Loop") asegurando que cada opinión negativa active una acción de rescate automática o manual.

## 2. Escenarios de Aplicación
- **Medición de Lealtad Trimestral:** Envío automatizado de encuestas NPS a la base de clientes activa para detectar riesgos de Churn.
- **Feedback Inmediato Post-compra:** Evaluación de la experiencia de compra y logística justo tras la recepción del producto.
- **Evaluación de Soporte Técnico:** Medición de la satisfacción (CSAT) tras la resolución de un ticket o consulta.
- **Identificación de 'Promotores' para Marketing:** Detección de usuarios con 9 o 10 en NPS para invitarles a dejar reseñas públicas (Skill 169).
- **Procesos de Mejora Continua (CI):** Uso de los comentarios abiertos para alimentar el backlog de producto o las revisiones de procesos de servicio.

## 3. Requisitos de Implementación
- **Plataformas de Encuestación Automatizada:** Integración de Typeform, SurveyMonkey o sistemas nativos via API.
- **Segmentación Dinámica de Audiencia:** Capacidad de enviar encuestas solo a usuarios que han tenido interacción reciente.
- **Lógica de 'Anti-Spam' de Encuestas:** Reglas para no saturar al mismo usuario con múltiples encuestas en periodos cortos.
- **Sistema de Alertas por Feedback Crítico:** Integración con Slack o CRM para notificar opiniones negativas al instante.

---

## 4. Diferencial: Encuestas Manuales vs. NPS System v2.0

| Dimensión | Enfoque Legacy (Manual) | NPS & Post-venta System (v2.0) |
| :--- | :--- | :--- |
| **Envío** | Campañas aisladas y pesadas. | Disparadores automáticos por hitos de cliente. |
| **Análisis** | Lectura manual de Excel. | Clasificación de temas y sentimientos por IA. |
| **Acción** | Los datos se guardan y olvidan. | Activación de protocolos de rescate (Alertas). |
| **Frecuencia** | Una vez al año (Datos obsoletos). | Seguimiento continuo y dinámico. |

---

## 5. Instrucciones y Pasos Detallados (Protocolo Maestro)

### Fase 1: Diseño de la Arquitectura de Feedback
**Objetivo:** Capturar datos valiosos sin fricción para el usuario.
1.  **Definición de la 'Métrica Maestra':** IA ayuda a decidir entre NPS (Lealtad), CSAT (Satisfacción) o CES (Esfuerzo) según el hito.
2.  **Redacción de la Pregunta de 'Follow-up':** IA sugiere preguntas abiertas dinámicas basadas en la puntuación numérica elegida por el cliente.

**Prompt Maestro de Sistema NPS:**
```text
Actúa como un Senior CX Analyst y Experto en Estrategia de Feedback. Diseña el sistema de encuestas para [REVOLUCIÓN_SERVICIO_PROYECTO]. 
1. Define los 3 'Trigger Points' de Feedback: ¿En qué momentos enviamos la encuesta (Ej: Registro, Primera compra, 3 meses de uso)? 
2. Diseña la 'Pregunta NPS Definitiva': Redacta el copy que maximice la tasa de respuesta. 
3. Lógica de 'Cierre del Círculo': Describe la acción automática si un cliente puntúa < 6 y la acción si puntúa > 8. 
4. Análisis de Comentarios Abiertos: ¿Cómo usamos la IA para resumir 500 comentarios en 5 'dolores' principales cada semana? 
5. Protocolo de 'Anonimato vs. Atribución': ¿Cuándo es mejor pedir nombre y cuándo dejarlo anónimo para obtener la verdad?
```

### Fase 2: Automatización de Alertas y Gestión del Cambio
... (Expansión técnica sobre la creación de Dashboards de NPS por segmento de cliente, la integración de las notas de satisfacción en el perfil del cliente del CRM para que el comercial sepa "cómo está el clima" antes de llamar, y la automatización de correos de agradecimiento personalizados tras recibir la opinión) ...

---

## 6. Arquitectura de Automatización Lógica (Agnostic Flow)
*Lógica de captación y reacción al feedback.*

1.  **Trigger:** Finalización exitosa de un proceso clave (Ej: Entrega de pedido, Fin de suscripción anual).
2.  **Nodo de Envío de Micro-Survey:** El sistema manda la encuesta optimizada para móviles (1 sola pregunta + 1 comentario).
3.  **Nodo de Procesamiento de Respuesta:** IA categoriza el sentimiento y el tema de la respuesta abierta.
4.  **Nodo de Acción Resolutiva:** Si la nota es baja, se crea una tarea de "Rescate de Cliente" en HubSpot; si es alta, se le agradece y se le pide una reseña pública.
5.  **Output:** Flujo constante de inteligencia de mercado; reducción de puntos ciegos operativos y aumento de la fidelidad del cliente por sentirse escuchado.

---

## 7. Ejemplo Práctico: Suscripción de Software 'DesignTool'
**Reto:** No sabían por qué los clientes se iban tras pagar el primer año. Las encuestas anuales tenían una tasa de respuesta del 5%.
**Acción v2.0:** Implementaron el NPS automatizado a los 3, 6 y 11 meses. A los 3 meses detectaron que mucha gente tenía dudas con la facturación.
**Resultado:** Arreglaron el portal de facturación proactivamente. La tasa de respuesta subió al 32% (encuestas cortas). El Churn anual bajó un 12% al resolver dudas "latentes" detectadas a los 6 meses.

---
**Autor:** Jesús García Fernández  
**Licencia:** CC BY-NC 4.0
