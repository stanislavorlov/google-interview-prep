def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_optimized(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break


input_arr = [6, 5, 5, 4, 3, 2, 2, 1]
bubble_sort_optimized(input_arr)

print(input_arr)

# T(n) = an^2+bn+c