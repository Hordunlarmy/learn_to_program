message = input("Enter a string to hide in uppercase: ")

print("Secret Message: ", end="")
for chr in message:
    print(f"{ord(chr)}", end="")
print(f" \nOriginal Message: {message}")
