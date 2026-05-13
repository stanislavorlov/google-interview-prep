# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # dfs binary tree and set parent
        # bfs virtual graph until k is reached

        parent = {root: None}

        def dfs(node):
            if not node:
                return
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)

        dfs(root)

        queue = deque([target])
        seen = {target}
        distance = 0

        while queue and distance < k:
            current_length = len(queue)

            for _ in range(current_length):
                node = queue.popleft()

                children = [node.left, node.right, parent[node]]
                for child in children:
                    if child and child not in seen:
                        queue.append(child)
                        seen.add(child)

                distance += 1

        return [node.val for node in queue]