---
title: "Cómo organizo el frontend de sitios AEM para múltiples marcas"
slug: "frontend-architecture-multi-brand-aem"
date: "2026-07-10"
layout: "post"
lang: "es"
permalink: "/blog/frontend-architecture-multi-brand-aem"
translation_url: "/en/blog/frontend-architecture-multi-brand-aem"
category: "Arquitectura frontend"
category_slug: "frontend-architecture"
tags: ["Arquitectura frontend", "AEM", "Sistemas de diseño", "Clientlibs", "Temas visuales"]
excerpt: "Cuando una implementación AEM sirve a varias marcas, el frontend necesita compartir estructura y permitir identidades distintas. Esta es la arquitectura que me ha resultado útil."
description: "Arquitectura frontend para proyectos AEM multimarca: componentes compartidos, temas con design tokens y bibliotecas de cliente con responsabilidades claras."
image: "/assets/images/brand/cover-image.webp"
thumb_image: "/assets/images/brand/cover-image.webp"
author: "fabiansato"
---

Una parte importante de mi trabajo con AEM fue para organizaciones que reúnen muchas marcas en una misma plataforma. Una implementación puede sostener una docena de sitios de marca, cada uno con identidad, mercado y equipo de marketing propios, pero compartiendo el modelo de edición y el proceso de publicación. Esa condición define la manera de construir el frontend.

## Separar estructura y apariencia

La decisión central es establecer un límite claro entre *estructura* y *apariencia*. La estructura es el HTML que produce un componente y su comportamiento: un hero tiene imagen, encabezado y llamada a la acción dentro de un DOM previsible. La apariencia reúne lo que cada marca puede cambiar: colores, tipografía, ritmo del espaciado, bordes y movimiento. Si ambas cosas se mezclan, cada marca termina con una copia del componente que habrá que mantener por separado.

En la práctica, los componentes producen marcado semántico independiente de la marca, con nombres de clase estables. No llevan colores, fuentes de marca ni valores arbitrarios incorporados. El componente garantiza la estructura; el tema aporta la identidad.

## Temas mediante design tokens

Cada marca se expresa como un conjunto de design tokens: propiedades personalizadas de CSS para color, escala tipográfica, espaciado y radios. La hoja compartida consume esos tokens y evita fijar valores que una marca podría necesitar cambiar.

```css
.cmp-button {
  background: var(--color-action);
  border-radius: var(--radius-button);
  font-family: var(--font-brand);
}
```

Cambiar una página de marca pasa a ser cuestión de cargar otro conjunto de tokens, sin distribuir otro código de componentes. Esto también ayuda a revisar la capa compartida: cuando un componente no admite temas mediante tokens, puede estar señalando un problema estructural que conviene resolver.

## Bibliotecas de cliente con dependencias claras

Las client libraries de AEM son potentes y también fáciles de usar mal. En proyectos multimarca las organizo en capas: una biblioteca base con estilos iniciales y de componentes compartidos; una por marca que define tokens y ajustes propios; y bibliotecas por página solamente cuando una plantilla necesita algo adicional. Las categorías y las relaciones `embed` y `dependencies` quedan documentadas para que nadie tenga que adivinar por qué se carga un estilo.

El beneficio alcanza tanto al mantenimiento como al rendimiento. Un esquema ordenado de clientlibs permite que cada página cargue una vez la base y un tema pequeño encima, sin acumular hojas CSS superpuestas que nadie se anima a borrar.

## Un contrato de componentes para todo el equipo

Como estos sitios pasan por muchas manos —backend, frontend y equipos de contenido de distintos mercados—, el límite de un componente debe funcionar como un contrato. Documento el DOM que produce, las clases que se pueden estilizar y los tokens que respeta. Con ese acuerdo, un equipo de marca puede adaptar la apariencia sin romper otra marca, y una persona de ingeniería puede reorganizar el código interno sin afectar los temas.

## Por qué permite crecer

La arquitectura permite crecer porque la parte más costosa, la lógica y la estructura de los componentes, se escribe una vez y se comparte. Lo que cambia con frecuencia, la identidad de marca, queda aislado en tokens y bibliotecas de tema que resultan más sencillas de agregar y modificar. Incorporar una marca nueva pasa a centrarse en definir su tema.

El trabajo multimarca expone los atajos con mucha rapidez. Los equipos que tratan estructura y apariencia como responsabilidades separadas pueden mantener el ritmo durante años; los que duplican todo por marca dedican ese tiempo a sostener las copias.

Hay más ejemplos de los trabajos que dieron forma a este enfoque en mis [proyectos]({{ '/projects/' | relative_url }}). También me gusta intercambiar experiencias en [LinkedIn](https://www.linkedin.com/in/fabiangonzalezdev).
