# ._base_parser.py

## File Path

./autodocs/parsers/._base_parser.py

## Overview

This module defines the base class for all parsers. It provides a common interface and handles basic functionalities like registering and retrieving parser types.

## Quick Reference

**Classes:**

*   `BaseParser`: The base class for all parsers.

**Functions:**

*   `register_parser(parser_type: str, parser_class: type) -> None`: Registers a parser class with a given type.
*   `get_parser(parser_type: str) -> type | None`: Retrieves a registered parser class by its type.

## Detailed Documentation

### `BaseParser` Class

The base class for all parsers. It provides a common interface and handles basic functionalities.

**Methods:**

*   `__init__(self, *args, **kwargs)`: Initializes the parser.  Accepts arbitrary arguments.
*   `parse(self, data: str) -> dict`: Abstract method to parse the input data.  Must be implemented by subclasses.  Returns a dictionary containing the parsed data.

### `register_parser(parser_type: str, parser_class: type) -> None` Function

Registers a parser class with a given type. This allows parsers to be looked up by their type string.

**Parameters:**

*   `parser_type`: The string identifier for the parser (e.g., "json", "xml").
*   `parser_class`: The parser class to register (must be a subclass of `BaseParser`).

**Returns:**

*   `None`

### `get_parser(parser_type: str) -> type | None` Function

Retrieves a registered parser class by its type.

**Parameters:**

*   `parser_type`: The string identifier of the parser to retrieve.

**Returns:**

*   The parser class if found, otherwise `None`.

## Usage Examples

While specific usage examples are not directly available from the code, here's how you would typically use the functions:

```python
from autodocs.parsers._base_parser import BaseParser, register_parser, get_parser

# Define a simple parser (this would typically be in a separate file)
class MyParser(BaseParser):
    def parse(self, data: str) -> dict:
        return {"parsed_data": data.upper()}

# Register the parser
register_parser("my_parser", MyParser)

# Retrieve the parser
parser_class = get_parser("my_parser")

if parser_class:
    # Instantiate the parser
    parser = parser_class()

    # Parse some data
    data = "hello world"
    parsed_data = parser.parse(data)
    print(parsed_data) # Output: {'parsed_data': 'HELLO WORLD'}
else:
    print("Parser not found")
```