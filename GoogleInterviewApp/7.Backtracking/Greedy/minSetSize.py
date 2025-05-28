# https://leetcode.com/problems/reduce-array-size-to-the-half/

import unittest
from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        n = len(arr)
        size = n
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        answer = 0
        for pair in sorted_counter:
            size -= pair[1]
            answer += 1
            if size <= n // 2:
                break

        return answer

    def minSetSize_sorting(self, arr: List[int]) -> int:
        arr.sort()

        counts = []
        current_run = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                current_run += 1
                continue
            counts.append(current_run)
            current_run = 1
        counts.append(current_run)

        counts.sort(reverse=True)

        numbers_removed = 0
        set_size = 0
        for count in counts:
            numbers_removed += count
            set_size += 1
            if numbers_removed >= len(arr) // 2:
                break

        return set_size

class TestMinSetSize(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        arr = [3,3,3,3,5,5,5,2,2,7]
        ans = self.solution.minSetSize_sorting(arr)

        self.assertEqual(ans, 2)

    def test_second(self):
        arr = [7,7,7,7,7,7]
        ans = self.solution.minSetSize_sorting(arr)

        self.assertEqual(ans, 1)