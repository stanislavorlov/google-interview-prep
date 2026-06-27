# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

import unittest
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binarySearch(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            i = binarySearch(potions, success / spell)
            ans.append(m-i)

        return ans

class SoltuionTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        spells = [5, 1, 3]
        potions = [1, 2, 3, 4, 5]
        success = 7

        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [4,0,3])

    def test2(self):
        spells = [3, 1, 2]
        potions = [8, 5, 8]
        success = 16

        self.assertEqual(self.solution.successfulPairs(spells, potions, success), [2,0,2])