s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) < 2 or len(s2) < 2:
    print("Both strings must have at least 2 characters")
else:
    result1 = s2[:2] + s1[2:]
    result2 = s1[:2] + s2[2:]

    print("First string:", result1)
    print("Second string:", result2)
