# a program to calculate numbers

first, sign, second = input("Enter Calulation: ").split()

if (sign == "+"):
    output = int(first) + int(second)
    print(f"{first} + {second} = {output}")
elif (sign == "-"):
    output = int(first) - int(second)
    print(f"{first} - {second} = {output}")
elif (sign == "/"):
    output = int(first) / int(second)
    print(f"{first} / {second} = {output}")
elif (sign == "*"):
    output = int(first) * int(second)
    print(f"{first} * {second} = {output}")
elif (sign == "%"):
    output = int(first) % int(second)
    print(f"{first} % {second} = {output}")
else:
    print(f"unrecognized math symbol {sign}")
