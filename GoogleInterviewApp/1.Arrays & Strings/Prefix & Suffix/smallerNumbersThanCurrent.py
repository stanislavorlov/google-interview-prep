# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
import unittest
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    counter += 1
            answer.append(counter)

        return answer

    def smallerNumbersThanCurrentPrefix(self, nums: List[int]) -> List[int]:
        # nums = [8,1,2,2,3]
        # freq = [1,1]
        # prefix[i] = number of elements < i

        max_elem = max(nums)
        n = max_elem + 1
        freq = [0] * n
        for i in range(len(nums)):
            freq[nums[i]] += 1

        prefix = [0]
        for i in range(max_elem):
            prefix.append(prefix[i] + freq[i])

        # nums = [8,1,2,2,3]
        # index:    0 1 2 3 4 5 6 7 8
        # freq:     0 1 2 1 0 0 0 0 1
        # prefix    0 0 1 3 4 4 4 4 4

        # answer = [prefix[8], prefix[1], prefix[2], prefix[2], prefix[3]]

        return [prefix[n] for n in nums]

class TestSmallNumbersThanCurrent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        nums = [8, 1, 2, 2, 3]
        self.assertEqual(self.solution.smallerNumbersThanCurrentPrefix(nums), [4, 0, 1, 1, 3])

    def test_second(self):
        nums = [6, 5, 4, 8]
        self.assertEqual(self.solution.smallerNumbersThanCurrentPrefix(nums), [2, 1, 0, 3])

    def test_third(self):
        nums = [7, 7, 7, 7]
        self.assertEqual(self.solution.smallerNumbersThanCurrentPrefix(nums),[0, 0, 0, 0])