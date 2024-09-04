# A majority element in an array A[] of size n is an element that appears more than n/2 times 
# (and hence there is at most one such element)

arr = [3, 4, 3, 2, 4, 4, 4, 4]
n = 8

def find_majority_element(arr, n):
    map = {}
    for i in arr:
        map[i] = map.get(i, 0) + 1
        
        if map[i] > n // 2:
            return i
        
    return -1

print(find_majority_element(arr, n))