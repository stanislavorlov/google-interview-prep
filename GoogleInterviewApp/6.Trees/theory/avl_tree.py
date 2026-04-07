import sys

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def insert_node(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        left_node = y.left
        y.left = z
        z.right = left_node
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    # Function to perform right rotation
    def right_rotate(self, z):
        y = z.left
        right_node = y.right
        y.right = z
        z.left = right_node
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    # Get the height of the node
    def get_height(self, root):
        if not root:
            return 0

        return root.height

    # Get balance factor of the node
    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    # Print the tree
    def print_helper(self, curr, indent: str, last: bool):
        if curr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr.key)
            self.print_helper(curr.left, indent, False)
            self.print_helper(curr.right, indent, True)

avl_tree = AVLTree()
root_node = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
nums.sort()
for num in nums:
    root_node = avl_tree.insert_node(root_node, num)
avl_tree.print_helper(root_node, " ", True)