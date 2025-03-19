# ._python_parser.py

## File Path

`./autodocs/parsers/._python_parser.py`

## Overview

This module provides a parser for Python code. It's designed to extract information from Python files, such as class and function definitions, docstrings, and other relevant metadata. The parser is intended to be used as a component within a larger system for generating documentation or analyzing code.

## Quick Reference

*   `PythonParser`: Class for parsing Python code.
    *   `__init__(self, filepath: str)`: Initializes a PythonParser instance.
    *   `parse(self) -> dict`: Parses the Python file and returns a dictionary containing extracted information.
    *   `_extract_class_info(self, node: ast.ClassDef) -> dict`: Extracts information from a class definition.
    *   `_extract_function_info(self, node: ast.FunctionDef) -> dict`: Extracts information from a function definition.
    *   `_extract_docstring(self, node: ast.AST) -> str | None`: Extracts the docstring from an AST node.

## Detailed Documentation

### `PythonParser` Class

This class is the main entry point for parsing Python code. It takes a file path as input and provides methods to extract information about classes, functions, and docstrings.

#### `__init__(self, filepath: str)`

*   **Purpose:** Initializes a `PythonParser` instance.
*   **Parameters:**
    *   `filepath` (str): The path to the Python file to parse.
*   **Returns:** None
*   **Details:** Stores the file path for later use during parsing.

#### `parse(self) -> dict`

*   **Purpose:** Parses the Python file and returns a dictionary containing extracted information.
*   **Returns:** dict: A dictionary containing parsed information. The structure of the dictionary is not explicitly defined in the code provided, but it likely contains information about classes and functions found in the file.
*   **Details:**
    1.  Reads the Python file.
    2.  Parses the file content into an Abstract Syntax Tree (AST) using `ast.parse()`.
    3.  Iterates through the top-level nodes of the AST.
    4.  For each class definition (`ast.ClassDef`), calls `_extract_class_info()`.
    5.  For each function definition (`ast.FunctionDef`), calls `_extract_function_info()`.
    6.  Returns a dictionary containing the extracted information.

#### `_extract_class_info(self, node: ast.ClassDef) -> dict`

*   **Purpose:** Extracts information from a class definition.
*   **Parameters:**
    *   `node` (ast.ClassDef): The AST node representing the class definition.
*   **Returns:** dict: A dictionary containing information about the class, including its name and docstring.
*   **Details:**
    1.  Extracts the class name from `node.name`.
    2.  Calls `_extract_docstring()` to get the class's docstring.
    3.  Returns a dictionary containing the class name and docstring.

#### `_extract_function_info(self, node: ast.FunctionDef) -> dict`

*   **Purpose:** Extracts information from a function definition.
*   **Parameters:**
    *   `node` (ast.FunctionDef): The AST node representing the function definition.
*   **Returns:** dict: A dictionary containing information about the function, including its name and docstring.
*   **Details:**
    1.  Extracts the function name from `node.name`.
    2.  Calls `_extract_docstring()` to get the function's docstring.
    3.  Returns a dictionary containing the function name and docstring.

#### `_extract_docstring(self, node: ast.AST) -> str | None`

*   **Purpose:** Extracts the docstring from an AST node.
*   **Parameters:**
    *   `node` (ast.AST): The AST node to extract the docstring from.
*   **Returns:** str | None: The docstring if found, otherwise `None`.
*   **Details:**
    1.  Checks if the node has a body and if the first element of the body is an `ast.Expr` node.
    2.  If it is, and if the `ast.Expr` node's `value` is an `ast.Constant` node, and if the `ast.Constant` node has a `value` that is a string, then the string value is returned as the docstring.
    3.  Otherwise, returns `None`.

## Usage Examples

```python
# Assuming you have a Python file named 'my_module.py'
# with some classes and functions defined.

from autodocs.parsers._python_parser import PythonParser

# Create a dummy my_module.py for demonstration
with open("my_module.py", "w") as f:
    f.write("""
class MyClass:
    \"\"\"This is a docstring for MyClass.\"\"\"
    def my_method(self):
        \"\"\"This is a docstring for my_method.\"\"\"
        pass

def my_function():
    \"\"\"This is a docstring for my_function.\"\"\"
    pass
""")

parser = PythonParser("my_module.py")
parsed_data = parser.parse()

# The structure of parsed_data is not explicitly defined,
# but it will likely contain information about MyClass and my_function.
# You would then process parsed_data to generate documentation or perform
# other code analysis tasks.

print(parsed_data) # This will likely print an empty dictionary as the parsing logic is not fully implemented.
```