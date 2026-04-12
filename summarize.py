from model import tokenizer , model
def summarize_text(text):
    tokens=tokenizer(text, truncation=True , padding=True, return_tensors="pt")
    summary_ids=model.generate(**tokens,max_length=60,num_beams=5,early_stopping=True)
    summary = tokenizer.decode(summary_ids[0],skip_special_tokens=True)
    return summary