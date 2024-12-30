# Contiguous Array
# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4845/

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
        
        for left in range(n):
            cnt = defaultdict(int)
            right = left + 1
            
            while right < n:
                num_zeroes, num_ones = 2-nums[right-1]-nums[right], nums[right-1]+nums[right]
                
                if num_zeroes == num_ones:
                    ans = max(ans, right-left+1)

                right += 1
            
        return ans

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

        self.assertEqual(ans, 2)
        
    def test_fourth(self):
        nums = [1,1,1,1,1,1,1,1]
        ans = self._solution.findMaxLength(nums)

        self.assertEqual(ans, 0)

unittest.main()