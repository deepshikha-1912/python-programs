def analyze_string(text):
    letters = sum(char.isalpha() for char in text)
    digits = sum(char.isdigit() for char in text)
    spaces = sum(char.isspace() for char in text)

    print("\n--- String Analysis ---")
    print("Original string :", repr(text))
    print("Uppercase       :", text.upper())
    print("Lowercase       :", text.lower())
    print("Title case      :", text.title())
    print("Reversed        :", text[::-1])
    print("Total characters:", len(text))
    print("Letters         :", letters)
    print("Digits          :", digits)
    print("Spaces          :", spaces)
    print("Word count      :", len(text.split()))
    print("Palindrome      :", text.lower().replace(" ", "")
          == text.lower().replace(" ", "")[::-1])


user_text = input("Enter a string: ")
analyze_string(user_text)
