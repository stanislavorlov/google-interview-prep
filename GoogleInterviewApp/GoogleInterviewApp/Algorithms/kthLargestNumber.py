# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

import sys
from typing import List

def kthLargestNumber(nums: List[int], k: int) -> int:
    min_v, max_v = sys.maxsize, -sys.maxsize

    for n in nums:
        min_v = min(min_v, n)
        max_v = max(max_v, n)

    map = {}
    for i in nums:
        map[i] = map.get(i, 0) + 1

    for i in range(max_v, min_v - 1, -1):
        if i in map:
            k -= map[i]
            if k <= 0:
                return i

    return -1

nums = [3, 6, 7, 10]
print(kthLargestNumber(nums, 4))