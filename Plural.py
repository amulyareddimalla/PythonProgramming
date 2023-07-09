def pluralize(word):
    if word.endswith('s') or word.endswith('x') or word.endswith('z'):
        return word + "es"
    elif word.endswith('y') and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    else:
        return word + "s"

word = input("Enter a word: ")
plural = pluralize(word)
print("The plural form of the word is:", plural)
