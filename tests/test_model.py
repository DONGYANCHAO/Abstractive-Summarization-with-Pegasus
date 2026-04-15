import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestModelModule:
    """Test cases for model.py module"""

    @patch('model.PegasusTokenizer.from_pretrained')
    @patch('model.PegasusForConditionalGeneration.from_pretrained')
    def test_tokenizer_initialization(self, mock_model, mock_tokenizer):
        """Test tokenizer is initialized with correct model name"""
        mock_tokenizer.return_value = MagicMock()
        mock_model.return_value = MagicMock()
        
        import importlib
        import model
        importlib.reload(model)
        
        mock_tokenizer.assert_called_once_with("google/pegasus-xsum")

    @patch('model.PegasusTokenizer.from_pretrained')
    @patch('model.PegasusForConditionalGeneration.from_pretrained')
    def test_model_initialization(self, mock_model_cls, mock_tokenizer):
        """Test model is initialized with correct model name"""
        mock_tokenizer.return_value = MagicMock()
        mock_model_cls.return_value = MagicMock()
        
        import importlib
        import model
        importlib.reload(model)
        
        mock_model_cls.assert_called_once_with("google/pegasus-xsum")

    @patch('model.PegasusTokenizer.from_pretrained')
    @patch('model.PegasusForConditionalGeneration.from_pretrained')
    def test_model_name_constant(self, mock_model, mock_tokenizer):
        """Test MODEL_NAME constant is correct"""
        import importlib
        import model
        importlib.reload(model)
        
        assert model.MODEL_NAME == "google/pegasus-xsum"
