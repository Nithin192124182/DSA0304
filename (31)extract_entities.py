import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_named_entities(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    named_entities = ne_chunk(pos_tags)
    return named_entities

def resolve_references(named_entities):
    resolved_text = ""
    for chunk in named_entities:
        if isinstance(chunk, nltk.Tree):
            entity_type = chunk.label()
            entity_text = ' '.join(c[0] for c in chunk.leaves())

            if entity_type == 'GPE':
                resolved_text += f"[Location: {entity_text}] "
            elif entity_type == 'PERSON':
                resolved_text += f"[Person: {entity_text}] "
            else:
                resolved_text += f"[{entity_type}: {entity_text}] "
        else:
            resolved_text += chunk[0] + ' '

    return resolved_text.strip()

# Example text
input_text = "Harvard University, located in Cambridge, Massachusetts, is a prestigious institution."

# Extract named entities
named_entities_result = extract_named_entities(input_text)

# Perform reference resolution
resolved_text = resolve_references(named_entities_result)

print("Original Text:")
print(input_text)
print("\nResolved Text:")
print(resolved_text)