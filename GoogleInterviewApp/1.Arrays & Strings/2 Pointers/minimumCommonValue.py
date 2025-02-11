# https://leetcode.com/problems/minimum-common-value/

# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
# If there is no common integer amongst nums1 and nums2, return -1.

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1

solution = Solution()
nums1 = [1,2,3]
nums2 = [2,4]
print(solution.getCommon(nums1, nums2))

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
print(solution.getCommon(nums1, nums2))