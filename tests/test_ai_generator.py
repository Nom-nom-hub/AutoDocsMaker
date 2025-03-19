import os
import pytest
from unittest.mock import patch, MagicMock
from autodocs.generators.ai_generator import AIGenerator

class TestAIGenerator:
    """Test cases for the AIGenerator class"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.config = {
            'openrouter_api_key': 'test_key',
            'ai_model': 'test_model',
            'project': {
                'name': 'Test Project',
                'description': 'A test project'
            }
        }
        self.generator = AIGenerator(self.config)
    
    @patch('requests.post')
    def test_call_ai_api(self, mock_post):
        """Test the _call_ai_api method"""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'Test response'}}]
        }
        mock_post.return_value = mock_response
        
        # Call the method
        result = self.generator._call_ai_api("Test prompt")
        
        # Verify the result
        assert result == 'Test response'
        
        # Verify the API was called correctly
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        assert kwargs['json']['model'] == 'test_model'
        assert kwargs['headers']['Authorization'] == 'Bearer test_key'
    
    @patch('autodocs.generators.ai_generator.AIGenerator._call_ai_api')
    def test_generate_file_doc_with_ai(self, mock_call_api):
        """Test the _generate_file_doc_with_ai method"""
        # Setup mock response
        mock_call_api.return_value = "# Test Documentation\n\nThis is a test."
        
        # Test data
        data = {
            'module_name': 'test_module',
            'module_doc': 'Test module documentation',
            'classes': [],
            'functions': []
        }
        
        # Call the method
        result = self.generator._generate_file_doc_with_ai(data)
        
        # Verify the result
        assert "# Test Documentation" in result
        assert mock_call_api.called