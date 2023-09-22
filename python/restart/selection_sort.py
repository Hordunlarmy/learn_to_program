arr = [5, 2, 1, 7, 8, 2, 6]
print("Before: ", arr)


def sorted_sub(arr, min_idx):
    res = [arr[i] for i in range(min_idx)]
    print(res)


def unsorted_sub(arr):
    j = 0
    res = [arr[i] for i in range(j, len(arr))]
    print(res)


for i in range(len(arr) - 2):
    min_idx = i
    print("\nSorted Sub")
    sorted_sub(arr, min_idx)

    print("Unsorted Sub")
    unsorted_sub(arr)

    for j in range(i, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
            print(f"swapped {arr[i]} for {arr[min_idx]}")

    if min_idx != i:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("\nAfter: ", arr)
