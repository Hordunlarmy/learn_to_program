tree_length = eval(input("How tall is the tree: "))
i = 0
j = 3
spaces = " " * tree_length
ospaces = " " * tree_length
tree = "#"
otree = "#"
decrement = tree_length

while (i <= tree_length):
    if (i == tree_length):
        print(f"{ospaces}{otree}")
        break
    print(f"{spaces}", end="")
    print(f"{tree}")
    decrement -= 1
    spaces = " " * (decrement)
    tree = "#" * (i + j)
    i += 1
    j += 1
