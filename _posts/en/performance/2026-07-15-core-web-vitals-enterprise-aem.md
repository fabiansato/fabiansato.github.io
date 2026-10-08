---
title: "Core Web Vitals on Enterprise AEM: What Actually Moves the Needle"
slug: "core-web-vitals-enterprise-aem"
date: "2026-07-15"
layout: "post"
lang: "en"
permalink: "/en/blog/core-web-vitals-enterprise-aem"
translation_url: "/blog/core-web-vitals-enterprise-aem"
category: "Performance"
category_slug: "performance"
tags: ["Performance", "Core Web Vitals", "AEM", "LCP", "CLS"]
excerpt: "On large AEM sites the biggest performance wins rarely come from micro-optimisations. They come from images, fonts, third parties and layout stability."
description: "A field guide to improving Core Web Vitals on enterprise Adobe Experience Manager sites: taming LCP with images and fonts, eliminating layout shift, and keeping third-party scripts honest."
image: "/assets/images/brand/cover-image.webp"
thumb_image: "/assets/images/brand/cover-image.webp"
author: "fabiansato"
---

Enterprise AEM sites tend to fail Core Web Vitals in boringly predictable ways. It is almost never a clever algorithm that needs optimising — it is a hero image that ships at full resolution, a web font that blocks text, a marketing tag that arrives late and shoves the page around. The good news is that predictable problems have repeatable fixes.

## Largest Contentful Paint is usually an image problem

On most brand pages the LCP element is the hero image, so that is where the attention should go. The wins are unglamorous but real: serve modern formats (WebP or AVIF), size the image to the breakpoint instead of shipping one huge file to phones, and mark the hero as high priority while lazy-loading everything below the fold.

```html
<img src="hero.webp" fetchpriority="high" width="1440" height="600" alt="...">
```

`fetchpriority="high"` signals a high loading priority. Explicit `width` and `height` reserve space before the image arrives, helping protect layout stability. On the AEM side, this is a job for responsive rendition handling and disciplined component defaults, not something you want authors solving one image at a time.

## Fonts quietly delay your text

Custom brand fonts are a common, hidden LCP tax. Depending on its configuration, a font without `font-display: swap` can hide text while it loads. Preloading only critical font files and allowing text to render with a fallback can reduce that delay. The fallback also needs care to limit layout shifts during the swap. Subsetting to the characters you actually use is the next step when you need more.

## Cumulative Layout Shift is a discipline, not a fix

Layout shift is rarely one bug; it is an accumulation of small omissions. Images without dimensions. Ad and embed slots with no reserved height. Content injected by scripts after first paint. The remedy is a habit: reserve space for anything that loads asynchronously. Give media intrinsic dimensions, give injected components a min-height, and never let a late banner reflow the article a reader has already started.

## Third-party scripts are the enemy you invited

The hardest performance conversations on enterprise sites are about tags — analytics, personalisation, A/B testing, chat, consent. Each one is added for a good reason, and together they can dominate the main thread. I treat the third-party budget as a first-class constraint: load what is needed, defer what is not critical to first render, and periodically audit what is actually firing. A tag that no campaign uses anymore is pure cost, and there is almost always at least one.

## Measure the field, not just the lab

Lighthouse in a clean lab is a useful signal, but Core Web Vitals is ultimately a field metric. Real users are on mid-range phones and imperfect networks. I keep an eye on field data (Chrome UX Report, real-user monitoring) because it catches the regressions a lab run flatters away — the personalisation script that only fires for logged-in users, the region where the CDN edge is further away.

None of this is exotic. On enterprise AEM, performance is mostly a matter of doing the ordinary things consistently: right-sized images, honest fonts, reserved space, and a firm hand with third parties. They provide a solid foundation for improving the experience, which should then be checked through measurement.

If you want to dig into any of these on a real project, I am on [LinkedIn](https://www.linkedin.com/in/fabiangonzalezdev){:target="_blank"}.
