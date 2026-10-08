---
title: "How I Structure the Frontend for Multi-Brand AEM Sites"
slug: "frontend-architecture-multi-brand-aem"
date: "2026-07-10"
layout: "post"
lang: "en"
permalink: "/en/blog/frontend-architecture-multi-brand-aem"
translation_url: "/blog/frontend-architecture-multi-brand-aem"
category: "Frontend Architecture"
category_slug: "frontend-architecture"
tags: ["Frontend Architecture", "AEM", "Design Systems", "Clientlibs", "Theming"]
excerpt: "When one AEM implementation serves a dozen brands, the frontend has to share structure and vary identity. Here is the architecture that has held up for me."
description: "A frontend architecture for multi-brand AEM projects: a shared component layer, per-brand theming through design tokens, disciplined client libraries and a clear boundary between structure and skin."
image: "/assets/images/brand/cover-image.webp"
thumb_image: "/assets/images/brand/cover-image.webp"
author: "fabiansato"
---

A lot of my AEM work has been for organisations that run many brands on a single platform. One implementation might power a dozen brand.com sites, each with its own identity, its own market and its own marketing team, but all sharing the same authoring model and release pipeline. That constraint shapes everything about how you build the frontend.

## Separate structure from skin

The core decision is to draw a hard line between *structure* and *skin*. Structure is the HTML a component produces and the behaviour it has: a hero has an image, a heading, a call to action, in a predictable DOM. Skin is everything a brand can change: colour, typography, spacing rhythm, border treatments, motion. If structure and skin are tangled together, every brand becomes a fork, and a fork is a maintenance liability forever.

In practice this means components render semantic, brand-agnostic markup with stable class names. No colours, no brand fonts, no magic numbers baked into the component. The component guarantees the shape; the theme supplies the identity.

## Theming through design tokens

Each brand is expressed as a set of design tokens — CSS custom properties for colour, type scale, spacing and radius. The shared stylesheet consumes those tokens; it never hardcodes a value that a brand might want to change.

```css
.cmp-button {
  background: var(--color-action);
  border-radius: var(--radius-button);
  font-family: var(--font-brand);
}
```

Switching a page from one brand to another becomes a matter of loading a different token set, not shipping different component code. This keeps the shared layer honest: if a component *can't* be themed with tokens, that is a signal it has a structural problem worth fixing.

## Client libraries with a clear dependency graph

AEM client libraries are powerful and easy to misuse. On multi-brand work I keep them deliberately layered: a base library with resets and shared component styles, a per-brand theme library that only defines tokens and brand-specific overrides, and page-level libraries only where a template genuinely needs something extra. Categories and `embed`/`dependencies` are documented, not improvised, so nobody has to guess why a style loads.

The payoff is performance as much as sanity. A disciplined clientlib graph means each page loads the base once and a small theme on top, instead of a growing pile of overlapping CSS that no one dares delete.

## A component contract the whole team can rely on

Because many people touch these sites — backend engineers, frontend developers, authors across markets — the component boundary has to be a contract. I document, for each component, the DOM it emits, the class names that are safe to style, and the tokens it respects. Once that contract exists, a brand team can restyle within the rules without breaking another brand, and an engineer can refactor internals without breaking the themes.

## Why this scales

The architecture scales because the expensive thing — component logic and structure — is written once and shared, while the thing that changes constantly — brand identity — is isolated in tokens and theme libraries that are cheap to add and safe to change. New brand onboarding stops being an engineering project and becomes a theming exercise.

Multi-brand work punishes shortcuts faster than anything else I have built. The teams that treat structure and skin as separate concerns move quickly for years; the ones that fork per brand spend those same years paying it back.

More of the brand projects that shaped this approach are on my [projects page]({{ '/en/projects/' | relative_url }}). I am always happy to compare notes on [LinkedIn](https://www.linkedin.com/in/fabiangonzalezdev){:target="_blank"}.
