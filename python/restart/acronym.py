words = input("Convert To Acronym: ")

word_to_list = words.split()

for word in word_to_list:
    print(word[0].upper(), end="")
print()
