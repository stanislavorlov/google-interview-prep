def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    l_arr = [0] * n1
    r_arr = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        l_arr[i] = arr[l + i]

    for j in range(0, n2):
        r_arr[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l:r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = l_arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = r_arr[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def merge_sort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

input_arr = [6, 5, 5, 4, 3, 2, 2, 1]
merge_sort(input_arr, 0, len(input_arr) - 1)

print(input_arr)

# T(n) = n log n