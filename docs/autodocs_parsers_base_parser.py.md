# base_parser

## File Path

`./autodocs/parsers/base_parser.py`

## Overview

Base class for all language parsers

## Quick Reference

**Classes:**

*   `BaseParser`

**Methods:**

*   `BaseParser.__init__(config)`
*   `BaseParser.parse(file_path)`
*   `BaseParser.extract_docstring(text)`

## Detailed Documentation

### `BaseParser` Class

Base class for all language parsers.

#### `__init__(config)`

*   **Description:** The constructor for the `BaseParser` class.
*   **Parameters:**
    *   `config`: Configuration object (type unspecified).
*   **Returns:** None

#### `parse(file_path)`

*   **Description:** Parse a file and extract documentation. This method is intended to be overridden by subclasses.
*   **Parameters:**
    *   `file_path` (str): Path to the file to parse.
*   **Returns:**
    *   dict: Parsed documentation data. The specific structure of the returned dictionary depends on the implementation in subclasses.
*   **Raises:**
    *   `NotImplementedError`:  This method raises this error if it is not overridden by a subclass.

#### `extract_docstring(text)`

*   **Description:** Extract docstring from text. This method provides a basic implementation for extracting docstrings.  Subclasses may override this method to handle different docstring formats or extraction logic.
*   **Parameters:**
    *   `text` (str): The text to extract the docstring from.
*   **Returns:**
    *   str: The extracted docstring, or an empty string if no docstring is found.

## Usage Examples

The `BaseParser` class is designed to be a base class, so direct instantiation and usage are not typical.  Subclasses would inherit from `BaseParser` and override the `parse` method to implement language-specific parsing logic.  Here's a conceptual example of how a subclass might be used:

```python
from autodocs.parsers.base_parser import BaseParser

class PythonParser(BaseParser):
    def __init__(self, config):
        super().__init__(config)

    def parse(self, file_path):
        # Implement Python-specific parsing logic here
        # Example: read the file, use ast module to parse, etc.
        with open(file_path, 'r') as f:
            code = f.read()
        # ... (parse the code and extract documentation) ...
        return {"file_path": file_path, "documentation": "Parsed Python documentation"}

# Example usage (assuming a PythonParser instance is created):
# parser = PythonParser(config) # config is a placeholder
# parsed_data = parser.parse("my_python_file.py")
# print(parsed_data)
```