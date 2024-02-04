import random

def main():
    for _ in range(5):
        print(make_sentence())

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()
    prepositional_phrase2 = get_prepositional_phrase().lower()
    return f"{determiner} {noun} {verb} {prepositional_phrase} {prepositional_phrase2}."

def get_determiner():
    determiners = ['A', 'One', 'The', 'Some', 'Many']
    return random.choice(determiners)

def get_noun():
    nouns = ['girl', 'boy', 'game', 'dogs', 'children', 'car', 'cats']
    return random.choice(nouns)

def get_verb():
    verbs = ['talked', 'drinks', 'dance', 'drank', 'laugh', 'will talk']
    return random.choice(verbs)

def get_preposition():
    prepositions = ['for', 'off', 'on', 'above', 'at', 'about']
    return random.choice(prepositions)

def get_prepositional_phrase():
    preposition = get_preposition()
    noun = get_noun()
    determiner = get_determiner()
    return f"{preposition} {determiner} {noun}"

if __name__ == "__main__":
    main()
