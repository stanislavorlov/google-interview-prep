# https://leetcode.com/problems/repeated-dna-sequences

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.

# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
# that occur more than once in a DNA molecule. You may return the answer in any order.

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

from collections import defaultdict
from typing import List
import unittest

class Solution:
    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        distinct = defaultdict(int)
        for right in range(len(s) - 9):
            distinct[s[right:right+10]] += 1
            
        return [key for key, value in distinct.items() if value > 1]
    
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        duplicates = set()
        hashes = set()
        for right in range(len(s) - 9):
            dna = s[right:right+10]
            if dna in hashes:
                duplicates.add(dna)
            else:
                hashes.add(dna)
        return list(duplicates)

class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self._solution = Solution()
        
    def test_first(self):
        s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
        output = ["AAAAACCCCC","CCCCCAAAAA"]
        self.assertEqual(self._solution.findRepeatedDnaSequences(s), output)

    def test_second(self):
        s = "AAAAAAAAAAAAA"
        output = ["AAAAAAAAAA"]
        self.assertEqual(self._solution.findRepeatedDnaSequences(s), output)
        
    def test_third(self):
        s = "AAAAAAAAAAA"
        output = ["AAAAAAAAAA"]
        self.assertEqual(self._solution.findRepeatedDnaSequences(s), output)

if __name__ == '__main__':
    unittest.main()