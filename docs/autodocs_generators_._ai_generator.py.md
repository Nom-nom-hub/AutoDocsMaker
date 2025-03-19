# ._ai_generator.py

## File Path

`./autodocs/generators/._ai_generator.py`

## Overview

This module provides a base class for AI-powered documentation generators. It defines the core structure and methods for interacting with an AI model to generate documentation content. Subclasses can implement specific logic for different documentation formats or AI models.

## Quick Reference

*   `BaseAIGenerator`: Base class for AI-powered documentation generators.
    *   `__init__(self, model_name: str, api_key: str)`: Initializes the generator with the AI model name and API key.
    *   `generate_text(self, prompt: str) -> str`: Abstract method to generate text based on a given prompt.
    *   `generate_documentation(self, code: str, docstring: str = "") -> str`: Generates documentation for a given code snippet.

## Detailed Documentation

### `BaseAIGenerator`

Base class for AI-powered documentation generators.

#### `__init__(self, model_name: str, api_key: str)`

Initializes the generator with the AI model name and API key.

*   **Parameters:**
    *   `model_name` (str): The name of the AI model to use (e.g., "gpt-3.5-turbo").
    *   `api_key` (str): The API key for accessing the AI model.

#### `generate_text(self, prompt: str) -> str`

Abstract method to generate text based on a given prompt.  This method *must* be implemented by subclasses.

*   **Parameters:**
    *   `prompt` (str): The prompt to send to the AI model.
*   **Returns:**
    *   str: The generated text from the AI model.
*   **Raises:**
    *   `NotImplementedError`: If the method is not implemented by a subclass.

#### `generate_documentation(self, code: str, docstring: str = "") -> str`

Generates documentation for a given code snippet. This method constructs a prompt using the provided code and optional existing docstring, then calls `generate_text` to get the AI-generated documentation.

*   **Parameters:**
    *   `code` (str): The code snippet to generate documentation for.
    *   `docstring` (str, optional): An existing docstring to include in the prompt. Defaults to "".
*   **Returns:**
    *   str: The generated documentation from the AI model.

## Usage Examples

```python
# Assuming a subclass of BaseAIGenerator is defined (e.g., OpenAIGenerator)
# and that the necessary API key is set up.

# Example 1: Generating documentation for a simple function
from autodocs.generators._ai_generator import BaseAIGenerator

class MockAIGenerator(BaseAIGenerator):
    def __init__(self, model_name: str, api_key: str):
        super().__init__(model_name, api_key)

    def generate_text(self, prompt: str) -> str:
        # Simulate AI response for testing
        if "def add" in prompt:
            return "This function adds two numbers."
        return "Generated documentation."

# Create an instance of the generator
generator = MockAIGenerator(model_name="mock_model", api_key="mock_api_key")

# Code snippet
code_snippet = """
def add(a, b):
    \"\"\"Adds two numbers.\"\"\"
    return a + b
"""

# Generate documentation
generated_doc = generator.generate_documentation(code_snippet)
print(generated_doc)

# Example 2: Using an existing docstring
existing_docstring = "This function calculates the sum of a list of numbers."
code_snippet_2 = """
def sum_list(numbers):
    return sum(numbers)
"""
generated_doc_2 = generator.generate_documentation(code_snippet_2, existing_docstring)
print(generated_doc_2)
```