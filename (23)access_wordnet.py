import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet

def explore_word_meanings(sentence):
    words = sentence.split()
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            print(f"\nWord: {word}")
            print("Definitions:")
            for synset in synsets:
                print(f"- {synset.definition()}")
            print("Synonyms:")
            synonyms = set()
            for synset in synsets:
                synonyms.update(synset.lemma_names())
            print(f"- {', '.join(synonyms)}")

# Given sentences
sentences = [
    "The cat sat on the mat.",
    "The dog barked loudly.",
    "She played the piano beautifully.",
]

# Explore word meanings for each sentence
for i, sentence in enumerate(sentences):
    print(f"\nSentence {i + 1}: {sentence}")
    explore_word_meanings(sentence)