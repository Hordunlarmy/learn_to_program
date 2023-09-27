def partition(array, start, end):
    pivot_value = array[end]
    low = start
    high = end

    print("start:", start, "end:", end)

    while high > low:
        while array[low] < pivot_value:
            low += 1
        while array[high] >= pivot_value:
            high -= 1
        if high > low:
            array[low], array[high] = array[high], array[low]

    array[high], array[end] = array[end], array[high]
    return high


def quickSort(array, size):
    if size > 1:
        quicksort_rec(array, 0, size - 1)


def quicksort_rec(array, start, end):
    if end > start:
        pivot_index = partition(array, start, end)
        quicksort_rec(array, start, pivot_index - 1)
        quicksort_rec(array, pivot_index + 1, end)


def main():
    myArr = [2, 7, 9, 4, 2, 8, 11, 3, 6]
    orig_Arr = myArr.copy()
    size = len(myArr)
    quickSort(myArr, size)
    print("Original array:", orig_Arr)
    print("Sorted array:", myArr)


if __name__ == "__main__":
    main()
