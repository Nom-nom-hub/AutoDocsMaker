# base_parser

## File Path

`./autodocs/parsers/base_parser.py`

## Overview

Base class for all language parsers

## Quick Reference

**Classes:**

*   `BaseParser`: Base class for all language parsers

**Methods:**

*   `BaseParser.__init__(config)`
*   `BaseParser.parse(file_path)`: Parse a file and extract documentation
*   `BaseParser.extract_docstring(text)`: Extract docstring from text

## Detailed Documentation

### `BaseParser` Class

Base class for all language parsers.

#### `__init__(config)`

Initializes a new instance of the `BaseParser` class.

*   **Parameters:**
    *   `config`: Configuration object.

#### `parse(file_path)`

Parse a file and extract documentation.

*   **Parameters:**
    *   `file_path`: Path to the file to parse.
*   **Returns:**
    *   `dict`: Parsed documentation data.

#### `extract_docstring(text)`

Extract docstring from text.

*   **Parameters:**
    *   `text`: The text to extract the docstring from.
*   **Returns:**
    *   `str`: The extracted docstring, or `None` if no docstring is found.

## Usage Examples

The `BaseParser` class is designed to be subclassed. Here's a conceptual example of how a subclass might use the `parse` method:

```python
from autodocs.parsers.base_parser import BaseParser

class PythonParser(BaseParser):
    def __init__(self, config):
        super().__init__(config)

    def parse(self, file_path):
        # Custom parsing logic for Python files
        with open(file_path, 'r') as f:
            code = f.read()
        # ... (Implementation details to extract documentation)
        return {"file_path": file_path, "docstrings": []} # Example return
```

In this example, `PythonParser` inherits from `BaseParser` and overrides the `parse` method to handle Python-specific parsing. The `extract_docstring` method from the base class could be used within the `parse` method to extract docstrings from the Python code.