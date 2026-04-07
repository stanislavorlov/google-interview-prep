# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
import unittest
from collections import defaultdict
from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        n = len(nums)

        for i in range(1, n+1):
            count[i]=0

        for num in nums:
            count[num] += 1

        return [c for c in count if count[c]==0]

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        arr = []
        count = [0] * (len(nums) + 1)
        for i in nums:
            count[i] += 1

        for j in range(1, len(count)):
            if not count[j]:
                arr.append(j)

        return arr

class TestFindDisappearedNumbers(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        self.assertEqual(self.sol.findDisappearedNumbers(nums), [5,6])

    def test2(self):
        nums = [1, 1]
        self.assertEqual(self.sol.findDisappearedNumbers(nums), [2])

