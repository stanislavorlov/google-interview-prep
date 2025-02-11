def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j] < arr[j-1]:
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp

arr = [6,5,4,3,2,1]
bubbleSort(arr)
print(arr)