# Contiguous Array
# https://leetcode.com/problems/contiguous-array/editorial/

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

from collections import defaultdict
from typing import List
import unittest

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n, left, ans = len(nums), 0, 0
        
        for right in range(n):
            left = right % 2
            while left < right:
                
                left = left + 1

class TestMethods(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        self._solution = Solution()
        super().__init__(methodName)
    
    def test_first(self):
        nums = [0,1]
        ans = self._solution.findMaxLength(nums)

        self.assertEqual(ans, 2)
        
    def test_second(self):
        nums = [0,1,0]
        ans = self._solution.findMaxLength(nums)

        self.assertEqual(ans, 2)
        
    def test_third(self):
        nums = [1,1,0,0]
        ans = self._solution.findMaxLength(nums)

        self.assertEqual(ans, 4)
        
    def test_fourth(self):
        nums = [1,1,1,1,1,1,1,1]
        ans = self._solution.findMaxLength(nums)

        self.assertEqual(ans, 0)
        
    def test_fifth(self):
        nums = [1,1,1,0,1,0,1,0,1,0,0,0]
        ans = self._solution.findMaxLength(nums)

        self.assertEqual(ans, 8)

unittest.main()