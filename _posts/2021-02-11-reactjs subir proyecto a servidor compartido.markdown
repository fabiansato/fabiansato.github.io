---
layout: post
title:  ReactJS - Subir a un server compartido
date:   2021-02-11 15:05:55 -0300
image:  /assets/images/blog/javascript-operadores-ternarios.jpg
author: fabiansato
tags:   nodejs
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
