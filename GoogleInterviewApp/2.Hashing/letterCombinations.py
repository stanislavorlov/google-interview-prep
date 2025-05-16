# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import unittest
from typing import List


# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.

class Solution:
    def __init__(self):
        self._mapping_digits_letters = {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        def backtrack(index, path):
            if len(path) == len(digits):
                output.append("".join(path))
                return

            possible_letters = self._mapping_digits_letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        output = []
        backtrack(0, [])

        return output

class TestMethods(unittest.TestCase):

    def test_first(self):
        solution = Solution()
        ans = solution.letterCombinations("23")

        self.assertEqual(["ad","ae","af","bd","be","bf","cd","ce","cf"], ans)

    def test_second(self):
        solution = Solution()
        ans = solution.letterCombinations("")

        self.assertEqual([], ans)

    def test_third(self):
        solution = Solution()
        ans = solution.letterCombinations("2")

        self.assertEqual(["a", "b", "c"], ans)

if __name__ == '__main__':
    unittest.main()