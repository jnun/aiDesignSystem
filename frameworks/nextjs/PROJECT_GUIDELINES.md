# **AI Coding Guidelines: Next.js App Router Project**

**Version:** 0.1
**Last Updated:** 2025-04-18

---

## 1. Objective

This document provides **mandatory rules and context** for AI code generation and modification within this Next.js App Router project. Adherence ensures consistency, security, performance, and leverages project-specific patterns. Reference this document when generating or modifying code.

---

## 2. Directory Structure (`src` Enabled)

Place files according to this structure. Co-locate route-specific files (`_components`, `_hooks`, `_utils`) within `src/app/` segments. Use shared directories (`src/components`, `src/lib`, etc.) for reusable code.

```
.
├── public/                # Static assets (served at /)
├── src/
│   ├── app/               # === Core App Router (Routing, UI, API) ===
│   │   ├── api/           # API Route Handlers (Protected)
│   │   ├── (group)/       # Route groups (Layout/Org)
│   │   ├── _components/   # CO-LOCATION: Private components
│   │   ├── layout.tsx     # Segment Layout UI
│   │   ├── page.tsx       # Segment Page UI
│   │   ├── loading.tsx    # Segment Loading UI
│   │   ├── error.tsx      # Segment Error UI (Client Component)
│   │   ├── not-found.tsx  # Segment Not Found UI
│   │   ├── route.ts       # Segment API Endpoint (Protected)
│   │   └── [dynamic]/     # Dynamic route segment
│   ├── components/        # SHARED Reusable UI Components
│   │   ├── ui/            # Generic UI elements (Button, Card etc.)
│   │   └── layout/        # Shared layout (Header, Footer)
│   ├── constants/         # App-wide constants
│   ├── context/           # React Context (Client only, use sparingly)
│   ├── hooks/             # Custom React Hooks (Client only)
│   ├── lib/               # Core logic, DB access, external APIs, Server Actions
│   │   ├── auth/          # Auth config/helpers (Clerk/Lucia)
│   │   ├── db.ts          # DB client instance (Prisma/Drizzle)
│   │   ├── actions.ts     # Shared Server Actions (Permission checks mandatory)
│   │   └── validators/    # Zod schemas
│   ├── middleware.ts      # Middleware (Edge Runtime - Auth checks)
│   ├── types/             # Shared TypeScript types
│   └── utils/             # General-purpose, pure utility functions (e.g., cn)
├── tests/                 # Automated tests (Unit, Integration, E2E)
# (Config files like next.config.mjs, tsconfig.json, tailwind.config.ts exist at root)
# (Env files like .env.local, .env.example exist at root)
```

---

## 3. Core Coding Rules & Patterns

### 3.1. File Handling
*   **Path Header:** **MUST** start every `.ts`/`.tsx`/`.js`/`.jsx` file in `src` with a comment: `// src/path/to/your/file.ext`. Maintain accuracy if files move.

### 3.2. Naming Conventions
*   Components: `PascalCase.tsx`
*   Hooks: `useCamelCase.ts`
*   Utilities/Lib: `camelCase.ts` or `kebab-case.ts`
*   Types: `PascalCase.types.ts` or co-located `types.ts`
*   Constants: `UPPER_SNAKE_CASE` (primitives), `camelCase` (objects)
*   API Routes: `.../route.ts`
*   Private Folders: Start with underscore (`_components`, `_hooks`)

### 3.3. Imports
*   **Aliases:** **MUST** use path alias `@/*` for all intra-`src` imports. Avoid relative paths (`../`).
*   **Order:** Enforce via ESLint: 1. React/Next, 2. External libs, 3. Internal aliases (`@/lib`, `@/components`, etc.), 4. Relative (rare), 5. Type imports. Alphabetize within groups.

### 3.4. Type Safety & Validation
*   **Strict TS:** Code **MUST** comply with `strict: true` in `tsconfig.json`. Avoid `any`.
*   **Validation:** Use **Zod** for runtime validation of **all** external inputs (API/Action request bodies, form data) and potentially complex internal types.

### 3.5. Environment Variables
*   Access via `process.env`.
*   Browser-exposed variables **MUST** be prefixed `NEXT_PUBLIC_`.
*   **NEVER** expose server-side secrets (API keys, DB creds) via `NEXT_PUBLIC_` variables or include them in client-side code/props.

### 3.6. Component Model (Server vs. Client)
*   **Default:** Components are **Server Components**. Implement logic server-side where possible.
*   **Server Components:** Run *only* on server. Access DB, secrets, server-only libs. **Cannot** use hooks (`useState`, `useEffect`), browser APIs, or Context.
*   **Client Components:** **MUST** use `'use client'` directive at the top. Required for hooks, state, effects, event listeners, browser APIs, Context. Render server-side (SSR) then hydrate on client.
*   **Boundaries:** Props from Server to Client **MUST** be serializable (plain objects, arrays, primitives). **NEVER** pass functions, Dates, Maps, Sets, or secrets as props to Client Components.
*   **Minimize Client JS:** Keep Client Components small and located deep in the tree ("leaf" components) whenever possible.

