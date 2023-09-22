def runningSum(*args):
    myList = []
    result = 0

    for i in args:
        result += i

        myList.append(result)

    for i in myList:
        if i == myList[-1]:
            print(i)
            break
        print(i, end=", ")


def main():
    runningSum(1, 2, 3, 4)


main()
