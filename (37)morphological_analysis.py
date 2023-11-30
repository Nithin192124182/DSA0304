import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

def perform_lemmatization(sentence):
    tokens = word_tokenize(sentence)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(lemmatized_words)

# Sample sentences
sentence1 = "The quick brown foxes jumped over the lazy dogs."
sentence2 = "I am running in the park with my friends."

# Perform lemmatization on each sentence
lemmatized_sentence1 = perform_lemmatization(sentence1)
lemmatized_sentence2 = perform_lemmatization(sentence2)

# Display the results
print("Original Sentence 1:", sentence1)
print("Lemmatized Sentence 1:", lemmatized_sentence1)
print("\nOriginal Sentence 2:", sentence2)
print("Lemmatized Sentence 2:", lemmatized_sentence2)