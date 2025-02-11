# Given an array the task is to check whether there exist two elements with given sum

# time O(n)
# space O(n)
def findPairs(arr, sum):
    size = len(arr)
    hash_map = {}
    for n in arr:
        if n in hash_map:
            return True
        hash_map[sum-n] = n
    return False

# time O(NlogN)
# space O(1)
def findPairsSort(arr, sum):
    def binary_search(arr, low, high, key):
        while low <= high:
            m = (low + high) // 2
            if arr[m] == key:
                return True
            if arr[m] < key:
                low = m + 1
            else:
                high = m - 1
                
        return False

    arr.sort()
    
    i = 0
    while i < len(arr):
        key = sum - arr[i]
        if binary_search(arr, i + 1, len(arr)-1, key):
            return True
        i += 1
        
    return False

A = [1, 4, 45, 6, 10, 8]
print(findPairsSort(A, 18))

