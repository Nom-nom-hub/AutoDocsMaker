# ._markdown_generator.py

## File Path

./autodocs/generators/._markdown_generator.py

## Overview

This module provides functionality to generate Markdown documentation from Python code, specifically designed for documenting other modules. It leverages introspection to extract information about classes, functions, and their docstrings, and then formats this information into Markdown.

## Quick Reference

*   `MarkdownGenerator(module)`
    *   `__init__(self, module)`
    *   `generate_markdown(self)`

## Detailed Documentation

### `MarkdownGenerator(module)`

This class is responsible for generating Markdown documentation for a given Python module.

#### `__init__(self, module)`

*   **Purpose:** Initializes a `MarkdownGenerator` instance.
*   **Parameters:**
    *   `module`: The Python module to document (e.g., the result of `import my_module`).
*   **Attributes:**
    *   `module`: Stores the input module.

#### `generate_markdown(self)`

*   **Purpose:** Generates the Markdown documentation string for the module. It iterates through the module's members (classes, functions, etc.), extracts their docstrings and other relevant information, and formats them into a Markdown string.
*   **Returns:** A string containing the generated Markdown documentation.
*   **Details:**
    *   The method constructs the Markdown document by:
        *   Adding a title for the module.
        *   Iterating through the module's members.
        *   For each member (class or function), it extracts its docstring and other attributes.
        *   It formats the information into Markdown sections (e.g., class/function name, docstring).
        *   It handles nested members (e.g., methods within a class).
        *   It uses helper functions (e.g., `_format_function_docstring`, `_format_class_docstring`) to format specific elements.

## Usage Examples

```python
# Assuming you have a module named 'my_module.py'
# and it contains classes and functions with docstrings.
import my_module
from autodocs.generators._markdown_generator import MarkdownGenerator

# Create a MarkdownGenerator instance.
generator = MarkdownGenerator(my_module)

# Generate the Markdown documentation.
markdown_output = generator.generate_markdown()

# Print or save the generated Markdown.
print(markdown_output)

# Or, save it to a file:
# with open("my_module_docs.md", "w") as f:
#     f.write(markdown_output)
```