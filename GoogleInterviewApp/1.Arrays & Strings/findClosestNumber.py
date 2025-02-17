# https://leetcode.com/problems/find-closest-number-to-zero/
import sys
from typing import List


# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.

# Input: nums = [-4,-2,1,4,8]
# Output: 1

# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.

def findClosestNumber(nums: List[int]) -> int:
    closest = sys.maxsize

    for n in nums:
        if abs(n) < abs(closest):
            closest = n
        elif abs(n) == abs(closest):
            closest = max(n, closest)

    return closest

nums = [2,-1,1]
print(findClosestNumber(nums))      # 1

nums = [-4,-2,1,4,8]
print(findClosestNumber(nums))      # 1

nums = [-100000,-100000]
print(findClosestNumber(nums))      # -100000