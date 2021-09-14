---
title: 'Javascript - Operadores ternarios'
date: '2018-12-15'
layout: post
author: fabiansato
tag: [tutorial, WebDev, JavaScript]
excerpt: >-
  In this tutorial we'll be building off of the previous tutorial updating our form to make our first HTTP request to the PokéAPI.
description: >-
  In this tutorial we'll be building off of the previous tutorial updating our form to make our first HTTP request to the PokéAPI.
image: '/images/ajax/tutorial-cover.png'
thumb_image: '/images/ajax/tutorial-cover.png'
style: code
---

**El operador ternario es aquel que nos sirve para escribir el código de una sentencia if de una forma más sencilla. Veremos como hacerlo**

El operador ternario es aquel que nos sirve para escribir el código de una sentencia if de una forma más sencilla. Imaginemos que tenemos un ejemplo que nos calcula cuál es el mayor de dos número en Javascript. El código sería sencillo como comprobamos a continuación.

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

Vemos que la cantidad de código Javascript a escribir es menor que cuando utilizábamos la estructura de control if
```

> Con el operador dernario podremos visualizar nuestro código de mas limpio y rápidaente

Les dejo un video explicando como funciona el markdown en nuestro código Javascript:
[![Operadores ternarios javascript](https://youtu.be/ww0Pl8-mMng)

<pre><code data-language="python">def openFile(path):
    file = open(path, "r")
    content = file.read()
    file.close()
    return content</code></pre>



    <pre>
<code data-language="javascript">window.Rainbow = {
    whatever: function(param) {

    },

    another: function(param) {

    }
};</code>
</pre>

<pre>
<code data-language="javascript">window.Rainbow = window.Rainbow || {};

Rainbow.extend('javascript', [
    {
        'name': 'selector',
        'pattern': /\$(?=\.|\()/g
    }
]);</code>
</pre>

<pre>
<code data-language="javascript">/**
 * cross browser get attribute for an element
 *
 * @see http://stackoverflow.com/questions/3755227/cross-browser-javascript-getattribute-method
 *
 * @param {Element} el
 * @param {string} attr     attribute you are trying to get
 * @returns {string}
 */
function _attr(el, attr) {
    var result = (el.getAttribute &amp;&amp; el.getAttribute(attr)) || null;

    if (!result) {
        var attrs = el.attributes,
            length = attrs.length,
            i;

        for (i = 0; i &lt; length; ++i) {
            if (attr[i].nodeName === attr) {
                result = attr[i].nodeValue;
            }
        }
    }

    return result;
}</code>
</pre>