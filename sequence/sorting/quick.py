def _partition(arr, low, high):
    pivot = arr[high]

    # Index of last found element <= pivot
    i = -1

    for j in range(low, high):
        if arr[j] <= pivot:
            # Index of last found element > pivot
            i += 1

            # This switch  even when i and j are the same
            if i != j:
                (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = _partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


if __name__ == "__main__":
    arr = [1, 23, 6, 2, 6]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
