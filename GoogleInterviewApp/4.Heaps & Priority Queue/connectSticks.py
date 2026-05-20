# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        total_cost = 0
        while len(sticks) > 1:
            new_stick = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, new_stick)
            total_cost += new_stick

        return total_cost