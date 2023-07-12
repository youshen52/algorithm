def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        l = r = a = 0

        while l < len(L) and r < len(R):
            if L[l] >= R[r]:
                arr[a] = L[l]
                l += 1
            else:
                arr[a] = R[r]
                r += 1
            a += 1

        if l < len(L):
            arr[a:] = L[l:]

        if r < len(R):
            arr[a:] = R[r:]


if __name__ == "__main__":
    arr = [9, 234, 7, 12, 8, 1, 45, 8, 23]
    merge_sort(arr)
    print(arr)
