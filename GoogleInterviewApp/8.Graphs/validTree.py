# https://leetcode.com/problems/graph-valid-tree/description/
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj_list = [[] for _ in range(n)]
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = set()

        def dfs(node, parent):
            if node in seen:
                return
            seen.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                result = dfs(neighbor, node)
                if not result:
                    return False

            return True

        return dfs(0, -1) and len(seen) == n