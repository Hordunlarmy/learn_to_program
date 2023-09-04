mul_table = [[0] * 13 for i in range(13)]

for i in range(1, 13):
    for j in range(1, 13):
        mul_table[i][j] = i * j

for i in range(1, 13):
    for j in range(1, 13):
        print("{: 4d}".format(mul_table[i][j]), end=" ")
    print()
