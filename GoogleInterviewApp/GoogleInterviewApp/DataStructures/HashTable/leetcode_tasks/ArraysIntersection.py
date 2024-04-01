# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

import collections
from itertools import zip_longest

class Solution:

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]: # type: ignore
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        res = set()
        list_res = list()
        n_set = set(nums1)
        for n in nums2:
            if n in n_set and n not in res:
                res.add(n)
                list_res.append(n)
        
        return list_res
    
solution = Solution()

nums1 = [8,0,3]
nums2 = [0,0]

print(solution.intersection(nums1, nums2))      # [0]

nums1 = [1,2,2,1]
nums2 = [2,2]
print(solution.intersection(nums1, nums2))      # [2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(solution.intersection(nums1, nums2))      # [9,4]