
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

def perform_stemming(sentence):
    tokens = word_tokenize(sentence)
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in tokens]
    return ' '.join(stemmed_words)

# Sample sentences
sentence1 = "Coding with Python is very enjoyable."
sentence2 = "I had a delicious meal at the restaurant."

# Perform stemming on each sentence
stemmed_sentence1 = perform_stemming(sentence1)
stemmed_sentence2 = perform_stemming(sentence2)

# Display the results
print("Original Sentence 1:", sentence1)
print("Stemmed Sentence 1:", stemmed_sentence1)
print("\nOriginal Sentence 2:", sentence2)
print("Stemmed Sentence 2:", stemmed_sentence2)