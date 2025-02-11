# https://leetcode.com/problems/subarray-product-less-than-k/

# Given an array of integers nums and an integer k, 
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    product, left, right = 1, 0, 0
    total_count = 0
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k:
            product //= nums[left]
            left += 1

        total_count += right - left + 1
            
    return total_count

nums = [10,5,2,6]
k = 100

print(numSubarrayProductLessThanK(nums, k))