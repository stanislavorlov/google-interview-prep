# https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# nums = [0,0,1,2,3]
# Output = [1,2,3,0,0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writer = 0
        for n in nums:
            if n:
                nums[writer] = n
                writer += 1
                
        while writer < len(nums):
            nums[writer] = 0
            writer += 1
            
    def moveZeroes2(self, nums: List[int]) -> None:
        writer = 0
        for i, n in enumerate(nums):
            if n:
                tmp = nums[writer]
                nums[writer] = n
                nums[i] = tmp
                writer += 1
                        
solution = Solution()
arr = [0,1,0,3,12]
solution.moveZeroes2(arr)        # [1,3,12,0,0]
print(arr)

arr = [1,0,3,0,12]
solution.moveZeroes2(arr)        # [1,3,12,0,0]
print(arr)