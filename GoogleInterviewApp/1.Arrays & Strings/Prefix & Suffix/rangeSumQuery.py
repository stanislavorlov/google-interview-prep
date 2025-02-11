# https://leetcode.com/problems/range-sum-query-immutable/description/

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.runningSum = [0] * (len(nums)+1)
        for i in range(0, len(nums)):
            self.runningSum[i+1] = self.runningSum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.runningSum[right+1] - self.runningSum[left]

# [0, -2, -2, 1, -4, -2, -3]
# sumRange(0, 1) = -2+0 = -2
# sumRange(0, 2) = -2+0+3 = 1
# sumRange(0, 3) = -2+0+3-5 = -4
# sumRange(2, 5) = 3-5+2-1 = -1
# sumRange(2, 2) = 3

# runningSum
# [0, -2, -2, 1, -4, -2, -3]

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0,2))
print(numArray.sumRange(2,5))
print(numArray.sumRange(0,5))