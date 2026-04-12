from transformers import PegasusForConditionalGeneration, PegasusTokenizer

MODEL_NAME = "google/pegasus-xsum"

tokenizer = PegasusTokenizer.from_pretrained(MODEL_NAME)
model = PegasusForConditionalGeneration.from_pretrained(MODEL_NAME)
