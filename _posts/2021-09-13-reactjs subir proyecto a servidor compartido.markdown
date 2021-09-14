---
title: 'ReactJS - Subir tu proyecto ReactJS a un servidor compartido (server tradicional)'
date: '2021-09-13'
layout: post
tag: [tutorial, WebDev, ReactJS]
excerpt: >-
  En este simple tutorial aprenderemos a subir nuestro proyecto ReactJS a un servidor compartido
description: >-
  En este simple tutorial aprenderemos a subir nuestro proyecto ReactJS a un servidor compartido
image: '/images/blog/reactjs-subir-a-un-server-tradicional.jpg'
thumb_image: '/images/blog/reactjs-subir-a-un-server-tradicional.jpg'
style: code
author: fabiansato
---

## Introducción
En este simple tutorial aprenderemos a subir nuestro proyecto ReactJS a un servidor compartido

## Manos a la obra!
Simplemente vamos a nuestro package.json y agregamos el siguiente atributo:

```json
"homepage": "https://nombredenuestrodominio"
```


El mejor lugar para colocarlo es arriba de "scripts"


Una vez hecho esto hacemos en el terminal:

```console
npm run build
```

Podemos encontrar todo nuestro proyecto en la carpeta `build` entramos a la misma y abrimos el archivo `index.html` para testear que se vé nuestro proyecto completo.

Si este problema persiste podemos agregar:

```json
"homepage": "/"
```



`Tip si persiste el error`: Si seguimos sin ver nuestra web abrimos el archivo `index.html` dentro de la carpeta `build` y cambiamos todas las url internas en el archivo html por alguna externa (donde ya tengamos el ftp subido) y eo soluciona todo

Una vez que vemos que todo el proyecto funciona correctamente sólo nos queda subir el proyecto a una web tradicional compartida con ftp.

¡Listo!
¡Espero que el tutorial te sirva!