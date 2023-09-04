height = eval(input("How tall is the tree: "))

tree = '#'
spaces = ' '
width = 1

for i in range(height):
    print(f"{spaces * (height - i)}", end="")
    print(f"{tree * width}")
    width += 2
print(f"{spaces * height}{tree}")
