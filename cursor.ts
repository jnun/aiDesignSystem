/**
 * Cursor — the primary agent abstraction for position-aware reasoning in code.
 *
 * A Cursor is not just a pointer. It's a thinking, moving reference point.
 * It can seek structure, detect intent, modify, insert, or summarize.
 * 
 * Cursors may operate over files, lines, or ASTs, and they may stack or
 * clone themselves for recursive agent behavior.
 *
 * This is a foundational primitive for agentic operations.
 *
 * Usage:
 * ```typescript
 * // Create a cursor at a specific position
 * const cursor = createCursor({ filePath: 'src/components/Button.tsx', line: 10 });
 * 
 * // Navigate to find structure
 * cursor.seekStructure('function');
 * 
 * // Edit with context awareness
 * const blockCode = cursor.extractBlock();
 * cursor.applyAction('extractFunction', { name: 'handleClick' });
 * 
 * // Clone cursor to explore multiple paths
 * const forkedCursor = cursor.fork();
 * ```
 */

export type CursorPosition = {
  filePath: string;
  line: number;
  column?: number;
  astNode?: ASTNodeReference;
};

export type CursorContext = {
  linesBefore: string[];
  currentLine: string;
  linesAfter: string[];
  fileExtension?: string;
  language?: string;
  projectRoot?: string;
  imports?: ImportReference[];
  scope?: ScopeContext;
};

export type ASTNodeReference = {
  type: string;
  range: [number, number];
  parent?: ASTNodeReference;
  children?: ASTNodeReference[];
};

export type ImportReference = {
  source: string;
  isRelative: boolean;
  symbols: string[];
  range: [number, number];
};

export type ScopeContext = {
  variables: string[];
  functions: string[];
  types: string[];
  parentScope?: ScopeContext;
};

export interface Cursor {
  position: CursorPosition;
  context: CursorContext;

  /** Move the cursor to a specific line (and optional column) */
  moveTo(position: CursorPosition): void;

  /** Shift the cursor by N lines (negative = up, positive = down) */
  shiftLines(delta: number): void;

  /** Read the current line */
  read(): string;

  /** Replace the current line */
  write(newLine: string): void;

  /** Insert a new line below */
  insertBelow(newLine: string): void;

  /** Remove the current line */
  delete(): void;

  /** Optional: clone the cursor (fork agent) */
  fork(): Cursor;
  
  /** Navigate to nearest structure of specified type */
  seekStructure(nodeType: string): boolean;
  
  /** Jump to the definition of symbol under cursor */
  gotoDefinition(symbol?: string): boolean;
  
  /** Extract code block containing current position */
  extractBlock(): string;
  
  /** Apply predefined code action at current position */
  applyAction(actionType: CodeActionType, options?: any): boolean;
  
  /** Get imports relevant to current context */
  getImports(): ImportReference[];
  
  /** Add an import statement following project conventions */
  addImport(source: string, symbols: string[]): boolean;
  
  /** Find all references to the symbol at current position */
  findReferences(symbol?: string): CursorPosition[];
  
  /** Navigate to the enclosing scope (function, class, block) */
  navigateToEnclosingScope(): boolean;
  
  /** Check if current position is part of JSX/TSX */
  isInJSX(): boolean;
  
  /** Get nearest parent component if in JSX/TSX */
  getParentComponent(): string | null;
  
  /** Analyze code and suggest improvements */
  analyzeCode(): CodeAnalysis;
  
  /** Create structural patch that can be applied to similar code */
  createTransformPattern(): CodeTransform;
}

export type CodeActionType = 
  | 'extractVariable'
  | 'extractFunction' 
  | 'inlineVariable'
  | 'renameSymbol'
  | 'organizeImports'
  | 'fixAllLintProblems'
  | 'convertToArrowFunction'
  | 'wrapWithTryCatch'
  | 'addTypeAnnotation'
  | 'convertToServerComponent'
  | 'convertToClientComponent'
  | 'extractToCustomHook'
  | 'convertToTypeScript'
  | 'refactorToUseReducer'
  | 'refactorToContextAPI'
  | 'optimizeImports'
  | 'extractToSharedComponent';
  
export type CodeAnalysis = {
  suggestions: string[];
  potentialIssues: string[];
  performance: string[];
  accessibility: string[];
  bestPractices: string[];
};

export type CodeTransform = {
  pattern: string;
  replacement: string;
  constraints: string[];
  appliesTo: string[];
};