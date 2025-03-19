import ast
import os
from .base_parser import BaseParser

class PythonParser(BaseParser):
    """Parser for Python files"""
    
    def parse(self, file_path):
        """
        Parse a Python file and extract documentation
        
        Args:
            file_path: Path to the Python file
        
        Returns:
            Dictionary with parsed documentation data
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source = f.read()
            
            tree = ast.parse(source)
            
            # Get module docstring
            module_doc = ast.get_docstring(tree)
            
            # Extract module name from file path
            module_name = os.path.basename(file_path)
            if module_name.endswith('.py'):
                module_name = module_name[:-3]
            
            # Extract classes and functions
            classes = []
            functions = []
            
            for node in ast.iter_child_nodes(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(self._parse_class(node))
                elif isinstance(node, ast.FunctionDef):
                    # Skip private functions if configured
                    if not node.name.startswith('_') or self.include_private:
                        functions.append(self._parse_function(node))
            
            return {
                'file_path': file_path,
                'module_name': module_name,
                'module_doc': module_doc,
                'classes': classes,
                'functions': functions
            }
        except Exception as e:
            return {
                'file_path': file_path,
                'error': str(e)
            }
    
    def _parse_class(self, node):
        """Parse a class definition"""
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.append(self._parse_function(item))
        
        return {
            'name': node.name,
            'docstring': ast.get_docstring(node),
            'methods': methods,
            'line_number': node.lineno
        }
    
    def _parse_function(self, node):
        """Parse a function definition"""
        docstring = ast.get_docstring(node) or ""
        
        # Extract return type from docstring if available
        return_info = ""
        if "Returns:" in docstring:
            return_section = docstring.split("Returns:")[1].strip()
            return_info = return_section.split("\n\n")[0].strip()
        
        # Extract parameters with types if available
        params = []
        for arg in node.args.args:
            if arg.arg != 'self':
                params.append(arg.arg)
        
        return {
            'name': node.name,
            'args': params,
            'docstring': docstring,
            'return_info': return_info,
            'lineno': node.lineno
        }
    
    def _parse_import(self, node):
        """Parse an import statement"""
        if isinstance(node, ast.Import):
            return {'type': 'import', 'names': [n.name for n in node.names]}
        else:  # ImportFrom
            return {
                'type': 'import_from',
                'module': node.module,
                'names': [n.name for n in node.names]
            }
