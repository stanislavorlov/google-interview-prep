# Given an array nums of n integers, return an array of all the unique quadruplets 
# [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# nums[a] + nums[b] + nums[c] + nums[d] == target

#Input: nums = [1,0,-1,0,-2,2], target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

#Input: nums = [2,2,2,2,2], target = 8
#Output: [[2,2,2,2]]

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list]:
        result = []

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            t = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                            if t not in result:
                                result.append(t)

        return result
    
    def fourSum2(self, nums: list[int], target: int) -> list[list]:
        return []
    
solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], target = 0))