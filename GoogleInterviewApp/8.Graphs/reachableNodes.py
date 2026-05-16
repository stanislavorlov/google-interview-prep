# https://leetcode.com/problems/reachable-nodes-with-restrictions/description/

from collections import defaultdict, deque
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        restricted_set = set(restricted)

        matrix = defaultdict(list)
        for node1, node2 in edges:
            matrix[node1].append(node2)
            matrix[node2].append(node1)

        queue = deque([0])
        visited = {0}

        answer = 1
        while queue:
            node = queue.popleft()

            for neighbor in matrix[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if neighbor not in restricted_set:
                        queue.append(neighbor)
                        answer += 1

        return answer