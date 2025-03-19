# cli

## File Path

`./autodocs/cli.py`

## Overview

Command-line interface for AutoDocs.

This module provides the entry point for the AutoDocs tool when used from the command line. It handles argument parsing, configuration loading, and orchestrates the documentation generation process.

## Quick Reference

**Functions:**

*   `main(args=None)`
*   `process_files(input_path, output_path, format_type, config)`
*   `should_process_file(file_path, config)`

## Detailed Documentation

### `main(args=None)`

**Purpose:**

The main entry point for the AutoDocs command-line tool. Parses command-line arguments, loads configuration, and initiates the documentation generation process.

**Parameters:**

*   `args`:  (Optional) A list of strings representing the command-line arguments. If `None`, arguments are parsed from `sys.argv`.

**Returns:**

None.

**Usage:**

This function is intended to be executed directly from the command line.  It is not designed to be called from within another Python script.

### `process_files(input_path, output_path, format_type, config)`

**Purpose:**

Processes files within the `input_path`, generating documentation and writing the output to `output_path` in the specified `format_type`. Uses the provided `config` for customization.

**Parameters:**

*   `input_path`: The path to the directory containing the source files to be documented.
*   `output_path`: The path to the directory where the generated documentation will be written.
*   `format_type`: The desired output format (e.g., "markdown", "html").
*   `config`: A configuration object or dictionary that influences the documentation generation process.  Details of the config are not specified in the provided code.

**Returns:**

None.

**Usage:**

```python
# Example (Conceptual - actual config details not provided)
config = {"exclude_patterns": ["*.test.py"]}
process_files("./src", "./docs", "markdown", config)
```

### `should_process_file(file_path, config)`

**Purpose:**

Determines whether a given file should be processed for documentation generation, based on the provided configuration.

**Parameters:**

*   `file_path`: The path to the file to evaluate.
*   `config`: A configuration object or dictionary containing rules for file inclusion/exclusion. Details of the config are not specified in the provided code.

**Returns:**

`True` if the file should be processed, `False` otherwise.

**Usage:**

```python
# Example (Conceptual - actual config details not provided)
config = {"exclude_patterns": ["__init__.py", "tests/"]}
if should_process_file("my_module.py", config):
    # Process the file
    pass
```