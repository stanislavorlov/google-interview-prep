# https://neetcode.io/problems/longest-consecutive-sequence

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# The elements do not have to be consecutive in the original array.

from collections import defaultdict
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        ans = 0
        for n in nums:
            if n-1 not in visited:
                cnt = 1
                while n + 1 in visited:
                    cnt += 1
                    n = n + 1
                ans = max(ans, cnt)
        return ans
    
    def longestConsecutive2(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
    
solution = Solution()
nums = [2,20,4,10,3,4,5]
print(solution.longestConsecutive2(nums))    # 4

nums = [0,3,2,5,4,6,1,1]
print(solution.longestConsecutive(nums))    # 7