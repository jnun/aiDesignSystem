# --- Next.js App Router Recommended Directory Structure ---
# Defines the standard file and directory layout for a Next.js application
# using the App Router and the optional `src` directory for better organization.
# Aligned with official Next.js documentation and common Vercel practices.

directories:

  # --- Root Level Directories ---
  public: "Contains static assets to be served directly (e.g., images, fonts, robots.txt). Files here are mapped to the root URL (/). Reference them starting with /."
  tests: "(Recommended) Houses automated tests (unit, integration, e2e). Structure often mirrors the `src` directory. Alternatively, tests can be co-located using `__tests__` folders or `.test.ts`/`.spec.ts` suffixes next to source files." 
  scripts: "(Optional) Utility scripts for the project (e.g., deployment, seeding data)."
  .vscode: "(Optional) Project-specific VSCode settings (e.g., recommended extensions, settings.json)."

  # --- Core Application Code (within `src`) ---
  src: "Top-level directory containing all application source code, separating it from root configuration files."

  src/app: > # Using > for multi-line description readability in YAML
    The core of the Next.js App Router. Contains all routes, layouts, pages, and API endpoints.
    - Folders define URL segments.
    - `page.tsx` defines the UI for a route segment.
    - `layout.tsx` defines shared UI wrapping child segments/pages.
    - `loading.tsx` defines loading UI using React Suspense.
    - `error.tsx` defines error UI for a segment.
    - `not-found.tsx` defines UI for 404 errors within a segment.
    - `route.ts` defines API endpoints (Route Handlers) for specific routes.
    - `template.tsx` is similar to layout but re-mounts on navigation.
    - `default.tsx` is a fallback for unmatched parallel route slots.
    - Components defined directly within `app` are typically route-specific. Colocate components used only by a specific route segment within that segment's folder (e.g., `src/app/dashboard/_components/`).

  src/components: >
    Shared, reusable UI components used across multiple parts of the application.
    - Organize by feature or type (e.g., `ui/`, `forms/`, `layout/`).
    - Components here can be Server Components (default) or Client Components (`'use client'`).
    - Aim for generic, reusable components. Very route-specific UI should be co-located within `src/app`.

  src/lib: >
    Core application logic, libraries, constants, and interactions with external services.
    - Examples: Database client setup & queries, API client functions (for external APIs), authentication logic, core algorithms, constants (`src/lib/constants.ts`), third-party SDK configurations.
    - Keeps business logic and data fetching separate from UI components and Route Handlers.

  src/utils: >
    General-purpose utility functions.
    - Should be small, pure, and reusable across the entire application (e.g., date formatters, string manipulation, class name helpers like `cn`).
    - Differentiated from `lib` by being less domain-specific and generally smaller in scope.

  src/hooks: >
    Custom React hooks for abstracting stateful logic, side effects, or accessing context.
    - Promotes reusability of component logic. Must adhere to Rules of Hooks.
    - Often used for client-side data fetching (like SWR/TanStack Query hooks), form handling, or complex state interactions.

  src/context: > # Renamed from `store` for clearer alignment with React Context API
    Shared state management using React Context API.
    - Define contexts, providers, and consumer hooks here.
    - For other state management libraries (Zustand, Jotai, Redux), consider `src/store` or integrate within `src/lib`.

  src/styles: >
    Global styles and configuration.
    - Contains `globals.css` for base styles, CSS variable definitions.
    - May include setup for CSS Modules, Tailwind CSS plugins/base styles, or CSS-in-JS theme configurations.

  src/types: > # Or `src/@types` if preferred
    Shared TypeScript type definitions, interfaces, and enums used across the application.
    - Enhances type safety and code clarity. Global types belong here; component-specific types can be co-located or placed here if shared.

  src/middleware.ts: > # File, but crucial placement context
    Next.js Middleware file, placed within `src`. Runs on the Edge runtime before requests are processed. Used for authentication, redirects, setting headers, etc. (Note: Can also be placed at the root level).

  # --- Optional Top-Level `src` Directories ---
  src/features: "(Optional, for large apps) Self-contained modules for distinct application features, potentially grouping components, hooks, lib functions, etc., related to that feature."
  src/config: "(Optional) Application-specific configuration files or setup (e.g., internationalization setup, theme config objects)."

