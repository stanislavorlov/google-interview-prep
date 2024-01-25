# You are given an array of strings words (0-indexed).
# 
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, 
# and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

# Input: words = ["abc","aabc","bc"]
# Output: true ["abc", "abc", "abc"]

# Input: words = ["ab","a"]
# Output: false

from collections import defaultdict

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        letters = defaultdict(int)
        wordsCount = len(words)
        for l in "".join(words):
           letters[l] += 1

        return all(value % wordsCount == 0 for value in letters.values())
        
solution = Solution()
print(solution.makeEqual(["abc","aabc","bc"]))
print(solution.makeEqual(["ab","a"]))