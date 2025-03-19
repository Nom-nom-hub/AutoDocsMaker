# AutoDocs - Automatic Documentation Generator

## Overview

AutoDocs is an automatic documentation generator designed to extract documentation from code comments and code structure. It supports multiple programming languages and output formats, simplifying the process of keeping your project documentation up-to-date.

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

*   Process source files located in the `./src` directory.
*   Generate documentation files in the `./docs` directory.
*   Format the output as Markdown.

## Configuration Information

AutoDocs can be configured using command-line arguments. The following options are available:

*   `--input`: Specifies the input directory containing the source code. (Required)
*   `--output`: Specifies the output directory for the generated documentation. (Required)
*   `--format`: Specifies the output format (e.g., `markdown`). (Required)
*   `--config`: Specifies a configuration file (optional).

## Table of Contents

*   [setup.py](setup.py.md)
*   autodocs/
    *   [autodocs_cli.py](autodocs_cli.py.md)
    *   [autodocs_config.py](autodocs_config.py.md)
    *   [autodocs/\_\_init\_\_.py](autodocs___init__.py.md)
    *   autodocs/parsers/
        *   [autodocs_parsers_base_parser.py](autodocs_parsers_base_parser.py.md)
        *   [autodocs_parsers_python_parser.py](autodocs_parsers_python_parser.py.md)
        *   [autodocs_parsers/\_\_init\_\_.py](autodocs_parsers___init__.py.md)
    *   autodocs/generators/
        *   [autodocs_generators_markdown_generator.py](autodocs_generators_markdown_generator.py.md)
        *   [autodocs_generators/\_\_init\_\_.py](autodocs_generators___init__.py.md)
        *   [autodocs_generators_ai_generator.py](autodocs_generators_ai_generator.py.md)
