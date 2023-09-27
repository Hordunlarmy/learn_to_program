def quickSort(arr, size):
    if size > 1:
        quickSortRecursion(arr, 0, size - 1)


def quickSortRecursion(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quickSortRecursion(arr, start, pivot_index - 1)
        quickSortRecursion(arr, pivot_index + 1, end)


def partition(arr, start, end):
    pivot_value = arr[end]
    print(f"\nNow, Pivot Value Is {pivot_value}")
    low = start
    for i in range(start, end):
        print(f"\n==== ROUND {i + 1} =====")
        print(f"Is {arr[i]} less than {pivot_value}??------->", end="")
        if (arr[i] <= pivot_value):
            print("YES")
            print(f"Swap ({arr[low]} at index {low}) with {arr[i]}")
            arr[low], arr[i] = arr[i], arr[low]
            print(arr)
            low += 1
            print(f"Low now at index {low}")
        else:
            print("NO")
            print("No SWAP")
            print(arr)
    print(f"\nNow we swap ({arr[low]} at index {low}) with {arr[end]}")
    arr[end], arr[low] = arr[low], arr[end]
    print(arr)
    return low


def main():
    myArr = [2, 7, 9, 4, 2, 8, 11, 3, 6]
    size = len(myArr)
    print("Original array:", myArr)
    quickSort(myArr, size)
    print("Sorted array", myArr)


if __name__ == "__main__":
    main()
