# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0.0
        for i in range(k):
            sum += nums[i]
            
        max_sum = sum
        for j in range(k, len(nums)):
            sum = sum - nums[j-k] + nums[j]
            max_sum = max(sum, max_sum)
            
        return max_sum / k

solution = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(solution.findMaxAverage(nums, k))