### 3.7. Data & Mutations
*   **Server Fetching:** Primarily fetch data in Server Components (`async/await` with `fetch`).
*   **Caching:** Use Next.js `fetch` options (`cache: 'no-store'`, `next: { revalidate: seconds, tags: [...] }`) to control caching behavior. Default is `force-cache`.
*   **Revalidation:** Use `revalidatePath()` / `revalidateTag()` to invalidate cache on-demand (typically within Server Actions or API routes after mutation).
*   **Route Handlers (`route.ts`):** Use for defining API endpoints. **MUST implement Security Rules (See Section 4).** Use `NextResponse`.
*   **Server Actions (`'use server'`):** **Prefer** for form submissions and data mutations. Define in components or `src/lib/actions.ts`. **MUST implement Security Rules (See Section 4).**
*   **Client Fetching:** Use TanStack Query/SWR in Client Components to fetch from protected Route Handlers or invoke Server Actions.

### 3.8. State Management (Client-Side)
*   Local State: `useState` (Client Components).
*   Shared State (Simple): React Context (`src/context/`) (Client Components).
*   Shared State (Complex/Global): Zustand / Jotai (Client Components).
*   Server Cache State: TanStack Query / SWR (Client Components).

### 3.9. Styling
*   Use **Tailwind CSS** utility classes primarily.
*   Use `class-variance-authority` (`cva`) for component variants.
*   Use the `cn` utility (`tailwind-merge` + `clsx`) from `src/utils/cn.ts` for conditional classes.

### 3.10. Next.js Optimizations
*   Images: **MUST** use `<Image>` (`next/image`). Configure `remotePatterns` in `next.config.mjs`.
*   Fonts: **MUST** use `next/font` (`google` or `local`).
*   Scripts: Use `<Script>` (`next/script`) for third-party scripts.
*   Navigation: Use `<Link>` (`next/link`) for internal client-side navigation.

### 3.11. Metadata API
*   Use `metadata` export or `generateMetadata` function in `layout.tsx`/`page.tsx` for `<head>` tags.

---

## 4. Security Rules (Mandatory)

*   **Secrets:** **NEVER** expose secrets (API keys, DB credentials, etc.) in client-side code (`'use client'` components), props passed to client components, or `NEXT_PUBLIC_` environment variables. Access only server-side.
*   **Input Validation:** **MUST** rigorously validate **all** client input (Route Handler requests, Server Action arguments) using Zod schemas before processing. Treat client input as untrusted.
*   **Authorization (RBAC):** **MUST** implement strict **Role-Based Access Control** or equivalent permission checks at the **beginning** of **every** Server Action, Route Handler, and within Server Components loading sensitive data. Verify user identity and permissions before any data access or mutation. Use project's auth library (Clerk/Lucia).
*   **Dependency Security:** Use **latest stable** dependency versions. Regularly run `npm audit`/`yarn audit` and apply patches. Adhere to documented security best practices for used libraries.
*   **Rate Limiting:** Apply rate limiting to public-facing API routes and potentially sensitive Server Actions.

---

## 5. Documentation (Code Level)

*   **TSDoc:** **MUST** document all exported functions, components, hooks, classes, and complex types using TSDoc syntax (`@param`, `@returns`, `@remarks`).
*   **File Purpose:** **MUST** include a TSDoc `@fileoverview` comment block at the top of significant `.ts`/`.tsx` files explaining the file's purpose.

---

## 6. Standard Tooling

Use these tools for the specified tasks:

*   **UI:** Tailwind CSS + Shadcn/UI + Radix UI + Lucide Icons
*   **State (Client):** Zustand / Jotai + TanStack Query (React Query) / SWR
*   **Forms:** React Hook Form + Zod
*   **DB/ORM:** Prisma / Drizzle (as configured for the project)
*   **Auth:** Clerk / Lucia Auth (as configured for the project - **NOT NextAuth.js**)
*   **Testing:** Vitest / Jest + React Testing Library (Unit/Integration), Playwright / Cypress (E2E)
*   **Lint/Format:** ESLint + Prettier
*   **Class Utils:** `class-variance-authority` + `clsx` + `tailwind-merge` (via `cn` utility)

---

## 7. Testing Requirements

*   **Coverage:** Focus on business logic, utilities, **security logic (RBAC, validation)**, Server Actions, Route Handlers, and critical component interactions.
*   **Dependency Contracts:** Test assumptions about external API/dependency responses.
*   **Tools:** Use standard tooling (Vitest/Jest, RTL, Playwright/Cypress).
*   **CI:** Tests **MUST** pass in CI pipeline.

---

## 8. AI Collaboration Directives

*   **Context:** Reference **this document (`PROJECT_GUIDELINES.md`)** in prompts. Provide relevant file paths (using `// src/...` header comments).
*   **Specificity:** Clearly state requirements, explicitly mentioning mandatory checks like **RBAC and Zod validation** where applicable.
*   **Review:** **Developer MUST critically review all AI output** for correctness, adherence to these guidelines (especially **Section 4 Security Rules**), performance, and maintainability.
*   **Live Structure Reporting:** When creating **new files or folders**, AI **MUST** include in its response:
    *   Full relative path (e.g., `src/lib/validators/order.ts`)
    *   A brief description of its purpose (e.g., "Contains Zod schema for validating order creation payloads.")
