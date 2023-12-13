x = input("Input: ")
print("Output: ", end="")
for letter in x:
    if not letter.lower() in ['a', 'e', 'i', 'u', 'o']:
        print(letter, end="")
print()