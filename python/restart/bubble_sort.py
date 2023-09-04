import random


def bubble_sort(my_list):
    n = len(my_list) - 1
    for i in range(n):
        for j in range(n-i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 10))

print("-----Unsorted List------")
for i in my_list:
    print(i, end=", ")

print()

bubble_sort(my_list)

print("\n-----Sorted List------")
for i in my_list:
    print(i, end=", ")
