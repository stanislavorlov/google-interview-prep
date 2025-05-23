def merge_sort(arr):
    width = 1
    while width < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = left + width - 1
            right = ((2 * width + left - 1, len(arr) - 1)[2 * width + left - 1 > len(arr)-1])
            merge(arr, left, mid, right)
            left = left + width * 2
        width = 2 * width

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    left = [0] * n1
    right = [0] * n2
    
    for i in range(0, n1):
        left[i] = arr[low + i]
        
    for i in range(0, n2):
        right[i] = arr[mid + i + 1] 
    
    i, j, k = 0, 0, low
        
    while i < n1 and j < n2:
        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1
        k += 1
     
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
        
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)

print(arr)