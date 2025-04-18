# **Project Guidelines: Next.js App Router Application**

**Version:** .01
**Last Updated:** 2025-04-18

---

## 1. Introduction

This document outlines the standard structure, conventions, and best practices for developing this Next.js application using the **App Router**. These guidelines apply to **both human developers and AI assistants** to ensure consistency, maintainability, performance, and quality. Adherence is key for effective collaboration.

These guidelines are aligned with official Next.js documentation but provide project-specific choices and conventions. **Refer to the official Next.js documentation for deeper explanations.**

---

## 2. Core Principles

*   **Consistency:** Rigorously follow defined structures and conventions.
*   **Server-First:** Default to Server Components; use Client Components judiciously.
*   **Performance:** Leverage Next.js optimizations (caching, Image, Font, Script, Link). Prioritize efficient data fetching and minimize client-side JS.
*   **Type Safety:** Utilize TypeScript strictly.
*   **Maintainability:** Write clear, logical, and testable code.
*   **Accessibility (a11y):** Build inclusive interfaces.
*   **Clarity:** Use explicit naming and provide context (e.g., file path comments).

---

## 3. Key Next.js Concepts (App Router)

Understanding these is fundamental:

*   **App Router (`src/app/`):** File-system based routing. Folders define segments, special files (`page.tsx`, `layout.tsx`, etc.) define UI and behavior.
*   **Server Components:** Default component type. Run *only* on the server. Ideal for data fetching, accessing backend resources directly. Cannot use state, effects, or browser APIs.
*   **Client Components (`'use client'` directive):** Render initially on the server (SSR), then hydrate and run on the client. Required for interactivity, state (`useState`), effects (`useEffect`), browser APIs (`window`), and Context. **Keep these small and push them towards the leaves of your component tree.**
*   **Server/Client Boundaries:** Data passed from Server to Client Components **must be serializable** (no functions, Dates, Maps, Sets, etc.). Client Components cannot be directly imported into Server Components (pass as props like `children`).
*   **Data Fetching:** Primarily done in Server Components using `async/await` with `fetch`. Next.js extends `fetch` for granular caching and revalidation control.
*   **Caching:** Next.js aggressively caches data fetched via `fetch` in Server Components. Understand and configure caching (`no-store`, `revalidate`, `tags`) to manage data freshness.
*   **Route Handlers (`route.ts`):** Create API endpoints within the `app` directory. Use for data mutations or custom API logic.
*   **Server Actions (`'use server'` directive):** Functions executed securely on the server, callable directly from Server or Client Components. Ideal for form submissions and mutations, often reducing the need for dedicated API routes. Can revalidate data using `revalidatePath`/`revalidateTag`.
*   **Metadata API:** Use `metadata` export or `generateMetadata` function in layouts/pages for SEO and head tag management.

---

## 4. Directory Structure (`src` Enabled)

```
.
├── .env.local             # Local secrets (DO NOT COMMIT)
├── .env.example           # Example env vars (Commit)
├── next.config.mjs        # Next.js config
├── package.json           # Dependencies & scripts
├── public/                # Static assets (root access '/')
├── src/
│   ├── app/               # === Core App Router ===
│   │   ├── api/           # API Route Handlers (e.g., /api/*)
│   │   ├── (group)/       # Route groups (organization, layouts)
│   │   ├── _components/   # CO-LOCATION: Private components for a route segment
│   │   ├── layout.tsx     # Segment UI Layout
│   │   ├── page.tsx       # Segment UI Page
│   │   ├── loading.tsx    # Segment Loading UI (Suspense)
│   │   ├── error.tsx      # Segment Error UI (Error Boundary)
│   │   ├── not-found.tsx  # Segment Not Found UI
│   │   ├── route.ts       # Segment API Endpoint
│   │   └── [dynamic]/     # Dynamic route segment convention
│   ├── components/        # SHARED, Reusable UI Components (atoms, molecules, organisms)
│   │   ├── ui/            # Generic elements (Button, Card - often Shadcn/UI based)
│   │   └── layout/        # Shared layout parts (Header, Footer)
│   ├── constants/         # App-wide constants
│   ├── context/           # React Context (use sparingly)
│   ├── hooks/             # Custom React Hooks (Client Components only)
│   ├── lib/               # Core logic, DB clients, external API fetches, non-UI utils
│   │   ├── db.ts          # e.g., Prisma client instance
│   │   ├── actions.ts     # Example location for shared Server Actions
│   │   └── validators/    # e.g., Zod schemas
│   ├── middleware.ts      # Next.js Middleware (Edge Runtime only)
│   ├── types/             # Shared TypeScript types/interfaces
│   └── utils/             # General-purpose, pure utility functions (e.g., cn, formatters)
├── tests/                 # Automated tests (unit, integration, e2e)
├── tsconfig.json          # TypeScript config (incl. path aliases)
└── tailwind.config.ts     # Tailwind CSS config
```

