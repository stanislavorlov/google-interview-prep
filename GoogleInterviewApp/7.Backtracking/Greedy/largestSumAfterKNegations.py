# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
import unittest
from typing import List


class Solution:
    def largestSumAfterKNegations2(self, nums: List[int], k: int) -> int:
        while k > 0:
            nums.sort()
            nums[0] *= -1
            k -= 1

        return sum(nums)

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] < 0 < k:
                nums[i] *= -1
                k -= 1

        nums = sorted(nums)

        if k > 0 and k % 2 != 0:
            nums[0] = -nums[0]

        return sum(nums)

class TestLargestSumAfterKNegations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        nums = [4, 2, 3]
        k = 1

        self.assertEqual(5, self.solution.largestSumAfterKNegations(nums, k))

    def test_second(self):
        nums = [3, -1, 0, 2]
        k = 3

        self.assertEqual(6, self.solution.largestSumAfterKNegations(nums, k))

    def test_third(self):
        nums = [2, -3, -1, 5, -4]
        k = 2

        self.assertEqual(13, self.solution.largestSumAfterKNegations(nums, k))
