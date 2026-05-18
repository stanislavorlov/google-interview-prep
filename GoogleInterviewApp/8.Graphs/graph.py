# G = (V,E)
# vertex edges
# V = {0,1,2,3}
# E = { (0,1), (0,2), (1,3), (2,3) }

from collections import defaultdict, deque
from typing import List

# First format - array of edges
def build_graph(edges: List[List[int]]) -> List[List[int]]:
    graph = defaultdict(list)
    for x,y in edges:
        graph[x].append(y)

    return graph

input_edges = [[0, 1], [1, 2], [2, 0], [2, 3]]

# Second format - adjacency list
graph = build_graph(input_edges)      # the list of outgoing edges from the i-th node

# Third format - adjacency matrix
# 2D matrix graph, if graph[i][j] == 1 that means there is an edge from i to j

# Last format - matrix
# Each element in matrix represents a node and its neighbors are adjacent nodes

# We might need to convert the input into Hash map first

def dfs_recursive(g, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in g[node]:
            dfs_recursive(g, neighbor, visited)

def dfs_iterative(g, node):
    visited = set()

    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(reversed(g[node]))

def bfs(g, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in g[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# [[0, 1], [1, 2], [2, 0], [2, 3]]
print("BFS iterative")
bfs(graph, 0)
print("DFS recursive")
dfs_recursive(graph, 0)
print("DFS iterative")
dfs_iterative(graph, 0)

# DFS - stack, pop, extend reversed neighbors
# BFS - queue, popleft, append neighbors