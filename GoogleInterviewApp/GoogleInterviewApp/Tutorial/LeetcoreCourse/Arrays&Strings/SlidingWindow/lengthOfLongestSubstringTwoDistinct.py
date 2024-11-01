# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

# Given a string s, return the length of the longest substring that contains at most two distinct characters.

# Input: s = "eceba"
# Output: 3 ("ece")

# Input: s = "ccaabbb"
# Output: 5 ("aabbb")

from collections import defaultdict
import unittest

class Solution:
    # store count of characters
    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        ans, left = 0, 0
        distinct = defaultdict(int)
        for right in range(len(s)):
            distinct[s[right]] += 1
            while len(distinct) > 2:
                distinct[s[left]] -= 1
                if distinct[s[left]] == 0:
                    del distinct[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            
        return ans
    
    # store index
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        
        left, right = 0, 0
        max_len = 2
        distinct = defaultdict()
        
        while right < n:
            distinct[s[right]] = right
            right += 1

            if len(distinct) == 3:
                del_idx = min(distinct.values())
                del distinct[s[del_idx]]
                left = del_idx + 1
                
            max_len = max(max_len, right - left)
            
        return max_len
    
class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._solution = Solution()
        
    def test_first(self):
        self.assertEqual(self._solution.lengthOfLongestSubstringTwoDistinct("eceba"), 3)
        
    def test_second(self):
        self.assertEqual(self._solution.lengthOfLongestSubstringTwoDistinct("ccaabbb"), 5)
        
if __name__ == '__main__':
    unittest.main()