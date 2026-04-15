import os
from dotenv import load_dotenv
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "google/pegasus-xsum")
CACHE_DIR = os.getenv("MODEL_CACHE_DIR", "./cache")

tokenizer = PegasusTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
model = PegasusForConditionalGeneration.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
