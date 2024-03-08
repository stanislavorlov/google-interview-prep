# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

import collections
from itertools import zip_longest

class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        cnt1 = {}
        cnt2 = {}
        for ch1, ch2 in zip_longest(s, t):
            if ch1 != None:
                cnt1[ch1] = cnt1.get(ch1, 0) + 1
            if ch2 != None:
                cnt2[ch2] = cnt2.get(ch2, 0) + 1

        return cnt1 == cnt2
    
    def isAnagram3(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
solution = Solution()
print(solution.isAnagram("a", "ab"))
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))