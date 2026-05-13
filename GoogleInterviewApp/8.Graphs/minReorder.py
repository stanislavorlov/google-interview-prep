# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/

from collections import defaultdict, deque
from typing import List


class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for u, v in connections:
            adj_list[u].add((v, True))
            adj_list[v].add((u, False))

        queue = deque([0])
        visited = {0}

        num_changes = 0
        while queue:
            node = queue.popleft()

            for neighbor, is_connected in adj_list[node]:
                if neighbor not in visited:
                    num_changes += is_connected
                    queue.append(neighbor)
                    visited.add(neighbor)

        return num_changes