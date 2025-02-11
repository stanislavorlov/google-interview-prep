# Find element in unsorted array

# O(n)
def findElement(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        
    return -1

# O(1)
def insert(arr, el):
    arr.append(el)

# O(n)
def deleteElement(arr, key):
    arr.delete(key)

arr = [12, 34, 10, 6, 40]
key = 40