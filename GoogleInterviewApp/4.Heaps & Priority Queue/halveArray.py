# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
import heapq
from typing import List


# You are given an array nums of positive integers.
# In one operation, you can choose any number from nums and reduce it to exactly half the number.
# (Note that you may choose this reduced number in future operations.)

# Return the minimum number of operations to reduce the sum of nums by at least half.

# Input: nums = [5,19,8,1]
# The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
# Pick the number 19 and reduce it to 9.5.
# Pick the number 9.5 and reduce it to 4.75.
# Pick the number 8 and reduce it to 4.

def halveArray(nums: List[int]) -> int:
    # we should choose the largest element.
    target = sum(nums) / 2
    heap = [-num for num in nums]
    heapq.heapify(heap)

    ans = 0
    while target > 0:
        ans += 1
        x = heapq.heappop(heap)
        target += x/2
        heapq.heappush(heap, x/2)

    return ans

arr = [5,19,8,1]
print(halveArray(arr))