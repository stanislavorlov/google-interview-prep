# https://leetcode.com/problems/top-k-frequent-elements/description/
import heapq
import unittest
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        counter = Counter(nums)

        return heapq.nlargest(k, counter.keys(), key=counter.get)

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        solution = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2

        self.assertCountEqual(solution.topKFrequent(nums, k), [1, 2])

    def test_case_2(self):
        solution = Solution()
        nums = [1]
        k = 1

        self.assertCountEqual(solution.topKFrequent(nums, k), [1])

    def test_case_3(self):
        solution = Solution()
        nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
        k = 2

        self.assertCountEqual(solution.topKFrequent(nums, k), [1, 2])