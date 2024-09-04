def mergeSort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        
        mergeSort(arr, left, middle)
        mergeSort(arr, middle + 1, right)
        
        merge(arr, left, middle, right)

def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    
    arrLeft = [0] * n1
    arrRight = [0] * n2
    
    for i in range(0, n1):
        arrLeft[i] = arr[left + i]
        
    for j in range(0, n2):
        arrRight[j] = arr[middle + j + 1]
        
    i, j, k = 0, 0, left
    
    while i < n1 and j < n2:
        if arrLeft[i] <= arrRight[j]:
            arr[k] = arrLeft[i]
            i += 1
        else:
            arr[k] = arrRight[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = arrLeft[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = arrRight[j]
        j += 1
        k += 1

arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr, 0, len(arr) - 1)

print(arr)