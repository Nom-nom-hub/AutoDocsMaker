# markdown\_generator

## File Path

./autodocs/generators/markdown\_generator.py

## Overview

Generator for Markdown documentation.

This class converts parsed code data into Markdown documentation files. It creates an index file and individual documentation files for each module in the codebase.

## Quick Reference

**Classes:**

*   `MarkdownGenerator`: Generator for Markdown documentation.

**Methods:**

*   `MarkdownGenerator.__init__(config)`: Initialize the Markdown generator.
*   `MarkdownGenerator.generate(parsed_data, output_path)`: Generate Markdown documentation from parsed data
*   `MarkdownGenerator._generate_index(parsed_data, output_path)`: Generate index file with links to all documentation
*   `MarkdownGenerator._generate_file_doc(data)`: Generate documentation for a single file
*   `MarkdownGenerator._format_class(cls)`: Format a class for markdown output
*   `MarkdownGenerator._format_function(func, is_method)`: Format a function for markdown output

## Detailed Documentation

### `MarkdownGenerator` Class

Generator for Markdown documentation.

This class converts parsed code data into Markdown documentation files. It creates an index file and individual documentation files for each module in the codebase.

#### `__init__(config)`

Initialize the Markdown generator.

**Args:**

*   `config` (dict, optional): Configuration dictionary with Markdown formatting options. Defaults to empty dict.

#### `generate(parsed_data, output_path)`

Generate Markdown documentation from parsed data

**Args:**

*   `parsed_data`: Dictionary of parsed file data
*   `output_path`: Directory to write output files

#### `_generate_index(parsed_data, output_path)`

Generate index file with links to all documentation

**Args:**

*   `parsed_data`: Dictionary of parsed file data
*   `output_path`: Directory to write output files

#### `_generate_file_doc(data)`

Generate documentation for a single file

**Args:**

*   `data`: Data for a single file

#### `_format_class(cls)`

Format a class for markdown output

**Args:**

*   `cls`: Class data

#### `_format_function(func, is_method)`

Format a function for markdown output

**Args:**

*   `func`: Function data
*   `is_method`: Boolean indicating if the function is a method

## Usage Examples

```python
# Assuming you have a config and parsed_data
config = {}  # Or your configuration
parsed_data = {} # Your parsed data

# Create an instance of the MarkdownGenerator
generator = MarkdownGenerator(config)

# Generate the documentation in the "docs/" directory
generator.generate(parsed_data, "docs/")
```