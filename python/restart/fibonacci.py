def fibonacci(num):
    if (num == 0):
        return (0)
    elif (num == 1):
        return (1)
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))


fibValues = int(input("How many fibonacci values should be found: "))

for i in range(1, fibValues):
    value = fibonacci(i)
    print(value)

print("All Done")
