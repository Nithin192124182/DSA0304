!pip install torch
!pip install transformers

from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, model_name="Helsinki-NLP/opus-mt-en-de"):
    # Load pre-trained model and tokenizer
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt")

    # Generate translation
    translation = model.generate(**inputs)

    # Decode and return the translated text
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
    return translated_text

# Example usage
english_text = "Hello, how are you?"
german_translation = translate_text(english_text)

print(f"English: {english_text}")
print(f"German: {german_translation}")

