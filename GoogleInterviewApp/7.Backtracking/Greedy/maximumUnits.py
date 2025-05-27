# https://leetcode.com/problems/maximum-units-on-a-truck/description/
import unittest
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        answer = 0
        for boxType in boxTypes:
            box_count = min(boxType[0], truckSize)
            answer += box_count * boxType[1]
            truckSize -= box_count
            if truckSize == 0:
                break

        return answer

class TestMaximum69Number(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        boxTypes = [[1,3],[2,2],[3,1]]
        truckSize = 4

        self.assertEqual(self.solution.maximumUnits(boxTypes, truckSize), 8)

    def test_second(self):
        boxTypes = [[5,10],[2,5],[4,7],[3,9]]
        truckSize = 10

        self.assertEqual(self.solution.maximumUnits(boxTypes, truckSize), 91)

    def test_third(self):
        boxTypes = [[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]]
        truckSize = 35

        self.assertEqual(self.solution.maximumUnits(boxTypes, truckSize), 76)