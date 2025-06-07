# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

import unittest


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        s_idx, t_idx = 0, 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                t_idx += 1
            s_idx += 1

        return len(t) - t_idx



class TestAppendCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        s = "coaching"
        t = "coding"

        result = self.solution.appendCharacters(s, t)
        self.assertEqual(result, 4)

    def test_second(self):
        s = "abcde"
        t = "a"

        result = self.solution.appendCharacters(s, t)
        self.assertEqual(result, 0)

    def test_third(self):
        s = "z"
        t = "abcde"

        result = self.solution.appendCharacters(s, t)
        self.assertEqual(result, 5)