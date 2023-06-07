def binary_search(arr, low, high, x):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid - 1
            binary_search(arr, low, high, x)
        else:
            low = mid + 1
            binary_search(arr, low, high, x)


if __name__ == "__main__":
    arr = [2, 3, 5, 6]
    low = 0
    high = len(arr) - 1
    x = 3
    index = binary_search(arr, low, high, x)
    if index != -1:
        print(f"{index}")
