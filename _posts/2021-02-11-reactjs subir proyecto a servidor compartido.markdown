---
title: 'ReactJS - Subir proyecto a servidor compartido'
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

**En este simple tutorial aprenderemos a subir nuestro proyecto ReactJS a un servidor compartido**

Simplemente vamos a nuestro package.json y agregamos un atributo (ponerlo arriba de scripts )

<pre>
<code data-language="json">
"homepage": "https://nombredenuestrodominio"
</pre>
</code>

Una vez hecho esto hacemos en el terminal
<pre>
<code data-language="javascript">
npm run build
```
</pre>
</code>

una vez hecho eso tenemos que subir nuestro proyecto 
