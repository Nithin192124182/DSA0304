import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
# Define the sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "She is an excellent chef and loves to cook delicious meals.",
    "The Eiffel Tower in Paris is a famous landmark."
]

# Function to extract noun phrases and their meanings
def extract_noun_phrases_meanings(sentences):
    for sentence in sentences:
        # Tokenize the sentence
        words = word_tokenize(sentence)

        # Perform Part-of-Speech (POS) tagging
        pos_tags = pos_tag(words)

        # Perform chunking to extract noun phrases
        chunks = ne_chunk(pos_tags)

        # Extract noun phrases and their meanings
        noun_phrases = []
        meanings = []
        for chunk in chunks:
            if hasattr(chunk, 'label') and chunk.label() == 'NP':
                noun_phrase = ' '.join([token for token, pos in chunk.leaves()])
                noun_phrases.append(noun_phrase)

                # Define meanings (for demonstration purposes)
                # In a real-world application, meanings might be retrieved from a knowledge base or database
                if 'Eiffel Tower' in noun_phrase:
                    meanings.append("A famous landmark in Paris, France.")
                elif 'chef' in noun_phrase:
                    meanings.append("Someone skilled in cooking.")
                else:
                    meanings.append("Meaning not defined.")

        # Display extracted noun phrases and their meanings
        print(f"Sentence: {sentence}")
        print("Extracted Noun Phrases:")
        for i, noun_phrase in enumerate(noun_phrases):
            print(f"{i + 1}. {noun_phrase}")
            print(f"   Meaning: {meanings[i]}")
        print("")

# Extract noun phrases and their meanings from the sentences
extract_noun_phrases_meanings(sentences)