# https://leetcode.com/problems/minimum-window-substring

# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# Example 1:
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

from collections import Counter, defaultdict
import string
import sys
import unittest

class Solution:
    def isCovered(self, s_map, t_map) -> bool:
        for key, value in t_map.items():
            if value > s_map.get(key, -1):
                return False
            
        return True

        # return all(t_map.get(key, None) == val for key, val in s_map.items())

    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        left, right, ans_len = 0, 0, sys.maxsize
        s_map = defaultdict(int)
        t_map = Counter(t)
        ans = ""
        while right < len(s):
            if s[right] in t_map:
                s_map[s[right]] += 1
            while self.isCovered(s_map, t_map):
                if right - left + 1 < ans_len:
                    ans_len = right - left
                    ans = s[left:right+1]
                s_map[s[left]] -= 1
                if s_map[s[left]] <= 0:
                    del s_map[s[left]]
                left += 1
            right += 1
                    
        return ans
    
class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._solution = Solution()
        
    def test_first(self):
        self.assertEqual(self._solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        
    def test_second(self):
        self.assertEqual(self._solution.minWindow("a", "a"), "a")

    def test_third(self):
        self.assertEqual(self._solution.minWindow("a", "aa"), "")
        
    def test_fourth(self):
        self.assertEqual(self._solution.minWindow("ab", "a"), "b")
        
if __name__ == '__main__':
    unittest.main()