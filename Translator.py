def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.isupper():
            translation=translation+ letter.lower()
        else:
            translation=translation+letter
    return translation
print(translate(input("Enter a phrase: ")))