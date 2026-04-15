import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestSummarizeText:
    """Test cases for summarize_text function"""

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_returns_string(self, mock_model, mock_tokenizer):
        """Test that summarize_text returns a string"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "This is a summary."
        mock_model.generate.return_value = [[1, 2, 3, 4, 5]]
        
        from summarize import summarize_text
        
        result = summarize_text("Some input text")
        assert isinstance(result, str)

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_with_valid_input(self, mock_model, mock_tokenizer):
        """Test summarize_text with valid input"""
        expected_summary = "This is a test summary."
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = expected_summary
        mock_model.generate.return_value = [[1, 2, 3, 4, 5]]
        
        from summarize import summarize_text
        
        input_text = "This is a long text that needs to be summarized."
        result = summarize_text(input_text)
        
        assert result == expected_summary
        mock_tokenizer.assert_called_once()

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_empty_input(self, mock_model, mock_tokenizer):
        """Test summarize_text with empty input"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = ""
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        result = summarize_text("")
        assert isinstance(result, str)

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_truncation_enabled(self, mock_model, mock_tokenizer):
        """Test that truncation is enabled in tokenizer"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        summarize_text("Test text")
        
        call_kwargs = mock_tokenizer.call_args[1]
        assert call_kwargs['truncation'] is True

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_padding_enabled(self, mock_model, mock_tokenizer):
        """Test that padding is enabled in tokenizer"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        summarize_text("Test text")
        
        call_kwargs = mock_tokenizer.call_args[1]
        assert call_kwargs['padding'] is True

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_max_length_parameter(self, mock_model, mock_tokenizer):
        """Test that max_length is passed to model.generate"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        summarize_text("Test text")
        
        call_kwargs = mock_model.generate.call_args[1]
        assert 'max_length' in call_kwargs
        assert call_kwargs['max_length'] == 60

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_num_beams_parameter(self, mock_model, mock_tokenizer):
        """Test that num_beams is passed to model.generate"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        summarize_text("Test text")
        
        call_kwargs = mock_model.generate.call_args[1]
        assert 'num_beams' in call_kwargs
        assert call_kwargs['num_beams'] == 5

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_early_stopping(self, mock_model, mock_tokenizer):
        """Test that early_stopping is enabled in model.generate"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        summarize_text("Test text")
        
        call_kwargs = mock_model.generate.call_args[1]
        assert call_kwargs['early_stopping'] is True

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_skip_special_tokens(self, mock_model, mock_tokenizer):
        """Test that skip_special_tokens is enabled in decode"""
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        summarize_text("Test text")
        
        decode_kwargs = mock_tokenizer.decode.call_args[1]
        assert decode_kwargs['skip_special_tokens'] is True

    @patch('summarize.tokenizer')
    @patch('summarize.model')
    def test_summarize_text_long_input(self, mock_model, mock_tokenizer):
        """Test summarize_text with long input text"""
        long_text = " ".join(["word"] * 1000)
        mock_tokenizer.return_value = {'input_ids': MagicMock(), 'attention_mask': MagicMock()}
        mock_tokenizer.decode.return_value = "Short summary"
        mock_model.generate.return_value = [[1, 2, 3]]
        
        from summarize import summarize_text
        
        result = summarize_text(long_text)
        assert result == "Short summary"


class TestModelLoading:
    """Test cases for model loading"""

    @patch('model.PegasusTokenizer.from_pretrained')
    @patch('model.PegasusForConditionalGeneration.from_pretrained')
    def test_model_uses_correct_model_name(self, mock_model_cls, mock_tokenizer_cls):
        """Test that correct model name is used"""
        mock_tokenizer_cls.return_value = MagicMock()
        mock_model_cls.return_value = MagicMock()
        
        import importlib
        import model as model_module
        importlib.reload(model_module)
        
        mock_tokenizer_cls.assert_called_with("google/pegasus-xsum")
        mock_model_cls.assert_called_with("google/pegasus-xsum")
