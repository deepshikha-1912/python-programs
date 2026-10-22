def classify_character(char):
    if len(char) != 1:
        return "Please enter exactly one character."

    if char.isalpha():
        if char.lower() in "aeiou":
            return "Alphabet: Vowel"
        return "Alphabet: Consonant"

    if char.isdigit():
        return "Digit"

    if char.isspace():
        return "Whitespace"

    return "Special character"


character = input("Enter one character: ")
print("Classification:", classify_character(character))
