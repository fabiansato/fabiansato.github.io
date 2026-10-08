# Fabián Sato · Portfolio & blog

Un espacio para presentar mi trabajo, compartir lo que aprendo y conectar diseño, código y contenido. Construido con **Jekyll**, con versiones completas en **español e inglés**.

**[Español](https://fabiansato.github.io/)** · **[English](https://fabiansato.github.io/en/)** · **[Trabajos / Work](https://fabiansato.github.io/projects/)** · **[Blog](https://fabiansato.github.io/blog/)**

## Español

Este repositorio contiene el sitio web de `fabiansato.github.io`. El README que aparece en el perfil de GitHub se mantiene por separado en [`fabiansato/fabiansato`](https://github.com/fabiansato/fabiansato).

La renovación reúne proyectos de clientes, campañas históricas y laboratorios de código abierto. Conserva Jekyll y los contenidos recuperados del portfolio anterior, con una presentación nueva, navegación bilingüe, fichas de trabajo, búsqueda en el blog y feeds RSS por idioma.

### Desarrollo local

Requisitos: **Ruby 3.4.11**, Bundler y **Python 3.9+** para la comprobación de enlaces.

```sh
gem install bundler -v 2.6.9
bin/setup
bin/serve
```

Abrir <http://127.0.0.1:4000>. La versión inglesa está en `/en/`.

```sh
bin/check # Compilación de producción, enlaces locales, anclas, idiomas y XML
```

Las versiones exactas de las gemas se mantienen en `Gemfile.lock`. El sitio generado queda en `_site/`; no se edita ni se sube al repositorio.

### Publicación y mantenimiento

El único workflow, `.github/workflows/pages.yml`, valida los PR y publica únicamente desde `main`. GitHub Pages debe usar **GitHub Actions** como fuente de publicación.

- [Guía de mantenimiento y contenido](docs/README.md)
- [Fuentes, decisiones y pasos de migración](docs/migration.md)

## English

This repository contains the `fabiansato.github.io` website. The GitHub profile README is maintained separately in [`fabiansato/fabiansato`](https://github.com/fabiansato/fabiansato).

The renewed portfolio brings together client work, historical campaigns and open-source experiments. It keeps Jekyll and the recovered portfolio content, with a new introduction, bilingual navigation, project pages, blog search and language-specific RSS feeds.

### Local development

Requirements: **Ruby 3.4.11**, Bundler and **Python 3.9+** for link validation.

```sh
gem install bundler -v 2.6.9
bin/setup
bin/serve
```

Open <http://127.0.0.1:4000/en/> for the English version. Run `bin/check` before publishing: it builds the production site and checks local links, anchors, language alternatives and XML files.

Exact gem versions are committed in `Gemfile.lock`. Generated files live in `_site/`; do not edit or commit them.

### Publishing and maintenance

The single workflow, `.github/workflows/pages.yml`, validates pull requests and only deploys `main`. Set the GitHub Pages publishing source to **GitHub Actions** before the first deployment.

See the [maintenance guide](docs/README.md) and the [migration record](docs/migration.md) for content conventions, audited sources and deployment steps.
