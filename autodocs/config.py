import json
import os

DEFAULT_CONFIG = {
    'exclude': [],
    'include_private': False,
    'output': {
        'markdown': {
            'toc': True,
            'code_highlighting': True
        },
        'html': {
            'theme': 'default',
            'syntax_highlighting': True
        },
        'pdf': {
            'page_size': 'A4',
            'font_size': 11
        }
    }
}

def load_config(config_path=None):
    """Load configuration from file or use defaults"""
    config = DEFAULT_CONFIG.copy()
    
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            # Merge user config with defaults
            deep_merge(config, user_config)
    elif os.path.exists('autodocs.config.json'):
        with open('autodocs.config.json', 'r') as f:
            user_config = json.load(f)
            deep_merge(config, user_config)
    
    return config

def deep_merge(base, update):
    """Recursively merge two dictionaries"""
    for key, value in update.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            deep_merge(base[key], value)
        else:
            base[key] = value