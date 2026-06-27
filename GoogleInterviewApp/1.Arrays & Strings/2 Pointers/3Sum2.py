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
    
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                amount = val + nums[left] + nums[right]
                if amount < 0:
                    left += 1
                elif amount > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

        return answer

def threeSum3(self, nums: list[int]) -> list[list[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1 :]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return  [list(x) for x in res]
        
solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum3(nums))     # [[-1,-1,2],[-1,0,1]]