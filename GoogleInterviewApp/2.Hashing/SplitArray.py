# You are given an integer array nums of even length. 
# You have to split the array into two parts nums1 and nums2 such that:

# nums1.length == nums2.length == nums.length / 2.
# nums1 should contain distinct elements.
# nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.

# Input: nums = [1,1,2,2,3,4]
# Output: true
# Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

from collections import defaultdict
import collections
from typing import List

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hash_map = defaultdict()
        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
            if hash_map[n] > 2:
                return False

        return True
    
class Solution2:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)

        return all(x <= 2 for x in counter.values())
    
solution = Solution2()
nums = [1,1,2,2,3,4]
print(solution.isPossibleToSplit(nums))

nums = [1,1,1,1]
print(solution.isPossibleToSplit(nums))