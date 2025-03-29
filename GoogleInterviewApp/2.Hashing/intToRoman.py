# https://leetcode.com/problems/integer-to-roman/
import math
import unittest
from unicodedata import digit


class Solution:

    def __init__(self):
        self.roman_to_integer_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

    def intToRoman(self, num: int) -> str:
        # 1 <= num <= 3999
        roman_digits = []
        for value, symbol in self.roman_to_integer_map:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman_digits.append(symbol * count)

        return "".join(roman_digits)

    def int_to_roman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            thousands[num // 1000] +
            hundreds[num % 1000 // 100] +
            tens[num % 100 // 10] +
            ones[num % 10]
        )

class TestMethods(unittest.TestCase):

    def test_first(self):
        solution = Solution()
        ans = solution.intToRoman2(3749)

        self.assertEqual("MMMDCCXLIX", ans)

    def test_second(self):
        solution = Solution()
        ans = solution.intToRoman2(58)

        self.assertEqual("LVIII", ans)

    def test_third(self):
        solution = Solution()
        ans = solution.intToRoman2(1994)

        self.assertEqual("MCMXCIV", ans)

    def test_ten(self):
        solution = Solution()
        ans = solution.intToRoman2(10)

        self.assertEqual("X", ans)

    def test_20(self):
        solution = Solution()
        ans = solution.intToRoman2(20)

        self.assertEqual("XX", ans)

if __name__ == '__main__':
    unittest.main()