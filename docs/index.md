```markdown
# AutoDocs - Index

## 1. Overview

AutoDocs is an automatic documentation generator that extracts documentation from code comments and structure. It supports multiple programming languages and output formats. This tool simplifies the process of creating and maintaining up-to-date documentation for your software projects.

## 2. Installation

To install AutoDocs, you can use pip:

```bash
pip install autodocs
```
Or, if you are installing locally from the cloned repository:

```bash
pip install -e .
```

## 3. Quick Start Guide

To generate documentation for your project, use the following command:

```bash
autodocs --input ./src --output ./docs --format markdown
```

*   `--input`: Specifies the directory containing your source code.  Replace `./src` with the actual path to your source code.
*   `--output`: Specifies the directory where the generated documentation will be saved. Replace `./docs` with your desired output directory.
*   `--format`: Specifies the output format. Currently, `markdown` is supported.  More formats may be added in the future.

This command will process the files in the `./src` directory, extract documentation, and generate Markdown files in the `./docs` directory.

## 4. Configuration Information

AutoDocs can be configured using a JSON configuration file named `autodocs.config.json` located in the project's root directory.  An example configuration file is provided below.

```json
{
  "input_dir": "./src",
  "output_dir": "./docs",
  "output_format": "markdown",
  "include_private": false,
  "ai_generator": {
    "enabled": false,
    "api_key": "YOUR_API_KEY"
  },
  "python_parser": {
      "include_undocumented": true
  }
}
```

*   **`input_dir`**:  (string) The directory containing the source code to be documented.  Defaults to `"./src"`.
*   **`output_dir`**: (string) The directory where generated documentation will be written. Defaults to `"./docs"`.
*   **`output_format`**: (string) The format for the generated documentation.  Currently, only `"markdown"` is supported. Defaults to `"markdown"`.
*   **`include_private`**: (boolean) Whether to include documentation for private members (e.g., methods or variables starting with `_`). Defaults to `false`.
*   **`ai_generator`**: (object) Configuration for the AI-powered documentation generator.
    *   **`enabled`**: (boolean)  Enables or disables the AI generator. Defaults to `false`.
    *   **`api_key`**: (string)  The API key for the AI service.  Required if `enabled` is `true`.
* **`python_parser`**: (object) Configuration for python parser.
    * **`include_undocumented`**: (boolean) Whether to include undocumented functions. Defaults to `true`.

## 5. Table of Contents

*   [project\_structure.txt](project_structure.txt)
*   [README.md](README.md)
*   [CONTRIBUTING.md](CONTRIBUTING.md)
*   [CHANGELOG.md](CHANGELOG.md)
*   [setup.py](setup.py)
*   [autodocs.config.json](autodocs.config.json)
*   **autodocs/**
    *   [cli.py](docs/autodocs_cli.py.md)
    *   [config.py](docs/autodocs_config.py.md)
    *   [**init**.py](docs/autodocs___init__.py.md)
    *   **parsers/**
        *   [base\_parser.py](docs/autodocs_parsers_base_parser.py.md)
        *   [python\_parser.py](docs/autodocs_parsers_python_parser.py.md)
        *   [**init**.py](docs/autodocs_parsers___init__.py.md)
    *   **generators/**
        *   [markdown\_generator.py](docs/autodocs_generators_markdown_generator.py.md)
        *   [ai\_generator.py](docs/autodocs_generators_ai_generator.py.md)
        *   [**init**.py](docs/autodocs_generators___init__.py.md)

