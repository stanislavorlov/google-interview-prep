# https://leetcode.com/problems/max-consecutive-ones/

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r = 0,0
        ans = 0
        for r,val in enumerate(nums):
            if not val:
                l = r + 1
            ans = max(ans, r-l+1)
        return ans

sol = Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))

print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))