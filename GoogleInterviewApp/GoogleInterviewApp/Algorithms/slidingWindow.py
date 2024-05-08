# Problem: Maximum Sum Subarray of Size K

# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

# Example: Input: nums = [2, 1, 5, 1, 3, 2], k = 3 Output: 9 (The subarray [5, 1, 3] has the maximum sum of 9)

def max_subarray_sum(nums, k):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i - (k - 1)]

    return max_sum
    
    
print(max_subarray_sum([4, 5, 6, 7, 1, 4, 9, 0, 3, 1, 7], 3)) # Output: 18