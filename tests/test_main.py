import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMainModule:
    """Test cases for main.py module"""

    def test_main_calls_summarize_text(self):
        """Test that main.py calls summarize_text function"""
        mock_result = "Test summary result"
        
        with patch('summarize.summarize_text', return_value=mock_result) as mock_summarize:
            with patch('builtins.print'):
                if 'main' in sys.modules:
                    del sys.modules['main']
                import main
        
        assert mock_summarize.call_count >= 1

    def test_main_prints_result(self):
        """Test that main.py prints the summary result"""
        expected_summary = "This is the expected summary."
        
        with patch('summarize.summarize_text', return_value=expected_summary):
            with patch('builtins.print') as mock_print:
                if 'main' in sys.modules:
                    del sys.modules['main']
                import main
        
        printed_calls = [str(call) for call in mock_print.call_args_list]
        assert any(expected_summary in str(call) for call in printed_calls)
