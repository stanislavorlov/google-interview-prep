# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4657/

# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# nums = [-3,2,-3,4,2]
# Output: 5 (5-3+2-3+4+2)
 
# nums = [1,2]
# Output: 1

# nums = [1,-2,-3]
# Output: 5

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal, total = 0, 0
        
        for num in nums:
            total += num
            minVal = min(minVal, total)
            
        return -minVal + 1

solution = Solution()
print(solution.minStartValue([-3,2,-3,4,2]))

print(solution.minStartValue([1,2]))

print(solution.minStartValue([1,-2,-3]))