*(See official Next.js docs for full details on `template.tsx`, parallel routes (`@`), intercepting routes (`(.)`), etc.)*

---

## 5. Coding Standards

### 5.1. Naming Conventions

*   **Components:** `PascalCase.tsx` (`UserProfile.tsx`)
*   **Pages/Layouts:** `page.tsx`, `layout.tsx` (lowercase special names)
*   **Hooks:** `useCamelCase.ts` (`useAuthSession.ts`)
*   **Utilities/Lib:** `camelCase.ts` or `kebab-case.ts` (`dateUtils.ts`)
*   **Types:** `PascalCase.types.ts` or co-located `types.ts`
*   **Constants:** `UPPER_SNAKE_CASE` (primitives), `camelCase` (objects)
*   **API Routes:** `src/app/api/**/route.ts`
*   **Private Folders:** `_components`, `_hooks`, `_utils` (co-location)

### 5.2. File Path Header Comment

*   **Rule:** Every `.ts`/`.tsx`/`.js`/`.jsx` file in `src` MUST start with `// src/path/to/file.ext`.
*   **Purpose:** Unambiguous context for developers and AI.
*   **⚠️ Maintenance:** MUST be updated if file is moved/renamed. Consider automation (ESLint rule, pre-commit hook).

```typescript
// src/components/ui/button.tsx

import React from "react";
// ... rest of file
```

### 5.3. Imports

*   **Path Aliases:** **Always** use `@/*` (configured in `tsconfig.json`) for imports within `src`. Avoid `../`.
*   **Order:** Enforce via ESLint (`eslint-plugin-import`):
    1.  React, Next.js imports
    2.  External libraries
    3.  Internal Aliases (`@/lib`, `@/components`, `@/hooks`, etc.)
    4.  Relative imports (`./`, `../` - rare)
    5.  Type imports (`import type ...`)
*   **Organization:** Group related imports. Alphabetize within groups.

### 5.4. Component Design

*   **Server Components First:** Default to Server Components for data fetching and logic without client-side interactivity.
*   **Client Components (`'use client'`):** Use only when necessary for hooks, state, effects, event listeners, browser APIs. Keep them small and located towards the leaves of the component tree.
*   **Boundaries & Props:** Understand Server/Client boundaries. Props passed across must be serializable. Avoid passing complex non-serializable data to Client Components.
*   **Composition:** Favor composition over inheritance.
*   **Props:** Use clear TypeScript interfaces/types.
*   **Co-location:** Use `_components`, `_hooks`, etc., for logic tightly coupled to a specific route segment. Use `src/components` for widely shared components.
*   **Styling:** Use Tailwind CSS. Leverage `class-variance-authority` for variants and `tailwind-merge` + `clsx` (via `src/utils/cn.ts`) for conditional classes.

### 5.5. Data Fetching, Caching & Mutations

*   **Server Components:** Fetch data directly using `async/await` and `fetch`.
*   **Caching (Server):** Master Next.js `fetch` extensions:
    *   `{ cache: 'force-cache' }` (Default) - Aggressively cache.
    *   `{ cache: 'no-store' }` - Fetch dynamically on every request.
    *   `{ next: { revalidate: seconds } }` - Incremental Static Regeneration (ISR).
    *   `{ next: { tags: ['tag1'] } }` - Tag-based caching for on-demand revalidation.
*   **Revalidation (Server):** Update cached data using:
    *   `revalidatePath('/path')` - On-demand revalidation by path.
    *   `revalidateTag('tag1')` - On-demand revalidation by tag.
*   **Route Handlers (`route.ts`):** Use for API endpoints (mutations, complex queries). Use `NextResponse` from `next/server`. Be mindful of the runtime (Node.js vs Edge).
*   **Server Actions (`'use server'`):** **Prefer** for form submissions and data mutations. Define in Server Components or separate files. Call directly from forms or programmatically. Use `revalidatePath`/`revalidateTag` inside actions.
*   **Client Components:** Use libraries like TanStack Query (React Query) or SWR for managing server state on the client (caching, background updates, mutations triggered from UI). Fetch data via Route Handlers or Server Actions called from the client.
*   **Database:** Use Prisma (recommended) or Drizzle. Keep DB logic primarily in `src/lib` or within Route Handlers/Server Actions.

### 5.6. State Management

