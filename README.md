```markdown
# AutoDocs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

AutoDocs is an automatic documentation generator that extracts documentation from code comments and structure.  It aims to simplify the process of creating and maintaining up-to-date project documentation.  AutoDocs supports multiple programming languages and output formats, making it a versatile tool for various development workflows. It can even leverage AI to generate documentation!

## Features

*   **Multi-Language Support:**  Currently supports Python, with plans to expand to other languages.
*   **Multiple Output Formats:** Generate documentation in Markdown and potentially other formats.
*   **Code Comment Extraction:**  Parses code comments (e.g., docstrings in Python) to extract documentation.
*   **Code Structure Analysis:**  Understands code structure (classes, functions, methods) to create organized documentation.
*   **Command-Line Interface:** Easy-to-use CLI for generating documentation.
*   **Configurable:** Customize the documentation generation process through configuration options.
*   **AI-Powered Generation:**  Utilize the `ai_generator` to create documentation using the OpenRouter API (requires configuration).
*   **Extensible Architecture:** Designed for easy addition of new parsers and generators.

## Installation

```bash
pip install autodocs  # Assuming the package is named 'autodocs' on PyPI
```

**Note:**  This assumes you have Python and pip installed.  If the package is not yet on PyPI, you might need to install it directly from the source code:

```bash
git clone <repository_url>  # Replace <repository_url> with the actual URL
cd autodocs
pip install .
```

## Usage

The primary way to use AutoDocs is through its command-line interface.  Here's a basic example:

```bash
autodocs --input ./src --output ./docs --format markdown
```

This command will:

1.  Read all source files within the `./src` directory.
2.  Parse the code and extract documentation.
3.  Generate documentation in Markdown format.
4.  Save the generated documentation to the `./docs` directory.

**AI-Powered Generation Example:**

To use the AI-powered generator, you'll need to configure your OpenRouter API key (see the Configuration section below).  Then, you can use the `--generator` option:

```bash
autodocs --input ./src --output ./docs --format markdown --generator ai
```

**Note:** AI generation may require additional dependencies.  Refer to the `autodocs/generators/ai_generator.py` file for details.

## Key Files and Directories

Here's a brief overview of the project's structure:

*   `autodocs/`:  The main package directory.
    *   `cli.py`:  Handles the command-line interface.
    *   `config.py`:  Manages configuration settings.
    *   `__init__.py`:  Package initialization file.
    *   `parsers/`:  Contains code parsers for different languages.
        *   `base_parser.py`:  Abstract base class for parsers.
        *   `python_parser.py`:  Parser for Python code.
        *   `__init__.py`:  Package initialization file.
    *   `generators/`:  Contains documentation generators for different output formats.
        *   `markdown_generator.py`:  Generator for Markdown output.
        *   `ai_generator.py`: AI-powered documentation generator using OpenRouter API.
        *   `__init__.py`:  Package initialization file.

## Configuration

AutoDocs can be configured using command-line arguments or a configuration file (e.g., `autodocs.config.yaml` or `autodocs.config.json`).

**Command-Line Options:**

*   `--input <path>`:  (Required) Specifies the input directory containing the source code.
*   `--output <path>`: (Required) Specifies the output directory for the generated documentation.
*   `--format <format>`: (Required) Specifies the output format (e.g., `markdown`).
*   `--generator <generator>`: Specifies the generator to use (e.g., `default`, `ai`). Default is `default`.
*   `--config <path>`: Specifies the path to a configuration file.
*   `--openrouter_api_key <key>`: Sets the OpenRouter API key for the AI generator (can also be set via environment variable `OPENROUTER_API_KEY`).

**Configuration File (Example - autodocs.config.yaml):**

```yaml
input: ./src
output: ./docs
format: markdown
generator: default
openrouter_api_key: your_openrouter_api_key  # Only needed for the 'ai' generator
```

**Environment Variables:**

*   `OPENROUTER_API_KEY`:  Sets the OpenRouter API key.  This is the recommended way to manage your API key for security reasons.

## Contributing

We welcome contributions to AutoDocs!  Here's how you can contribute:

1.  **Fork the repository:** Create a fork of the AutoDocs repository on GitHub.
2.  **Create a branch:** Create a new branch for your feature or bug fix (e.g., `feature/add-javascript-parser`, `bugfix/fix-markdown-formatting`).
3.  **Make your changes:** Implement your feature or fix the bug.
4.  **Write tests:**  Add unit tests to ensure your code works correctly.
5.  **Run tests:** Make sure all tests pass before submitting your changes.
6.  **Submit a pull request:** Create a pull request from your branch to the main AutoDocs repository.  Provide a clear description of your changes.

Please follow the existing code style and conventions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (You'll need to create a LICENSE file with the MIT license text).
```
