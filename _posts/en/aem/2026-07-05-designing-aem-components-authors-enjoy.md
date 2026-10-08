---
title: "Designing AEM Components Authors Actually Enjoy Using"
slug: "designing-aem-components-authors-enjoy"
date: "2026-07-05"
layout: "post"
lang: "en"
permalink: "/en/blog/designing-aem-components-authors-enjoy"
translation_url: "/blog/designing-aem-components-authors-enjoy"
category: "AEM"
category_slug: "aem"
tags: ["AEM", "Authoring", "HTL", "Sling Models", "Component Design"]
excerpt: "A component is not finished when it renders. It is finished when an author can configure it without asking an engineer for help."
description: "Practical patterns for building Adobe Experience Manager components that are easy to author: sensible dialogs, safe defaults, resilient HTL and Sling Models that fail gracefully."
image: "/assets/images/brand/cover-image.webp"
thumb_image: "/assets/images/brand/cover-image.webp"
author: "fabiansato"
---

Most conversations about AEM components focus on the developer experience: the Sling Model, the HTL, the client libraries. That matters, but it is only half of the story. A component lives or dies by how the marketing or content team feels when they open its dialog at 6pm before a campaign goes live. After years building brand sites on AEM, I have learned that the components that survive are the ones authors trust.

## The dialog is the product

For an author, the dialog *is* your component. If a field is ambiguously labelled, if a required image has no size guidance, or if leaving a field empty breaks the layout, the author learns to be afraid of that component. Fear leads to copy-paste of a "known good" instance, which leads to inconsistent pages and support tickets.

I try to design dialogs the way I would design a form for a stranger. Group related fields under tabs or field sets. Write descriptions that answer the question the author will actually ask ("Recommended: 1440x600, JPG or WebP"). Use sensible field types instead of free text: a pathfield for links, a real image picker for media, a dropdown for the three layout variants you actually support. Every free-text field is a future inconsistency.

## Safe defaults over required fields

A component should render something reasonable even when it is dropped onto a page and never configured. Required fields feel like discipline, but in practice they produce half-authored pages that throw validation errors during a deadline. I prefer safe defaults: a default heading level, a default variant, a placeholder that clearly reads as "configure me" rather than a broken box.

This is where Sling Models earn their place. Put the decision logic in the model, not in the HTL. Compute the effective value — the authored value, or a fallback — and expose a single clean getter. The HTL then stays declarative and readable, and the fallback behaviour is unit-testable.

```java
public String getHeadingLevel() {
    return StringUtils.defaultIfBlank(headingLevel, "h2");
}
```

## HTL that fails gracefully

HTL should assume that data can be missing. Wrap optional blocks in `data-sly-test`, never assume a list is non-empty, and never let an unconfigured field render an empty tag that collapses the layout. The goal is that a partially authored component looks intentional, not broken.

```html
<sly data-sly-test="${model.image}">
  <img class="cmp-hero__img" src="${model.image.src}" alt="${model.image.alt}"/>
</sly>
```

The `data-sly-test` guard is small, but it is the difference between a graceful empty state and a support call.

## Model the content, not the design

The most reusable components describe *what* the content is, not *how* it looks this quarter. A "hero" that hardcodes a specific background treatment will be forked the first time a brand wants something different. A hero that exposes a variant and a handful of content slots survives redesigns. When a field only exists to satisfy today's visual comp, it is usually a sign that the design belongs in the style layer, not the dialog.

## Author-friendly is maintainable

There is a happy coincidence here: the choices that make a component pleasant to author — clear boundaries, safe defaults, resilient rendering, logic in testable models — are the same ones that make it maintainable for the next engineer. When you optimise for the person configuring the component, you tend to end up with cleaner code as well.

Build for the author who opens the dialog under pressure, and both of your audiences win.

You can see some of the brand work behind these lessons on my [projects page]({{ '/en/projects/' | relative_url }}), or connect with me on [LinkedIn](https://www.linkedin.com/in/fabiangonzalezdev){:target="_blank"}.
