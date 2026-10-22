filename = "sample.txt"

with open(filename, "w") as f:
    f.write("Hello Python!\n")
    f.write("This is file handling.")

with open(filename, "r") as f:
    content = f.read()

print("File content:")
print(content)
