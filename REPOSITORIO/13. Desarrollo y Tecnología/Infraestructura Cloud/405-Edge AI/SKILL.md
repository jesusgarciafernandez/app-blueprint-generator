---
title: Edge AI
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['edge-ai', 'tinyml', 'on-device-inference', 'iot', 'hardware-acceleration', 'quantization', 'latency-optimization', 'privacy-by-design']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 405
---

## Descripción
Habilidad de ingeniería avanzada centrada en la optimización y ejecución de modelos de Inteligencia Artificial directamente en el hardware final (el "borde" de la red), eliminando la dependencia de la nube para la inferencia. Edge AI permite que smartphones, cámaras de seguridad, sensores industriales y dispositivos IoT tomen decisiones en milisegundos, aumentando la privacidad, reduciendo drásticamente la latencia y permitiendo el funcionamiento en entornos sin conexión a internet. Esta skill abarca desde la compresión de modelos pesados hasta el aprovechamiento de aceleradores de hardware específicos (NPU, TPU).

## Cuándo usarla
Escenarios que activan esta skill:
- En cámaras de seguridad inteligentes que deben detectar rostros o movimientos sospechosos sin enviar el video a la nube por privacidad.
- Para implementar control por voz en electrodomésticos que deben funcionar sin conexión Wi-Fi de forma instantánea.
- En vehículos autónomos o drones donde la latencia de enviar datos a la nube para una decisión de frenado sería fatal.
- Para monitorización de salud en wearables (relojes inteligentes) que analizan el ritmo cardíaco de forma continua con bajo consumo de batería.
- En fábricas (Smart Industry) para el control de calidad en líneas de montaje de alta velocidad.

## Requisitos
- Conocimiento de técnicas de optimización de modelos (Cuantización, Pruning, Distilación).
- Dominio de frameworks de Edge (TensorFlow Lite, ONNX Runtime, CoreyML, OpenVINO).
- Familiaridad con hardware específico (NVIDIA Jetson, Raspberry Pi, microcontroladores con ESP32).
- Capacidad de programar en lenguajes de bajo nivel (C++, Rust) para maximizar el rendimiento.
- Entendimiento de los balances entre Precisión del Modelo vs Consumo de Batería/Memoria.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
