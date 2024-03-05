# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        idx1 = 0
        idx2 = 0
        str = []
        
        while idx1 < l1 or idx2 < l2:
            if idx1 < l1:
                str += word1[idx1]
                idx1 += 1

            if idx2 < l2:
                str += word2[idx2]
                idx2 += 1

        return "".join(str)
    
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        str = ""
        for w1,w2 in zip_longest(word1, word2, fillvalue = ''):
            str = str + w1 + w2

        return str
    
solution = Solution()
print(solution.mergeAlternately2("abc", "pqr"))      #   "apbqcr"
print(solution.mergeAlternately2("ab", "pqrs"))      #   "apbqrs"
print(solution.mergeAlternately2("abcd", "pq"))      #   "apbqcd"