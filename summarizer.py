from transformers import pipeline
import logging

# 🛑 Suppress Hugging Face max_length warnings
logging.getLogger("transformers").setLevel(logging.ERROR)

# ✅ Load summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=130):
    if not text:
        return "❌ Couldn't extract article."
    
    input_length = len(text.split())

    # 🧠 Dynamically adjust max_length based on input size
    if input_length < 30:
        max_length = 40
    elif input_length < 60:
        max_length = 80

    try:
        summary = summarizer(text[:1024], max_length=max_length, min_length=20, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"❌ Summarization failed: {str(e)}"
