# https://leetcode.com/problems/largest-unique-number/editorial/

# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

# Input: nums = [5,7,3,9,4,9,8,3,1]
# Output: 8

# Input: nums = [9,9,8,8]
# Output: -1

from typing import Counter, List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = -1
        for c in counter:
            if counter[c] == 1:
                ans = max(ans, c)
                
        return ans
    
solution = Solution()
nums = [5,7,3,9,4,9,8,3,1]
print(solution.largestUniqueNumber(nums))       # 8

nums = [9,9,8,8]
print(solution.largestUniqueNumber(nums))       # -1