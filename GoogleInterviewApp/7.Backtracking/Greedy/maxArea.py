# https://leetcode.com/problems/container-with-most-water/description/

import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0

        while left < right:
            answer = max(answer, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

        self.assertEqual(49, self.solution.maxArea(height))

    def test_case2(self):
        height = [1, 1]

        self.assertEqual(1, self.solution.maxArea(height))