# ._config.py

## File Path

`./autodocs/._config.py`

## Overview

This module defines configuration settings for the autodocs tool. It includes settings for file extensions, directory exclusions, and other relevant parameters used during the documentation generation process.

## Quick Reference

*   `DEFAULT_EXCLUDE_DIRS`: A list of directory names to exclude from documentation generation.
*   `DEFAULT_FILE_EXTENSIONS`: A list of file extensions to include in documentation generation.
*   `OUTPUT_DIR`: The default directory to output generated documentation.
*   `TEMPLATE_DIR`: The directory containing Jinja2 templates for documentation generation.
*   `CONFIG_FILE_NAME`: The name of the configuration file.
*   `load_config(config_file_path=None)`: Loads configuration settings from a file.

## Detailed Documentation

### `DEFAULT_EXCLUDE_DIRS`

A list of directory names to exclude from documentation generation.

*   **Type:** `list` of `str`
*   **Default Value:** `['.git', '__pycache__', '.pytest_cache']`
*   **Purpose:** Prevents the documentation generator from processing and including unnecessary directories.

### `DEFAULT_FILE_EXTENSIONS`

A list of file extensions to include in documentation generation.

*   **Type:** `list` of `str`
*   **Default Value:** `['.py']`
*   **Purpose:** Specifies the file types that the documentation generator should process.

### `OUTPUT_DIR`

The default directory to output generated documentation.

*   **Type:** `str`
*   **Default Value:** `'./docs'`
*   **Purpose:** Defines the location where the generated documentation files will be saved.

### `TEMPLATE_DIR`

The directory containing Jinja2 templates for documentation generation.

*   **Type:** `str`
*   **Default Value:** `'./templates'`
*   **Purpose:** Specifies the location of the template files used to format the generated documentation.

### `CONFIG_FILE_NAME`

The name of the configuration file.

*   **Type:** `str`
*   **Default Value:** `'autodocs.cfg'`
*   **Purpose:** Defines the name of the configuration file that `load_config` will attempt to load.

### `load_config(config_file_path=None)`

Loads configuration settings from a file.

*   **Parameters:**
    *   `config_file_path` (str, optional): The path to the configuration file. If `None`, it defaults to `CONFIG_FILE_NAME`.
*   **Returns:** `dict`: A dictionary containing the loaded configuration settings.  Returns an empty dictionary if the file is not found or if there's an error during loading.
*   **Purpose:** Reads a configuration file (typically in INI format) and returns its settings as a dictionary.  Allows overriding default settings.

## Usage Examples

The following examples demonstrate how to use the `load_config` function.  It is assumed that a configuration file named `autodocs.cfg` exists in the current working directory.

**Example 1: Loading the default configuration file**

```python
from ._config import load_config

config = load_config()
print(config)
```

This will load the configuration from `autodocs.cfg` if it exists.

**Example 2: Loading a configuration file with a specific path**

```python
from ._config import load_config

config = load_config(config_file_path="./my_config.cfg")
print(config)
```

This will load the configuration from the file `my_config.cfg`.

**Example 3: Handling a missing configuration file**

```python
from ._config import load_config

config = load_config(config_file_path="./nonexistent.cfg")
print(config)
```

This will load an empty dictionary because the file does not exist.