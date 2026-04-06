---
title: Gestión de Dependencias
version: 1.1
author: Jesús García Fernández
website: jesusgarciafernandez.com
created: 2026-04-01
updated: 2026-04-06
category: 13. Desarrollo y Tecnología
subcategory: General
tags: ['dependencies', 'npm', 'pip', 'maven', 'security', 'vulnerability-scanning', 'sbom', 'artifactory', 'supply-chain']

license: CC BY-NC 4.0
license_url: https://creativecommons.org/licenses/by-nc/4.0/
notice: >
  Esta skill es de autoría original de Jesús García Fernández.
  Permitido su uso personal y educativo citando la fuente.
  Prohibida su venta, redistribución comercial o modificación
  sin autorización expresa del autor.
id: 384
---

## Descripción
Habilidad crítica para la administración, actualización y securización de las librerías de terceros y módulos externos que componen una aplicación moderna. Esta skill se centra en el dominio de gestores de paquetes (npm/yarn, pip, maven, cargo), el análisis de la cadena de suministro de software (Software Supply Chain Security) y la mitigación de vulnerabilidades conocidas. Abarca el uso de archivos de bloqueo (lockfiles) para garantizar la reproducibilidad, la creación de inventarios de componentes (SBOM - Software Bill of Materials) y la automatización de escaneos de seguridad para detectar paquetes maliciosos o desactualizados que pongan en riesgo la integridad del sistema.

## Cuándo usarla
Escenarios que activan esta skill:
- Al iniciar un nuevo proyecto para seleccionar y configurar el gestor de paquetes más adecuado.
- Para solucionar conflictos de versiones o errores de "dependency hell" que impiden la compilación.
- Durante el proceso de auditoría de seguridad para identificar y parchear CVEs (Common Vulnerabilities and Exposures) en librerías externas.
- Cuando se requiere garantizar que todos los desarrolladores y entornos de CI/CD utilicen exactamente las mismas versiones de las dependencias.
- Para gestionar repositorios privados de paquetes dentro de una organización (ej: JFrog Artifactory, GitHub Packages).

## Requisitos
- Familiaridad con gestores de paquetes específicos del lenguaje utilizado (npm, pip, composer, etc.).
- Conocimientos de versionado semántico (SemVer).
- Experiencia con herramientas de escaneo de seguridad (npm audit, Snyk, Dependabot).
- Entendimiento de los riesgos de "Typosquatting" y ataques a la cadena de suministro.
- Capacidad para interpretar reportes de vulnerabilidades técnicas.

## Instrucciones y Pasos detallados que se debe seguir:


## Workflow N8N
Referencia al archivo `workflow.json` o scripts integrados.

## Notas y advertencias
- ⚠️ **Mantenimiento Técnico**: Requiere verificación mensual.

## Changelog
- v1.0 — Versión inicial
- v1.1 — Enriquecimiento técnico especializado y normalización de formato V1.1
