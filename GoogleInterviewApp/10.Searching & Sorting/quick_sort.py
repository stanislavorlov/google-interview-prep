import random


def partition(arr, low, high):
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

    return partition(arr, low, high)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -=1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

# worst case: T(n)=T(n-1)+T(0)+Θ(n)=T(n-1)+Θ(n)=Θ(n^2)
# best case: T(n)=2T(n/2)+Θ(n)=Θ(n lgn)
def quick_sort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)

        quick_sort(arr, low, q-1)
        quick_sort(arr, q+1, high)

def quick_sort_randomized(arr, low, high):
    if low < high:
        q = randomized_partition(arr, low, high)
        quick_sort_randomized(arr, low, q)
        quick_sort_randomized(arr, q + 1, high)

def quick_sort_hoare(arr, low, high):
    if low < high:
        q = hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, q)
        quick_sort_hoare(arr, q+1, high)

def recursive_quick_sort(arr, low, high):
    while low < high:
        q = partition(arr, low, high)
        recursive_quick_sort(arr, low, q - 1)
        low = q + 1

input_arr = [2,8,7,1,3,5,6,4]
low_arr, high_arr = 0, len(input_arr)-1

#quick_sort(input_arr, low_arr, high_arr)
#print(input_arr)

#quick_sort_randomized(input_arr, low_arr, high_arr)
#print(input_arr)

#quick_sort_hoare(input_arr, low_arr, high_arr)
#print(input_arr)

recursive_quick_sort(input_arr, low_arr, high_arr)
print(input_arr)