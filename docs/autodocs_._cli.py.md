# ._cli.py

## File Path

`./autodocs/._cli.py`

## Overview

```
"""
This module defines the command-line interface (CLI) for the autodocs tool.
It uses `argparse` to handle command-line arguments and options.
"""
```

## Quick Reference

*   `ArgumentParser`:  (class) Custom argument parser for the autodocs tool.
    *   `__init__(self, *args, **kwargs)`: Initializes the argument parser.
    *   `error(self, message)`: Overrides the default error method to provide custom error handling.
*   `parse_args(args=None, namespace=None)`: (function) Parses command-line arguments.

## Detailed Documentation

### `ArgumentParser` Class

```python
class ArgumentParser(argparse.ArgumentParser):
    """
    Custom argument parser for the autodocs tool.  Overrides the default error method
    to provide more informative error messages and exit with a non-zero code.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the argument parser.  Calls the superclass constructor.
        """
        super().__init__(*args, **kwargs)

    def error(self, message):
        """
        Overrides the default error method to provide custom error handling.
        Prints the error message to stderr, prints help, and exits.

        Args:
            message (str): The error message.
        """
        self.print_usage(sys.stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(2, '%(prog)s: error: %(message)s\n' % args)
```

*   **Purpose:** Provides a custom argument parser that extends `argparse.ArgumentParser`. It overrides the `error` method for improved error handling and informative messages.
*   **Initialization (`__init__`)**:
    *   Calls the constructor of the parent class `argparse.ArgumentParser`.
*   **`error(message)` Method**:
    *   **Purpose:** Handles errors during argument parsing.
    *   **Arguments:**
        *   `message` (str): The error message to display.
    *   **Behavior:**
        1.  Prints the usage information to `stderr`.
        2.  Prints a formatted error message to `stderr`.
        3.  Exits the program with an exit code of 2.

### `parse_args` Function

```python
def parse_args(args=None, namespace=None):
    """
    Parses command-line arguments.

    Args:
        args (list, optional): A list of argument strings. If not provided, arguments are taken from sys.argv.
        namespace (object, optional): An object to store the parsed arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = ArgumentParser(
        description="Generate documentation from code.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "paths",
        metavar="path",
        type=str,
        nargs="+",
        help="Path(s) to the Python files or directories to document.",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="output_path",
        type=str,
        default="docs",
        help="Output directory for the generated documentation (default: docs).",
    )
    parser.add_argument(
        "-f",
        "--format",
        metavar="format",
        type=str,
        default="markdown",
        choices=["markdown", "html"],
        help="Output format for the generated documentation (default: markdown).",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively search directories for Python files.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output.",
    )

    return parser.parse_args(args, namespace)
```

*   **Purpose:** Parses command-line arguments using the custom `ArgumentParser`. Defines arguments for input paths, output directory, output format, recursive search, and verbosity.
*   **Arguments:**
    *   `args` (list, optional): A list of argument strings. If `None`, arguments are parsed from `sys.argv`.
    *   `namespace` (object, optional): An object to store the parsed arguments.
*   **Returns:**
    *   `argparse.Namespace`: An object containing the parsed arguments.
*   **Argument Definitions:**
    *   `paths`:
        *   `metavar`: "path"
        *   `type`: `str`
        *   `nargs`: "+" (one or more)
        *   `help`: "Path(s) to the Python files or directories to document."
    *   `-o`, `--output`:
        *   `metavar`: "output_path"
        *   `type`: `str`
        *   `default`: "docs"
        *   `help`: "Output directory for the generated documentation (default: docs)."
    *   `-f`, `--format`:
        *   `metavar`: "format"
        *   `type`: `str`
        *   `default`: "markdown"
        *   `choices`: `["markdown", "html"]`
        *   `help`: "Output format for the generated documentation (default: markdown)."
    *   `-r`, `--recursive`:
        *   `action`: `store_true`
        *   `help`: "Recursively search directories for Python files."
    *   `-v`, `--verbose`:
        *   `action`: `store_true`
        *   `help`: "Enable verbose output."

## Usage Examples

The following examples demonstrate how the CLI arguments can be used.  These are inferred from the argument definitions in the `parse_args` function.

1.  **Basic Usage (document a single file):**

    ```bash
    python your_script.py my_module.py
    ```

    This would generate documentation for `my_module.py` in the default "docs" directory using the "markdown" format.

2.  **Document multiple files:**

    ```bash
    python your_script.py module1.py module2.py module3.py
    ```

    This would generate documentation for `module1.py`, `module2.py`, and `module3.py` in the default "docs" directory using the "markdown" format.

3.  **Specify an output directory:**

    ```bash
    python your_script.py my_package -o my_docs
    ```

    This would generate documentation for the `my_package` directory in the `my_docs` directory using the "markdown" format.

4.  **Specify an output format (HTML):**

    ```bash
    python your_script.py my_module.py -f html
    ```

    This would generate documentation for `my_module.py` in the default "docs" directory using the "html" format.

5.  **Recursively search directories:**

    ```bash
    python your_script.py my_project -r
    ```

    This would recursively search the `my_project` directory for Python files and generate documentation in the default "docs" directory using the "markdown" format.

6.  **Enable verbose output:**

    ```bash
    python your_script.py my_module.py -v
    ```

    This would generate documentation for `my_module.py` in the default "docs" directory using the "markdown" format and print verbose output to the console.