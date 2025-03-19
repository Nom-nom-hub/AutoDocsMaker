# config

## File Path

`./autodocs/config.py`

## Overview

This module provides functions for loading and merging configuration data. It includes a function to load configuration from a file, using default values if the file is not found, and a function to recursively merge two dictionaries.

## Quick Reference

**Functions:**

*   `load_config(config_path)`: Load configuration from file or use defaults
*   `deep_merge(base, update)`: Recursively merge two dictionaries

## Detailed Documentation

### `load_config(config_path)`

Loads configuration data from a specified file path. If the file does not exist, it returns a default configuration (implementation details not provided in the code).

**Parameters:**

*   `config_path` (str): The path to the configuration file.

**Returns:**

*   dict: A dictionary containing the loaded configuration data.

**Raises:**

*   (Potentially) FileNotFoundError: If the config file is not found and default values are not handled gracefully. (This is an assumption based on the docstring.)

**Usage Examples:**

```python
# Assuming a config file exists at 'my_config.yaml'
config = load_config('my_config.yaml')
print(config)
```

```python
# Assuming 'my_config.yaml' does not exist, and default values are used
config = load_config('my_config.yaml')
print(config) # Prints the default configuration
```

### `deep_merge(base, update)`

Recursively merges two dictionaries.  The `update` dictionary's values will overwrite corresponding values in the `base` dictionary. If a value in `update` is a dictionary and the corresponding value in `base` is also a dictionary, the merge is performed recursively.

**Parameters:**

*   `base` (dict): The base dictionary to merge into.
*   `update` (dict): The dictionary containing updates.

**Returns:**

*   dict: A new dictionary that is the result of the deep merge.  The original `base` dictionary is not modified (assuming the function creates a copy internally).

**Usage Examples:**

```python
base_config = {
    'database': {
        'host': 'localhost',
        'port': 5432
    },
    'logging': {
        'level': 'INFO'
    }
}

update_config = {
    'database': {
        'port': 8000,
        'user': 'admin'
    },
    'cache': {
        'enabled': True
    }
}

merged_config = deep_merge(base_config, update_config)

print(merged_config)
# Expected Output:
# {
#     'database': {
#         'host': 'localhost',
#         'port': 8000,
#         'user': 'admin'
#     },
#     'logging': {
#         'level': 'INFO'
#     },
#     'cache': {
#         'enabled': True
#     }
# }

print(base_config) # base_config is unchanged
# Expected Output:
# {
#     'database': {
#         'host': 'localhost',
#         'port': 5432
#     },
#     'logging': {
#         'level': 'INFO'
#     }
# }
```