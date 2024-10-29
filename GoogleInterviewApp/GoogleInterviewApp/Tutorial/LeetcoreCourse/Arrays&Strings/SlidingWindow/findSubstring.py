# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]
# 0 = "barfoo"
# 9 = "foobar"

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        word_count = len(words)
        window_size = word_size * word_count
        step = 0
        outputs = []
        
        for step in range(len(s) - window_size + 1):
            j = step
            combinations = []
            while j < step + window_size:
                combinations.append(s[j:j+word_size])
                j += word_size
            if sorted(words) == sorted(combinations):
                outputs.append(step)
                
        return outputs

solution = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(solution.findSubstring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(solution.findSubstring(s, words))

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(solution.findSubstring(s, words))

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(solution.findSubstring(s, words))