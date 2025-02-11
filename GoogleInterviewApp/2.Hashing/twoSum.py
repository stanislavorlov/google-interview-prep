# https://neetcode.io/problems/two-integer-sum

from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i, n in enumerate(nums):
            if n in diff:
                return [diff[n], i]
            diff[target-n]=i
        return []