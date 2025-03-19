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

The main function, serving as the entry point for the AutoDocs command-line tool. It parses command-line arguments, loads configuration, and initiates the documentation generation process.

**Parameters:**

*   `args`: (Optional) A list of strings representing the command-line arguments. If `None`, arguments are parsed from `sys.argv`.

**Returns:**

None.

**Usage:**

This function is called when the `autodocs` command is executed from the command line.

### `process_files(input_path, output_path, format_type, config)`

**Purpose:**

Processes files within the specified input path, generating documentation based on the configured format and settings, and saves the generated documentation to the output path.

**Parameters:**

*   `input_path`: The path to the directory containing the source files to be documented.
*   `output_path`: The path to the directory where the generated documentation will be saved.
*   `format_type`: The desired output format (e.g., "markdown", "html").
*   `config`: A configuration object or dictionary containing settings for the documentation generation process.

**Returns:**

None.

**Usage:**

Called by `main()` to perform the core documentation generation logic.

### `should_process_file(file_path, config)`

**Purpose:**

Determines whether a given file should be processed for documentation generation based on the provided configuration. This function likely implements filtering logic to exclude certain files or directories.

**Parameters:**

*   `file_path`: The path to the file to be evaluated.
*   `config`: A configuration object or dictionary containing settings for filtering files.

**Returns:**

`True` if the file should be processed, `False` otherwise.

**Usage:**

Called by `process_files()` to decide which files to include in the documentation process.

## Usage Examples

The following examples illustrate how the `autodocs` command might be used.  These are inferred from the module docstring.

**Example 1: Basic usage with Markdown format**

```bash
autodocs --input ./src --output ./docs --format markdown
```

This command processes files in the `./src` directory, generates documentation in Markdown format, and saves the output to the `./docs` directory.

**Example 2: Using short options and HTML format**

```bash
autodocs -i ./src -o ./docs -f html
```

This command is equivalent to the first example, but uses short options for input, output, and format, and specifies HTML as the output format.