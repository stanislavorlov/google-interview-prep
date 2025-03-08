# T(n)=O(lg n)
def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i +2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# T(n)=O(n)
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        max_heapify(arr, n, i)

# T(n)=O(n log n)
def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

input_arr = [12, 11, 13, 5, 6, 7, ]
print(input_arr)

heap_sort(input_arr)
print(input_arr)