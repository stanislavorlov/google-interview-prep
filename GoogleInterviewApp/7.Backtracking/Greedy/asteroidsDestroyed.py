# https://leetcode.com/problems/destroying-asteroids/
import unittest
from typing import List


class Solution:
    def ateroirdsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False

            mass += asteroid

        return True

solution = Solution()

class TestAsteroidsDestroyed(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        mass = 10
        asteroids = [3, 9, 19, 5, 21]
        self.assertTrue(self.solution.ateroirdsDestroyed(mass, asteroids))

    def test_second(self):
        mass = 5
        asteroids = [4, 9, 23, 4]
        self.assertFalse(self.solution.ateroirdsDestroyed(mass, asteroids))