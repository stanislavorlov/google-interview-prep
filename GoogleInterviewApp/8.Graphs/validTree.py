# https://leetcode.com/problems/graph-valid-tree/description/
from collections import defaultdict, deque
from typing import List

class Solution:
    # DFS with constant space
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

    # DFS with additional space
    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        parent = {0: None}
        visited = set()

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in visited:
                    return False

                parent[neighbor] = node
                result = dfs(neighbor)
                if not result:
                    return False

            return True

        return dfs(0) and len(visited) == n

    def validTreeBfs(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        q = deque()
        q.append((-1, 0))

        adj_list = defaultdict(list)
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)

        while q:
            parent, node = q.popleft()

            if node in seen:
                return False

            seen.add(node)

            for child in adj_list[node]:
                if parent == child:
                    continue

                q.append((node, child))

        return len(seen) == n