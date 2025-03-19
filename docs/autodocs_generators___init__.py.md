# __init__

## File Path

`./autodocs/generators/__init__.py`

## Overview

This module provides the entry point for generating documentation in various formats. It takes parsed data, an output path, a desired format, and a configuration dictionary as input to produce the documentation.

## Quick Reference

**Functions:**

*   `generate_documentation(parsed_data, output_path, format_type, config)`

## Detailed Documentation

### `generate_documentation(parsed_data, output_path, format_type, config)`

**Purpose:**

Generates documentation in the specified format.

**Arguments:**

*   `parsed_data` (dict): A dictionary containing the parsed data from the source files. The structure of this dictionary is not defined in this module, but it is assumed to contain information necessary for documentation generation.
*   `output_path` (str): The directory where the generated documentation files will be written.
*   `format_type` (str): The desired format for the documentation. Supported formats include "markdown", "html", "pdf", and "ai".  The specific implementation for each format is likely handled by other modules or functions.
*   `config` (dict): A configuration dictionary that may contain settings relevant to the documentation generation process. This could include options specific to the chosen `format_type`.

**Returns:**

This function likely does not return a value (returns `None`). It's primary function is to write files to the `output_path`.

## Usage Examples

While the exact usage depends on the structure of `parsed_data` and the contents of `config`, here's a general example:

```python
from autodocs.generators import generate_documentation

# Assume you have parsed data and a configuration
parsed_data = {"module_name": "my_module", "functions": [{"name": "my_function", "docstring": "Does something"}]}
output_directory = "./docs"
format_to_generate = "markdown"
configuration = {"markdown": {"include_source": True}} # Example config

generate_documentation(parsed_data, output_directory, format_to_generate, configuration)
```

This example demonstrates how to call `generate_documentation` with example data, an output directory, a format, and a configuration. The actual content of the generated documentation will depend on the `parsed_data` and the implementation of the format-specific generation logic.