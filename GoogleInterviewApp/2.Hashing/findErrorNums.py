# https://leetcode.com/problems/set-mismatch/
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        output = []

        for num in nums:
            if num in seen:
                output.append(num)
            else:
                seen.add(num)

        for i in range(1, n+1):
            if not i in seen:
                output.append(i)

        return output