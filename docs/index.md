# AutoDocs - Automatic Documentation Generator

## Overview

AutoDocs is an automatic documentation generator designed to extract documentation from code comments and structure. It supports multiple programming languages and output formats, making it easy to create and maintain up-to-date documentation for your projects.

## Installation

To install AutoDocs, you can use pip:

```bash
pip install autodocs
```

## Quick Start Guide

To generate documentation for your project, navigate to the root directory of your project and run the following command:

```bash
autodocs --input ./src --output ./docs --format markdown
```

This command will:

*   Process the source code located in the `./src` directory.
*   Generate documentation files in the `./docs` directory.
*   Format the output as Markdown files.

## Configuration Information

AutoDocs can be configured using command-line arguments. Here are the available options:

*   `--input`: Specifies the input directory containing the source code. (Required)
*   `--output`: Specifies the output directory for the generated documentation. (Required)
*   `--format`: Specifies the output format (e.g., `markdown`). (Required)
*   `--config`: Specifies a configuration file (e.g., `autodocs.cfg`).
*   `--help`: Displays help information.

## Table of Contents

*   [setup.py](setup.py.md)
*   autodocs/
    *   [autodocs_cli.py](autodocs_cli.py.md)
    *   [autodocs_config.py](autodocs_config.py.md)
    *   [__init__.py](autodocs___init__.py.md)
    *   parsers/
        *   [base_parser.py](autodocs_parsers_base_parser.py.md)
        *   [python_parser.py](autodocs_parsers_python_parser.py.md)
        *   [__init__.py](autodocs_parsers___init__.py.md)
    *   generators/
        *   [markdown_generator.py](autodocs_generators_markdown_generator.py.md)
        *   [__init__.py](autodocs_generators___init__.py.md)
        *   [ai_generator.py](autodocs_generators_ai_generator.py.md)
