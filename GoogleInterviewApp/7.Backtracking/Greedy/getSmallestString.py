# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description/

from collections import deque


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # a = 1, z = 26
        d = deque()
        while k > 0:
            code = min(k - n + 1, 26)
            d.appendleft(chr(code - 1 + ord('a')))
            k -= code
            n -= 1

        return ''.join(d)

    def getSmallestString2(self, n: int, k: int) -> str:
        char_arr = [''] * n
        for position in range(n):
            position_left = (n - position - 1)
            if k > position_left * 26:
                add = k - (position_left * 26)
                char_arr[position] = chr(add - 1 + ord('a'))
                k -= add
            else:
                char_arr[position] = 'a'
                k -= 1

        return ''.join(char_arr)

solution = Solution()
print(solution.getSmallestString2(n=3, k=27))    # aay       1+1+25

print(solution.getSmallestString2(n=5, k=73))    # aaszz     1+1+19+26+26
