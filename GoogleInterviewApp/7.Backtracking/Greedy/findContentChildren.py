import unittest
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if s[s_idx] >= g[g_idx]:
                g_idx += 1
            s_idx += 1

        return g_idx

class TestFindContentChildren(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findContentChildren(self):
        assert self.solution.findContentChildren([1,2,3], [1,1]) == 1

    def test_findContentChildren_two(self):
        assert self.solution.findContentChildren([1,2], [1,2,3]) == 2

    def test_findContentChildren_three(self):
        assert self.solution.findContentChildren([10,9,8,7], [5,6,7,8]) == 2