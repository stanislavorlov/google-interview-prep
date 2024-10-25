# https://leetcode.com/problems/sort-array-by-parity/

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1] or [4,2,3,1], [2,4,1,3], and [4,2,1,3]

# Input: nums = [0]
# Output: [0]

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        isLeftOdd, isRightEven = False, False
        while left < right:
            isLeftOdd = nums[left] % 2 != 0
            isRightEven = nums[right] % 2 == 0
                
            if isLeftOdd and isRightEven:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -=1
            elif isLeftOdd and not isRightEven:
                right -= 1
            else:
                left += 1
                
        return nums
    
    def sortArrayByParity2(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] % 2 == 0:
                left += 1
                
            if nums[right] % 2 == 0:
                right -= 1
            
        return nums

sol = Solution()
print(sol.sortArrayByParity2([3,1,2,4]))
print(sol.sortArrayByParity2([0]))
print(sol.sortArrayByParity2([1,0,3,2]))