---
title: "Componentes AEM que los equipos de contenido disfrutan usar"
slug: "designing-aem-components-authors-enjoy"
date: "2026-07-05"
layout: "post"
lang: "es"
permalink: "/blog/designing-aem-components-authors-enjoy"
translation_url: "/en/blog/designing-aem-components-authors-enjoy"
category: "AEM"
category_slug: "aem"
tags: ["AEM", "Edición de contenido", "HTL", "Sling Models", "Diseño de componentes"]
excerpt: "Un componente no está terminado cuando se renderiza, sino cuando una persona puede configurarlo sin pedir ayuda a ingeniería."
description: "Patrones prácticos para crear componentes AEM fáciles de editar: diálogos claros, valores predeterminados seguros, HTL resistente y Sling Models mantenibles."
image: "/assets/images/brand/cover-image.webp"
thumb_image: "/assets/images/brand/cover-image.webp"
author: "fabiansato"
---

La mayoría de las conversaciones sobre componentes AEM se concentra en la experiencia de desarrollo: el Sling Model, el HTL, las bibliotecas de cliente. Eso importa, pero es solo la mitad de la historia. Un componente se juega su utilidad en lo que siente el equipo de marketing o contenidos cuando abre su diálogo a las seis de la tarde, justo antes de lanzar una campaña. Después de años creando sitios de marca con AEM, aprendí que los componentes que perduran son aquellos en los que quienes editan confían.

## El diálogo es el producto

Para quien edita, el diálogo *es* el componente. Si un campo tiene una etiqueta ambigua, si una imagen obligatoria no indica qué tamaño usar o si dejar un campo vacío rompe la composición, esa persona aprende a desconfiar del componente. Esa desconfianza lleva a copiar y pegar una instancia que «funciona», y de ahí nacen páginas inconsistentes y pedidos de soporte.

Intento diseñar los diálogos como diseñaría un formulario para alguien que no conozco. Agrupar campos relacionados en pestañas o conjuntos. Escribir descripciones que respondan la pregunta real de quien edita: «Recomendado: 1440 × 600, JPG o WebP». Elegir tipos de campo adecuados en lugar de texto libre: un selector de rutas para enlaces, uno de imágenes para medios y un desplegable para las tres variantes de diseño disponibles. Cada campo de texto libre abre otra posibilidad de inconsistencia.

## Valores predeterminados seguros

Un componente debería mostrar algo razonable incluso si se agrega a una página sin configurarlo. Los campos obligatorios parecen una forma de imponer orden, pero en la práctica pueden dejar páginas a medio editar y errores de validación durante una entrega. Prefiero valores predeterminados seguros: un nivel de encabezado, una variante y un estado que indique claramente «configurame» en lugar de una caja rota.

Ahí es donde Sling Models aporta valor. La lógica de decisión pertenece al modelo, no al HTL. Calcular el valor efectivo —el configurado o su alternativa— y exponer un único getter claro mantiene el HTL declarativo y legible. Además, permite verificar ese comportamiento mediante pruebas unitarias.

```java
public String getHeadingLevel() {
    return StringUtils.defaultIfBlank(headingLevel, "h2");
}
```

## HTL que tolera datos incompletos

El HTL debe contemplar que pueden faltar datos. Proteger los bloques opcionales con `data-sly-test`, no suponer que una lista tiene elementos y evitar que un campo sin configurar produzca una etiqueta vacía que desarme la composición. La idea es que un componente parcialmente editado siga teniendo una presentación cuidada.

```html
<sly data-sly-test="${model.image}">
  <img class="cmp-hero__img" src="${model.image.src}" alt="${model.image.alt}"/>
</sly>
```

La condición `data-sly-test` es pequeña, pero puede marcar la diferencia entre un estado vacío bien resuelto y una llamada de soporte.

## Modelar el contenido

Los componentes más reutilizables describen *qué* es el contenido, sin quedar atados a la apariencia de este trimestre. Un hero que tiene un tratamiento de fondo fijo se duplicará en cuanto una marca quiera algo distinto. Uno que expone una variante y algunos espacios de contenido puede sobrevivir a un rediseño. Cuando un campo existe solamente para resolver la composición visual del momento, suele ser una señal de que esa decisión pertenece a los estilos y no al diálogo.

## Una buena experiencia de edición facilita el mantenimiento

Hay una coincidencia útil: las decisiones que hacen agradable editar un componente —límites claros, valores seguros, renderizado resistente y lógica en modelos verificables— también facilitan su mantenimiento para la próxima persona que trabaje en el código. Al pensar en quien configura el componente, suele aparecer un código más claro.

Diseñar para esa persona que abre el diálogo bajo presión beneficia a ambos lados del equipo.

Podés ver algunos de los trabajos de marca detrás de estas ideas en mis [proyectos]({{ '/projects/' | relative_url }}), o conectar conmigo en [LinkedIn](https://www.linkedin.com/in/fabiangonzalezdev).
