---
title: 'Javascript - Operadores Ternarios'
date: '2021-09-13'
layout: post
tag: [tutorial, WebDev, Javascipt]
excerpt: >-
  El operador ternario es aquel que nos sirve para escribir el código de una sentencia if de una forma más sencilla. Veremos como hacerlo
description: >-
  El operador ternario es aquel que nos sirve para escribir el código de una sentencia if de una forma más sencilla. Veremos como hacerlo
image: '/images/blog/javascript-operadores-ternarios.png'
thumb_image: '/images/blog/javascript-operadores-ternarios.png'
page.image: '/images/blog/javascript-operadores-ternarios.png'
style: code
author: fabiansato
---

## Introducción
El operador ternario es aquel que nos sirve para escribir el código de una sentencia if de una forma más sencilla. Imaginemos que tenemos un ejemplo que nos calcula cuál es el mayor de dos número en Javascript. El código sería sencillo como comprobamos a continuación.

## Manos a la obra!
Miremos como tradicionalmente cargaríamos una variable y la evaluaríamos con un `if` y un `else`
```javascript
var x = 10;
var y = 8;

if (x>y)
  document.write("El mayor de los dos números es " + x);
else
  document.write("El mayor de los dos números es " + y);
```

Vemos que tenemos una estructura de control if que ejecuta una sentencia en caso de que la validación correcta y la sentencia else en el caso de que la validación de if sea incorrecta. El operador ternario en Javascript nos permite hacer esto en una sola línea de código.

La estructura del operador tenernario es la siguiente:
```javascript
resultado = (condicion)?valor1:valor2;
```

Si la condición es verdadera se asigna el valor1 como resultado, en caso contrario se asigna el valor2. Vemos que el operador ternario se representa mediante una interrogación ? y dos puntos :

Para realizar el código del mayor de dos número escribiremos las siguientes sentencias de código Javascript.

```javascript
mayor = (x>y)?x:y;
document.write("El mayor de los dos números es " + mayor);


```

Vemos que la cantidad de código Javascript a escribir es menor que cuando utilizábamos la estructura de control if

> Con el operador dernario podremos visualizar nuestro código de mas limpio y ejecutar condicionales if en una sóla línea

Les dejo un video explicando como funciona el markdown en nuestro código Javascript:
<iframe width="480" height="215" src="https://www.youtube.com/embed/ww0Pl8-mMng" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>