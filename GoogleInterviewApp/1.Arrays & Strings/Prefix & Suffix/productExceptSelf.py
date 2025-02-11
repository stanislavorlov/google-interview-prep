# https://neetcode.io/problems/products-of-array-discluding-self

# Given an integer array nums, return an array output 
# where output[i] is the product of all the elements of nums except nums[i].

# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for j in range(n-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
            
        return res
    
solution = Solution()
nums = [1,2,4,6]
print(solution.productExceptSelf(nums))     # [48,24,12,8]

nums = [-1,0,1,2,3]
print(solution.productExceptSelf(nums))     # [0,-6,0,0,0]