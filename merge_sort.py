def merge_sort(array):
    if len(array) == 1:
        return array

    n = len(array)
    half = n - int(n / 2)
    sorted_1st = merge_sort(array[:half])
    sorted_2nd = merge_sort(array[half:])

    k = 0
    i = 0
    j = 0

    while i < len(sorted_1st) and j < len(sorted_2nd):
        if sorted_1st[i] < sorted_2nd[j]:
            array[k] = sorted_1st[i]
            i += 1
            k += 1
        else:
            array[k] = sorted_2nd[j]
            j += 1
            k += 1

    while i < len(sorted_1st):
        array[k] = sorted_1st[i]
        i += 1
        k += 1

    while j < len(sorted_2nd):
        array[k] = sorted_2nd[j]
        j += 1
        k += 1

    return array