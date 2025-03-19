# .___init__.py

## File Path

./autodocs/parsers/.\_\_\_init\_\_\_.py

## Overview

This module serves as the initialization file for the `autodocs.parsers` package. It imports all parser modules within the package, making their classes and functions directly accessible when the `autodocs.parsers` package is imported. This simplifies the import process for users of the package.

## Quick Reference

*   **Modules Imported:**
    *   `autodocs.parsers.python_parser`
    *   `autodocs.parsers.markdown_parser`
    *   `autodocs.parsers.rst_parser`

## Detailed Documentation

This file primarily handles the import of other modules within the `autodocs.parsers` package. There are no classes or functions defined within this file itself. The documentation for the imported modules can be found in their respective files.

## Usage Examples

The primary usage of this file is implicit. When you import the `autodocs.parsers` package, the modules imported in this `__init__.py` file become accessible. For example:

```python
from autodocs.parsers import python_parser

# Now you can use the PythonParser class:
# parser = python_parser.PythonParser()
```

This example demonstrates how importing the `autodocs.parsers` package makes the `python_parser` module and its contents available. The other parser modules (`markdown_parser`, `rst_parser`) would be accessed similarly.