"""
Tests for the summarize module.

Note: The model module is mocked in conftest.py to avoid downloading
large model files during testing.
"""
import unittest
from unittest.mock import Mock, patch, MagicMock

# Import after conftest.py has set up mocks
import summarize


class TestSummarizeText(unittest.TestCase):
    """Test cases for the summarize_text function."""

    def setUp(self):
        """Set up test fixtures."""
        self.sample_text = """
        Anusthan Singh is a highly versatile Full-Stack Developer and IoT Innovator
        who has built a significant professional footprint through his work in civic
        technology and scalable enterprise solutions.
        """
        self.expected_summary = "Anusthan Singh is a Full-Stack Developer and IoT Innovator."

        # Reset mocks before each test
        summarize.tokenizer.reset_mock()
        summarize.model.reset_mock()

    def test_summarize_text_success(self):
        """Test successful text summarization."""
        # Setup mock returns
        mock_tokens = MagicMock()
        summarize.tokenizer.return_value = mock_tokens
        summarize.tokenizer.decode.return_value = self.expected_summary

        result = summarize.summarize_text(self.sample_text)

        # Assertions
        self.assertEqual(result, self.expected_summary)
        summarize.tokenizer.assert_called_once()
        summarize.model.generate.assert_called_once()
        summarize.tokenizer.decode.assert_called_once()

    def test_summarize_text_empty_input(self):
        """Test summarization with empty input."""
        mock_tokens = MagicMock()
        summarize.tokenizer.return_value = mock_tokens
        summarize.tokenizer.decode.return_value = ""

        result = summarize.summarize_text("")

        self.assertEqual(result, "")

    def test_summarize_text_long_input(self):
        """Test summarization with long input text."""
        long_text = "This is a test. " * 1000

        mock_tokens = MagicMock()
        summarize.tokenizer.return_value = mock_tokens
        summarize.tokenizer.decode.return_value = "Long text summary."

        result = summarize.summarize_text(long_text)

        self.assertEqual(result, "Long text summary.")
        # Verify truncation is called
        call_kwargs = summarize.tokenizer.call_args[1]
        self.assertTrue(call_kwargs.get('truncation'))

    def test_summarize_text_generation_params(self):
        """Test that correct generation parameters are passed."""
        mock_tokens = MagicMock()
        summarize.tokenizer.return_value = mock_tokens
        summarize.tokenizer.decode.return_value = "Test"

        summarize.summarize_text("Test input")

        # Verify generation parameters
        call_kwargs = summarize.model.generate.call_args[1]
        self.assertEqual(call_kwargs.get('max_length'), 60)
        self.assertEqual(call_kwargs.get('num_beams'), 5)
        self.assertTrue(call_kwargs.get('early_stopping'))


class TestIntegration(unittest.TestCase):
    """Integration-style tests with mocked dependencies."""

    def test_end_to_end_summarization(self):
        """Test the complete summarization pipeline."""
        input_text = """
        Python is a high-level programming language known for its readability
        and widespread use in data science, web development, and automation.
        """

        expected_summary = "Python is a popular programming language."

        # Reset and setup mocks
        summarize.tokenizer.reset_mock()
        summarize.model.reset_mock()

        mock_tokens = MagicMock()
        summarize.tokenizer.return_value = mock_tokens
        summarize.tokenizer.decode.return_value = expected_summary

        result = summarize.summarize_text(input_text)

        self.assertEqual(result, expected_summary)


if __name__ == '__main__':
    unittest.main()
