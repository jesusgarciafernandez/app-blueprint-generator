---
title: Hardening de Sistemas
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['hardening', 'cybersecurity', 'os-security', 'cis-benchmarks', 'linux-security', 'bastion', 'encryption', 'compliance', 'sysadmin']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 423
---

## Descripción
Habilidad técnica especializada en la reducción de la superficie de ataque de sistemas operativos, servidores y contenedores mediante la eliminación de servicios innecesarios, la configuración restrictiva de permisos y la aplicación de políticas de seguridad estrictas. Esta skill se centra en la implementación de estándares internacionales como los CIS Benchmarks y el cumplimiento del modelo de defensa en profundidad. Abarca desde la securización del kernel y el sistema de archivos hasta la configuración avanzada de SSH, cortafuegos (iptables/nftables) y la gestión de identidades, asegurando que cada nodo de la infraestructura sea resiliente ante intentos de explotación de vulnerabilidades.

## Cuándo usarla
Escenarios que activan esta skill:
- Al desplegar nuevos servidores en producción (Bare Metal o Cloud) para garantizar que no tengan configuraciones por defecto inseguras.
- Para preparar infraestructuras críticas que deben cumplir con estándares de cumplimiento (ej: PCI-DSS, SOC2).
- Durante el proceso de respuesta ante incidentes para cerrar brechas de seguridad tras una detección de intrusión.
- Cuando se requiere aislar servicios internos mediante el uso de "Bastion Hosts" o entornos de ejecución restringidos.
- Para optimizar la seguridad de imágenes de contenedor (Docker/Kubernetes) eliminando binarios innecesarios (Distroless).

## Requisitos
- Dominio de administración de sistemas Linux (RHEL, Debian, Ubuntu).
- Familiaridad con los CIS Benchmarks y estándares NIST.
- Conocimientos de herramientas de auditoría de seguridad (Lynis, OpenSCAP).
- Experiencia en gestión de usuarios, grupos y permisos avanzados (ACLs, SELinux/AppArmor).
- Entendimiento de protocolos de red y criptografía básica.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
