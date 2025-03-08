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

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        max_heapify(arr, n, i)

def heap_maximum(arr):
    return arr[0]

nums = [43, 2, 13, 634, 120]
build_max_heap(nums)

print(nums)