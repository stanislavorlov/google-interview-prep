# Find element in sorted array

# O(log(n))
def binary_search(arr, low, high, key):
    if high >= low:
        mid = low + (high - low) // 2
        
        if arr[mid] == key:
            return mid
    
        if key > arr[mid]:
            return binary_search(arr, mid + 1, high, key)
    
        if key < arr[mid]:
            return binary_search(arr, low, mid - 1, key)
    
    return -1

# O(N)
def insert_sorted(arr, key):
    arr.append(key)
    idx = 0
    while key > arr[idx]:
        idx += 1
    val1 = arr[idx]
    arr[idx] = key
    for j in range(idx + 1, len(arr)):
        val2 = arr[j]
        arr[j] = val1
        val1 = val2

# O(N)
def delete_sorted(arr, key):
    l = len(arr)
    idx = binary_search(arr, 0, l - 1, key)
    
    for i in range(idx, l-1):
        arr[i] = arr[i+1]
        
    del arr[l-1]

arr = [5, 6, 8, 9, 10]
print(binary_search(arr, 0, len(arr) - 1, 8))

insert_sorted(arr, 7)
print(arr)

delete_sorted(arr, 5)
print(arr)