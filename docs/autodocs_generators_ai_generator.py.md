# ai_generator

## File Path

./autodocs/generators/ai_generator.py

## Overview

AI-powered documentation generator using OpenRouter API.

This module provides functionality to generate documentation using AI models through the OpenRouter API.

## Quick Reference

**Classes:**

*   `AIGenerator`: Generator for AI-powered documentation.

**Methods:**

*   `AIGenerator.__init__(config)`: Initialize the AI generator.
*   `AIGenerator.generate(parsed_data, output_path)`: Generate AI-powered documentation from parsed data
*   `AIGenerator._generate_docs_sequential(valid_files, output_path)`: Generate documentation sequentially for each file
*   `AIGenerator._generate_docs_parallel(valid_files, output_path)`: Generate documentation in parallel for each file
*   `AIGenerator._process_file(data, output_file)`: Process a single file for parallel execution
*   `AIGenerator._generate_index(parsed_data, output_path)`: Generate index file with links to all documentation
*   `AIGenerator._generate_file_doc_with_ai(data)`: Generate documentation for a file using AI
*   `AIGenerator._call_ai_api(prompt)`: Call the OpenRouter API with the given prompt
*   `AIGenerator._create_file_doc_prompt(data)`: Create a prompt for generating file documentation
*   `AIGenerator._create_index_prompt(files_info, project_info)`: Create a prompt for generating index documentation
*   `AIGenerator._create_readme_prompt(files_info, project_info)`: Create a prompt for generating README documentation

## Detailed Documentation

### `AIGenerator` Class

Generator for AI-powered documentation.

This class uses the OpenRouter API to generate documentation for code files using AI models like open-r1/olympiccoder-32b.

#### `AIGenerator.__init__(config)`

Initialize the AI generator.

**Args:**

*   `config` (dict, optional): Configuration dictionary with API settings. Defaults to empty dict.

#### `AIGenerator.generate(parsed_data, output_path)`

Generate AI-powered documentation from parsed data

**Args:**

*   `parsed_data`: Dictionary of parsed file data
*   `output_path`: Directory to write output files

#### `AIGenerator._generate_docs_sequential(valid_files, output_path)`

Generate documentation sequentially for each file

#### `AIGenerator._generate_docs_parallel(valid_files, output_path)`

Generate documentation in parallel for each file

#### `AIGenerator._process_file(data, output_file)`

Process a single file for parallel execution

#### `AIGenerator._generate_index(parsed_data, output_path)`

Generate index file with links to all documentation

#### `AIGenerator._generate_file_doc_with_ai(data)`

Generate documentation for a file using AI

#### `AIGenerator._call_ai_api(prompt)`

Call the OpenRouter API with the given prompt

#### `AIGenerator._create_file_doc_prompt(data)`

Create a prompt for generating file documentation

#### `AIGenerator._create_index_prompt(files_info, project_info)`

Create a prompt for generating index documentation

#### `AIGenerator._create_readme_prompt(files_info, project_info)`

Create a prompt for generating README documentation

## Usage Examples

It's difficult to provide complete usage examples without knowing the exact structure of the `parsed_data` and the contents of the configuration. However, we can infer some basic usage patterns.

**Example 1: Initializing the Generator**

```python
from autodocs.generators.ai_generator import AIGenerator

# Assuming you have an API key and model preference
config = {
    "api_key": "YOUR_OPENROUTER_API_KEY",
    "model": "open-r1/olympiccoder-32b"
}
generator = AIGenerator(config)
```

**Example 2: Generating Documentation**

```python
# Assuming you have parsed data and an output directory
parsed_data = {
    "file1.py": {
        "content": "def my_function():\n  pass",
        "imports": [],
        "classes": [],
        "functions": ["my_function"]
    },
    "file2.py": {
        "content": "class MyClass:\n  pass",
        "imports": [],
        "classes": ["MyClass"],
        "functions": []
    }
}
output_path = "docs"

generator.generate(parsed_data, output_path)
```

This would generate documentation for `file1.py` and `file2.py` in the `docs` directory, potentially creating an index file as well. The exact output depends on the prompts and the AI model's response.