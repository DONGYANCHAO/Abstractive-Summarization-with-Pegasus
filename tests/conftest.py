import sys
import os
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

mock_tokenizer_instance = MagicMock()
mock_model_instance = MagicMock()

mock_tokenizer_class = MagicMock(return_value=mock_tokenizer_instance)
mock_model_class = MagicMock(return_value=mock_model_instance)

mock_transformers = MagicMock()
mock_transformers.PegasusTokenizer = MagicMock()
mock_transformers.PegasusTokenizer.from_pretrained = MagicMock(return_value=mock_tokenizer_instance)
mock_transformers.PegasusForConditionalGeneration = MagicMock()
mock_transformers.PegasusForConditionalGeneration.from_pretrained = MagicMock(return_value=mock_model_instance)

sys.modules['transformers'] = mock_transformers
sys.modules['transformers.PegasusForConditionalGeneration'] = mock_transformers.PegasusForConditionalGeneration
sys.modules['transformers.PegasusTokenizer'] = mock_transformers.PegasusTokenizer

import model as model_module
model_module.tokenizer = mock_tokenizer_instance
model_module.model = mock_model_instance

import summarize as summarize_module
summarize_module.tokenizer = mock_tokenizer_instance
summarize_module.model = mock_model_instance
