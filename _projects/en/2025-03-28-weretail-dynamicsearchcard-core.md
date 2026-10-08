---
title: "We.Retail · Dynamic Search Card Core"
slug: "weretail-dynamicsearchcard-core"
date: "2025-03-28"
layout: "project"
lang: "en"
permalink: "/en/project/weretail-dynamicsearchcard-core"
translation_url: "/project/weretail-dynamicsearchcard-core"
group: "lab"
year: "2025"
featured: false
order: 8
subtitle: "Lab · Java and AEM"
description: "An exploration of a Java service and Sling servlet for exposing external JSON data."
technologies: ["Java", "Maven", "Apache Sling", "OSGi", "JSON"]
repository_url: "https://github.com/fabiansato/weretail-dynamicsearchcard-core"
---

An exploration of a Java service and Sling servlet for exposing external JSON data.

The repository organises a Java core with Maven. The public implementation registers a GET servlet at /bin/api/searchcards, delegates the request to an OSGi service and returns a JSON response.

This lab focuses on communication between the servlet and the service, and on exposing JSON data. It is a starting point for further exploration of AEM integrations.

## Technologies

Java, Maven, Apache Sling, OSGi, JSON.

[Explore the code on GitHub](https://github.com/fabiansato/weretail-dynamicsearchcard-core).
