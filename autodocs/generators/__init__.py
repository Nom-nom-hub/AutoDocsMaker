from .markdown_generator import MarkdownGenerator
from .ai_generator import AIGenerator
# Import other generators as they're implemented

def generate_documentation(parsed_data, output_path, format_type, config):
    """
    Generate documentation in the specified format
    
    Args:
        parsed_data: Dictionary of parsed file data
        output_path: Directory to write output files
        format_type: Type of documentation to generate (markdown, html, pdf, ai)
        config: Configuration dictionary
    """
    if format_type == 'markdown':
        generator = MarkdownGenerator(config)
        generator.generate(parsed_data, output_path)
    elif format_type == 'html':
        # generator = HTMLGenerator(config)
        # generator.generate(parsed_data, output_path)
        print("HTML generation not implemented yet")
    elif format_type == 'pdf':
        # generator = PDFGenerator(config)
        # generator.generate(parsed_data, output_path)
        print("PDF generation not implemented yet")
    elif format_type == 'ai':
        generator = AIGenerator(config)
        generator.generate(parsed_data, output_path)
    else:
        raise ValueError(f"Unsupported format: {format_type}")
