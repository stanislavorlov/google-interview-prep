# https://leetcode.com/problems/top-k-frequent-words/
import heapq
import unittest
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []

        for word, freq in counter.items():
            heapq.heappush(heap, (-freq, word))

        return [heapq.heappop(heap)[1] for _ in range(k)]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2

        self.assertSequenceEqual(["i","love"], self.solution.topKFrequent(words, k))

    def test_case_2(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4

        self.assertSequenceEqual(["the","is","sunny","day"], self.solution.topKFrequent(words, k))