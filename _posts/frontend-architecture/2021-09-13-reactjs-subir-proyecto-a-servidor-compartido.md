---
title: "React en hosting compartido: un tutorial del archivo"
slug: "reactjs-subir-proyecto-a-servidor-compartido"
date: "2021-09-13"
last_modified_at: "2026-10-08"
layout: "post"
lang: "es"
permalink: "/blog/reactjs-subir-proyecto-a-servidor-compartido"
translation_url: "/en/blog/reactjs-subir-proyecto-a-servidor-compartido"
category: "Arquitectura frontend"
category_slug: "frontend-architecture"
tags: ["React", "Create React App", "Apache", "Tutorial"]
excerpt: "Cómo publicar el build estático de una aplicación Create React App y revisar rutas en un hosting compartido."
description: "Tutorial histórico de 2021 para Create React App: homepage, build estático y un caso de rutas en Apache. Revisado en octubre de 2026."
image: "/assets/images/blog/reactjs-subir-a-un-server-tradicional.webp"
thumb_image: "/assets/images/blog/reactjs-subir-a-un-server-tradicional.webp"
author: "fabiansato"
archive: true
---

> **Archivo 2021 · Revisión técnica de octubre de 2026.** El uso de `homepage` y la carpeta `build` sitúa este tutorial en el flujo de **Create React App**. [React anunció su deprecación para aplicaciones nuevas en 2025](https://react.dev/blog/2025/02/14/sunsetting-create-react-app). Esta guía sirve como referencia para mantener proyectos existentes con ese sistema; otros frameworks y herramientas tienen instrucciones de despliegue propias.

## Configurar la dirección de publicación

En un proyecto Create React App, agregar `homepage` al objeto principal de `package.json` permite indicar dónde se va a publicar. Para un sitio en la raíz de un dominio, el fragmento es:

```json
{
  "homepage": "https://example.com"
}
```

Se agrega la propiedad al archivo existente, conservando sus dependencias y scripts. Su posición dentro del objeto no cambia el resultado. Si la aplicación se publica bajo una subcarpeta, la dirección debe incluirla, por ejemplo `https://example.com/mi-app`. Este comportamiento corresponde a [Create React App](https://create-react-app.dev/docs/deployment/#building-for-relative-paths).

## Generar y comprobar el resultado

Desde la carpeta del proyecto:

```console
npm run build
```

Create React App genera la carpeta `build`. Para revisarla, usar un servidor HTTP local. Por ejemplo, si `serve` está disponible en el entorno:

```console
serve -s build
```

Abrir la dirección HTTP que muestra la herramienta y comprobar la página y sus recursos. Abrir `index.html` directamente mediante `file://` no reproduce las condiciones del hosting.

## Subir los archivos

El paso original de este tutorial consiste en transferir **el contenido de `build`** al directorio público del hosting, usando el mecanismo de transferencia que ofrezca el proveedor. Los archivos y subcarpetas deben conservar su estructura.

Si faltan imágenes, CSS o JavaScript, revisar la ruta de publicación configurada y volver a generar el build. La corrección se hace en la configuración del proyecto; editar a mano los enlaces del HTML generado se perdería en la siguiente compilación.

## Caso específico: rutas de una SPA en Apache

Esta sección completa el tutorial original para un hosting que utilice **Apache 2.4** y permita configurar `mod_dir`. Si la aplicación tiene rutas del navegador, una recarga en una ruta interna necesita devolver el documento de entrada. Para una aplicación publicada en la raíz, puede configurarse en `.htaccess`:

```apache
FallbackResource /index.html
```

Apache sigue sirviendo los archivos que existen y utiliza ese documento para las solicitudes que no corresponden a un archivo. Si la aplicación vive en `/mi-app/`, el destino debe ser `/mi-app/index.html`. La posibilidad de usar esta directiva depende de los permisos y la configuración del hosting; su alcance está documentado en [Apache: FallbackResource](https://httpd.apache.org/docs/2.4/mod/mod_dir.html#fallbackresource).

También hay que ajustar la ruta base del router cuando corresponda. Probar tanto la navegación desde la portada como la recarga directa de una ruta interna ayuda a detectar esa diferencia entre el servidor de desarrollo y el hosting.
