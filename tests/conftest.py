"""
Pytest configuration file.
This file runs before any tests are collected/executed.
"""
import sys
from unittest.mock import MagicMock

# Mock the model module BEFORE any imports happen
mock_model_module = MagicMock()
mock_tokenizer = MagicMock()
mock_model = MagicMock()

# Setup default mock behaviors
mock_tokens = MagicMock()
mock_tokenizer.return_value = mock_tokens
mock_summary_ids = MagicMock()
mock_model.generate.return_value = mock_summary_ids
mock_tokenizer.decode.return_value = "Mocked summary text."

mock_model_module.tokenizer = mock_tokenizer
mock_model_module.model = mock_model
mock_model_module.MODEL_NAME = "google/pegasus-xsum"

# Inject the mock into sys.modules before any real imports
sys.modules['model'] = mock_model_module

# Also mock transformers to prevent actual model loading
mock_transformers = MagicMock()
sys.modules['transformers'] = mock_transformers
