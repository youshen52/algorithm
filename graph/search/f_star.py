def merge_arrays(array1, array2):
    merged_array = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    merged_array.extend(array1[i:])
    merged_array.extend(array2[j:])

    return merged_array
