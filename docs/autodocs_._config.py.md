# ._config.py

## File Path

`./autodocs/._config.py`

## Overview

This module defines configuration settings for the autodocs project. It includes settings for file paths, template directories, and other project-specific configurations.

## Quick Reference

*   `Config` (class)
    *   `__init__(self, project_name: str, project_root: str)`
    *   `get_project_name(self) -> str`
    *   `get_project_root(self) -> str`
    *   `get_templates_dir(self) -> str`
    *   `get_output_dir(self) -> str`
    *   `get_autodocs_dir(self) -> str`
    *   `get_config_file_path(self) -> str`
    *   `get_source_code_dir(self) -> str`
    *   `get_autodocs_template_file_path(self) -> str`
    *   `get_module_template_file_path(self) -> str`
    *   `get_class_template_file_path(self) -> str`
    *   `get_function_template_file_path(self) -> str`
    *   `get_method_template_file_path(self) -> str`
    *   `get_attribute_template_file_path(self) -> str`
    *   `get_markdown_extension(self) -> str`
    *   `get_default_ignore_patterns(self) -> list[str]`

## Detailed Documentation

### `Config` Class

This class encapsulates all configuration settings for the autodocs project. It provides methods to access various file paths and other configuration parameters.

#### `__init__(self, project_name: str, project_root: str)`

The constructor for the `Config` class.

*   **Parameters:**
    *   `project_name` (str): The name of the project.
    *   `project_root` (str): The root directory of the project.

#### `get_project_name(self) -> str`

Returns the project name.

*   **Returns:**
    *   str: The project name.

#### `get_project_root(self) -> str`

Returns the project root directory.

*   **Returns:**
    *   str: The project root directory.

#### `get_templates_dir(self) -> str`

Returns the directory containing the template files.

*   **Returns:**
    *   str: The templates directory path.  Defaults to a "templates" directory within the autodocs directory.

#### `get_output_dir(self) -> str`

Returns the directory where the generated documentation will be saved.

*   **Returns:**
    *   str: The output directory path. Defaults to an "output" directory within the project root.

#### `get_autodocs_dir(self) -> str`

Returns the directory where the autodocs project files are located.

*   **Returns:**
    *   str: The autodocs directory path. Defaults to a ".autodocs" directory within the project root.

#### `get_config_file_path(self) -> str`

Returns the path to the configuration file.

*   **Returns:**
    *   str: The configuration file path. Defaults to a "config.yaml" file within the autodocs directory.

#### `get_source_code_dir(self) -> str`

Returns the directory containing the source code.

*   **Returns:**
    *   str: The source code directory path. Defaults to the project root.

#### `get_autodocs_template_file_path(self) -> str`

Returns the path to the main autodocs template file.

*   **Returns:**
    *   str: The autodocs template file path. Defaults to "autodocs.md.jinja2" within the templates directory.

#### `get_module_template_file_path(self) -> str`

Returns the path to the module template file.

*   **Returns:**
    *   str: The module template file path. Defaults to "module.md.jinja2" within the templates directory.

#### `get_class_template_file_path(self) -> str`

Returns the path to the class template file.

*   **Returns:**
    *   str: The class template file path. Defaults to "class.md.jinja2" within the templates directory.

#### `get_function_template_file_path(self) -> str`

Returns the path to the function template file.

*   **Returns:**
    *   str: The function template file path. Defaults to "function.md.jinja2" within the templates directory.

#### `get_method_template_file_path(self) -> str`

Returns the path to the method template file.

*   **Returns:**
    *   str: The method template file path. Defaults to "method.md.jinja2" within the templates directory.

#### `get_attribute_template_file_path(self) -> str`

Returns the path to the attribute template file.

*   **Returns:**
    *   str: The attribute template file path. Defaults to "attribute.md.jinja2" within the templates directory.

#### `get_markdown_extension(self) -> str`

Returns the file extension for markdown files.

*   **Returns:**
    *   str: The markdown file extension. Defaults to ".md".

#### `get_default_ignore_patterns(self) -> list[str]`

Returns a list of default file patterns to ignore when generating documentation.

*   **Returns:**
    *   list[str]: A list of ignore patterns. Defaults to `['.venv', '__pycache__', 'tests']`.

## Usage Examples

```python
from ._config import Config

# Assuming the project root is '/path/to/my_project'
config = Config(project_name="MyProject", project_root="/path/to/my_project")

print(config.get_project_name())
print(config.get_output_dir())
print(config.get_default_ignore_patterns())
```