import random

rand_num = random.randrange(1, 11)

while True:
    number = int(input("Enter a number between 1 and 10: "))

    if (number == rand_num):
        print("You guessed it")
        break
    
    print("WRONG, Try Again")
    # print(f"I guessed {rand_num}")
