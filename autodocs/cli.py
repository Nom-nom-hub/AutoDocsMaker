"""
Command-line interface for AutoDocs.

This module provides the entry point for the AutoDocs tool when used from
the command line. It handles argument parsing, configuration loading, and
orchestrates the documentation generation process.

Usage:
    autodocs --input ./src --output ./docs --format markdown
    autodocs -i ./src -o ./docs -f html
"""

import argparse
import os
import sys
import logging
from .config import load_config
from .parsers import get_parser_for_file
from .generators import generate_documentation

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger('autodocs')

def main():
    parser = argparse.ArgumentParser(description='AutoDocs - Automatic Documentation Generator')
    parser.add_argument('--input', '-i', required=True, help='Input directory or file')
    parser.add_argument('--output', '-o', required=True, help='Output directory')
    parser.add_argument('--format', '-f', choices=['markdown', 'html', 'pdf', 'ai'], default='markdown',
                        help='Output format (default: markdown)')
    parser.add_argument('--config', '-c', help='Path to config file (default: autodocs.config.json)')
    parser.add_argument('--api-key', '-k', help='OpenRouter API key for AI generation')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Load configuration
    logger.info(f"Loading configuration from {args.config or 'default location'}")
    config = load_config(args.config)
    
    # Override API key if provided
    if args.api_key:
        config['openrouter_api_key'] = args.api_key
        logger.info("Using API key from command line arguments")
    
    # Process files
    logger.info(f"Starting documentation generation for {args.input}")
    process_files(args.input, args.output, args.format, config)
    logger.info(f"Documentation generation complete. Output saved to {args.output}")

def process_files(input_path, output_path, format_type, config):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        logger.info(f"Created output directory: {output_path}")
    
    files_to_process = []
    
    if os.path.isfile(input_path):
        files_to_process.append(input_path)
        logger.info(f"Processing single file: {input_path}")
    else:
        logger.info(f"Scanning directory: {input_path}")
        for root, _, files in os.walk(input_path):
            for file in files:
                file_path = os.path.join(root, file)
                if should_process_file(file_path, config):
                    files_to_process.append(file_path)
    
    logger.info(f"Found {len(files_to_process)} files to process")
    
    parsed_data = {}
    for i, file_path in enumerate(files_to_process):
        logger.info(f"Parsing file {i+1}/{len(files_to_process)}: {file_path}")
        parser = get_parser_for_file(file_path)
        if parser:
            parsed_data[file_path] = parser.parse(file_path)
        else:
            logger.warning(f"No parser available for {file_path}")
    
    logger.info(f"Generating documentation in {format_type} format")
    generate_documentation(parsed_data, output_path, format_type, config)

def should_process_file(file_path, config):
    # Check if file should be excluded based on config
    if 'exclude' in config:
        for pattern in config['exclude']:
            if pattern in file_path:
                return False
    
    # Check if file extension is supported
    _, ext = os.path.splitext(file_path)
    return ext.lower() in ['.py', '.js', '.php', '.java', '.cpp', '.h']

if __name__ == '__main__':
    main()
