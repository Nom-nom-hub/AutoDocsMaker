# AutoDocs

## Project Name and Description

AutoDocs is an automatic documentation generator that extracts documentation from code comments and structure. It supports multiple programming languages and output formats, streamlining the documentation process.

## Features

*   **Automatic Documentation Generation:** Generates documentation from code comments and structure.
*   **Multiple Language Support:** Designed to support various programming languages (currently Python).
*   **Multiple Output Formats:** Supports generating documentation in different formats (currently Markdown).
*   **AI-Powered Documentation:** Includes an AI-powered documentation generator using the OpenRouter API (optional).

## Installation

To install AutoDocs, use pip:

```bash
pip install .
```

This command should be run from the root directory of the project, where `setup.py` is located.

## Usage

The primary way to use AutoDocs is through its command-line interface (CLI).

**Basic Usage:**

To generate documentation for your project, run:

```bash
autodocs --input ./src --output ./docs --format markdown
```

This command will:

*   Process source code files located in the `./src` directory.
*   Generate documentation in Markdown format.
*   Output the generated documentation to the `./docs` directory.

## Configuration

AutoDocs can be configured using command-line arguments.

*   `--input`: Specifies the input directory containing the source code. (Required)
*   `--output`: Specifies the output directory for the generated documentation. (Required)
*   `--format`: Specifies the output format (e.g., `markdown`). (Required)

## Contributing

Contributions to AutoDocs are welcome! Here's how you can contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
