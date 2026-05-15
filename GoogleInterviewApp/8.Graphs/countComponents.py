# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

# edges = [[0,1],[1,2],[3,4]]
#
# matrix = {
#     0: [1],
#     1: [0,2],
#     2: [1],
#     3: [4],
#     4: [3]
# }
#
# edges2 = [[0,1],[1,2],[2,3],[3,4]]
#
# matrix2 = {
#     0: [1],
#     1: [0,2],
#     2: [1,3],
#     3: [2,4],
#     4: [3]
# }
from collections import defaultdict, deque
from typing import List

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.count -= 1

        return True

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            nonlocal visited, answer

            if not node in visited:
                answer += 1

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        answer = 0

        for i in range(n):
            dfs(i)

        return answer

    def countComponentsBfs(self, n: int, edges: List[List[int]]) -> int:
        # 1. Build the adjacency list for an undirected graph
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        components = 0

        # 2. Iterate through every node
        for i in range(n):
            # If the node hasn't been visited, it's a new component
            if i not in visited:
                components += 1

                # 3. Launch BFS to explore the entire component
                queue = deque([i])
                visited.add(i)

                while queue:
                    current = queue.popleft()

                    for neighbor in adj[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

        return components

    def countComponentsDSU(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        return uf.count

solution = Solution()
print(solution.countComponentsDSU(5, [[0,1],[1,2],[3,4]]))      # 2

print(solution.countComponentsBfs(5, [[0,1],[1,2],[2,3],[3,4]]))   # 1