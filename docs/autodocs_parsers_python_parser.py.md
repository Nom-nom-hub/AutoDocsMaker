# python_parser

## File Path

./autodocs/parsers/python_parser.py

## Overview

Parser for Python files

## Quick Reference

**Classes:**

*   `PythonParser`: Parses Python files and extracts documentation.

**Methods:**

*   `PythonParser.parse(file_path)`: Parses a Python file and extracts documentation.
*   `PythonParser._parse_class(node)`: Parses a class definition.
*   `PythonParser._parse_function(node)`: Parses a function definition.
*   `PythonParser._parse_import(node)`: Parses an import statement.

## Detailed Documentation

### Class: `PythonParser`

**Docstring:** Parser for Python files

**Methods:**

#### `parse(file_path)`

**Docstring:** Parse a Python file and extract documentation

**Args:**

*   `file_path` (str): Path to the Python file

**Returns:**

*   dict: Dictionary with parsed documentation data

**Example Usage:**

```python
from autodocs.parsers.python_parser import PythonParser

parser = PythonParser()
data = parser.parse("my_module.py")
print(data)
```

#### `_parse_class(node)`

**Docstring:** Parse a class definition

**Args:**

*   `node`: Represents a class definition in the Abstract Syntax Tree (AST).

**Returns:**

*   dict: Dictionary containing parsed class information.

**Implementation Details:**

This method is intended for internal use within the `PythonParser` class. It processes a class definition node from the AST, extracting relevant information such as the class name, docstrings, and potentially details of methods and attributes within the class.

#### `_parse_function(node)`

**Docstring:** Parse a function definition

**Args:**

*   `node`: Represents a function definition in the Abstract Syntax Tree (AST).

**Returns:**

*   dict: Dictionary containing parsed function information.

**Implementation Details:**

This method is intended for internal use within the `PythonParser` class. It processes a function definition node from the AST, extracting relevant information such as the function name, docstrings, parameters, and return types.

#### `_parse_import(node)`

**Docstring:** Parse an import statement

**Args:**

*   `node`: Represents an import statement in the Abstract Syntax Tree (AST).

**Returns:**

*   dict: Dictionary containing parsed import information.

**Implementation Details:**

This method is intended for internal use within the `PythonParser` class. It processes an import statement node from the AST, extracting information about the imported modules or objects.