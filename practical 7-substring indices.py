s = input("Enter a string: ")
sub = input("Enter substring: ")

start = 0
found = False

while True:
    index = s.find(sub, start)

    if index == -1:
        break

    print("Substring found at index:", index)
    start = index + 1
    found = True

if not found:
    print("Substring not found")
