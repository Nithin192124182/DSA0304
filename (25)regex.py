import re

def perform_regex_operations(text, patterns):
    print("Original Text:")
    print(text)

    for pattern in patterns:
        print("\nRegex Pattern:", pattern)
        matches = re.findall(pattern, text)
        if matches:
            print("Matches:", matches)
        else:
            print("No matches found.")

# Given text
text = "Regular expressions are a powerful tool for pattern matching in text. They provide a flexible way to search and manipulate strings."

# List of regex patterns
regex_patterns = [
    r"regex",
    r"4G\*",
    r"powerful|flexible|manipulate",
]

# Perform regex operations on the text
perform_regex_operations(text, regex_patterns)