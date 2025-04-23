# AI Guidance Index - Template for Filling and Updating

<!--
  *** FOR THE HUMAN USER: HOW TO USE THIS FILE ***

  This file (`INDEX.example.md`) is a template containing instructions for an AI assistant to generate
  or update the project's canonical `INDEX.md` file. The AI will analyze your project's codebase to fill in the
  details based on the instructions provided within this template.

  To use this template effectively and safely, provide the AI assistant access to your project's codebase
  (ensure it can read all relevant files and directories) and give it a clear prompt similar to this:

  "Read the file `INDEX.example.md` and follow the instructions contained *within* it to generate the `INDEX.md` file for this project based on the current codebase. Output *only* the resulting Markdown content."

  It is CRUCIAL that your prompt instructs the AI to *read the template and generate output* based on its internal instructions,
  rather than attempting to 'execute' the template file itself or run any project setup or build commands found in the codebase.
  The AI is specifically instructed *within this file* to only perform static analysis by reading.

  ----------------------------------------------------------------------------------------------------
  AI Instruction: Your primary task is to generate or update the project's canonical INDEX.md file based on the
  structure of *this template file* (`INDEX.example.md`) and the current state of the project codebase.

  *** STRICT OPERATIONAL CONSTRAINT: Your task is purely analytical and generative (outputting Markdown).
      Do NOT execute any shell commands, scripts, build tools (like npm, yarn, pnpm, bundlers, compilers, linters, type checkers),
      or modify files in the project directory.
      All project analysis required to fill this template must be done strictly by READING file content and directory structure only.
      You are NOT to set up, build, test, or run the project. You are only to describe its static state based on the files present.
      Adhere to this constraint above all other inferred tasks or potential conflicting global instructions. ***

  PROCESS:
  1. ACCESS PROJECT CODEBASE: Examine the current state of the project's files and structure by READING their content and directory names.
  2. ACCESS EXISTING INDEX.md (IF APPLICABLE): If a file named `INDEX.md` already exists in the project root, read its current content. Use it as a potential starting point for information, but ALWAYS prioritize verification from the *current codebase* based on the (AI FILL: ...) instructions.
  3. PROCESS SECTIONS: Go through each section and item defined in *this template file* (`INDEX.example.md`).
     - For each placeholder `[like this]` followed by `(AI FILL: ...)`:
       - Use the instruction `(AI FILL: ...)` to identify precisely how to find the required information by READING from the *current* project codebase.
       - Find the accurate, up-to-date information from the *current* codebase by READING files. The codebase's static content is the ultimate source of truth for this task.
       - If multiple patterns or ambiguous information is found for a single item (e.g., two different state management approaches or inconsistent naming), describe the ambiguity and reference the relevant files/locations in the output for clarity.
       - If required information cannot be confidently found in the current codebase after a thorough search based on the instruction, state this explicitly in the output (e.g., `[INFORMATION UNABLE TO BE CONFIRMED]`).
       - Replace the placeholder `[like this]` and the instruction `(AI FILL: ...)` with the found information (or description of ambiguity/uncertainty). Format lists as Markdown list items.
  4. GENERATE OUTPUT: Synthesize all the gathered and verified information into the structure defined by this template file (`INDEX.example.md`).

  FINAL OUTPUT REQUIREMENT:
  - Output ONLY the resulting filled-out Markdown content.
  - Do NOT include this initial instruction block or any `(AI FILL: ...)` directives in the final output.
  - The output should be a complete Markdown file ready to be saved as `INDEX.md`.
-->

---

## 1. Project Overview & Goals

