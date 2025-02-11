# https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

import sys
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sum = 0
        ans = sys.maxsize
        
        for right in range(len(nums)):
            sum += nums[right]
            
            while sum >= target:
                ans = min(ans, right-left+1)
                sum -= nums[left]
                left += 1
            
        return ans if ans != sys.maxsize else 0
    
solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))

print(solution.minSubArrayLen(4, [1,4,4]))

print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))