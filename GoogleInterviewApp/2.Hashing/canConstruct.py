# https://leetcode.com/problems/ransom-note/editorial/

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
# by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from typing import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        
        for r_l in r_counter:
            if r_l not in m_counter or m_counter[r_l] < r_counter[r_l]:
                return False
            
        return True
    
solution = Solution()
print(solution.canConstruct("aa", "aab"))   # true

print(solution.canConstruct("a", "b"))      # false

print(solution.canConstruct("aa", "ab"))      # false