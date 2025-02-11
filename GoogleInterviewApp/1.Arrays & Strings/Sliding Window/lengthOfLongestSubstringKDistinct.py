# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

# Given a string s and an integer k, return the length of the longest 
# substring of s that contains at most k distinct characters.

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.

from collections import defaultdict
import sys
import unittest

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        distinct = defaultdict()
        
        n = len(s)
        left, right = 0, 0
        ans = -sys.maxsize
        while right < n:
            distinct[s[right]] = right
            right+=1
            
            if len(distinct) > k:
                del_idx = min(distinct.values())
                del distinct[s[del_idx]]
                left = del_idx + 1
            ans = max(ans, right-left)

        return ans

class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._solution = Solution()
        
    def test_first(self):
        s = "eceba"
        k = 2
        output = 3
        self.assertEqual(self._solution.lengthOfLongestSubstringKDistinct(s, k), output)

    def test_second(self):
        s = "aa"
        k = 1
        output = 2
        self.assertEqual(self._solution.lengthOfLongestSubstringKDistinct(s, k), output)

if __name__ == '__main__':
    unittest.main()