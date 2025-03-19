import os

class MarkdownGenerator:
    """
    Generator for Markdown documentation.
    
    This class converts parsed code data into Markdown documentation files.
    It creates an index file and individual documentation files for each
    module in the codebase.
    
    Example:
        ```python
        generator = MarkdownGenerator(config)
        generator.generate(parsed_data, "docs/")
        ```
    """
    
    def __init__(self, config=None):
        """
        Initialize the Markdown generator.
        
        Args:
            config (dict, optional): Configuration dictionary with Markdown
                formatting options. Defaults to empty dict.
        """
        self.config = config or {}
    
    def generate(self, parsed_data, output_path):
        """
        Generate Markdown documentation from parsed data
        
        Args:
            parsed_data: Dictionary of parsed file data
            output_path: Directory to write output files
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # Generate index file
        self._generate_index(parsed_data, output_path)
        
        # Generate individual files
        for file_path, data in parsed_data.items():
            if 'error' in data:
                continue
                
            rel_path = os.path.relpath(file_path)
            output_file = os.path.join(
                output_path, 
                rel_path.replace('/', '_').replace('\\', '_') + '.md'
            )
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(self._generate_file_doc(data))
    
    def _generate_index(self, parsed_data, output_path):
        """Generate index file with links to all documentation"""
        with open(os.path.join(output_path, 'index.md'), 'w', encoding='utf-8') as f:
            # Title and project name
            project_name = self.config.get('project', {}).get('name', 'Project Documentation')
            f.write(f"# {project_name} Documentation\n\n")
            
            # Overview section
            f.write("## Overview\n\n")
            if self.config.get('project', {}).get('description'):
                f.write(f"{self.config.get('project', {}).get('description')}\n\n")
            
            # Installation section
            f.write("## Installation\n\n")
            f.write("```bash\npip install autodocs\n```\n\n")
            
            # Quick Start section
            f.write("## Quick Start\n\n")
            f.write("Run AutoDocs on your project:\n\n")
            f.write("```bash\nautodocs --input ./src --output ./docs --format markdown\n```\n\n")
            
            # Configuration section
            f.write("## Configuration\n\n")
            f.write("AutoDocs can be configured using a `autodocs.config.json` file in your project root:\n\n")
            f.write("```json\n{\n  \"exclude\": [\"venv/\", \"node_modules/\"],\n  \"include_private\": false,\n  \"project\": {\n    \"name\": \"Your Project\",\n    \"description\": \"Project description\"\n  }\n}\n```\n\n")
            
            # Supported Languages section
            f.write("## Supported Languages\n\n")
            f.write("- Python (fully supported)\n")
            f.write("- JavaScript (coming soon)\n")
            f.write("- Java (coming soon)\n")
            f.write("- C++ (coming soon)\n\n")
            
            # Table of Contents
            f.write("## Table of Contents\n\n")
            
            # Group by directories
            modules_by_dir = {}
            for file_path, data in parsed_data.items():
                if 'error' in data:
                    continue
                    
                dir_name = os.path.dirname(file_path) or "root"
                if dir_name not in modules_by_dir:
                    modules_by_dir[dir_name] = []
                
                rel_path = os.path.relpath(file_path)
                doc_path = rel_path.replace('/', '_').replace('\\', '_') + '.md'
                
                modules_by_dir[dir_name].append({
                    'name': data.get('module_name', os.path.basename(file_path)),
                    'path': doc_path,
                    'description': data.get('module_doc', '').split('\n')[0] if data.get('module_doc') else ''
                })
            
            # Write grouped TOC
            for dir_name, modules in sorted(modules_by_dir.items()):
                if dir_name != "root":
                    f.write(f"### {dir_name}\n\n")
                
                for module in sorted(modules, key=lambda m: m['name']):
                    desc = f" - {module['description']}" if module['description'] else ""
                    f.write(f"- [{module['name']}]({module['path']}){desc}\n")
                
                f.write("\n")
    
    def _generate_file_doc(self, data):
        """Generate documentation for a single file"""
        output = []
        
        # File header
        output.append(f"# {data['module_name']}\n")
        output.append(f"**File:** `{data['file_path']}`\n\n")
        
        # Module docstring
        if data.get('module_doc'):
            output.append(f"{data['module_doc']}\n\n")
        
        # Quick reference/TOC
        output.append("## Quick Reference\n\n")
        
        if data.get('classes'):
            output.append("**Classes:**\n")
            for cls in data['classes']:
                output.append(f"- [`{cls['name']}`](#class-{cls['name'].lower()})\n")
            output.append("\n")
        
        if data.get('functions'):
            output.append("**Functions:**\n")
            for func in data['functions']:
                output.append(f"- [`{func['name']}`](#function-{func['name'].lower()})\n")
            output.append("\n")
        
        # Classes
        if data.get('classes'):
            output.append("## Classes\n\n")
            for cls in data['classes']:
                output.append(self._format_class(cls))
        
        # Functions
        if data.get('functions'):
            output.append("## Functions\n\n")
            for func in data['functions']:
                output.append(self._format_function(func))
        
        return "\n".join(output)
    
    def _format_class(self, cls):
        """Format a class for markdown output"""
        output = []
        
        output.append(f"### `{cls['name']}`\n")
        
        if cls.get('docstring'):
            output.append(f"{cls['docstring']}\n\n")
        
        if cls.get('methods'):
            output.append("#### Methods\n\n")
            for method in cls['methods']:
                output.append(self._format_function(method, is_method=True))
        
        return "\n".join(output)
    
    def _format_function(self, func, is_method=False):
        """Format a function for markdown output"""
        output = []
        
        prefix = "##### " if is_method else "### "
        output.append(f"{prefix}`{func['name']}({', '.join(func['args'])})`\n")
        
        if func.get('docstring'):
            output.append(f"{func['docstring']}\n\n")
        else:
            output.append("*No documentation available*\n\n")
        
        return "\n".join(output)
