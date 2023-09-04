string = input("Enter a string to hide as unicode ")
secret = ""

for char in string:
    secret += str(ord(char))
print(f"Secret Message: {secret}")
print(f"Original Message: {string}")
