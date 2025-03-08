# https://leetcode.com/problems/last-stone-weight/
import heapq
from typing import List


# You are given an array of integers stones where stones[i] is the weight of the i-th stone.
# On each turn, we choose the heaviest two stones and smash them together.

# Suppose the heaviest two stones have weights x and y with x <= y.
# If x == y, then both stones are destroyed.
# If x != y, then x is destroyed and y loses x weight.
# Return the weight of the last remaining stone, or 0 if there are no stones left.

def last_stone_weight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = abs(heapq.heappop(stones))      # log(n) is much faster than linear time
        second = abs(heapq.heappop(stones))     # log(n) is much faster than linear time
        if first != second:
            heapq.heappush(stones, -abs(first-second))

    return -stones[0] if stones else 0

stones_arr = [2,7,4,1,8,1]
print(last_stone_weight(stones_arr))