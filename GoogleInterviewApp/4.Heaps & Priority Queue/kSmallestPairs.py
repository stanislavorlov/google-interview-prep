# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
import unittest
from typing import List
from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0,0))]
        visited.add((0,0))

        while k > 0 and minHeap:
            val, (i,j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i+1 < m and (i+1,j) not in visited:
                heappush(minHeap, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))

            if j+1 < n and (i, j+1) not in visited:
                heappush(minHeap, (nums1[i]+nums2[j+1], (i, j +1)))
                visited.add((i, j+1))

            k = k-1

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3

        self.assertSequenceEqual([[1,2],[1,4],[1,6]], self.solution.kSmallestPairs(nums1, nums2, k))

    def test2(self):
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 2

        self.assertSequenceEqual([[1,1],[1,1]], self.solution.kSmallestPairs(nums1, nums2, k))
