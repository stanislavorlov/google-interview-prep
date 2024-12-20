# Permutation in String

# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise.

# Input: s1 = "abc", s2 = "lecabee"
# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Input: s1 = "abc", s2 = "lecaabee"
# Output: false

from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)
        s1Counter = Counter(s1)
        
        while right <= len(s2):
            s2Counter = Counter(s2[left:right])
            
            if s1Counter == s2Counter:
                return True
            
            left, right = left + 1, right + 1
            
        return False
    
solution = Solution()
print(solution.checkInclusion(s1 = "abc", s2 = "lecabee"))      # true

print(solution.checkInclusion(s1 = "abc", s2 = "lecaabee"))     # false