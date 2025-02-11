def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

input_arr = [6, 5, 5, 4, 3, 2, 2, 1]
insertion_sort(input_arr)

print(input_arr)

# T(n) = an^2+bn+c