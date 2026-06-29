# https://leetcode.com/problems/clone-graph/
from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        new_node = Node(node.val, [])
        self.visited[node] = new_node

        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return new_node

    def cloneGraphBfs(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}
        queue = deque([node])

        visited[node] = Node(node.val, [])

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if not neighbor in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

                visited[node].neighbors.append(visited[neighbor])

        return visited[node]