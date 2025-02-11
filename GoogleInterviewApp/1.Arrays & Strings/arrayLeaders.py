# find all leaders in array. An element is a leader if it is greater than all the elements to right side.

# O(n)
def findLeaders(arr):
    n = len(arr)
    
    if n < 1:
        return []
    
    max_el = arr[n-1]
    leaders = [max_el]
    
    for i in range(n-2, 0, -1):
        if arr[i] > max_el:
            leaders.append(arr[i])
            max_el = arr[i]
    
    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(findLeaders(arr))