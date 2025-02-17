# https://leetcode.com/problems/roman-to-integer/

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# four consistent chars not allowed

class Solution:
    def __init__(self):
        self._roman_values = {
            '': 0,
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        number = 0
        prev = ''

        for idx in range(len(s) - 1, -1, -1):
            if self._roman_values[prev] > self._roman_values[s[idx]]:
                number -= self._roman_values[s[idx]]
            else:
                number += self._roman_values[s[idx]]
            prev = s[idx]

        return number

solution = Solution()
s = "III"
print(solution.romanToInt(s))

s = "LVIII"
print(solution.romanToInt(s))

s = "MCMXCIV"
print(solution.romanToInt(s))