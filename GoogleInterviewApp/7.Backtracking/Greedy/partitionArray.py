# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/

import unittest
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - x > k:
                ans += 1
                x = nums[i]

        return ans


class TestPartitionArray(unittest.TestCase):
    def test_partitionArray_one(self):
        solution = Solution()

        assert solution.partitionArray([3,6,1,2,5], 2) == 2

    def test_partitionArray_two(self):
        solution = Solution()

        assert solution.partitionArray([1,2,3], 1) == 2

    def test_partitionArray_three(self):
        solution = Solution()

        assert solution.partitionArray([2,2,4,5], 0) == 3