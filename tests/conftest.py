import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture(autouse=True)
def mock_model_and_tokenizer():
    import sys

    mock_module = Mock()

    mock_tokenizer = Mock()
    mock_tokenizer.return_value = {"input_ids": Mock()}
    mock_tokenizer.decode.return_value = "Generated summary text"

    mock_model = Mock()
    mock_model.generate.return_value = [[1, 2, 3]]

    mock_module.tokenizer = mock_tokenizer
    mock_module.model = mock_model

    sys.modules["model"] = mock_module

    yield mock_module
