# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

# Given a string s, return true if s is a good string, or false otherwise.
# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

from collections import defaultdict

class Solution:
    def areOccurrencesEqual2(self, s: str) -> bool:
        freq = defaultdict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        val = freq[s[0]]

        return all(value == val for value in freq.values())
    
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        val = freq[s[0]]

        for key in freq:
            if freq[key] != val:
                return False
            
        return True

solution = Solution()
print(solution.areOccurrencesEqual("abacbc"))       # true

print(solution.areOccurrencesEqual("aaabb"))        # false