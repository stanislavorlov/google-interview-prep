class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            nonlocal num_good_nodes

            if node and node.val >= max_val:
                num_good_nodes += 1
            if node.left:
                dfs(node.left, max(max_val, node.val))
            if node.right:
                dfs(node.right, max(max_val, node.val))

        num_good_nodes = 0
        dfs(root, root.val)

        return num_good_nodes

    def goodNodesStack(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        answer = 1
        while stack:
            node, val = stack.pop()
            if node.left:
                if node.left.val >= val:
                    answer += 1
                stack.append((node.left, max(val, node.left.val)))
            if node.right:
                if node.right.val >= val:
                    answer += 1
                stack.append((node.right, max(val, node.right.val)))
        return answer

solution = Solution()
tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))

print(solution.goodNodesStack(tree))