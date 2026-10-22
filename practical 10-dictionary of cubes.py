n = int(input("Enter the limit: "))

cubes = {}

for i in range(1, n + 1):
    cubes[i] = i**3

print("Dictionary of cubes:")
print(cubes)
