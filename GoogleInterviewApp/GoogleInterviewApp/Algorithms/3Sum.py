# https://leetcode.com/problems/3sum/description/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution:
      
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans, l = [], len(nums)

        for i in range(0, l):
            res = self.twoSum(nums, i+1, l, -nums[i])
            if res:
                ans.append((nums[i], res))

        return ans
    
    def twoSum(self, nums: list[int], start, end, sum):
        s, res = {}, []
        for i in range(start, end):
            n = nums[i]
            if n in s:
                res.append((n, s[n]))
            s[sum - n] = n
        return res

        
solution = Solution()
nums = [-1,0,1,2,-1,-4]
# -4, -1, -1,  0,  1,  2
#  0   1   2   3   4   5
print(solution.threeSum(nums))