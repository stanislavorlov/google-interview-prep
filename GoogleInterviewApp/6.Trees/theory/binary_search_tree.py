import sys
from typing import Optional


class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
        self.parent: Optional[TreeNode] = None

tree = TreeNode(15, TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, None, TreeNode(13, TreeNode(9)))), TreeNode(18, TreeNode(17), TreeNode(20)))

def tree_search(root: TreeNode, key):
    if not root or root.val == key:
        return root

    if key < root.val:
        return tree_search(root.left, key)
    else:
        return tree_search(root.right, key)

def tree_search_iterative(root: TreeNode, key):
    while root and root.val != key:
        if key < root.val:
            root = root.left
        else:
            root = root.right

    return root

node = tree_search(tree, 13)
if node:
    print(node.val)

node_iterative = tree_search_iterative(tree, 7)
if node_iterative:
    print(node_iterative.val)

def tree_minimum(root: TreeNode):
    while root.left:
        root = root.left

    return root

def tree_maximum(root: TreeNode):
    while root.right:
        root = root.right

    return root

def insert(root: TreeNode, key):
    if root is None:
        return TreeNode(key)

    if root.val == key:
        return root

    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root

def successor(root: TreeNode):
    if root.right:
        return tree_minimum(root.right)

    parent = root.parent
    while parent and root == parent.right:
        root = parent
        parent = parent.parent

    return parent

print('successor')
print(successor(tree).val)

def insert_iterative(root: TreeNode, key):
    new_node = TreeNode(key)

    if not root:
        return new_node

    parent = None
    cur = root
    while cur is not None:
        parent = cur
        if cur.val > key:
            cur = cur.left
        elif cur.val < key:
            cur = cur.right
        else:
            return root

    if parent.val > key:
        parent.left = new_node
    else:
        parent.right = new_node

    return root

insert(tree, 5)
insert_iterative(tree, 8)

# replace subtree with root of sub_tree_u by subtree with root sub_tree_v
def transplant(tree_node, node_to_delete, replacement_node):
    if node_to_delete.parent is None:
        tree_node.root = replacement_node
    elif node_to_delete == node_to_delete.parent.left:
        node_to_delete.parent.left = replacement_node
    else:
        node_to_delete.parent.right = replacement_node

    if not replacement_node is None:
        replacement_node.parent = node_to_delete.parent


def tree_delete(root, node_delete):
    if not node_delete.left:
        transplant(root, node_delete, node_delete.right)
    elif not node_delete.right:
        transplant(root, node_delete, node_delete.left)
    else:
        successor_node = tree_minimum(node_delete.right)
        if successor_node.parent != node_delete:
            transplant(root, successor_node, successor_node.right)
            successor_node.right = node_delete.right
            successor_node.right.parent = successor_node
        transplant(root, node_delete, successor_node)
        successor_node.left =  node_delete.left
        successor_node.left.parent = successor_node

tree = TreeNode(12, TreeNode(5, TreeNode(2), TreeNode(9)), TreeNode(18, TreeNode(15, None, TreeNode(17)), TreeNode(19)))

def print_tree(tree_node: TreeNode, indent: str, last: bool):
    if tree_node:
        sys.stdout.write(indent)
        if last:
            sys.stdout.write("R----")
            indent += "     "
        else:
            sys.stdout.write("L----")
            indent += "|    "
        print(tree_node.val)
        print_tree(tree_node.left, indent, False)
        print_tree(tree_node.right, indent, True)


delete_node = tree.right.left   # 15
print(delete_node.val)

print('Binary tree')
print_tree(tree, " ", True)
tree_delete(tree, delete_node)