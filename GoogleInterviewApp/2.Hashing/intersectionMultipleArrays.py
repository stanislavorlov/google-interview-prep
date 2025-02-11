# https://leetcode.com/problems/intersection-of-multiple-arrays/

# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
# return the list of integers that are present in each array of nums sorted in ascending order.

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]

# Input: nums = [[1,2,3],[4,5,6]]
# Output: []

from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans_set = set(nums[0])
        for idx in range(1, len(nums)):
            ans_set = ans_set & set(nums[idx])
            
        return sorted(ans_set)
    
    def intersection2(self, nums: List[List[int]]) -> List[int]:
        res = []
        map = {}
        for arr in nums:
            for val in arr:
                map[val] = map.get(val, 0) + 1
                
        for k, v in map.items():
            if v == len(nums):
                res.append(k)
                
        return sorted(res)
    
solution = Solution()
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
print(solution.intersection2(nums))

nums = [[1,2,3],[4,5,6]]
print(solution.intersection2(nums))