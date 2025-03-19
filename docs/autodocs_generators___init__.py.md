# autodocs.generators

## File Path

`./autodocs/generators/__init__.py`

## Overview

This module provides a function to generate documentation in various formats.

## Quick Reference

**Functions:**

*   `generate_documentation(parsed_data, output_path, format_type, config)`

## Detailed Documentation

### `generate_documentation(parsed_data, output_path, format_type, config)`

**Purpose:** Generate documentation in the specified format.

**Arguments:**

*   `parsed_data` (dict): Dictionary of parsed file data. This likely contains information extracted from the source code, such as function signatures, docstrings, and class definitions.
*   `output_path` (str): Directory to write output files. The generated documentation files will be saved here.
*   `format_type` (str): Type of documentation to generate. Supported formats include:
    *   `markdown`
    *   `html`
    *   `pdf`
    *   `ai` (likely refers to a format for artificial intelligence or a specific AI-related tool)
*   `config` (dict): Configuration dictionary. This allows for customization of the documentation generation process. The contents of this dictionary are not specified in the provided information, but it likely contains settings such as styling options, file naming conventions, or specific options for each format type.

**Return Value:**

This function likely does not return a value (returns `None`). The primary function is to write files to the `output_path`.

**Usage Examples:**

While a specific usage example cannot be provided without knowing the structure of `parsed_data` and the contents of `config`, a general example is shown below. This example assumes that you have already parsed your code into the `parsed_data` dictionary.

```python
from autodocs.generators import generate_documentation

# Assume 'parsed_data' is populated with data from your code
parsed_data = {
    "module_name": "my_module",
    "functions": [
        {
            "name": "my_function",
            "docstring": "This function does something.",
            "args": ["arg1", "arg2"],
        }
    ],
}
output_directory = "./docs"
format_to_generate = "markdown"
configuration = {"stylesheet": "custom.css"} # Example configuration

generate_documentation(parsed_data, output_directory, format_to_generate, configuration)
```

This example would generate markdown documentation in the `./docs` directory, potentially using a custom stylesheet. The exact output would depend on the implementation details of the `generate_documentation` function.