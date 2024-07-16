# https://leetcode.com/problems/4sum/description/

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
        s, m = set(), len(nums)
        nums.sort()

        for i in range(m-3):
            for j in range(i+1, m-2):
                l,r = j+1, m-1

                while l < r:
                    if nums[i]+nums[j]+nums[l]+nums[r] == target:
                        s.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[i]+nums[j]+nums[l]+nums[r] < target:
                        l += 1
                    else:
                        r -= 1

        return list(s)
    
solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], target = 0))