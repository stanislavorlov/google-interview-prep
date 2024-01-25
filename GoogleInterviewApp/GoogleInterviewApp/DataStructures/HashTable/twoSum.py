# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        map = {}
        for idx, num in enumerate(nums):
            if num in map.keys():
                return [map[num], idx]
            
            dif = target - num
            if dif not in map.keys():
                map[dif] = idx

        return []
    
# nums = [2,7,11,15]
# target = 9
    
# nums = [3,2,4]
# target = 6
    
nums = [3,3]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))