# https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Input: nums = [0]
# Output: [0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]):
        k = 0
        for i,n in enumerate(nums):
            if nums[i] != 0:
                tmp = nums[k]
                nums[k] = nums[i]
                nums[i] = tmp
                k+= 1
        
solution = Solution()
num1 = [0,1,0,3,12]
solution.moveZeroes(num1)
print(num1)

num2 = [0]
solution.moveZeroes(num2)
print(num2)