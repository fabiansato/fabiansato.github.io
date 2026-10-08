---
title: "Core Web Vitals en AEM: los cambios que más se notan"
slug: "core-web-vitals-enterprise-aem"
date: "2026-07-15"
layout: "post"
lang: "es"
permalink: "/blog/core-web-vitals-enterprise-aem"
translation_url: "/en/blog/core-web-vitals-enterprise-aem"
category: "Rendimiento"
category_slug: "performance"
tags: ["Rendimiento", "Core Web Vitals", "AEM", "LCP", "CLS"]
excerpt: "En sitios AEM grandes, las mejoras más útiles suelen estar en imágenes, fuentes, scripts externos y estabilidad visual."
description: "Mejoras prácticas de Core Web Vitals en AEM: imágenes para LCP, carga de fuentes, espacio reservado para evitar CLS y revisión de scripts de terceros."
image: "/assets/images/brand/cover-image.webp"
thumb_image: "/assets/images/brand/cover-image.webp"
author: "fabiansato"
---

Los sitios empresariales en AEM suelen tener problemas de Core Web Vitals bastante previsibles. Casi nunca se trata de optimizar un algoritmo sofisticado: suele ser una imagen principal enviada a resolución completa, una fuente que bloquea el texto o una etiqueta de marketing que llega tarde y mueve la página. La ventaja es que los problemas repetidos permiten aplicar soluciones conocidas.

## Largest Contentful Paint suele llevarnos a las imágenes

En muchas páginas de marca, el elemento LCP es la imagen principal. Ahí conviene empezar. Las mejoras son concretas: formatos modernos como WebP o AVIF, tamaños adaptados al ancho de pantalla en lugar de un archivo enorme para todos los teléfonos y prioridad alta para la imagen principal, junto con carga diferida de las imágenes que quedan debajo de la primera pantalla.

```html
<img src="hero.webp" fetchpriority="high" width="1440" height="600" alt="...">
```

`fetchpriority="high"` indica una prioridad de carga alta. Los atributos `width` y `height` reservan espacio antes de que llegue la imagen y ayudan a mantener estable la composición. En AEM, esto se resuelve con variantes de imagen adaptables y valores predeterminados coherentes en los componentes, sin dejar cada decisión a quien carga el contenido.

## Las fuentes pueden demorar el texto

Las fuentes de marca pueden introducir una demora de LCP difícil de advertir. Según su configuración, una fuente sin `font-display: swap` puede ocultar texto mientras carga. Precargar solamente los archivos críticos y permitir que el texto aparezca primero con una fuente alternativa ayuda a reducir esa espera. También conviene ajustar esa alternativa para limitar los cambios de composición durante el reemplazo. Reducir la fuente a los caracteres necesarios es otra opción cuando hace falta seguir optimizando.

## Cumulative Layout Shift exige constancia

Los movimientos de contenido rara vez vienen de un único error. Se acumulan pequeñas omisiones: imágenes sin dimensiones, espacios publicitarios y elementos incrustados sin altura reservada, contenido que un script agrega después del primer renderizado. La solución requiere un hábito: reservar espacio para lo que carga de forma asíncrona. Dar dimensiones a los medios, una altura mínima a los componentes insertados y evitar que un banner tardío desplace un artículo que alguien ya empezó a leer.

## Los scripts de terceros también tienen un costo

Las conversaciones más difíciles sobre rendimiento suelen involucrar etiquetas de analítica, personalización, pruebas A/B, chat y consentimiento. Cada una se agrega por una razón, pero juntas pueden ocupar gran parte del hilo principal. Trato su presupuesto como una restricción del proyecto: cargar lo necesario, diferir lo que no es crítico para el primer renderizado y revisar periódicamente qué se ejecuta. Una etiqueta que ya no utiliza ninguna campaña sigue teniendo costo.

## Medir la experiencia real

Lighthouse en un entorno de laboratorio controlado aporta una señal útil, pero Core Web Vitals también requiere observar datos de campo. Las personas usan teléfonos de gama media y conexiones imperfectas. Reviso fuentes como Chrome UX Report y monitoreo de usuarios reales porque permiten detectar regresiones que una prueba de laboratorio podría ocultar: un script de personalización que aparece solo al iniciar sesión o una región alejada del nodo de la CDN.

No son técnicas exóticas. En AEM empresarial, gran parte del trabajo consiste en aplicar bien y de forma constante medidas conocidas: imágenes del tamaño adecuado, una carga cuidada de fuentes, espacio reservado y control de terceros. Son una base sólida para mejorar la experiencia, que después hay que comprobar con mediciones.

Si querés conversar sobre cómo aplicar estas ideas en un proyecto, me encontrás en [LinkedIn](https://www.linkedin.com/in/fabiangonzalezdev).
