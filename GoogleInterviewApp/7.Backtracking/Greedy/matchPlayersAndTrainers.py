# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

import unittest
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()      # [4,7,9]
        trainers.sort()     # [2,5,8,8]

        i, j = 0, 0 # player, trainer
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
            j += 1

        return i

class TestMatchPlayersTrainers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_match1(self):
        assert self.solution.matchPlayersAndTrainers([4,7,9], [8,2,5,8]) == 2

    def test_match2(self):
        assert self.solution.matchPlayersAndTrainers([1,1,1], [10]) == 1