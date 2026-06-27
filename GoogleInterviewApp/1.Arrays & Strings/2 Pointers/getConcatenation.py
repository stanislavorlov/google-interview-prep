# https://leetcode.com/problems/concatenation-of-array/
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 2 * n
        ans = [0] * l

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans