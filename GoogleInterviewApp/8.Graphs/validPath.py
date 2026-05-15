# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

from collections import deque, defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_matrix = defaultdict(list)
        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)

        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in adj_matrix[node]:
                if neighbor in visited:
                    continue

                queue.append(neighbor)
                visited.add(neighbor)

        return False

    def validPath2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = [source]
        seen = [False] * n
        seen[source] = True

        while stack:
            current = stack.pop()

            for neighbor in graph[current]:
                if neighbor == destination:
                    return True

                if not neighbor in seen:
                    stack.append(neighbor)

        return seen[destination]

solution = Solution()
print(solution.validPath(3, [[0,1],[1,2],[2,0]], 0, 2))

print(solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]],  0, 5))