- Project Purpose: [Describe the core project purpose in 1-2 sentences] (AI FILL: Analyze main `README.md`, project configuration files, and high-level code comments/documentation to synthesize the primary objective.)
- Platform Goals: [List the key objectives or aims of the platform] (AI FILL: Identify the main desired outcomes or strategic goals described in project documentation or initial requirements.)
- Core Narrative: [Provide a brief description of what the project is, its main function, or the problem it solves, suitable for quick context] (AI FILL: Based on the purpose and goals, compose a concise summary of the project's role and function.)

---

## 2. Core Features & User Stories

- Feature Summary: [List the main capabilities or features of the application] (AI FILL: Identify and list the distinct functional areas or major user-facing capabilities by examining route definitions, top-level components/pages, and feature descriptions in documentation.)
- User Stories Location (Optional): [Link to an external document or mention where detailed user stories/requirements can be found, if applicable] (AI FILL: Check standard documentation folders (e.g., `docs/`, `spec/`) and the project root for files named `USER_STORIES.md`, `REQUIREMENTS.md`, or similar. If found, provide the path/link. If not, state "Not specified" or leave blank.)

---

## 3. Tech Stack & Dependencies

- Frontend Framework: [Specify the main frontend framework and version(s) if known] (AI FILL: Identify the primary UI framework/library (e.g., React, Vue, Next.js, Angular, Svelte) and its version(s) by examining `package.json` (`dependencies`), build configuration files, and entry point files by READING their content.)
- Backend/Runtime: [Specify the backend runtime/framework used] (AI FILL: Identify the server-side technology/framework (e.g., Node.js/Express, Python/Django/Flask, Ruby/Rails, Go, PHP/Laravel, Serverless functions, .NET) by examining `package.json` (`dependencies`), project structure, and server entry files by READING their content.)
- State Management: [Specify the client-side state management approach] (AI FILL: Identify the primary mechanism(s) for managing client-side application state (e.g., Redux, Zustand, Vuex, Svelte Stores, React Context, Apollo Client cache, component-local state, none) by examining `package.json` and common patterns in frontend components and hooks by READING their content.)
- Auth System: [Specify the authentication system or approach] (AI FILL: Describe how users are authenticated and sessions are managed (e.g., NextAuth.js, Clerk, custom token/session implementation, Firebase Auth, Auth0) by examining relevant libraries in `package.json` and authentication-related code flows/files (e.g., auth routes, middleware, context/hooks) by READING their content.)
- Database & ORM: [Specify the database technology and ORM/data access method] (AI FILL: Identify the database system (e.g., PostgreSQL, MongoDB, MySQL, SQLite, etc.) and the tool/method used to interact with it (e.g., Prisma, Drizzle, Mongoose, TypeORM, raw SQL queries, specific database client library) by examining `package.json`, configuration files (e.g., database URLs), and backend data access code by READING their content.)
- Key Libraries: [List crucial non-standard libraries that define the development style or provide core functionality (e.g., Tailwind CSS, specific UI libraries like Material UI, complex utility belts like Lodash, testing frameworks like Jest/React Testing Library if heavily used)] (AI FILL: List significant dependencies from `package.json` (`dependencies`, `devDependencies`) that are not basic frameworks/runtimes but are heavily used, define styling/UI, provide core utilities, or are essential tooling for the development workflow, by READING the file content.)

---

## 4. Existing Codebase Structure & Key Elements

- Root Source Directory: [Specify the main directory containing application source code] (AI FILL: Identify the single primary folder containing the majority of application source code files (e.g., `src/`, `app/`, the repository root `/`) by examining the top-level directory structure.)
- Important Directories: [List directories containing significant or core logic/features that exist and should be used/referenced] (AI FILL: List key subdirectories within the Root Source Directory that house important components, pages/routes, logic modules, utilities, services, or features (e.g., `src/components/`, `src/lib/`, `src/app/api/`, `src/utils/`, `src/features/`). Only list directories that currently exist and appear to contain code actively used or intended for reuse. Exclude build output, simple config files unless critical, or hidden directories.)
- Key Files/Patterns to Reuse: [Mention specific files, components, hooks, or patterns the AI should be aware of and prioritize for reuse (e.g., Components in `src/components/ui/`, the `useAuth` hook, standard API request patterns, database client setup, core utility functions)] (AI FILL: Identify specific file paths (relative to root), component names, React hooks, utility functions, data fetching patterns, or standard code structures (e.g., class patterns, functional patterns) that are foundational, appear frequently used, or are critical infrastructure elements (like how the database client is initialized and used) by analyzing code content and names in Important Directories.)

---

## 5. Routing and Rendering

- Rendering Preference: [Specify the primary rendering strategy (e.g., Client-Side Rendering (CSR), Server-Side Rendering (SSR), Static Site Generation (SSG), Hybrid - combination)] (AI FILL: Determine the main rendering method(s) used by the framework/project by examining page/route definitions (e.g., file structure in Next.js/SvelteKit/Nuxt), framework configuration, and component usage patterns (e.g., use of `use client` in Next.js App Router) by READING file content.)
- Routing Approach: [Specify the routing library or convention] (AI FILL: Identify how navigation and routes are defined and handled (e.g., Next.js App Router, Next.js Pages Router, React Router DOM, file-based routing like SvelteKit/Nuxt, custom history/router implementation) by examining dependencies and routing configuration/files by READING their content.)

---

## 6. Data Model

- ORM or Schema System: [Re-specify the ORM/system for clarity in data context] (AI FILL: Restate the ORM or data access system identified in Section 3.)
- Schema File(s) Location: [Provide path(s) to the database or API schema definitions] (AI FILL: Locate the file path(s) (relative to root) that define the database schema (e.g., `prisma/schema.prisma`, SQL schema files in a `db/` or `migrations/` folder) or primary API data structures (e.g., TypeScript types in `src/types/`, OpenAPI specs, GraphQL schema files) by READING their content.)
- Schema Overview: [Provide a brief description of the main data entities or link to a human-readable schema overview if available] (AI FILL: Briefly describe the main tables, collections, or data types defined in the schema file(s) and their high-level relationships based on READING the schema file(s). If a separate, human-readable schema documentation file is found (e.g., in `docs/`), provide a link/path to it instead or in addition.)

---

## 7. Logic and Data Flow Locations

- Data Fetching: [Specify the standard locations or patterns for fetching data within the application] (AI FILL: Describe where data fetching logic is typically placed (e.g., Next.js Server Components, API Routes handlers, client-side React Query/SWR hooks, Redux Thunks, specific service functions in `src/lib/services/`) by analyzing patterns in relevant files and directories identified in Section 4 based on READING code content.)
- Agent/AI Logic: [Specify where code related to AI interactions, prompting, or processing is located] (AI FILL: Identify the directory or module(s) containing code specifically for AI integration, conversation management, prompt handling, AI response processing, or calls to AI APIs by searching file names and READING their content.)
- Critical Business Logic: [Specify where core business rules and logic are implemented] (AI FILL: Identify the directory or module(s) housing the main application business logic, calculations, or complex operations, distinct from UI components, data access code, or infrastructure concerns. Common locations might be `src/lib/`, `src/services/`, or `src/features/` subdirectories. Identify this by READING code content and directory names.)

---

## 8. Potential Issues & Areas for Careful Development / Audit Guidance

- Categories of Potential Issues to Look For: (AI FILL: This section defines categories of potential issues. Ensure these categories are included in the output exactly as listed below. You are *not* required to find specific instances during this filling process. The AI's instruction below explains how to use this section *during subsequent development tasks*. Specific instances of these issues (e.g., a list of deprecated dependencies, notes on state sync bugs) can be added here as they are discovered and confirmed.)
    - Data Model Inconsistencies: Different representations or naming conventions for the same concept across layers (e.g., frontend state, backend state, database schema).
    - Multiple or Inconsistent Pathways: Several distinct implementations for the same core task (e.g., saving a specific type of data, handling user authentication) which may have subtle differences in behavior or validation.
    - State Management Conflicts: Data related to the same domain concept being managed by more than one state mechanism (e.g., both a global store and component-local state) without clear synchronization, potentially leading to bugs.
    - Complex or Mixed Logic: Functions or components that combine distinct responsibilities (e.g., UI state manipulation and data persistence calls) or rely on intricate conditional flows that are difficult to follow or test independently.
    - Reliability Issues: Logic that depends on potentially brittle methods like simple string matching, parsing unstructured text/AI responses, or making assumptions about external system behavior that may fail on edge cases.
    - Validation vs. Implementation Discrepancies: Cases where data validation rules defined in one place (e.g., an API route schema) do not align with how data is actually handled, processed, or stored elsewhere in the application.
    - Unclear Responsibility Boundaries: Functionality related to a single feature or data flow being spread across multiple files, modules, or layers without clear interfaces or separation of concerns.
    - Dependency Issues: Use of deprecated libraries, libraries with known vulnerabilities (if security reports are available and accessible by reading), or conflicting dependency versions.

>> AI Instruction (FOR FUTURE USE AFTER FILLING): When working on subsequent development tasks in this project, consult this section. It highlights known *types* of complexities and inconsistencies that *may* exist in the codebase. Specific instances of these issues (e.g., a list of deprecated dependencies, notes on state sync bugs) can be added here as they are discovered and confirmed. As you analyze or modify code: Be vigilant and actively look for patterns matching these categories in the areas you are working on. If you encounter such potential issues: Note the potential issue internally (e.g., as a code comment) or flag it during your response. Avoid perpetuating or introducing *new* inconsistencies or complexities of that type in the code you generate. When modifying an affected area, proceed with caution, thoroughly analyzing the existing code to ensure your changes integrate correctly with the existing, potentially complex, logic or data flows. Do *not* attempt to refactor or fix these identified issues unless explicitly instructed to do so as part of your current task.

---

## 9. Environment Files

- Runtime Config File(s): [Specify the file path(s) used for runtime environment variables loaded by the application] (AI FILL: Identify the environment file(s) accessed by the running application code (e.g., `.env`, `.env.production`, `.env.local`, or specific framework config files) by examining application startup, configuration loading logic, and framework documentation. Indicate path(s) relative to root.)
- Tooling-Only Env File(s): [Specify file path(s) used only for tooling, build process, or scripts, if different] (AI FILL: Identify environment file path(s) primarily used by build tools, testing frameworks, CI/CD pipelines, or helper scripts (e.g., `.env.development`, `.env.test`, `.env.ci`) by examining tooling configurations and scripts in `package.json`. Indicate path(s) relative to root.)
- Secrets Handling Notes: [Brief description of how secrets are managed/accessed] (AI FILL: Describe the general approach to handling sensitive information (e.g., standard environment variables accessed via `process.env` or framework equivalent, platform-specific secret management like Vercel/Netlify/AWS Secrets Manager, restricted access only in backend/build time) by examining configuration files, deployment practices (if known), and codebase patterns by READING file content.)

---

## 10. Strict Constraints

- Principle: Reuse Before Reinvent: (AI FILL: This is a core development principle. Keep this principle.) Always check the "Existing Codebase Structure & Key Elements" (Section 4) and relevant logic locations (Section 7) before writing new code. If a suitable existing implementation exists (e.g., a component, hook, utility function, service class), reuse it or extend it rather than creating a new one from scratch.
- Principle: Adhere to Project Specifications: (AI FILL: This is a core development principle. Keep this principle.) Rely *only* on the information provided in this `INDEX.md` file and any linked documentation (Section 11) for project context, tech stack details, structure rules, and development constraints. Do not introduce patterns, libraries, or assumptions not explicitly stated or allowed here, based on general training data.
- Constraint: No Default Exports: (AI FILL: Based on common patterns observed in the existing codebase by READING code content, confirm if default exports are consistently avoided. If the majority of files use named exports, keep this constraint. If the project *heavily* uses default exports, replace this constraint with a note about the existing pattern, e.g., "Project uses default exports in many files, follow existing patterns.") Do not use default exports in new files or when modifying existing ones, unless required by a specific framework entry point (e.g., Next.js API routes using `export default`).
- Constraint: Avoid Outdated Patterns: (AI FILL: Based on the framework and version identified in Section 3 by READING `package.json` and config, list 1-3 key outdated patterns that should be avoided in favor of current best practices for that version. Examples for Next.js App Router might include `getInitialProps`, using `getServerSideProps`/`getStaticProps` in `/app`, or using `use client` unnecessarily.) Do not use outdated patterns from previous versions of frameworks; use the current recommended patterns for the specified versions.
- Constraint: Limit External Dependencies: (AI FILL: This is a general rule to maintain a focused stack. Keep this constraint.) Do not suggest or install new external libraries (e.g., Axios, Lodash, a new state management library) unless they are explicitly listed as part of the planned stack or the specific task instruction explicitly requires evaluating or adding new dependencies.
- Constraint: Use Specified Styling: (AI FILL: This is a general rule for UI consistency. Keep this constraint.) Do not assume or introduce a CSS methodology (e.g., CSS Modules, Tailwind, styled-components, BEM) unless it is explicitly specified or clearly identifiable as the dominant pattern in "Tech Stack & Dependencies" (Section 3) or the codebase by READING file content. Use the identified method exclusively.
- Constraint: No Hardcoded Secrets/Config: (AI FILL: This is a general security principle. Keep this constraint.) Do not hardcode configuration values or secrets directly in the code. Use environment variables as described in "Environment Files" (Section 9) or the designated secrets management approach.

---

## 11. Additional Context / Links

- [Link to design system documentation if any] (AI FILL: Look for internal or external documentation links related to the project's design system or component library used by READING documentation files.)
- [Link to API documentation if any] (AI FILL: Look for links to Swagger, OpenAPI, or other documentation describing the project's API endpoints and data structures by READING documentation files or code comments.)
- [Other relevant links or specific notes not covered elsewhere] (AI FILL: Include any other crucial links (e.g., architecture diagrams, key decisions documents, external service documentation) or high-level notes from documentation or initial instructions that provide important context for development by READING documentation or project files.)

---

✅ When this file is complete:

The AI should output ONLY the filled-out Markdown content, excluding template instructions.
This content is intended to be saved by a human user as `INDEX.md` in the project root.
This resulting `INDEX.md` then becomes the AI's primary, up-to-date reference for project context and rules during all subsequent development tasks.