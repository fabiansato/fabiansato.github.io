---
title: "We.Retail · Dynamic Search Card Core"
slug: "weretail-dynamicsearchcard-core"
date: "2025-03-28"
layout: "project"
lang: "es"
permalink: "/project/weretail-dynamicsearchcard-core"
translation_url: "/en/project/weretail-dynamicsearchcard-core"
group: "lab"
year: "2025"
featured: false
order: 8
subtitle: "Laboratorio · Java y AEM"
description: "Exploración de un servicio Java y un servlet Sling para exponer datos JSON externos."
technologies: ["Java", "Maven", "Apache Sling", "OSGi", "JSON"]
repository_url: "https://github.com/fabiansato/weretail-dynamicsearchcard-core"
---

Exploración de un servicio Java y un servlet Sling para exponer datos JSON externos.

El repositorio organiza un núcleo Java con Maven. La implementación pública registra un servlet GET en /bin/api/searchcards que delega la consulta en un servicio OSGi y devuelve una respuesta JSON.

El foco de este laboratorio está en la comunicación entre el servlet y el servicio, y en la exposición de datos JSON. Es un punto de partida para seguir explorando integraciones en AEM.

## Tecnologías

Java, Maven, Apache Sling, OSGi, JSON.

[Explorar el código en GitHub](https://github.com/fabiansato/weretail-dynamicsearchcard-core).
