# https://leetcode.com/problems/first-missing-positive/description/
import unittest
from typing import List


# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * (n+1)

        for num in nums:
            if 0 < num <= n:
                seen[num] = True

        for i in range(1, n+1):
            if not seen[i]:
                return i

        return n+1

class TestMethods(unittest.TestCase):

    def test_first(self):
        solution = Solution()
        ans = solution.firstMissingPositive([1,2,0])

        self.assertEqual(3, ans)

    def test_second(self):
        solution = Solution()
        ans = solution.firstMissingPositive([3,4,-1,1])

        self.assertEqual(2, ans)

    def test_third(self):
        solution = Solution()
        ans = solution.firstMissingPositive([7,8,9,11,12])

        self.assertEqual(1, ans)

if __name__ == '__main__':
    unittest.main()