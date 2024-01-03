def count_inversions(array):
    """
    Merge sort an array and count the number of inversions,
    returns sorted array and number of inversions
    """

    # Base case - one element, zero inversions
    if len(array) == 1:
        return array, 0

    # Not always half, as the array can have uneven number of elements
    half = int(len(array) / 2)

    # Recursively sort and count number of inversions in the first array
    sorted_1st, inversions_1st = count_inversions(array[:half])
    # Recursively sort and count number of inversions in the second array
    sorted_2nd, inversions_2nd = count_inversions(array[half:])

    k = 0  # New array's index
    i = 0  # Index in the first array
    j = 0  # Index in the second array
    inversions_split = 0

    while i < len(sorted_1st) and j < len(sorted_2nd):
        if sorted_1st[i] < sorted_2nd[j]:
            # No inversion, just copying the element
            array[k] = sorted_1st[i]
            i += 1
            k += 1
        else:
            array[k] = sorted_2nd[j]
            # There are len(sorted_1st) split inversions
            inversions_split += len(sorted_1st) - i
            j += 1
            k += 1

    while i < len(sorted_1st):
        array[k] = sorted_1st[i]
        i += 1
        k += 1

    while j < len(sorted_2nd):
        array[k] = sorted_2nd[j]
        # There are len(sorted_1st) split inversions
        inversions_split += len(sorted_1st) - i
        j += 1
        k += 1

    inversions = inversions_split + inversions_1st + inversions_2nd
    return array, inversions
