import spacy

def recognize_dialog_acts(dialog):
    nlp = spacy.load("en_core_web_sm")
    dialog_acts = []

    for utterance in dialog:
        doc = nlp(utterance)
        if any(token.text.lower() in ["hello", "hi", "hey"] for token in doc):
            dialog_acts.append(("Greeting", utterance))
        elif any(token.text.lower() in ["how", "doing"] for token in doc) and "you" in [token.text.lower() for token in doc]:
            dialog_acts.append(("Inquiry - Well-being", utterance))
        elif any(token.text.lower() in ["thank", "thanks", "thank you"] for token in doc):
            dialog_acts.append(("Expression of Thanks", utterance))
        elif any(token.text.lower() in ["please", "could", "can"] for token in doc) and "you" in [token.text.lower() for token in doc]:
            dialog_acts.append(("Request", utterance))
        elif any(token.text.lower() in ["sure", "here", "go"] for token in doc):
            dialog_acts.append(("Acknowledgment/Confirmation", utterance))
        elif any(token.text.lower() in ["time", "meeting", "tomorrow"] for token in doc):
            dialog_acts.append(("Inquiry - Meeting Time", utterance))
        else:
            dialog_acts.append(("Other", utterance))

    return dialog_acts

# Given dialog
dialog = [
    "Hello! How are you today?",
    "I'm doing well, thank you. How about you?",
    "Can you please pass the salt?",
    "Sure, here you go.",
    "What time is the meeting tomorrow?",
    "The meeting is at 2:00 PM.",
]

# Recognize dialog acts
recognized_acts = recognize_dialog_acts(dialog)

# Print the recognized dialog acts
for act, utterance in recognized_acts:
    print(f"{act}: {utterance}")