def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (high + low) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
        
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
        
arr = [2, 3, 5, 7, 20, 25, 34, 45, 46, 47, 65, 80, 100]
print(binary_search(arr, 2, 1, len(arr)))
print(binary_search_iterative(arr, 34))