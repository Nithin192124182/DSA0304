import re

def recognize_dialog_acts(dialog):
    dialog_acts = []

    for utterance in dialog:
        if re.search(r'\b(?:hi|hello|good morning|good afternoon|good evening)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "greeting"})
        elif re.search(r'\b(?:how\'s the weather today)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "weather inquiry"})
        elif re.search(r'\b(?:\w+ it\'s going to be \w+ and \w+)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "weather report"})
        elif re.search(r'\b(?:please send me the \w+ by \d+\s?(?:am|pm)?)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "request"})
        elif re.search(r'\b(?:of course|sure|yes|okay)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "confirmation"})
        elif re.search(r'\b(?:do you know where(?: the)? nearest (?:\w+ )?post office is)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "location inquiry"})
        elif re.search(r'\b(?:the post office is \w+ blocks down the street)\b', utterance, re.IGNORECASE):
            dialog_acts.append({"utterance": utterance, "act": "location information"})
        else:
            dialog_acts.append({"utterance": utterance, "act": "unclassified"})

    return dialog_acts

# Example dialog
dialog = [
    "Good morning! How's the weather today?",
    "I heard it's going to be sunny and warm.",
    "Could you please send me the report by 3 PM?",
    "Of course, I'll send it over before the deadline.",
    "Do you know where the nearest post office is?",
    "The post office is two blocks down the street."
]

# Recognize dialog acts
recognized_acts = recognize_dialog_acts(dialog)

# Print results
for act in recognized_acts:
    print(f"Dialog Act: {act['act']}\nUtterance: {act['utterance']}\n")