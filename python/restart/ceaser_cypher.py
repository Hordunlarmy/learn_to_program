"""Unicode Range
A - Z = 65 - 90
a - z = 97 - 122
"""
message = input("Enter Your Message: ")
key = int(input("Enter The Number Of Character To Shift: "))
new_message = ""

for i in message:
    if (i.isalpha()):
        cypher = key + ord(i)

        if (i.isupper()):
            if (cypher < ord("A")):
                cypher += 26
            if (cypher > ord("Z")):
                cypher -= 26

        elif (i.islower()):
            if (cypher < ord("a")):
                cypher += 26
            if (cypher > ord("z")):
                cypher -= 26
        new_message += chr(cypher)

    else:
        new_message += i
print(f"Encrypted: {new_message}")
print(f"Original Message: {message}")
