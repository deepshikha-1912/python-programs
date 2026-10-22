def print_pyramid(rows):
    for row in range(1, rows + 1):
        spaces = " " * (rows - row)
        stars = "* " * row
        print(spaces + stars)


def print_inverted_pyramid(rows):
    for row in range(rows, 0, -1):
        spaces = " " * (rows - row)
        stars = "* " * row
        print(spaces + stars)


try:
    rows = int(input("Enter number of rows (1-50): "))

    if 1 <= rows <= 50:
        print("\n--- Normal Pyramid ---")
        print_pyramid(rows)

        print("\n--- Inverted Pyramid ---")
        print_inverted_pyramid(rows)
    else:
        print("Rows must be between 1 and 50.")

except ValueError:
    print("Please enter a valid integer.")
