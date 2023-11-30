
import re

# Sample text
sample_text = "Once upon a time, there was a young boy named Peter."

# Function to check coherence
def check_coherence(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    coherence_score = 0

    # Simple coherence check based on sentence structure
    for sentence in sentences:
        # Check if sentence starts with an uppercase letter and ends with punctuation
        if sentence[0].isupper() and sentence[-1] in ['.', '!', '?']:
            coherence_score += 1

    # Normalize coherence score
    normalized_score = coherence_score / max(len(sentences), 1)

    return normalized_score

# Check coherence of the sample text
coherence = check_coherence(sample_text)
print(f"The coherence score of the text is: {coherence}")