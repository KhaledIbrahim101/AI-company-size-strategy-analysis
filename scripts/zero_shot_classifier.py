# zero_shot_classifier.py
import pandas as pd
from transformers import pipeline
from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt')
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

LABELS = [
    "Strategic planning", "Leadership style", "Risk management",
    "Operational detail", "Sustainability", "Innovation", "Financial stability"
]

def classify_10k_text(text, threshold=0.6):
    sentences = sent_tokenize(text)
    results = []

    for sent in sentences:
        out = classifier(sent, LABELS, multi_label=True)
        for label, score in zip(out["labels"], out["scores"]):
            if score >= threshold:
                results.append({"sentence": sent, "label": label, "score": score})
    
    return pd.DataFrame(results)

# Example usage:
# with open("sec_filings/sample.html") as f:
#     text = BeautifulSoup(f.read(), "html.parser").get_text()
# df = classify_10k_text(text)
# df.to_csv("10k_classified.csv", index=False)
