import random
grammar = {
    "S": ["NP VP", 1.0],
    "NP": ["Det N", 0.5, "NP PP", 0.4, "'the'", 0.1],
    "VP": ["V NP", 0.7, "VP PP", 0.3],
    "PP": ["P NP", 1.0],
    "Det": ["'the'", 0.7, "'a'", 0.3],
    "N": ["'fox'", 0.4, "'dog'", 0.3, "'cat'", 0.2, "'bird'", 0.1],
    "V": ["'jumps'", 0.5, "'runs'", 0.3, "'sits'", 0.2],
    "P": ["'over'", 0.6, "'on'", 0.4]
}

def parse_sentence(sentence):
    parse_tree = []
    tokens = sentence.split()

    def expand_symbol(symbol):
        if symbol in grammar:
            options = grammar[symbol]
            choice = random.choices(options)[0]

            if type(choice) is list:
                prob = choice[1]
                if random.random() < prob:
                    parse_tree.append((symbol, choice[0]))
                    for sub_symbol in choice[0]:
                        expand_symbol(sub_symbol)
                else:
                    expand_symbol(symbol)
            else:
                parse_tree.append((symbol, choice))
        else:
            parse_tree.append((symbol, tokens.pop(0)))

    expand_symbol("S")

    return parse_tree

sentence = "The quick brown fox jumps over the lazy dog."
parsed_tree = parse_sentence(sentence)
print("Parse tree:", parsed_tree)