def replaceWord(sentence, target_word, replacement):
    word_split = sentence.split()
    word_replaced = []

    for word in word_split:
        if word == target_word:
            word_replaced.append(replacement)
        else:
            word_replaced.append(word)
        output_word = " ".join(word_replaced)
    return output_word


def main():
    sentence = input("Enter the sentence: ")
    target = input("Enter word to be replace: ")
    if target not in sentence:
        print("target word is not in sentence")
        exit()
    replacement = input("Enter word to replace with: ")

    print(replaceWord(sentence, target, replacement))


main()
