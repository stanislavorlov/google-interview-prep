# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [3,2,1,5,6,4]
        k = 2

        self.assertEqual(5, self.solution.findKthLargest(nums, k))

    def test_case_2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4

        self.assertEqual(4, self.solution.findKthLargest(nums, k))