```markdown
# ai_generator

**File Path:** `./autodocs/generators/ai_generator.py`

## Overview

AI-powered documentation generator using OpenRouter API.

This module provides functionality to generate documentation using
AI models through the OpenRouter API.

## Quick Reference

**Classes:**

-   `AIGenerator`

**Functions:**

-   `__init__(config)`
-   `generate(parsed_data, output_path)`
-   `_generate_docs_sequential(valid_files, output_path)`
-   `_generate_docs_parallel(valid_files, output_path)`
-   `_process_file(data, output_file)`
-   `_generate_index(processed_files, output_path)`
-   `_generate_file_doc_with_ai(data)`
-   `_call_ai_api(prompt)`
-   `_create_file_doc_prompt(data)`
-   `_create_index_prompt(files_info, project_info)`
-   `_generate_readme(files_info)`

## Detailed Documentation

### Class: `AIGenerator`

Generator for AI-powered documentation.

This class uses the OpenRouter API to generate documentation for code files
using AI models like open-r1/olympiccoder-32b.

#### `__init__(config)`

Initialize the AI generator.

**Args:**

-   `config` (dict, optional): Configuration dictionary with API settings. Defaults to empty dict.

#### `generate(parsed_data, output_path)`

Generate AI-powered documentation from parsed data

**Args:**

-   `parsed_data`: Dictionary of parsed file data
-   `output_path`: Directory to write output files

#### `_generate_docs_sequential(valid_files, output_path)`

Generate documentation sequentially for each file

#### `_generate_docs_parallel(valid_files, output_path)`

Generate documentation in parallel for each file

#### `_process_file(data, output_file)`

Process a single file for parallel execution

#### `_generate_index(processed_files, output_path)`

Generate index file with links to all documentation

#### `_generate_file_doc_with_ai(data)`

Generate documentation for a file using AI

#### `_call_ai_api(prompt)`

Call the OpenRouter API with the given prompt

#### `_create_file_doc_prompt(data)`

Create a prompt for generating file documentation

#### `_create_index_prompt(files_info, project_info)`

Create a prompt for generating index documentation

#### `_generate_readme(files_info)`

Generate README.md file for the project

## Usage Examples

While specific usage examples aren't directly present in the code, we can infer some general patterns:

1.  **Initialization:**

    ```python
    from autodocs.generators.ai_generator import AIGenerator

    config = {
        "api_key": "YOUR_OPENROUTER_API_KEY",  # Replace with your actual API key
        # Other configuration options, if any
    }
    generator = AIGenerator(config)
    ```

2.  **Generating Documentation:**

    ```python
    # Assuming 'parsed_data' is a dictionary containing parsed code information
    #  and 'output_path' is the directory where documentation should be saved.
    parsed_data = {
        "file1.py": {
            "classes": [...],
            "functions": [...],
            "docstring": "...",
        },
        # ... more files
    }
    output_path = "docs/"

    generator.generate(parsed_data, output_path)
    ```

3. **Prompt Generation (Conceptual):**
   The internal methods `_create_file_doc_prompt` and `_create_index_prompt` suggest how prompts are built for the AI.  They likely take the parsed code data and format it into a text prompt suitable for an LLM.  For example, `_create_file_doc_prompt` might take the code, docstrings, and function signatures and create a prompt like:  "Generate documentation for the following Python code: [code here]".

4. **API Call (Conceptual):**
   The `_call_ai_api` method indicates that the generated prompt is sent to the OpenRouter API.  This would involve making an HTTP request to the API endpoint with the prompt and receiving the generated documentation as a response.

5. **Sequential vs. Parallel (Conceptual):**
    The presence of `_generate_docs_sequential` and `_generate_docs_parallel` suggests that the generator can process files one at a time or concurrently.  The `generate` method likely chooses one of these approaches based on configuration or internal logic.

6. **Index and README Generation (Conceptual):**
    The `_generate_index` and `_generate_readme` methods suggest that the generator can create an index file (likely in Markdown) linking to all the generated documentation files, and a README.md file providing an overview of the project.  These would be generated after processing individual files.
```