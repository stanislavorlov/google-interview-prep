# T(n) =  Θ(1) + 2T(n/2) + Θ(n) + Θ(1) = 2T(n/2) + Θ(n) =  Θ(n lg n)
def find_maximum_subarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)                    # T(n/2)
        right_low, right_high, right_sum = find_maximum_subarray(arr, mid + 1, high)            # T(n/2)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)      # Θ(n)
        if left_sum >= right_sum and left_sum >= cross_sum:                                     # Θ(1)
            return left_low, left_high, left_sum                                                # Θ(1)
        elif right_sum >= left_sum and right_sum >= cross_sum:                                  # Θ(1)
            return right_low, right_high, right_sum                                             # Θ(1)
        else:                                                                                   # Θ(1)
            return cross_low, cross_high, cross_sum                                             # Θ(1)

# Θ(n) = (mid-low+1) + (high-mid) = high - low + 1 = n
def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum_val = 0
    max_left = -1
    for i in range(mid, low, -1):
        sum_val = sum_val + arr[i]
        if sum_val > left_sum:
            left_sum = sum_val
            max_left = i
    right_sum = float('-inf')
    sum_val = 0
    max_right = -1
    for j in range(mid+1, high):
        sum_val = sum_val + arr[j]
        if sum_val > right_sum:
            right_sum = sum_val
            max_right = j
            
    return max_left, max_right, left_sum + right_sum

input_array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(find_maximum_subarray(input_array, 0, len(input_array) - 1))      # [18,20,-7,12]