# --- Key Root Level Files (Context for AI) ---
# - next.config.js / next.config.mjs: Next.js build and server configuration.
# - tsconfig.json: TypeScript compiler options and path aliases.
# - tailwind.config.ts / postcss.config.js: CSS framework configurations (if used).
# - .env / .env.local / .env.*: Environment variable files (NEVER commit secrets).
# - package.json: Project metadata, dependencies, and scripts.
# - README.md: Essential project documentation.
# - .eslintrc.json / .prettierrc.json: Linter and formatter configurations.
# - Dockerfile / docker-compose.yml: Containerization configuration (if used).
# - vercel.json / netlify.toml: Platform-specific deployment configuration.

# --- Recommended Dependencies ---
dependencies:
  # --- Core UI Libraries ---
  ui:
    tailwindcss: "Latest utility-first CSS framework for rapidly building custom designs"
    shadcn-ui: "High-quality UI components built with Radix UI and Tailwind CSS"
    headlessui: "Completely unstyled, accessible UI components"
    radix-ui: "Unstyled, accessible components for building high‑quality design systems"
    framer-motion: "Production-ready animation library for React"
    lucide-react: "Beautiful, consistent icon set with React components"

  # --- Form Libraries ---
  forms:
    react-hook-form: "Performant, flexible form validation with minimal re-renders"
    zod: "TypeScript-first schema validation with static type inference"
    yup: "Schema builder for runtime value parsing and validation"
    
  # --- Data Fetching & State Management ---
  data:
    tanstack-query: "Powerful data synchronization for React"
    swr: "React Hooks for Data Fetching"
    zustand: "Small, fast, scalable state management solution"
    jotai: "Primitive and flexible state management for React"
    
  # --- Authentication ---
  auth:
    next-auth: "Authentication for Next.js applications"
    clerk: "Complete user management solution"
    supabase-auth: "Open source Firebase alternative with built-in auth"
    
  # --- Database & ORM ---
  database:
    prisma: "Next-generation ORM for TypeScript and Node.js"
    drizzle-orm: "Lightweight TypeScript ORM with type safety"
    mongoose: "MongoDB object modeling for Node.js"
    kysely: "Type-safe SQL query builder"
    
  # --- Testing ---
  testing:
    vitest: "Blazing fast testing framework compatible with Jest"
    jest: "Delightful JavaScript testing framework"
    testing-library: "Simple and complete testing utilities for React"
    playwright: "Reliable end-to-end testing for modern web apps"
    cypress: "Fast, easy and reliable testing for anything that runs in a browser"

  # --- Utilities ---
  utils:
    date-fns: "Modern JavaScript date utility library"
    lodash: "A modern JavaScript utility library"
    class-variance-authority: "For creating variants for UI components"
    clsx: "Tiny utility for constructing className strings"
    tailwind-merge: "Merge Tailwind CSS classes without conflicts"
    
  # --- Internationalization ---
  i18n:
    next-intl: "Internationalization for Next.js"
    i18next: "Internationalization framework"
    
  # --- Analytics & Monitoring ---
  analytics:
    vercel-analytics: "Analytics for Vercel-deployed apps"
    posthog: "Open-source product analytics"
    sentry: "Application monitoring and error tracking"

# --- Test Structure Recommendations ---
testing:
  unitTests: "Place in `src/**/__tests__/*.test.ts` alongside source files or in `tests/unit/`"
  integrationTests: "Place in `tests/integration/`"
  e2eTests: "Place in `tests/e2e/`, preferably using Playwright or Cypress"
  testingStrategy: >
    Prioritize unit tests for business logic and utilities.
    Component tests should focus on key interactions and edge cases.
    Minimize E2E tests to critical user flows to reduce maintenance burden.
    Set up CI to run tests on each PR.