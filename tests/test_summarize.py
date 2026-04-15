import pytest
from unittest.mock import patch, MagicMock


class TestSummarizeText:
    def test_summarize_text_calls_tokenizer(self):
        mock_tokenizer = MagicMock()
        mock_model = MagicMock()
        mock_model.generate.return_value = [[1, 2, 3]]
        mock_tokenizer.decode.return_value = "Test summary"

        with patch("summarize.tokenizer", mock_tokenizer), patch(
            "summarize.model", mock_model
        ):
            from summarize import summarize_text

            input_text = "This is a long text that needs to be summarized."
            result = summarize_text(input_text)

            mock_tokenizer.assert_called_once_with(
                input_text, truncation=True, padding=True, return_tensors="pt"
            )

            assert result == "Test summary"

    def test_summarize_text_with_empty_input(self):
        mock_tokenizer = MagicMock()
        mock_model = MagicMock()
        mock_model.generate.return_value = [[1, 2, 3]]
        mock_tokenizer.decode.return_value = ""

        with patch("summarize.tokenizer", mock_tokenizer), patch(
            "summarize.model", mock_model
        ):
            from summarize import summarize_text

            result = summarize_text("")

            mock_tokenizer.assert_called_once_with(
                "", truncation=True, padding=True, return_tensors="pt"
            )
            mock_model.generate.assert_called_once()
            assert isinstance(result, str)

    def test_summarize_text_generation_parameters(self):
        mock_tokenizer = MagicMock()
        mock_model = MagicMock()
        mock_model.generate.return_value = [[1, 2, 3]]
        mock_tokenizer.decode.return_value = "Summary"

        with patch("summarize.tokenizer", mock_tokenizer), patch(
            "summarize.model", mock_model
        ):
            from summarize import summarize_text

            tokens = {"input_ids": MagicMock()}
            mock_tokenizer.return_value = tokens

            summarize_text("Test input")

            mock_model.generate.assert_called_once_with(
                **tokens, max_length=60, num_beams=5, early_stopping=True
            )

    def test_summarize_text_skips_special_tokens(self):
        mock_tokenizer = MagicMock()
        mock_model = MagicMock()
        mock_model.generate.return_value = [[1, 2, 3]]

        with patch("summarize.tokenizer", mock_tokenizer), patch(
            "summarize.model", mock_model
        ):
            from summarize import summarize_text

            summarize_text("Test")

            mock_tokenizer.decode.assert_called_once_with([1, 2, 3], skip_special_tokens=True)

    @pytest.mark.parametrize(
        "input_text,expected_called",
        [
            ("Short text", True),
            ("Long text " * 100, True),
            ("Single sentence", True),
        ],
    )
    def test_summarize_text_handles_various_lengths(
        self, input_text, expected_called
    ):
        mock_tokenizer = MagicMock()
        mock_model = MagicMock()
        mock_model.generate.return_value = [[1, 2, 3]]
        mock_tokenizer.decode.return_value = "Generated summary"

        with patch("summarize.tokenizer", mock_tokenizer), patch(
            "summarize.model", mock_model
        ):
            from summarize import summarize_text

            result = summarize_text(input_text)

            assert mock_tokenizer.called == expected_called
            assert isinstance(result, str)
            assert len(result) > 0
