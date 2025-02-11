# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]
# 0 = "barfoo"
# 9 = "foobar"

from collections import defaultdict
from typing import Counter, List
import unittest

class Solution:
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
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

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = len(words)
        step = word_count * word_len
        ans = []
        w_dict = Counter(words)

        for i in range(len(s) - step + 1):
            j = i
            c_dict = dict(w_dict)
            
            while j < i + step:
                word = s[j:j + word_len]
                if word in c_dict:
                    c_dict[word] -= 1
                    if c_dict[word] <= 0:
                        del c_dict[word]
                j += word_len
            if len(c_dict) == 0:
                ans.append(i)
        
        return ans

class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._solution = Solution()
        
    def test_first(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        self.assertEqual(self._solution.findSubstring(s, words), [0,9])

    def test_second(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        self.assertEqual(self._solution.findSubstring(s, words), [])

    def test_third(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]
        self.assertEqual(self._solution.findSubstring(s, words), [8])

    def test_fourth(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        self.assertEqual(self._solution.findSubstring(s, words), [6, 9, 12])
        
    def test_fifth(self):
        s = "aaaa"
        words = ["a", "a", "a", "a"]
        self._solution.findSubstring(s, words)
        
if __name__ == '__main__':
    unittest.main()