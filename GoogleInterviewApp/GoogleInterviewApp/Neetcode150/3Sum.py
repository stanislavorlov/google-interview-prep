# https://neetcode.io/problems/three-integer-sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

import collections
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        
        for i,val in enumerate(nums):
            if val > 0:
                break
            
            if i > 0 and val == nums[i - 1]:
                continue

            left, right = i+1, n-1
            while left < right:
                threeSum = nums[left]+nums[right]+val
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append((val, nums[left], nums[right]))
                    left += 1
                    right -=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
        return result
    
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))

# [-4,-1,-1,0,1,2]