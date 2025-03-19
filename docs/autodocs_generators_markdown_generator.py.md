```markdown
# Module: markdown_generator

## File Path

`./autodocs/generators/markdown_generator.py`

## Overview

Generator for Markdown documentation.

This class converts parsed code data into Markdown documentation files.
It creates an index file and individual documentation files for each
module in the codebase.

Example:
    ```python
    generator = MarkdownGenerator(config)
    generator.generate(parsed_data, "docs/")
    ```

## Quick Reference

### Classes

*   [`MarkdownGenerator`](#class-markdowngenerator)

### Functions
*   `__init__(config)`
*   `generate(parsed_data, output_path)`
*   `_generate_index(parsed_data, output_path)`
*   `_generate_file_doc(data)`
*   `_format_class(cls)`
*   `_format_function(func, is_method)`

## Detailed Documentation

### Class: `MarkdownGenerator`

Generator for Markdown documentation.

This class converts parsed code data into Markdown documentation files.
It creates an index file and individual documentation files for each
module in the codebase.

Example:
    ```python
    generator = MarkdownGenerator(config)
    generator.generate(parsed_data, "docs/")
    ```

#### Methods

##### `__init__(config)`

Initialize the Markdown generator.

**Args:**

*   `config` (dict, optional): Configuration dictionary with Markdown
    formatting options. Defaults to empty dict.

##### `generate(parsed_data, output_path)`

Generate Markdown documentation from parsed data

**Args:**

*   `parsed_data`: Dictionary of parsed file data
*   `output_path`: Directory to write output files

##### `_generate_index(parsed_data, output_path)`

Generate index file with links to all documentation

##### `_generate_file_doc(data)`

Generate documentation for a single file

##### `_format_class(cls)`

Format a class for markdown output

##### `_format_function(func, is_method)`

Format a function for markdown output
```