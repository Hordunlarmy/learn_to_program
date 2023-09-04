string = input("Make Your Entry: ").strip()
upper_string = string.upper()
split_string = upper_string.split()
for word in split_string:
    print(word[0], end="")
print()
