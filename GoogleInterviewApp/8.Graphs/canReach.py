# https://leetcode.com/problems/jump-game-iii/description/
import unittest
from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        queue = deque([start])
        visited = {start}
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True

            left_jump, right_jump = node - arr[node], node + arr[node]
            if left_jump >= 0 and not left_jump in visited:
                queue.append(left_jump)
                visited.add(left_jump)
            if right_jump < len(arr) and not right_jump in visited:
                queue.append(right_jump)
                visited.add(right_jump)

        return False

class SolutionDfs:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] *= -1

            return self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])

        return False

class UniTests(unittest.TestCase):
    def setUp(self):
        self.solution = SolutionDfs()

    def test1(self):
        actual = self.solution.canReach([4, 2, 3, 0, 3, 1, 2], 5)
        self.assertEqual(actual, True)

    def test2(self):
        actual = self.solution.canReach([4, 2, 3, 0, 3, 1, 2], 0)
        self.assertEqual(actual, True)

    def test3(self):
        actual = self.solution.canReach([3, 0, 2, 1, 2], 2)
        self.assertEqual(actual, False)