class BaseParser:
    """Base class for all language parsers"""
    
    def __init__(self, config=None):
        self.config = config or {}
        
    def parse(self, file_path):
        """
        Parse a file and extract documentation
        
        Args:
            file_path: Path to the file to parse
            
        Returns:
            dict: Parsed documentation data
        """
        raise NotImplementedError("Subclasses must implement parse()")
    
    def extract_docstring(self, text):
        """Extract docstring from text"""
        raise NotImplementedError("Subclasses must implement extract_docstring()")