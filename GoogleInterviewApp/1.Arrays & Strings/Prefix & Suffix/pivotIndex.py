# https://leetcode.com/problems/find-pivot-index/

# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly 
# to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# nums = [1,7,3,6,5,6]
# Output: 3
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            
        return -1
    
solution = Solution()
print(solution.pivotIndex([1,7,3,6,5,6]))       # nums[0] + nums[1] + nums[2] == nums[4] + nums[5] == 1

print(solution.pivotIndex([1,2,3]))             # -1

print(solution.pivotIndex([2,1,-1]))            # 0 == nums[1] + nums[2]