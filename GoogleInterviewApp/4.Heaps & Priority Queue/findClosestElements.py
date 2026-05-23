# https://leetcode.com/problems/find-k-closest-elements/

import unittest
from typing import List
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            distance = abs(num - x)
            heapq.heappush(heap, (-distance, -num))
            if len(heap) > k:
                heapq.heappop(heap)

        return sorted([-num[1] for num in heap])

    def findClosestElementsBinarySearch(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        arr = [1, 2, 3, 4, 5]
        k = 4
        x = 3
        # k closest to x
        self.assertEqual([1,2,3,4], self.solution.findClosestElementsBinarySearch(arr, k, x))

    def test_case_2(self):
        arr = [1,1,2,3,4,5]
        k = 4
        x = -1

        self.assertEqual([1,1,2,3], self.solution.findClosestElements(arr, k, x))