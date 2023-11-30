!pip install spacy

import spacy

def perform_ner(text):
    # Load the spaCy model for English
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy
    doc = nlp(text)

    # Extract named entities
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]

    return named_entities

# Example text
input_text = "Microsoft Corporation is headquartered in Redmond, Washington."

# Perform Named Entity Recognition
ner_results = perform_ner(input_text)

# Print the results
print("Named Entities:")
for entity, label in ner_results:
    print(f"{entity} - {label}")