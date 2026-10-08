# Migración a fabiansato / Migration record

Fecha de revisión: **8 de octubre de 2026**.

## Destinos

- Sitio: [`fabiansato/fabiansato.github.io`](https://github.com/fabiansato/fabiansato.github.io), rama `main`, URL prevista `https://fabiansato.github.io/`.
- Presentación de GitHub: [`fabiansato/fabiansato`](https://github.com/fabiansato/fabiansato), rama `master`. GitHub utiliza el README del repositorio cuyo nombre coincide con el usuario.

Son repositorios distintos: publicar el sitio no actualiza automáticamente la presentación del perfil.

## Fuentes auditadas

La revisión del contenido y de los repositorios históricos recuperó la base del sitio y sus recursos. Las referencias de partida son:

| Fuente | Evidencia y uso |
| --- | --- |
| [`fabiansato/fabiangonzalezdev.github.io`](https://github.com/fabiansato/fabiangonzalezdev.github.io), HEAD `85fcb4f` | Fuente principal de Jekyll, experiencia, proyectos y artículos recientes. |
| [`fabiansato/fabiangonzalezdev`](https://github.com/fabiansato/fabiangonzalezdev) | Presentación previa del perfil, consultada para conservar el recorrido profesional. |
| `fabiansatojekyll` y recursos del sitio destino | Recuperación de imágenes históricas: 56 archivos WebP disponibles; 44 referencias `/images` de la fuente no resolvían. |
| Proyectos NCO, Quadama y Hellmann’s Burger | Trabajos recuperados de versiones anteriores del portfolio. |
| Repositorios públicos Lighthouse, CartaTienda, WeRetail, MIMO-FE y Kit Maestro | Verificación de código y README para describir los nuevos laboratorios sin atribuir capacidades no demostradas. |
| `fabiansatoshi` | Plantilla descartada como fuente editorial porque contenía texto de muestra. |
| Backend PHP privado | Revisado como contexto; no se trasladó su código al sitio público. |

Los repositorios destino se comprobaron antes de trabajar: perfil `f310a19669aaae73e39b0ef77ccd78923b2304aa`; sitio `2ae5a84f45edf73477f30a1ee7b7b13e485d7421`. Estas referencias identifican el punto de partida, no la revisión final que se publique.

## Decisiones

- Mantener **Jekyll**, Markdown y GitHub Pages. La renovación no requiere un backend ni un framework de aplicación.
- Usar español como idioma de entrada y versiones completas en inglés bajo `/en/`.
- Conservar slugs históricos de fichas y artículos, con navegación explícita a su traducción.
- Separar trabajos de clientes de laboratorios y enlazar los repositorios que respaldan cada descripción.
- Mantener las imágenes recuperadas como registro histórico de las versiones documentadas.
- Recuperar los dos tutoriales originales de 2021 del sitio destino, preservar sus permalinks y añadir traducciones completas con revisión técnica explícita.
- Resultado editorial: 40 proyectos y 6 artículos por idioma.
- Reemplazar los workflows duplicados por uno que valida PR y publica solo `main`.
- Retirar `jekyll-paginate` y `jekyll-tagging`; los listados se generan con Liquid y se filtran progresivamente en el navegador. El plugin de sitemap se conserva y el RSS se genera mediante plantillas del sitio.
- Fijar Ruby **3.4.11**, Jekyll **4.4.1** y Bundler **2.6.9**, con un lockfile resuelto realmente para macOS ARM y Linux.

La compilación sigue el propósito de la skill `verify-build` del repositorio fuente: verificar Jekyll y su contenido antes de publicar. Su instrucción antigua sobre páginas individuales de categorías queda reemplazada por la navegación de categorías del nuevo listado.

## Paso necesario en GitHub Pages

Pages utilizaba el modo **legacy**, rama `main`, carpeta `/`. El 8 de octubre de 2026 se cambió a **GitHub Actions** mediante la API de GitHub. El workflow de `main` compila con el lockfile y publica el artefacto generado. La primera versión renovada se verificó en el dominio público.

Para próximas actualizaciones, confirmar el resultado en Actions y en el dominio final. Los cambios en PR se validan, pero no se publican hasta integrar en `main`.

El hostname antiguo `fabiangonzalezdev.github.io` depende del usuario anterior y de GitHub. Este repositorio no puede garantizar una redirección desde ese dominio. Los enlaces y las URL canónicas nuevos apuntan a `fabiansato.github.io`.

## Verificación y entorno local

La compilación real y `bin/check` pasaron con Ruby 3.4.11 y Jekyll 4.4.1: **115 páginas HTML**, enlaces locales, anclas, alternativas ES/EN y **3 archivos XML** válidos. La página bilingüe 404 y la entrada histórica `/about` se comprueban como rutas especiales sin exigirles una pareja de traducción; el archivo de verificación de Google se reconoce por su contenido exacto.

El equipo de trabajo tenía Ruby 2.6 del sistema; se descargó el runtime oficial de `ruby/ruby-builder` y se reubicó en un directorio temporal, junto con las bibliotecas GMP/YAML de Homebrew. No se reemplazó Ruby del sistema.

Ese runtime temporal es una comodidad de esta sesión, no una dependencia del repositorio. Para nuevas máquinas usar la versión de `.ruby-version` con un gestor de Ruby. En CI, `ruby/setup-ruby` instala la misma versión. `bin/check` es el comando reproducible de validación final; la inspección visual complementa la verificación automatizada.

Referencias oficiales consultadas: [Ruby releases](https://www.ruby-lang.org/en/news/), [Ruby builder](https://github.com/ruby/ruby-builder), [Jekyll 4.4.1](https://rubygems.org/gems/jekyll/versions/4.4.1), [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## English

This migration keeps Jekyll and GitHub Pages, restores historical project assets, adds evidence-backed public repositories and introduces complete Spanish/English content pairs. The old Jekyll repository at `85fcb4f` is the primary content source; previous local portfolios supplied missing screenshots and recovered work. Placeholder copy and private backend code were not migrated.

The website and GitHub profile README remain separate repositories. Spanish is served at `/`, English at `/en/`. The new build uses Ruby 3.4.11, Jekyll 4.4.1 and a generated dependency lockfile. A single workflow validates PRs and deploys only `main`.

GitHub Pages was switched from legacy `main`/root mode to **GitHub Actions** on October 8, 2026. The first renewed version was verified on the public domain. For later changes, check the completed workflow and final domain. Redirecting the former username’s hostname is outside this repository’s control.
