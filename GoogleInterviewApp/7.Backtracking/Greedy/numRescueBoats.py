# https://leetcode.com/problems/boats-to-save-people/description/
import unittest
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people) - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1

            ans += 1

        return ans

class TestNumRescueBoats(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        people = [1, 2]
        limit = 3

        self.assertEqual(self.solution.numRescueBoats(people, limit), 1)

    def test_second(self):
        people = [3, 2, 2, 1]
        limit = 3

        self.assertEqual(self.solution.numRescueBoats(people, limit), 3)

    def test_third(self):
        people = [3, 5, 3, 4]
        limit = 5

        self.assertEqual(self.solution.numRescueBoats(people, limit), 4)