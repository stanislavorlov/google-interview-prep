def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

input_arr = [6, 5, 5, 4, 3, 2, 2, 1]
bubble_sort(input_arr)

print(input_arr)

# T(n) = an^2+bn+c