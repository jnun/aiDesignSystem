# AI Design System

![Pirate’s Code Licensed](./img/fafo_capitalist_cove.jpg)

# 🏴‍☠️ AI Design System  
_Governed by The Pirate’s Code_

> A comprehensive framework for effective AI-developer collaboration, created with freedom and honor.

## Purpose

This system enhances collaboration between developers and AI assistants by providing:

1. Structure and consistency for AI-developer interactions
2. Framework and language-specific guidelines that respect context limitations
3. Position-aware code navigation via cursors for precision editing
4. Templates for common operations to standardize workflows
5. Best practices for maximizing the effectiveness of AI collaboration

## Key Components

- **Cursor System**: Position-aware navigation for precise code context and editing
- **Framework Guides**: Specialized guidelines for Next.js, Python, and other frameworks
- **Communication Templates**: Standardized patterns for requests and responses
- **Project Structure Rules**: Conventions for organizing code that AI can understand
- **Workflow Patterns**: Techniques for exploration, planning, and implementation

## Structure

- `core/` - Universal patterns, principles, and guidance for AI collaboration
- `cursor.ts` - TypeScript implementation of position-aware code navigation interface
- `frameworks/` - Framework-specific guidelines, patterns, and utilities
  - `nextjs/` - Next.js directory structures, component patterns, and best practices
  - `python/` - Python project organization, templates, and workflow guides
- `languages/` - Language-specific tools and guidelines (coming soon)

## Usage

Include only the relevant guidance sections when working with AI assistants to maximize context efficiency:

```
// For working on a Next.js component:
[Include: core/GUIDANCE.md, frameworks/nextjs/nextjs.md]

// For Python data processing:
[Include: core/GUIDANCE.md, frameworks/python/structure.md, frameworks/python/data_pipelines.md]
```

## Current Status

This project is under active development. Contributions and suggestions are welcome!

## Getting Started

1. Review `core/GUIDANCE.md` for universal collaboration principles
2. Explore framework-specific guides that match your project
3. Start using cursor-based navigation for precise code editing
4. Adopt the communication templates for clearer AI interactions
