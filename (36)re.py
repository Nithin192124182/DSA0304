import re

def extract_words_with_pattern(text, pattern):
    matches = re.findall(pattern, text)
    return matches

# Input sentence
input_sentence = "The quick brown fox jumps over the lazy dog. The cat is also agile."

# Regular expression pattern
pattern = r'\b\w{3}\b'

# Extracting three-letter words using the pattern
result = extract_words_with_pattern(input_sentence, pattern)

# Displaying the result
print("Input Sentence:", input_sentence)
print("Three-letter words:", result)