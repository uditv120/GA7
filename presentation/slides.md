---
marp: true
paginate: true
math: katex
size: 16:9
theme: custom
class: lead
title: Product Documentation with Marp

# Note: When exporting with CLI, include:
#   marp presentation/slides.md --theme-set presentation/themes/custom.css
---

# Product Documentation

Building maintainable, version-controlled, multi-format docs with Marp.

- Markdown-first workflow
- Consistent themes and styles
- Export to HTML, PDF, PPTX, images

<!-- _footer: © 2025 Your Company | 22f3002257@ds.study.iitm.ac.in -->

---

<!-- Custom theme via inline CSS (can be extracted to themes/custom.css) -->
<style>
:root {
  --brand-bg: #0f172a;       /* slate-900 */
  --brand-fg: #e2e8f0;       /* slate-200 */
  --brand-accent: #38bdf8;   /* sky-400 */
  --code-bg: #0b1020;
}
section {
  background: var(--brand-bg);
  color: var(--brand-fg);
}
h1, h2, h3 { color: var(--brand-accent); }
blockquote { border-left: 0.25rem solid var(--brand-accent); padding-left: 1rem; opacity: .9; }
code, pre { background: var(--code-bg); color: #f8fafc; }
section.footerless::after { content: none !important; }

/* Responsive typography */
section { font-size: calc(0.9vw + 0.9vh + 8px); }
</style>

<!-- _class: footerless -->

## Why Marp for Product Docs?

> One source of truth: author in Markdown, publish anywhere.

- Keep docs with code in Git
- Reuse fragments across README and slides
- Enforce visual consistency with themes

---

<!-- Background image with overlay using Marp background helpers -->
![bg](https://placehold.co/1600x900/png?text=Background)

<!-- _backgroundColor: rgba(15,23,42,0.65) -->
<!-- _color: #e2e8f0 -->

# Architecture Overview

- Module boundaries and contracts
- Extension points and APIs
- Release artifacts and versioning

---

## Custom Styling via Directives

<!-- _header: **Docs** | Build, Test, Release -->
<!-- _footer: *Confidential · Do not distribute* -->
<!-- _color: #e2e8f0 -->

- Per-slide headers/footers
- Emphasis states via `_class`
- Slide-specific colors and backgrounds

```bash
# Export PDF with local images
marp presentation/slides.md --pdf --allow-local-files
```

---

## Math and Algorithms

We annotate complexity and formulae directly in slides.

- Amortized complexity for a sequence of operations:

  $\displaystyle \frac{1}{n} \sum_{i=1}^{n} T_i = \Theta(\log n)$

- Master theorem (case 1): for $T(n)=a\,T(n/b)+f(n)$, if $f(n)=O(n^{\log_b a - \epsilon})$ then $T(n)=\Theta(n^{\log_b a})$.

- Space usage approximation:

  $$ S(n) = S_0 + k n + O(\log n) $$

---

## Release Artifacts & Automation

- HTML (web): `marp presentation/slides.md -o dist/slides.html`
- PDF (share): `marp presentation/slides.md --pdf --allow-local-files`
- PPTX: `marp presentation/slides.md --pptx`

> Raw GitHub URL once pushed: `https://raw.githubusercontent.com/USER/REPO/main/presentation/slides.md`

---

## Contact

- Author: GitHub Copilot
- Email: 22f3002257@ds.study.iitm.ac.in
- Repo: Use GitHub Actions to build and publish artifacts

Thanks!
