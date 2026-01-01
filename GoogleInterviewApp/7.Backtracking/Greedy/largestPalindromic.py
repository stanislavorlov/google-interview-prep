# https://leetcode.com/problems/largest-palindromic-number/description/

import unittest
from collections import Counter, defaultdict


class Solution:
    # works
    def largestPalindromic2(self, num: str) -> str:
        # build only front string
        counter = defaultdict(int)
        for c in num:
            counter[int(c)] += 1
        front = ''
        mid = ''
        n = 9

        while n > -1:
            if counter[n] > 1:
                front += str(n)
                counter[n] -= 2
            elif counter[n] == 1 and not len(mid):
                mid += str(n)
            else:
                n -= 1

        output = front.lstrip('0') + mid + front[::-1].rstrip('0')
        if not len(output) and len(num):
            return '0'

        return output

    # works
    def largestPalindromic(self, num: str) -> str:
        counter = defaultdict(int)
        for c in num:
            counter[int(c)] += 1
        max_dig = max(counter)

        front = ''
        mid = ''
        for i in range(max_dig, -1, -1):
            quotient, remainder = divmod(counter[i], 2)
            if remainder > 0 and not len(mid):
                mid += str(i)
            front += str(i) * quotient

        if max_dig > 0:
            front = front.lstrip('0')

            return front + mid + front[::-1]
        else:
            return "0"

solution = Solution()
print(solution.largestPalindromic('444947137'))
print(solution.largestPalindromic('00009'))
print(solution.largestPalindromic('00000'))

class TestLargestPalindromic(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test1(self):
        self.assertEqual(
            '7449447',
            self.solution.largestPalindromic('444947137'),
        )

    def test2(self):
        self.assertEqual(
            '9',
            self.solution.largestPalindromic('00009'),
        )

    def test3(self):
        self.assertEqual(
            '1005001',
            self.solution.largestPalindromic('00001105'),
        )

    def test4(self):
        self.assertEqual(
            "0",
            self.solution.largestPalindromic('00000'),
        )