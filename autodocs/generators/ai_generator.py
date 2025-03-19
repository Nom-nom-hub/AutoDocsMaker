"""
AI-powered documentation generator using OpenRouter API.

This module provides functionality to generate documentation using
AI models through the OpenRouter API.
"""

import os
import requests
import json
from pathlib import Path
import logging
import time
import fnmatch  # Add fnmatch for pattern matching

# Optional tqdm import with fallback
try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False

logger = logging.getLogger('autodocs')

class AIGenerator:
    """
    Generator for AI-powered documentation.
    
    This class uses the OpenRouter API to generate documentation for code files
    using AI models like open-r1/olympiccoder-32b.
    """
    
    def __init__(self, config=None):
        """
        Initialize the AI generator.
        
        Args:
            config (dict, optional): Configuration dictionary with API settings.
                Defaults to empty dict.
        """
        self.config = config or {}
        self.api_key = self.config.get('openrouter_api_key', os.environ.get('OPENROUTER_API_KEY'))
        
        # Get AI model from config, with fallback to environment variable
        self.model = self.config.get('ai_model', 
                                    os.environ.get('AUTODOCS_AI_MODEL', 
                                    'google/gemini-2.0-flash-lite-preview-02-05:free'))
        
        # Allow custom API URL to support different AI providers
        self.api_url = self.config.get('ai_api_url', 
                                      os.environ.get('AUTODOCS_AI_API_URL', 
                                      "https://openrouter.ai/api/v1/chat/completions"))
        
        # Add temperature and max tokens parameters
        self.temperature = float(self.config.get('ai_temperature', 0.3))  # Lower temperature for more focused docs
        self.max_tokens = int(self.config.get('ai_max_tokens', 4000))  # Reasonable limit for docs
        
        # Add parallel processing option
        self.parallel = self.config.get('parallel_processing', False)
        self.max_workers = int(self.config.get('max_workers', 4))
        
        # Add rate limiting to avoid API throttling
        self.rate_limit = float(self.config.get('rate_limit_seconds', 1.0))
        self.last_request_time = 0
        
        logger.info(f"AI Generator initialized with model: {self.model}")
        
    def generate(self, parsed_data, output_path):
        """
        Generate AI-powered documentation from parsed data
    
        Args:
            parsed_data: Dictionary of parsed file data
            output_path: Directory to write output files
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # Check if API key is available
        self.api_key = self.config.get('openrouter_api_key') or os.environ.get('OPENROUTER_API_KEY')
        if not self.api_key:
            logger.error("OpenRouter API key is required for AI documentation generation.")
            logger.error("Set it in config file or OPENROUTER_API_KEY environment variable.")
            return
        
        # Add project root directory to config if not present
        if 'project' not in self.config:
            self.config['project'] = {}
        
        # Try to determine project root from input files
        if parsed_data:
            # Get the common prefix of all file paths
            file_paths = list(parsed_data.keys())
            common_prefix = os.path.commonpath(file_paths) if file_paths else os.getcwd()
            self.config['project']['root_dir'] = common_prefix
        else:
            self.config['project']['root_dir'] = os.getcwd()
        
        logger.info(f"Using project root directory: {self.config['project']['root_dir']}")
        
        # Generate index file
        logger.info("Generating index documentation using AI...")
        self._generate_index(parsed_data, output_path)
        
        # Generate individual files
        file_count = len(parsed_data)
        current = 0
        
        # Use tqdm for progress bar if available
        try:
            from tqdm import tqdm
            file_iterator = tqdm(parsed_data.items(), total=file_count, desc="Generating file documentation")
        except ImportError:
            file_iterator = parsed_data.items()
            logger.info(f"Processing {file_count} files...")
        
        for file_path, data in file_iterator:
            current += 1
            rel_path = os.path.relpath(file_path)
            
            # Create a more readable output filename
            output_file = os.path.join(
                output_path, 
                rel_path.replace('/', '_').replace('\\', '_') + '.md'
            )
            
            if not isinstance(file_iterator, dict):  # If using tqdm
                pass  # tqdm handles the progress display
            else:
                logger.info(f"Generating documentation for file {current}/{file_count}: {rel_path}")
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Generate documentation using AI
            doc_content = self._generate_file_doc_with_ai(data)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            logger.info(f"Documentation saved to {output_file}")

    def _generate_docs_sequential(self, valid_files, output_path):
        """Generate documentation sequentially for each file"""
        file_count = len(valid_files)
        current = 0
        
        # Create a progress bar if tqdm is available
        try:
            from tqdm import tqdm
            file_iterator = tqdm(valid_files.items(), total=file_count, desc="Generating docs")
        except ImportError:
            file_iterator = valid_files.items()
        
        for file_path, data in file_iterator:
            current += 1
            rel_path = os.path.relpath(file_path)
            
            # Create a more readable output filename
            output_file = os.path.join(
                output_path, 
                rel_path.replace('/', '_').replace('\\', '_') + '.md'
            )
            
            if not isinstance(file_iterator, dict):  # If using tqdm
                pass  # tqdm handles the progress display
            else:
                logger.info(f"Generating documentation for file {current}/{file_count}: {rel_path}")
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Generate documentation using AI
            doc_content = self._generate_file_doc_with_ai(data)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(doc_content)
            
            logger.info(f"Documentation saved to {output_file}")

    def _generate_docs_parallel(self, valid_files, output_path):
        """Generate documentation in parallel for each file"""
        import concurrent.futures
        import time
        
        logger.info(f"Generating documentation in parallel with {self.max_workers} workers")
        
        # Prepare the tasks
        tasks = []
        for file_path, data in valid_files.items():
            rel_path = os.path.relpath(file_path)
            output_file = os.path.join(
                output_path, 
                rel_path.replace('/', '_').replace('\\', '_') + '.md'
            )
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            tasks.append((data, output_file, rel_path))
        
        # Process files in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_file = {
                executor.submit(self._process_file, data, output_file): rel_path
                for data, output_file, rel_path in tasks
            }
            
            # Process results as they complete
            try:
                from tqdm import tqdm
                for future in tqdm(concurrent.futures.as_completed(future_to_file), 
                                  total=len(future_to_file),
                                  desc="Generating docs"):
                    rel_path = future_to_file[future]
                    try:
                        future.result()  # This will raise any exceptions that occurred
                    except Exception as e:
                        logger.error(f"Error processing {rel_path}: {str(e)}")
            except ImportError:
                for future in concurrent.futures.as_completed(future_to_file):
                    rel_path = future_to_file[future]
                    try:
                        future.result()
                        logger.info(f"Completed documentation for {rel_path}")
                    except Exception as e:
                        logger.error(f"Error processing {rel_path}: {str(e)}")

    def _process_file(self, data, output_file):
        """Process a single file for parallel execution"""
        # Apply rate limiting
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < self.rate_limit:
            time.sleep(self.rate_limit - time_since_last)
        
        # Generate documentation using AI
        doc_content = self._generate_file_doc_with_ai(data)
        self.last_request_time = time.time()
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(doc_content)
        
        return output_file

    def _generate_index(self, parsed_data, output_path):
        """Generate index file with links to all documentation"""
        # Collect information about all files
        files_info = []
        for file_path, data in parsed_data.items():
            if 'error' in data:
                continue
                
            rel_path = os.path.relpath(file_path)
            doc_path = rel_path.replace('/', '_').replace('\\', '_') + '.md'
            
            files_info.append({
                'name': data.get('module_name', os.path.basename(file_path)),
                'path': doc_path,
                'description': data.get('module_doc', '').split('\n')[0] if data.get('module_doc') else '',
                'file_path': file_path
            })
        
        # Generate index using AI
        prompt = self._create_index_prompt(files_info, self.config.get('project', {}))
        index_content = self._call_ai_api(prompt)
        
        with open(os.path.join(output_path, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        logger.info(f"Index documentation saved to {os.path.join(output_path, 'index.md')}")
        
        return index_content
    
    def _generate_file_doc_with_ai(self, data):
        """Generate documentation for a file using AI"""
        prompt = self._create_file_doc_prompt(data)
        response = self._call_ai_api(prompt)
        
        # Remove any wrapping triple backticks if present
        if response.startswith("```") and response.endswith("```"):
            # If it starts with ```markdown or similar
            if "\n" in response[:20]:
                first_line_end = response.find("\n")
                if "```" in response[:first_line_end]:
                    response = response[first_line_end+1:]
            else:
                response = response[3:]  # Remove opening ```
                
            if response.endswith("```"):
                response = response[:-3]  # Remove closing ```
        
        return response.strip()
    
    def _call_ai_api(self, prompt):
        """Call the OpenRouter API with the given prompt"""
        if not self.api_key:
            raise ValueError("OpenRouter API key is required. Set it in config or OPENROUTER_API_KEY environment variable.")
        
        logger.debug(f"Calling AI API with model: {self.model}")
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": self.config.get('site_url', 'https://autodocs.dev'),  # For attribution
            "X-Title": self.config.get('project', {}).get('name', 'AutoDocs')     # For attribution
        }
        
        # Create system prompt with more detailed instructions
        system_prompt = """You are a documentation expert specializing in software documentation.
