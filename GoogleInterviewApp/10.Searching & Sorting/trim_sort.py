RUN_SIZE = 32

def calc_min_run(n):
    r = 0
    while n >= RUN_SIZE:
        r |= n & 1
        n >> 1

    return n + r

def insertion_sort(arr, left, right):
    for i in range(left+1, right+1):
        j = i
        while j > left and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def merge(arr, left, med, right):
    n1, n2 = med - left + 1, right - med
    l_arr, r_arr = [], []
    for i in range(n1):
        l_arr[i] = arr[left + i]

    for i in range(n2):
        r_arr[i] = arr[med + i + 1]

    i, j, k = 0, 0, 1
    while i < n1 and j < n2:
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = l_arr[i]
        k, i = k+1, i+1

    while j < n2:
        arr[k] = r_arr[j]
        k,i = k+1, j+1

def trim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n-1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size = size * 2

array = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]
trim_sort(array)
print(array)