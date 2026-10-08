---
title: "JavaScript: the ternary operator"
slug: "javascript-operadores-ternarios"
date: "2021-10-03"
last_modified_at: "2026-10-08"
layout: "post"
lang: "en"
permalink: "/en/blog/javascript-operadores-ternarios"
translation_url: "/blog/javascript-operadores-ternarios"
category: "Frontend Architecture"
category_slug: "frontend-architecture"
tags: ["JavaScript", "Tutorial"]
excerpt: "How to choose between two values with JavaScript’s conditional operator, using a simple example."
description: "A tutorial from the 2021 archive: comparing if/else with the ternary operator, with examples updated to const and console.log."
image: "/assets/images/blog/javascript-operadores-ternarios.webp"
thumb_image: "/assets/images/blog/javascript-operadores-ternarios.webp"
author: "fabiansato"
archive: true
---

> **2021 archive · Examples reviewed in October 2026.** The original exercise is preserved, with its syntax updated to `const` and `console.log`.

## Introduction

The conditional operator, also known as the ternary operator, chooses between two values based on a condition. It has three parts: the condition, the value selected when it is met, and the value selected when it is not. The [MDN JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) describes its syntax and evaluation.

This tutorial compares two numbers and displays the larger one.

## Starting with if and else

```javascript
const x = 10;
const y = 8;

if (x > y) {
  console.log("The larger of the two numbers is " + x);
} else {
  console.log("The larger of the two numbers is " + y);
}
```

If `x > y` is true, the first block runs. Otherwise, the second block runs. With these values, the console displays `The larger of the two numbers is 10`.

## The ternary operator’s structure

```javascript
const result = condition ? value1 : value2;
```

This fragment represents the general structure: `condition`, `value1` and `value2` must exist in the program. The `?` separates the condition from the first value, and `:` introduces the alternative. If the condition evaluates to true, the result is `value1`; if it evaluates to false, the result is `value2`. Only the selected branch is evaluated.

## The same exercise with a ternary

```javascript
const x = 10;
const y = 8;
const larger = x > y ? x : y;

console.log("The larger of the two numbers is " + larger);
```

The comparison selects a number and stores it in `larger`. The message stays separate from the decision, and the result matches the `if` and `else` example. If the numbers are equal, `y` is selected, and its value is also equal to `x`.

This example reduces the code needed to obtain a value. The exercise demonstrates that equivalence without changing the program’s result.

## Material from the original publication

The 2021 entry included [this accompanying video](https://www.youtube.com/watch?v=ww0Pl8-mMng). The written example on this page preserves the exercise and uses the browser or Node.js console to display the result.
