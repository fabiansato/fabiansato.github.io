# Mantenimiento del portfolio / Portfolio maintenance

## Ejecutar y verificar

La versión de Ruby se declara en `.ruby-version` y las dependencias exactas en `Gemfile.lock`. Usar un gestor de Ruby que respete esa versión; el Ruby 2.6 incluido en macOS no sirve para este proyecto.

```sh
gem install bundler -v 2.6.9
bin/setup
bin/serve
bin/check
```

`bin/setup` instala las gemas dentro de `vendor/bundle`. `bin/serve` abre un servidor local en `127.0.0.1:4000` con recarga; se puede cambiar el puerto con `PORT=4001 bin/serve`. Reiniciar el servidor al cambiar `_config.yml`.

`bin/check` compila con `JEKYLL_ENV=production`, falla ante front matter inválido y revisa el HTML generado: destinos locales, anclas, pares de idioma y XML. Usa Python 3.9+ de la máquina; no descarga paquetes de Python ni consulta servicios externos. No comprueba la disponibilidad actual de sitios de terceros.

## Dónde editar

| Contenido | Ubicación |
| --- | --- |
| Dominio, colecciones y plugins | `_config.yml` |
| Textos de la interfaz en español e inglés | `_data/i18n.json` |
| Datos generales y enlaces del autor | `_data/settings.yml` |
| Estructura y componentes | `_layouts/`, `_includes/` |
| Páginas de presentación | `_pages/` |
| Proyectos | `_projects/` y `_projects/en/` |
| Artículos | `_posts/`, agrupados por categoría o idioma |
| Imágenes y documentos públicos | `assets/` |
| Compilación y publicación | `.github/workflows/pages.yml`, `bin/` |

## Dos idiomas, dos páginas completas

Español vive en `/`; inglés en `/en/`. Cada página de contenido tiene `lang`, un `permalink` explícito y `translation_url` que apunta a la otra versión. Las traducciones deben apuntarse mutuamente. Mantener los slugs publicados evita romper enlaces existentes.

Ejemplo de proyecto en español:

```yaml
---
title: "Nombre del proyecto"
slug: "nombre-del-proyecto"
date: "2026-10-08"
layout: project
lang: es
permalink: /project/nombre-del-proyecto
translation_url: /en/project/nombre-del-proyecto
group: lab
year: "2026"
featured: false
order: 50
subtitle: "Laboratorio · Una breve idea"
description: "Qué hace el proyecto y cuál fue mi participación."
technologies: [TypeScript, React]
repository_url: https://github.com/fabiansato/nombre-del-proyecto
---
```

Crear la pareja en `_projects/en/`, traducir el título, subtítulo, descripción y cuerpo, cambiar `lang` a `en` e intercambiar ambas rutas. Usar `group: client` para trabajos de clientes y `group: lab` para laboratorios. Referenciar imágenes reales que existan dentro de `assets/`; no inventar resultados, clientes, métricas o tecnologías.

Para artículos, el nombre del archivo empieza por `YYYY-MM-DD-`. Usar `layout: post`, la pareja de rutas `/blog/slug` y `/en/blog/slug`, y traducir también `excerpt`, `description`, categorías legibles y texto alternativo de imágenes. Ver un artículo existente para los campos de categoría que utiliza el listado. Mantener el mismo `category_slug` y el mismo orden cronológico en ambas versiones.

Los listados se generan con Jekyll. La búsqueda y los filtros funcionan como mejora en el navegador: el contenido debe seguir siendo accesible sin JavaScript. Los feeds y metadatos deben enlazar con el mismo idioma de la página.

## Imágenes y enlaces históricos

Las capturas representan la versión del trabajo documentada, no necesariamente el sitio actual de la marca. Un dominio puede seguir activo aunque el trabajo original haya cambiado. Antes de añadir un botón externo, comprobar que el enlace lleva al trabajo o a una referencia pertinente. Los repositorios de laboratorio son el respaldo de sus descripciones técnicas.

Preferir WebP, dimensiones explícitas y texto alternativo que describa el contenido. Los recursos públicos no deben incluir secretos ni código de proyectos privados. Para rutas locales en Liquid usar `relative_url`; para URL canónica y feeds usar `absolute_url`.

## Publicar

1. Ejecutar `bin/check` y revisar la vista local en móvil y escritorio, en ambos idiomas.
2. Revisar el diff y abrir un PR. El workflow construye y valida sin publicar desde el PR.
3. En **Settings → Pages → Build and deployment**, elegir **GitHub Actions** como fuente.
4. Integrar el cambio en `main`; el workflow sube `_site/` y despliega ese artefacto a Pages.
5. Confirmar el resultado del job `deploy` y revisar `/`, `/en/`, proyectos, blog, selector de idioma, sitemap y feeds en el dominio final.

`workflow_dispatch` permite volver a ejecutar el workflow, pero solo publica si se ejecuta sobre `main`. Los permisos `pages: write` e `id-token: write` están limitados al job de publicación. Las acciones se fijan por SHA; al actualizarlas, verificar sus revisiones oficiales.

No mantener otro workflow de Pages en paralelo. No usar el generador legacy de Pages: compilaría con un conjunto de dependencias distinto del probado aquí.

## English quick reference

Use Ruby from `.ruby-version`, Bundler from `Gemfile.lock` and Python 3.9+. Run `bin/setup`, then `bin/serve`; run `bin/check` before publishing. Generated `_site/` files and `vendor/bundle/` are local output.

Spanish content uses `/`; English uses `/en/`. Create complete translated pairs with `lang`, explicit `permalink` and reciprocal `translation_url` values. Translate titles, descriptions, excerpts, body copy and image descriptions. Keep established public slugs. UI translations live in `_data/i18n.json`; author data lives in `_data/settings.yml`.

Add projects to `_projects/` and `_projects/en/`, with `group: client` or `group: lab`. Dated Markdown articles live in `_posts/`. Describe only work supported by the project sources; historical screenshots may differ from current brand websites.

Pull requests build and validate without deploying. Set **Settings → Pages → Build and deployment → Source** to **GitHub Actions**, then merge into `main` to publish. Review both languages and the deployment result. Keep the single Pages workflow and update its pinned action revisions deliberately.
