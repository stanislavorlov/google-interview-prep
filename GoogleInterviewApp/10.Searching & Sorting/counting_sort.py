input_arr = [2,5,3,0,2,3,0,3]

# Θ(k+n)
def counting_sort(arr):
    max_elem = max(arr)
    count_arr = [0] * (max_elem+1)

    # k
    for num in arr:
        count_arr[num] += 1
    # count_arr contains count of num elements

    for i in range(1, max_elem+1):
        count_arr[i] += count_arr[i-1]
    # count_arr contains count of elements less or equals i

    output = [0] * len(arr)

    # n
    for i in range(len(arr) - 1, -1, -1):
        output[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1

    return output

input_array = [4, 3, 12, 1, 5, 5, 3, 9]
print(counting_sort(input_array))