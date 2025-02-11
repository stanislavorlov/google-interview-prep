# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

from collections import defaultdict
import collections
from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    interset = defaultdict(int)
    res = []
    for n1 in nums1:
        interset[n1] += 1

    for n2 in nums2:
        if n2 in interset and interset[n2] > 0:
            interset[n2] -= 1
            res.append(n2)

    return res

def intersect2(nums1: List[int], nums2: List[int]) -> List[int]:
    c12 = collections.Counter(nums1) & collections.Counter(nums2)
    #c12.items()    # [(4, 1), (9, 1), (5, 1)]
    return list(c12.elements())

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))      # 82 ms

print(intersect2(nums1, nums2))     # 51 ms