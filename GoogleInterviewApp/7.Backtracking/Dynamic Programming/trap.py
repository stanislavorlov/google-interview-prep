# https://leetcode.com/problems/trapping-rain-water/description/
import unittest
from typing import List


class Solution:

    # brute force
    def trap(self, height: List[int]) -> int:
        answer = 0
        size = len(height)
        for i in range(1, size-1):
            left_max, right_max = 0, 0

            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])

            for j in range(i, size):
                right_max = max(right_max, height[j])

            answer += min(left_max, right_max) - height[i]

        return answer

    # dynamic programming
    def trap2(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1
        left_max, right_max = -1, -1
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                answer += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                answer += right_max - height[right]
                right -= 1

        return answer

class TestMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test1(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        ans = self.solution.trap2(height)
        self.assertEqual(ans, 6)

    def test2(self):
        height = [4, 2, 0, 3, 2, 5]
        ans = self.solution.trap2(height)
        self.assertEqual(ans, 9)