*   **Local:** `useState` (Client Components).
*   **Context:** React Context API (`src/context/`) for simple, localized state sharing (Client Components).
*   **Global Client:** Zustand or Jotai for complex client-side state.
*   **Server Cache State (Client):** TanStack Query / SWR (see 5.5).

### 5.7. Error Handling

*   **Route Segments:** Use `error.tsx` for UI error boundaries (must be Client Components).
*   **Not Found:** Use `notFound()` from `next/navigation` and `not-found.tsx` file.
*   **APIs/Actions:** Return meaningful errors (e.g., using `NextResponse` status codes). Handle errors from `fetch`, Server Actions, and client-side fetching appropriately in the UI.
*   **Logging:** Integrate a service like Sentry.

### 5.8. Type Safety

*   **Strict:** Enable `strict: true` in `tsconfig.json`.
*   **Avoid `any`:** Use specific types or `unknown`.
*   **Shared Types:** `src/types/`.
*   **Validation:** Use Zod for runtime validation (forms, API inputs/outputs) and type inference.

### 5.9. Environment Variables

*   Use `.env.*` files. Commit `.env.example`. Never commit `.env.local`.
*   Prefix browser-exposed variables with `NEXT_PUBLIC_`.
*   Validate required env vars at build time or runtime (e.g., using Zod in `next.config.mjs` or `src/lib/env.ts`).

### 5.10. Next.js Optimizations

*   **Images:** **Always** use `<Image>` (`next/image`) for optimized, responsive images. Configure `remotePatterns` in `next.config.mjs`.
*   **Fonts:** **Always** use `next/font` for optimized font loading (eliminates layout shift).
*   **Scripts:** Use `<Script>` (`next/script`) for third-party scripts with optimized loading strategies.
*   **Links:** Use `<Link>` (`next/link`) for client-side navigation and prefetching between pages.

### 5.11. Metadata & SEO

*   Use the Metadata API (`metadata` export or `generateMetadata` function) in `layout.tsx` and `page.tsx` for managing `<head>` content.

---

## 6. Recommended Tooling

*   **UI:** Tailwind CSS, Shadcn/UI (recommended), Radix UI, Lucide Icons
*   **State (Client):** Zustand / Jotai, TanStack Query (React Query) / SWR
*   **Forms:** React Hook Form + Zod
*   **DB/ORM:** Prisma / Drizzle
*   **Auth:** NextAuth.js / Clerk
*   **Testing:** Vitest / Jest (Unit/Integration), React Testing Library, Playwright / Cypress (E2E)
*   **Lint/Format:** ESLint, Prettier
*   **Utils:** `date-fns`, `class-variance-authority`, `clsx`, `tailwind-merge`

---

## 7. Testing Strategy

*   **Unit:** Test utilities, helpers, complex logic (`src/lib`, `src/utils`, co-located `_utils`) using Vitest/Jest.
*   **Integration:** Test interactions between components, hooks, Server Actions, or simple API routes. Use RTL for component interactions.
*   **E2E:** Test critical user flows using Playwright/Cypress. Keep minimal due to cost/speed.
*   **Focus:** Prioritize testing business logic, critical paths, Server Actions, and complex component interactions.
*   **CI:** Run lint, types, and tests on every PR.

---

## 8. Git & Workflow

*   **Branching:** Feature branches from `main` (or `develop`). Descriptive names (`feat/add-settings-page`).
*   **Commits:** Use Conventional Commits (`feat:`, `fix:`, `refactor:`, `chore:`, `docs:`, `test:`).
*   **Pull Requests:** Clear descriptions, link issues, ensure CI passes, require reviews, use Squash/Rebase merge.
*   **Reviews:** Focus on guidelines, logic, performance, security, tests. Be constructive.

---

## 9. AI Collaboration Principles

*   **Context:** Provide goal, relevant file paths (using header comments `// src/...`), and reference **these guidelines (`PROJECT_GUIDELINES.md`)**.
*   **Specificity:** Ask for precise actions related to Next.js patterns (e.g., "Refactor this fetch in `// src/app/products/page.tsx` to use `{ next: { revalidate: 3600 } }`", "Create a Server Action in `// src/lib/actions.ts` for updating user profile, ensure it uses `revalidatePath`").
*   **Incrementality:** Prefer smaller, focused requests.
*   **Review:** **CRITICALLY REVIEW ALL AI OUTPUT.** Verify correctness, adherence to these guidelines (especially Server/Client boundaries, caching, security), and performance. You own the final code.
*   **Guidance:** Explicitly remind AI of rules ("Make this a Server Component", "Ensure props passed to this Client Component are serializable").

---
