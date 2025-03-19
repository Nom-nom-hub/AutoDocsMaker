```markdown
# `cli` Module

## File Path

`./autodocs/cli.py`

## Overview

Command-line interface for AutoDocs.

This module provides the entry point for the AutoDocs tool when used from
the command line. It handles argument parsing, configuration loading, and
orchestrates the documentation generation process.

Usage:
    autodocs --input ./src --output ./docs --format markdown
    autodocs -i ./src -o ./docs -f html

## Quick Reference

### Functions

*   `main()`
*   `process_files(input_path, output_path, format_type, config)`
*   `should_process_file(file_path, config)`

## Detailed Documentation

### Function: `main()`

Main entry point for the AutoDocs CLI.

### Function: `process_files(input_path, output_path, format_type, config)`

| Parameter     | Description                                      |
| ------------- | ------------------------------------------------ |
| `input_path`  | Path to the directory containing source files.   |
| `output_path` | Path to the directory where documentation will be written.|
| `format_type` | The desired output format (e.g., 'markdown', 'html').|
| `config`      | Configuration object containing settings.          |

This function likely iterates through files in the `input_path`, determines if they should be processed (likely using `should_process_file`), and then generates documentation in the specified `format_type`, saving the output to the `output_path`.  The `config` object probably controls various aspects of the process, such as file inclusion/exclusion rules, formatting options, etc.

### Function: `should_process_file(file_path, config)`

| Parameter   | Description                                      |
| ----------- | ------------------------------------------------ |
| `file_path` | The path to the file being considered.           |
| `config`    | Configuration object containing settings.          |

This function likely determines whether a given file should be processed based on the provided configuration.  It probably checks against inclusion/exclusion rules, file extensions, or other criteria specified in the `config` object. It returns a boolean value indicating whether the file should be processed (True) or skipped (False).

## Usage Examples

The following examples demonstrate how to use the `autodocs` command-line tool based on the provided module docstring.

1.  **Generate Markdown documentation:**

    ```bash
    autodocs --input ./src --output ./docs --format markdown
    ```
    or
    ```bash
    autodocs -i ./src -o ./docs -f markdown
    ```

    This command processes files in the `./src` directory and generates Markdown documentation in the `./docs` directory.

2.  **Generate HTML documentation:**

    ```bash
    autodocs --input ./src --output ./docs --format html
    ```
    or
    ```bash
    autodocs -i ./src -o ./docs -f html
    ```
    This command processes files in the `./src` directory and generates HTML documentation in the `./docs` directory.
```