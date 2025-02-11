# https://leetcode.com/problems/sliding-window-maximum/

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# Input: nums = [1], k = 1
# Output: [1]

from collections import deque
import sys
from typing import List
import unittest

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        return ans
    
class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._solution = Solution()
        
    def test_first(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        output = [3,3,5,5,6,7]
        self.assertEqual(self._solution.maxSlidingWindow(nums, k), output)

    def test_second(self):
        nums = [1]
        k = 1
        output = [1]
        self.assertEqual(self._solution.maxSlidingWindow(nums, k), output)

if __name__ == '__main__':
    unittest.main()