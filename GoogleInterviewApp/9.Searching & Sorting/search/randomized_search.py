import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition_high(arr, low, high):
    pivot = arr[high]               # Could arr[low], arr[high], arr[(low+high) //2], arr[random(low, high)]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i+1, high)

    return i+1

def randomized_partition(arr, low, high):
    i = random.randrange(low, high)
    swap(arr, high, i)

    return partition_high(arr, low, high)

# returns the ith smallest element
def randomized_search(arr, left, right, i):
    if left == right:
        return arr[left]

    partition = randomized_partition(arr, left, right)
    mid = partition - left + 1
    if i == mid:
        return arr[partition]
    elif i < mid:
        return randomized_search(arr, left, partition - 1, i)
    else:
        return randomized_search(arr, partition + 1, right, i - mid)

array = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]
print(randomized_search(array, 0, len(array) - 1, 6))