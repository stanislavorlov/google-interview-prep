# https://neetcode.io/problems/longest-consecutive-sequence

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# The elements do not have to be consecutive in the original array.

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest, length = 0, 1
        for n in nums:
            seen.add(n)
            if n-1 in seen:
                length += 1
            else:
                longest = max(longest, length)
                length = 1
        return longest
    
solution = Solution()
nums = [2,20,4,10,3,4,5]
print(solution.longestConsecutive(nums))    # 4

nums = [0,3,2,5,4,6,1,1]
print(solution.longestConsecutive(nums))    # 7