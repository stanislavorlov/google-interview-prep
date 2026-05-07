# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        queue = deque([root])
        while queue:
            num_nodes = len(queue)
            row = []
            for _ in range(num_nodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                row.append(node.val)

            if len(answer) % 2 == 1:
                row.reverse()
                answer.append(row)
            else:
                answer.append(row)

        return answer

    def zigzagLevelOrderBfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer

        level_list = deque()
        node_queue = deque([root, None])    # delimeter for level
        is_order_left = True

        while len(node_queue):
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                answer.append(list(level_list))

                if len(node_queue) > 0:
                    node_queue.append(None)

                level_list = deque()
                is_order_left = not is_order_left

        return answer

solution = Solution()
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.zigzagLevelOrder(tree))  # [[3],[20,9],[15,7]]