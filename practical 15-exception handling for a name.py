class InvalidNameError(Exception):
    """Raised when a name does not meet the requirements."""


def validate_name(name):
    name = name.strip()

    if not name:
        raise InvalidNameError("Name cannot be empty.")

    if not all(
        part.isalpha()
        for part in name.split()
    ):
        raise InvalidNameError(
            "Use letters only, with spaces between names."
        )

    return name.title()


try:
    name = input("Enter your full name: ")
    valid_name = validate_name(name)

    print("\n--- Registration Successful ---")
    print("Welcome,", valid_name)
    print("Name length:", len(valid_name))

except InvalidNameError as error:
    print("Validation error:", error)

finally:
    print("\nName validation process completed.")
