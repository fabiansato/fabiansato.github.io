---
title: "React on shared hosting: a tutorial from the archive"
slug: "reactjs-subir-proyecto-a-servidor-compartido"
date: "2021-09-13"
last_modified_at: "2026-10-08"
layout: "post"
lang: "en"
permalink: "/en/blog/reactjs-subir-proyecto-a-servidor-compartido"
translation_url: "/blog/reactjs-subir-proyecto-a-servidor-compartido"
category: "Frontend Architecture"
category_slug: "frontend-architecture"
tags: ["React", "Create React App", "Apache", "Tutorial"]
excerpt: "How to publish a Create React App static build and check routes on shared hosting."
description: "A historical 2021 Create React App tutorial covering homepage, a static build and Apache routing. Reviewed in October 2026."
image: "/assets/images/blog/reactjs-subir-a-un-server-tradicional.webp"
thumb_image: "/assets/images/blog/reactjs-subir-a-un-server-tradicional.webp"
author: "fabiansato"
archive: true
---

> **2021 archive · Technical review in October 2026.** The use of `homepage` and the `build` directory places this tutorial in the **Create React App** workflow. [React announced its deprecation for new applications in 2025](https://react.dev/blog/2025/02/14/sunsetting-create-react-app). This guide is a reference for maintaining existing projects using that system; other frameworks and tools have their own deployment instructions.

## Configure the deployment address

In a Create React App project, adding `homepage` to the top-level `package.json` object specifies the deployment location. For a website at the root of a domain, the fragment is:

```json
{
  "homepage": "https://example.com"
}
```

Add this property to the existing file, preserving its dependencies and scripts. Its position within the object does not change the result. If the application is published in a subdirectory, include it in the address, for example `https://example.com/my-app`. This behaviour belongs to [Create React App](https://create-react-app.dev/docs/deployment/#building-for-relative-paths).

## Generate and check the result

From the project directory:

```console
npm run build
```

Create React App generates the `build` directory. Review it through a local HTTP server. For example, if `serve` is available in the environment:

```console
serve -s build
```

Open the HTTP address shown by the tool and check the page and its assets. Opening `index.html` directly through `file://` does not reproduce the hosting environment.

## Upload the files

The original deployment step consists of transferring **the contents of `build`** to the host’s public directory, using the transfer method supported by the provider. Preserve the structure of the files and subdirectories.

If images, CSS or JavaScript fail to load, check the configured deployment path and generate the build again. Make the correction in the project configuration; manually editing links in generated HTML would be lost during the next build.

## A specific case: SPA routes on Apache

This section extends the original tutorial for hosting that uses **Apache 2.4** and permits `mod_dir` configuration. If the application has browser routes, reloading an internal route needs to return the entry document. For an application published at the domain root, `.htaccess` can contain:

```apache
FallbackResource /index.html
```

Apache continues serving files that exist and uses that document for requests that do not map to a file. If the application lives under `/my-app/`, the target must be `/my-app/index.html`. Whether this directive is available depends on the host’s permissions and configuration; its scope is documented in [Apache: FallbackResource](https://httpd.apache.org/docs/2.4/mod/mod_dir.html#fallbackresource).

Adjust the router’s base path where applicable as well. Testing navigation from the homepage and a direct reload of an internal route helps reveal this difference between the development server and the hosting environment.
