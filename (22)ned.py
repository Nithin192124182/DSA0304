import wikipediapi
import requests

# Input sentences
sentences = [
    "Apple is a leading tech company.",
    "I love apples as a fruit.",
    "Python is a popular programming language.",
    "The python is a non-venomous snake."
]

# Set a custom user-agent for accessing Wikipedia
headers = {
    'User-Agent': 'My_User_Agent/1.0 (Your_Name_or_Application_Name)'
}

# Initialize Wikipedia API with custom headers
wiki_wiki = wikipediaapi.Wikipedia('en', headers=headers)

# Function to perform named entity disambiguation
def disambiguate_entities(sentences):
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            # Check if the word is a Wikipedia page title
            page = wiki_wiki.page(word)
            if page.exists():
                print(f"Entity Mention: {word}")
                print(f"Corresponding Wikipedia Entity: {page.fullurl}")
                print(f"Summary: {page.summary}")
                print("")

# Perform named entity disambiguation
disambiguate_entities(sentences)



