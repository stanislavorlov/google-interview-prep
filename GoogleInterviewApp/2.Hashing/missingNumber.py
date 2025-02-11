# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4602/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Input: nums = [3,0,1]
# Output: 2

# Input: nums = [0,1]
# Output: 2

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        seen = set(nums)
        for i in range(n):
            if not i in seen:
                return i
            
sol = Solution()
print(sol.missingNumber([3,0,1]))

print(sol.missingNumber([0,1]))

print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))