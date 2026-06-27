import heapq
import math
import unittest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            # √(x1 - x2)2 + (y1 - y2)2
            distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

            heapq.heappush(heap, (-distance, [-x, -y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[-point[1][0], -point[1][1]] for point in heap]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        points = [[1, 3], [-2, 2]]
        k = 1

        self.assertCountEqual([[-2,2]], self.solution.kClosest(points, k))

    def test2(self):
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2

        self.assertCountEqual([[3, 3], [-2, 4]], self.solution.kClosest(points, k))