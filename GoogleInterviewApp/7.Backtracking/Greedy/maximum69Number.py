# https://leetcode.com/problems/maximum-69-number/description/
import unittest


class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)
        if '6' in num_str:
            six_index = num_str.index('6')
            output = ''
            for i in range(len(num_str)):
                if i == six_index:
                    output += '9'
                else:
                    output += num_str[i]

            return int(output)

        return num

    def maximum69Number2(self, num: int) -> int:
        num_char_list = list(str(num))

        for i, cur_char in enumerate(num_char_list):
            if cur_char == '6':
                num_char_list[i] = '9'
                break

        return int(''.join(num_char_list))

    def maximum69Number3(self, num: int) -> int:
        num_string = str(num)

        return int(num_string.replace('6', '9', 1))

    def maximum69Number4(self, num: int) -> int:
        # Since we start with the lowest digit, initialize curr_digit = 0.
        curr_digit = 0
        index_first_six = -1
        num_copy = num

        # Check every digit of 'num_copy' from low to high.
        while num_copy:
            # If the current digit is '6', record it as the highest digit of 6.
            if num_copy % 10 == 6:
                index_first_six = curr_digit

            # Move on to the next digit.
            num_copy //= 10
            curr_digit += 1

        # If we don't find any digit of '6', return the original number,
        # otherwise, increment 'num' by the difference made by the first '6'.
        return num if index_first_six == -1 else num + 3 * 10 ** index_first_six


class TestMaximum69Number(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        num = 9669

        self.assertEqual(self.solution.maximum69Number(num), 9969)

    def test_second(self):
        num = 9996

        self.assertEqual(self.solution.maximum69Number(num), 9999)

    def test_third(self):
        num = 9999

        self.assertEqual(self.solution.maximum69Number(num), 9999)