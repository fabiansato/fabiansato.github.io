---
title: "JavaScript: operadores ternarios"
slug: "javascript-operadores-ternarios"
date: "2021-10-03"
last_modified_at: "2026-10-08"
layout: "post"
lang: "es"
permalink: "/blog/javascript-operadores-ternarios"
translation_url: "/en/blog/javascript-operadores-ternarios"
category: "Arquitectura frontend"
category_slug: "frontend-architecture"
tags: ["JavaScript", "Tutorial"]
excerpt: "Cómo elegir entre dos valores con el operador condicional de JavaScript, a partir de un ejemplo sencillo."
description: "Tutorial del archivo 2021: comparación entre if/else y el operador ternario, con ejemplos actualizados a const y console.log."
image: "/assets/images/blog/javascript-operadores-ternarios.webp"
thumb_image: "/assets/images/blog/javascript-operadores-ternarios.webp"
author: "fabiansato"
archive: true
---

> **Archivo 2021 · Ejemplos revisados en octubre de 2026.** Se conserva el ejercicio original y se actualiza su escritura con `const` y `console.log`.

## Introducción

El operador condicional, también llamado ternario, permite elegir entre dos valores a partir de una condición. Tiene tres partes: la condición, el valor que corresponde cuando se cumple y el valor que corresponde cuando no se cumple. La [referencia de JavaScript en MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) describe su sintaxis y evaluación.

El ejemplo de este tutorial compara dos números para mostrar el mayor.

## Primero, con if y else

```javascript
const x = 10;
const y = 8;

if (x > y) {
  console.log("El mayor de los dos números es " + x);
} else {
  console.log("El mayor de los dos números es " + y);
}
```

Si `x > y` es verdadero, se ejecuta el primer bloque. En caso contrario se ejecuta el segundo. Con estos valores, la consola muestra `El mayor de los dos números es 10`.

## La estructura del operador ternario

```javascript
const resultado = condicion ? valor1 : valor2;
```

Este fragmento representa la estructura general: `condicion`, `valor1` y `valor2` deben existir en el programa. El signo `?` separa la condición del primer valor y `:` introduce la alternativa. Si la condición se evalúa como verdadera, el resultado es `valor1`; si se evalúa como falsa, es `valor2`. Solo se evalúa la rama elegida.

## El mismo ejercicio con un ternario

```javascript
const x = 10;
const y = 8;
const mayor = x > y ? x : y;

console.log("El mayor de los dos números es " + mayor);
```

La comparación selecciona un número y lo guarda en `mayor`. El mensaje queda separado de la decisión, y el resultado es el mismo que en el ejemplo con `if` y `else`. Si los números son iguales, se elige `y`, cuyo valor también es igual al de `x`.

En este caso se reduce el código necesario para obtener un valor. El objetivo del ejercicio es reconocer esa equivalencia, sin cambiar el resultado del programa.

## Material de la publicación original

La entrada de 2021 incluía [este video de acompañamiento](https://www.youtube.com/watch?v=ww0Pl8-mMng). El ejemplo escrito de esta página conserva el ejercicio y usa la consola del navegador o de Node.js para mostrar el resultado.
