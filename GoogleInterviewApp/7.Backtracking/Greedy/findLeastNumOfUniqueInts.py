# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
import unittest
from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1]))

        for key, value in sorted_counter.items():
            if k:
                counter[key] -= min(value, k)
                k -= min(value, k)
                if counter[key] <= 0:
                    del counter[key]
            else:
                break

        return len(counter)

    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        frequencies = list(freq_map.values())

        frequencies.sort()

        elements_removed = 0

        for i in range(len(frequencies)):
            elements_removed += frequencies[i]

            if elements_removed > k:
                return len(frequencies) - i

        return 0

class TestPartitionArray(unittest.TestCase):
    def test_findLeastNumOfUniqueInts_one(self):
        solution = Solution()

        assert solution.findLeastNumOfUniqueInts2([5,5,4], 1) == 1

    def test_findLeastNumOfUniqueInts_two(self):
        solution = Solution()

        assert solution.findLeastNumOfUniqueInts2([4,3,1,1,3,3,2], 3) == 2