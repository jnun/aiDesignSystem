# Project Rules — Guidelines for AI and Developer Collaboration

These rules instruct both AI agents and developers on expected project structure,
safe operations, and disciplined practices within this Next.js App Router environment.

## Cursor Integration

This project uses the Cursor concept as a primary abstraction for position-aware code reasoning.
Cursors help navigate, understand, and modify code with structural awareness.

```typescript
// Example cursor usage
const cursor = createCursor({
  filePath: 'src/components/Button.tsx',
  line: 15
});

// Move within file structure
cursor.seekStructure('function');

// Edit with context awareness
cursor.extractBlock();
```

## File Structure Rules

```typescript
export const fileStructureRules = {
  rootDirectories: [
    "public", "src", "tests", "scripts", ".vscode"
  ],
  srcSubdirectories: [
    "app", "components", "lib", "utils", "hooks", "context", "styles", "types"
  ],
  optionalDirectories: [
    "features", "config"
  ],
  appRouterFiles: [
    "page.tsx", "layout.tsx", "loading.tsx", "error.tsx", "route.ts", 
    "not-found.tsx", "template.tsx", "default.tsx"
  ],
  routeConventions: {
    privateComponents: "_components", // private to the route 
    privateUtils: "_utils", // private to the route
    privateHooks: "_hooks", // private to the route
    interceptRoutes: "(.)name", // for intercepting routes
    parallelRoutes: "@name", // for parallel routes
    dynamicSegments: "[param]", // for dynamic segments
    catchAllSegments: "[...param]", // for catch-all segments
    optionalCatchAll: "[[...param]]" // for optional catch-all segments
  },
  namingConventions: {
    components: "PascalCase.tsx", // React components
    hooks: "useCamelCase.ts", // React hooks 
    utils: "camelCase.ts", // Utility functions
    types: "PascalCase.types.ts", // Type definitions
    constants: "UPPER_CASE or camelCase", // Constants
    apis: "camelCase.api.ts", // API clients and functions
  }
};
```

## Import Rules

```typescript
export const importRules = {
  /** Enforce path aliasing instead of relative imports */
  usePathAliases: true,
  aliasBase: "@", // maps to 'src/' via tsconfig.json
  disallowedPatterns: ["../", "../../", "../../../"],
  exceptionPaths: ["../../node_modules", "../public"], // if strictly necessary
  importOrder: [
    "^(react|next)(/.*)?$", // React and Next.js imports first
    "^@/lib/(.*)$", // Library imports 
    "^@/components/(.*)$", // Component imports
    "^@/hooks/(.*)$", // Hook imports
    "^@/utils/(.*)$", // Utility imports
    "^@/(.*)$", // Other internal imports
    "^[./]" // Relative imports last (should be rare)
  ],
  groupRelatedImports: true,
  alphabetizeWithinGroups: true,
};
```

## Best Practices

```typescript
export const bestPractices = {
  // Structural
  componentCoLocation: true, // colocate deeply route-specific components 
  keepLibPure: true, // avoid UI or hooks logic in lib
  typeSafety: true, // shared types live in src/types or colocated if local
  apiHandlersOnlyInRouteTS: true,
  avoidSideEffectsInUtils: true,
  avoidDuplicateLogic: true,
  explicitHooksOnly: true, // enforce custom hooks in src/hooks

  // Code Quality
  strictTypeChecking: true, // ensure strict TypeScript mode
  exhaustiveTypeChecking: true, // use type unions with discriminants
  noAny: true, // avoid the 'any' type whenever possible
  testCriticalPaths: true, // ensure critical code paths have tests
  cleanupEffects: true, // always cleanup side effects in useEffect
  
  // UI Components 
  metadataAPI: true, // use Next.js Metadata API for SEO
  responsiveFirst: true, // design for mobile first
  accessibilityFocus: true, // ensure ARIA attributes and keyboard navigation
  serverComponentsDefault: true, // prefer Server Components where feasible
  streamingSSR: true, // leverage Next.js streaming for better UX
  
  // Data Strategy
  serverFetchPreferred: true, // prefer server-side data fetching
  revalidateStrategy: "per route", // configure revalidation strategy per route
  edgeRuntimeForDynamicRoutes: true, // use Edge Runtime for highly dynamic routes
};
```

## Implementation Guidelines

```typescript
export const implementationRules = {
  authStrategies: [
    "next-auth", // Comprehensive auth solution for Next.js
    "clerk", // Complete user management with minimal setup
    "supabase-auth", // Authentication tied to Supabase backend
  ],
  
  formPatterns: {
    recommended: "react-hook-form + zod",
    alternatives: ["formik + yup", "custom useState implementation"]
  },
  
  stateManagement: {
    small: "useState + useContext",
    medium: "Zustand or Jotai",
    large: "Redux Toolkit (only for complex global state needs)"
  },
  
  dataFetching: {
    server: "fetch with Next.js fetch optimization",
    client: "TanStack Query (React Query) or SWR",
    hybrid: "Server components for initial data + client fetching for updates"
  },
  
  componentDesign: {
    atomic: true, // Use atomic design principles (atoms, molecules, organisms)
    composable: true, // Prefer composition over inheritance
    propTyping: true, // Always type component props
    derivedState: true, // Calculate derived state inline, avoid redundant state
  },
  
  // Common backend/API patterns
  apiPatterns: {
    recommended: "Route Handlers in app/api/**",
    payload: "Use Zod for request validation",
    responses: "Use typed responses with consistent error format",
    pagination: "Use cursor-based pagination for large datasets",
  },
  
  databaseAccess: {
    orm: "Prisma or Drizzle",
    connection: "Connection pooling (e.g. with PgBouncer)",
    migrations: "Rely on ORM migrations (Prisma migrate or Drizzle kit)",
  },
  
  testing: {
    unit: "Vitest or Jest for utilities and pure functions",
    component: "React Testing Library for component testing",
    e2e: "Playwright for critical user flows",
    coverage: "Focus on business logic coverage over UI coverage"
  },
  
  performance: {
    images: "Use Next.js Image component with proper sizing",
    fonts: "Use next/font for optimized font loading",
    lazyLoad: "Implement lazy loading for below-fold content",
    bundleSize: "Monitor and optimize bundle size per route"
  },
  
  deployment: {
    ci: "GitHub Actions or similar CI for testing before deployment",
    platform: "Vercel for simplest deployment experience",
    containerization: "Docker for more complex deployments",
    envVars: "Validate required environment variables on startup" 
  }
};
```

## Project Setup Checklist

To start a new Next.js project following these best practices:

1. **Create project foundation**
   ```bash
   npx create-next-app@latest my-project --typescript --eslint --tailwind --app --src-dir --import-alias="@/*"
   ```

2. **Configure linting and formatting**
   ```bash
   npm install --save-dev @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-config-prettier prettier
   ```

3. **Add recommended dependencies**
   ```bash
   # UI components
   npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu lucide-react class-variance-authority clsx tailwind-merge
   
   # Form handling
   npm install react-hook-form zod @hookform/resolvers
   
   # Data fetching
   npm install @tanstack/react-query
   
   # Utils
   npm install date-fns
   ```

4. **Configure directory structure**
   ```bash
   mkdir -p src/{components/{ui,layout,forms},lib,utils,hooks,context,styles,types}
   touch src/middleware.ts
   ```

5. **Add validation and testing**
   ```bash
   # Testing
   npm install --save-dev vitest @testing-library/react @testing-library/jest-dom
   
   # End-to-end testing
   npx playwright install
   ```