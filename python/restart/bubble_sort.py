import random


def bubble_sort(my_list):
    n = len(my_list) - 1
    for i in range(n):
        print(f"\n=======Round {i + 1}=======")
        for j in range(n-i):
            print(f"Is {my_list[j]} > {my_list[j + 1]}?   --->   ", end="")
            if my_list[j] > my_list[j + 1]:
                print("YES")
                # if my_list[j] < my_list[j + 1]: for reverse sort
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                print("Swapped")
            else:
                print("NO")
                print("Not Swapped")
            print(f"Updated List ---> {my_list}")


my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 10))

print("-----Unsorted List------")
res = [i for i in my_list]
print(res)

print()

bubble_sort(my_list)

print("\n-----Sorted List------")
res = [i for i in my_list]
print(res)
