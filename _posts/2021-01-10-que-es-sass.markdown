---
title: '¿Qué es Sass? Y como usarlo fácilmente '
date: '2021-09-13'
layout: post
tag: [tutorial, Sass, Curso, CSS]
excerpt: >-
  En esta pagina veremos como usar completamente sass. Instalarlo en cualquier proyecto y poder usarlo de manera eficiente
description: >-
  El operador ternario es aquel que nos sirve para escribir el código de una sentencia if de una forma más sencilla. Veremos como hacerlo
image: '/images/blog/que-es-sass.png'
thumb_image: '/images/blog/que-es-sass.png'
style: code
author: fabiansato
---

### ¿Qué es SASS?

Sass es un preprocesador CSS es una herramienta que nos permite generar, de manera automática, hojas de estilo, añadiéndoles características que no tiene CSS, y que son propias de los lenguajes de programación, como pueden ser variables, funciones, selectores anidados, herencia, etcétera.

Estas características de los procesadores nos permiten, además, que el CSS que se genera sea más fácil de mantener y más reutilizable.

## ventajas
Ventajas de utilizar Sass


    Reduce el tiempo para crear y mantener el CSS.

    Permite tener una organización modular de los estilos, lo cual es vital para proyectos grandes.

    Proporciona estructuras avanzadas propias de los lenguajes de programación, como variables, listas, funciones y estructuras de control.

    Permite generar distintos tipos de salida, comprimida, normal o minimizada, trabajando tanto en desarrollo como en producción, además se hace una forma muy fácil.

    Permite vigilar los ficheros, de tal manera que, si ha habido un cambio en la hoja de estilos, se regenera automáticamente (modo watch).

    Tiene muy pocas dependencias, sobre todo la nueva versión, que es dart-sass. En las anteriores versiones se dependía de muchas librerías de Ruby y era un poco engorroso de instalar, pero con la nueva versión, la instalación es muy fácil.

    Existen muchas herramientas asociadas, muchas librerías hechas con Sass y una comunidad muy importante de usuarios.


## Instalación

Primero Antes que nada debemos ir a la página oficial de sass:
´´´
https://sass-lang.com/install´
´´´

Para poder tener sass globalmente en nuestra máquina con windows debemos hacer lo siguiente:
Instalar ruby installer en windows

Instalaremos sass en nuestro proyecto
´´´
gem install sass
´´´

luego tipearemos
´´´
sass -v
´´´

para verificar si se isntaló sass correctamente. Esto se instala a nivel global


Allí veremos que existen dos formas de instalarlo mediante aplicacións o por la línea de comandos para nuestro proyecto de html completo.

### Agregar nuestro sass a nuestro proyecto ReactJS:
Si bien reactjs posee un compilador interno de sass, nunca está de más poder agregarlo dentro de nuestro proyecto ya existente de la siguiente manera:
´´´
npm i sass
´´´