Generate clear, concise, and helpful documentation for code.
Focus on explaining the purpose, usage patterns, and important details.
Use proper Markdown formatting with headers, code blocks, and lists.
Be thorough but avoid unnecessary verbosity.
Include usage examples where possible.
IMPORTANT: Do not wrap the entire response in triple backticks (```). Only use backticks for code blocks within the document."""

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        
        # Add retry logic for API calls
        max_retries = 3
        retry_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                logger.debug("Sending request to OpenRouter API...")
                response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
                response.raise_for_status()
                result = response.json()
                logger.debug("Received response from OpenRouter API")
                content = result['choices'][0]['message']['content']
                
                # Strip any wrapping triple backticks if present
                if content.startswith("```markdown") and content.endswith("```"):
                    content = content[len("```markdown"):].rstrip("```").strip()
                elif content.startswith("```") and content.endswith("```"):
                    content = content[3:].rstrip("```").strip()
                    
                return content
            except requests.exceptions.Timeout:
                logger.warning(f"API request timed out (attempt {attempt+1}/{max_retries})")
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    logger.error("All retry attempts failed")
                    return "# Error Generating Documentation\n\nThe API request timed out after multiple attempts. Please try again later."
            except requests.exceptions.HTTPError as e:
                logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
                if e.response.status_code >= 500 and attempt < max_retries - 1:  # Server error, retry
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    return f"# Error Generating Documentation\n\nHTTP error: {e.response.status_code}\n\n```\n{e.response.text}\n```"
            except Exception as e:
                logger.error(f"Error calling AI API: {str(e)}")
                return f"# Error Generating Documentation\n\nAn error occurred while generating documentation: {str(e)}"

    def _create_file_doc_prompt(self, data):
        """Create a prompt for generating file documentation"""
        prompt = f"Generate markdown documentation for the following code:\n\n"
        prompt += f"File: {data['file_path']}\n"
        prompt += f"Module name: {data.get('module_name', os.path.basename(data['file_path']))}\n\n"
        
        if data.get('module_doc'):
            prompt += f"Module docstring:\n{data['module_doc']}\n\n"
        
        # Add code content with syntax highlighting if available
        if data.get('code_content'):
            file_ext = os.path.splitext(data['file_path'])[1].lstrip('.')
            lang = file_ext if file_ext else 'python'  # Default to python
            prompt += f"Code content:\n```{lang}\n{data['code_content']}\n```\n\n"
        
        # Add classes with better formatting
        if data.get('classes'):
            prompt += "Classes:\n"
            for cls in data['classes']:
                prompt += f"- Class: {cls['name']}\n"
                if cls.get('docstring'):
                    prompt += f"  Docstring: {cls['docstring']}\n"
                
                # Add class attributes if available
                if cls.get('attributes'):
                    prompt += "  Attributes:\n"
                    for attr in cls['attributes']:
                        prompt += f"  - {attr['name']}: {attr.get('type', '')}\n"
                        if attr.get('docstring'):
                            prompt += f"    {attr['docstring']}\n"
                
                # Add methods with better formatting
                if cls.get('methods'):
                    prompt += "  Methods:\n"
                    for method in cls['methods']:
                        args_str = ', '.join(method.get('args', []))
                        prompt += f"  - {method['name']}({args_str})\n"
                        if method.get('docstring'):
                            prompt += f"    Docstring: {method['docstring']}\n"
        
        # Add functions with better formatting
        if data.get('functions'):
            prompt += "Functions:\n"
            for func in data['functions']:
                args_str = ', '.join(func.get('args', []))
                prompt += f"- {func['name']}({args_str})\n"
                if func.get('docstring'):
                    prompt += f"  Docstring: {func['docstring']}\n"
        
        # Add imports if available
        if data.get('imports'):
            prompt += "Imports:\n"
            for imp in data['imports']:
                prompt += f"- {imp}\n"
        
        prompt += "\nCreate comprehensive markdown documentation for this file with the following sections:\n"
        prompt += "1. Title (module name)\n"
        prompt += "2. File Path\n"
        prompt += "3. Overview (from module docstring)\n"
        prompt += "4. Quick Reference (list of classes and functions)\n"
        prompt += "5. Detailed documentation for each class and function\n"
        prompt += "6. Usage examples (if you can infer them from the code)\n"
        
        return prompt
    
    def _create_index_prompt(self, files_info, project_info):
        """Create a prompt for generating index documentation"""
        prompt = "Generate a comprehensive index page for a software project with the following details:\n\n"
        
        # Add project info
        prompt += f"Project name: {project_info.get('name', 'AutoDocs')}\n"
        prompt += f"Project description: {project_info.get('description', 'An automatic documentation generator')}\n"
        prompt += f"Project usage: {project_info.get('usage', '')}\n\n"
        
        # Add files info
        prompt += "The project contains the following files that have been documented:\n\n"
        for file_info in files_info:
            prompt += f"- {file_info['path']}\n"
            if file_info.get('module_doc'):
                prompt += f"  Brief description: {file_info['module_doc']}\n"
        
        # Scan project directory to get actual file structure
        project_root = project_info.get('root_dir', os.getcwd())
        exclude_patterns = self.config.get('exclude', [])
        
        prompt += "\nThe complete project structure is:\n"
        
        for root, dirs, files in os.walk(project_root):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if not any(fnmatch.fnmatch(os.path.join(root, d), pattern) for pattern in exclude_patterns)]
            
            # Get relative path
            rel_path = os.path.relpath(root, project_root)
            if rel_path == '.':
                rel_path = ''
            
            # Skip excluded files
            files = [f for f in files if not any(fnmatch.fnmatch(os.path.join(root, f), pattern) for pattern in exclude_patterns)]
            
            # Add files to prompt
            for file in files:
                file_path = os.path.join(rel_path, file) if rel_path else file
                prompt += f"- {file_path}\n"
        
        # Add specific instructions
        prompt += "\nPlease create a markdown index page with the following sections:\n"
        prompt += "1. Overview - A brief description of the project\n"
        prompt += "2. Installation - How to install the project\n"
        prompt += "3. Quick Start Guide - Basic usage instructions\n"
        prompt += "4. Configuration Information - Available configuration options\n"
        prompt += "5. Table of Contents - A list of all the files in the project, organized by directory\n\n"
        
        # Important instruction for TOC
        prompt += "IMPORTANT: For the Table of Contents section, ONLY include the actual files listed in the project structure above. "
        prompt += "Organize them by directory and include links to each file using the format: [filename](path/to/file.md)\n"
        prompt += "For documentation files, link to the .md file that corresponds to the source file.\n"
        
        return prompt
