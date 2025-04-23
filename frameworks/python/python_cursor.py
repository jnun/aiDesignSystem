"""
PythonCursor: A structure-aware code navigation and manipulation tool.

This provides position and context awareness for AI to navigate Python code,
understanding its structure and relationships.
"""

import ast
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Tuple, Union


@dataclass
class Position:
    """Represents a position in the source code."""
    line: int
    column: int


@dataclass
class Range:
    """Represents a range in the source code."""
    start: Position
    end: Position


class PythonCursor:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.lines = source_code.splitlines()
        self._ast = ast.parse(source_code)
        self._node_ranges = self._compute_node_ranges()
        
    def _compute_node_ranges(self) -> Dict[ast.AST, Range]:
        """Compute line and column ranges for all nodes in the AST."""
        ranges = {}
        for node in ast.walk(self._ast):
            if hasattr(node, 'lineno') and hasattr(node, 'end_lineno'):
                start_pos = Position(node.lineno, node.col_offset)
                end_pos = Position(node.end_lineno, node.end_col_offset)
                ranges[node] = Range(start_pos, end_pos)
        return ranges
    
    def find_definition(self, name: str) -> Optional[Range]:
        """Find the definition of a function, class, or variable."""
        for node in ast.walk(self._ast):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)) and node.name == name:
                return self._node_ranges.get(node)
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == name:
                        return self._node_ranges.get(node)
        return None
    
    def find_class_methods(self, class_name: str) -> List[str]:
        """Find all methods defined in a class."""
        for node in ast.walk(self._ast):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                return [method.name for method in node.body if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef))]
        return []
    
    def find_imports(self) -> List[str]:
        """Find all imports in the file."""
        imports = []
        for node in ast.walk(self._ast):
            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.append(name.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for name in node.names:
                    imports.append(f"{module}.{name.name}")
        return imports
    
    def extract_function_signature(self, func_name: str) -> Optional[str]:
        """Extract the signature of a function."""
        for node in ast.walk(self._ast):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == func_name:
                args = []
                for arg in node.args.args:
                    arg_name = arg.arg
                    arg_type = ""
                    if arg.annotation:
                        arg_type = f": {ast.unparse(arg.annotation)}"
                    args.append(f"{arg_name}{arg_type}")
                
                returns = ""
                if node.returns:
                    returns = f" -> {ast.unparse(node.returns)}"
                
                return f"def {func_name}({', '.join(args)}){returns}"
        return None
    
    def find_function_calls(self, func_name: str) -> List[Range]:
        """Find all calls to a specific function."""
        calls = []
        for node in ast.walk(self._ast):
            if isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id == func_name:
                if node in self._node_ranges:
                    calls.append(self._node_ranges[node])
        return calls
    
    def extract_docstring(self, name: str) -> Optional[str]:
        """Extract the docstring of a function or class."""
        for node in ast.walk(self._ast):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)) and node.name == name:
                if ast.get_docstring(node):
                    return ast.get_docstring(node)
        return None
    
    def insert_at_position(self, position: Position, text: str) -> str:
        """Insert text at a specific position and return the new source."""
        result = []
        for i, line in enumerate(self.lines):
            line_num = i + 1
            if line_num == position.line:
                result.append(line[:position.column] + text + line[position.column:])
            else:
                result.append(line)
        return '\n'.join(result)
    
    def replace_range(self, range_to_replace: Range, new_text: str) -> str:
        """Replace a range of text and return the new source."""
        start_line = range_to_replace.start.line - 1  # 0-indexed
        end_line = range_to_replace.end.line - 1  # 0-indexed
        
        result = []
        for i, line in enumerate(self.lines):
            if i < start_line or i > end_line:
                result.append(line)
            elif i == start_line and i == end_line:
                # Replace part of a single line
                result.append(
                    line[:range_to_replace.start.column] + 
                    new_text + 
                    line[range_to_replace.end.column:]
                )
            elif i == start_line:
                # First line of multi-line replacement
                result.append(line[:range_to_replace.start.column] + new_text.splitlines()[0])
            elif i == end_line:
                # Last line of multi-line replacement
                if len(new_text.splitlines()) > 1:
                    result.append(new_text.splitlines()[-1] + line[range_to_replace.end.column:])
                else:
                    result.append(line[range_to_replace.end.column:])
            elif i > start_line and i < end_line and len(new_text.splitlines()) > i - start_line:
                # Middle lines of multi-line replacement
                result.append(new_text.splitlines()[i - start_line])
                
        return '\n'.join(result)