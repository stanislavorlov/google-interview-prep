def merge_sort(arr):
    if len(arr) < 2:
        return
    
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
        
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
        
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

arr_test = [2,3,5,1,7,4,4,4,2,6,0]
merge_sort(arr_test)

print(arr_test)