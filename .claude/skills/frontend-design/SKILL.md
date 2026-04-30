---
name: spendly-ui-designer
description: >
  Generates modern, production-ready UI components and pages for Spendly — a personal expense tracker built with Flask, Jinja2 templates, and custom CSS. Use this skill whenever the user asks to design, build, create, redesign, or improve any page or component for Spendly, including dashboard, expenses list, add/edit forms, budgets, reports, settings, and navigation. Trigger on phrases like "design the ___ page", "create UI for", "build component for", "redesign", "improve the UI", or any Spendly-related frontend request — even vague ones like "make it look better". When in doubt, use this skill.
---

# Spendly UI Designer

You are designing UI for **Spendly** — a personal expense tracker built with:
- **Backend**: Python Flask
- **Templates**: Jinja2 (`.html` files in `/templates`)
- **Styles**: Custom CSS (in `/static/css`)
- **JavaScript**: Vanilla JS (minimal, in `/static/js`)
- **Icons**: Lucide Icons (via CDN) or Heroicons

Your output should slot directly into this stack — no React, no Tailwind, no build steps unless the user explicitly asks.

---

## Step 0 — Gather Context

Before generating anything:

1. **Check if the user has shared existing code/screenshots.** If they have, extract the design tokens (colors, fonts, border-radius, spacing scale) before writing a single line.
2. **If no existing design is visible**, ask: *"Could you share a screenshot or paste your existing CSS variables / base styles? I want to match your current look."*
3. **Identify the component/page** being requested. If ambiguous, ask one clarifying question.
4. **Note any constraints** — data shape, route names, special interactions.

Only skip Step 0 if the user explicitly says "just generate something" or "start fresh."

---

## Design System (Defaults — override with project's actual values if shared)

These are sensible defaults for a modern fintech SaaS. Always defer to the actual project styles if provided.

```css
:root {
  /* Colors */
  --color-bg:          #f8f9fc;
  --color-surface:     #ffffff;
  --color-surface-alt: #f1f3f9;
  --color-border:      #e4e7ef;
  --color-primary:     #4f46e5;   /* indigo */
  --color-primary-hover: #4338ca;
  --color-success:     #16a34a;
  --color-danger:      #dc2626;
  --color-warning:     #d97706;
  --color-text:        #111827;
  --color-text-muted:  #6b7280;
  --color-text-subtle: #9ca3af;

  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.125rem;
  --text-xl:   1.25rem;
  --text-2xl:  1.5rem;
  --text-3xl:  1.875rem;

  /* Spacing (8px grid) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;

  /* Shape */
  --radius-sm:  6px;
  --radius-md:  10px;
  --radius-lg:  16px;
  --radius-xl:  20px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.08), 0 2px 4px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 24px rgba(0,0,0,0.10), 0 4px 8px rgba(0,0,0,0.05);
}
```

---

## Output Format

For every request, produce output in this order:

### 1. UI Structure (brief)
A short paragraph or bullet list covering:
- Layout overview (sidebar/topnav, grid, sections)
- Key UX decisions and why
- Any notable interactions

### 2. HTML (Jinja2 template)
- Extend from a base template: `{% extends "base.html" %}` 
- Use `{% block content %}...{% endblock %}`
- Semantic HTML5 elements (`<main>`, `<section>`, `<article>`, `<header>`)
- Include Lucide icons via `<i data-lucide="icon-name"></i>` + `lucide.createIcons()` at bottom
- BEM-style class naming: `.card`, `.card__header`, `.card__body`, `.btn`, `.btn--primary`
- No inline styles unless absolutely necessary

### 3. CSS
- Scoped to the page/component (prefix classes with page name, e.g. `.dashboard-*`)
- Use CSS variables from the design system above
- Mobile-first media queries
- Transitions on interactive elements: `transition: all 0.15s ease`

### 4. JavaScript (if needed)
- Vanilla JS only
- Small, focused event handlers
- No jQuery unless already in the project

---

## Design Rules (Non-Negotiable)

| Rule | Detail |
|------|--------|
| **Card-based layout** | Group related content in cards with `var(--shadow-sm)` and `var(--radius-md)` |
| **8px spacing grid** | All margins/paddings in multiples of 4px or 8px |
| **Consistent typography** | Use CSS variable font sizes; headings bold, labels muted |
| **Meaningful icons** | Every action/category has a Lucide icon. Never decorative-only. |
| **Subtle color** | Primary color for CTAs only. States use success/danger/warning vars. |
| **No clutter** | One primary action per section. Secondary actions visually subordinate. |
| **Responsive** | Works on mobile (375px) and desktop (1280px+) |
| **Empty states** | Always include an empty-state design if the component can have no data |

---

## Common Spendly Components

Reference these patterns for consistency:

### Stat Card
```html
<div class="stat-card">
  <div class="stat-card__icon">
    <i data-lucide="trending-down"></i>
  </div>
  <div class="stat-card__body">
    <p class="stat-card__label">Total Spent</p>
    <p class="stat-card__value">£1,240.50</p>
    <p class="stat-card__change stat-card__change--up">+12% this month</p>
  </div>
</div>
```

### Expense Row
```html
<div class="expense-row">
  <div class="expense-row__icon expense-row__icon--food">
    <i data-lucide="utensils"></i>
  </div>
  <div class="expense-row__info">
    <p class="expense-row__title">Lunch at Pret</p>
    <p class="expense-row__meta">Food & Drink · Today</p>
  </div>
  <p class="expense-row__amount expense-row__amount--debit">-£8.50</p>
</div>
```

### Category Colors (for icon badges)
```css
.cat--food      { background: #fef3c7; color: #d97706; }
.cat--transport { background: #dbeafe; color: #2563eb; }
.cat--health    { background: #dcfce7; color: #16a34a; }
.cat--shopping  { background: #fce7f3; color: #db2777; }
.cat--bills     { background: #ede9fe; color: #7c3aed; }
.cat--other     { background: #f3f4f6; color: #6b7280; }
```

---

## Pages in Spendly

Known pages to reference for navigation/breadcrumbs:
- `/` — Dashboard
- `/expenses` — Expenses list
- `/add` — Add expense
- `/edit/<id>` — Edit expense
- `/budgets` — Budgets
- `/reports` — Reports/Analytics
- `/settings` — Settings

---

## Quality Checklist (self-review before output)

Before finishing, verify:
- [ ] CSS variables used throughout (no hardcoded hex colors)
- [ ] Lucide icons initialized with `lucide.createIcons()`
- [ ] Mobile layout tested mentally at 375px
- [ ] Empty state included if component lists data
- [ ] No more than one primary CTA per section
- [ ] Jinja2 template blocks used correctly
- [ ] Class names follow BEM convention
- [ ] All interactive elements have hover/focus states

---

## Consistency Rule

If the user shares existing HTML/CSS:
1. Extract their actual CSS variables and class patterns
2. Override the defaults in this skill with the real values
3. Match their exact border-radius, shadow, font, and color choices
4. Never introduce a new design pattern if an existing one already handles it

If the existing design is unclear → ask for a screenshot before generating.