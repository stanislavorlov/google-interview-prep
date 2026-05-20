# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/

import heapq
import unittest
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)

        while k > 0:
            pile = heapq.heappop(heap) * -1
            heapq.heappush(heap, ((pile - floor(pile / 2)) * -1))
            k -= 1

        return sum([-num for num in heap])

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        self.assertEqual(12, solution.minStoneSum([5,4,9], 2))

    def test_case_2(self):
        solution = Solution()
        self.assertEqual(12, solution.minStoneSum([4,3,6,7], 3))