def isArraySorted(arr, n):
    if n == 1:
        return 1
    
    return 0 if arr[n-1] < arr[n-2] else isArraySorted(arr, n-1)

arr = [2,1,3,4,5]
print(isArraySorted(arr, len(arr)))