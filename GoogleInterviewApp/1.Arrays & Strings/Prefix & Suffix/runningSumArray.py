# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4658/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        
        for i in range(1, len(nums)):
            runningSum.append(runningSum[-1] + nums[i])
            
        return runningSum
    
solution = Solution()
nums = [1,2,3,4]
print(solution.runningSum(nums))

nums = [1,1,1,1,1]
print(solution.runningSum(nums))

nums = [3,1,2,10,1]
print(solution.runningSum(nums))

nums = [-2, 0, 3, -5, 2, -1]
print(solution.runningSum(nums))