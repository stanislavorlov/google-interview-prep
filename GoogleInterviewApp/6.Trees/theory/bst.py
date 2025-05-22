# https://www.programiz.com/dsa/binary-search-tree
import sys
from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

def search(root: Node, number: int):
    if not root:
        return root
    elif root.data == number:
        return root
    elif number < root.data:
        return search(root.left, number)
    else:
        return search(root.right, number)

def insert(node: Optional[Node], data: int):
    if not node:
        return Node(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    return node

def min_value_node(node: Node):
    current = node

    # Find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current

def delete_node(root: Node, key: int):
    if not root:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # if only 1 child or no child
        if not root.left:
            temp = root.right
            root = None

            return temp

        elif not root.right:
            temp = root.left
            root = None

            return temp

        temp = min_value_node(root.right)

        root.data = temp.data

        # delete the inorder successor
        root.right = delete_node(root.right, temp.data)

    return root

# Inorder traversal
def inorder(root, indent: str, last: bool):
    if root:
        sys.stdout.write(indent)
        print(root.data)
        if last:
            sys.stdout.write("R----")
            indent += "     "
        else:
            sys.stdout.write("L----")
            indent += "|    "
        inorder(root.left, indent, False)
        inorder(root.right, indent, True)

tree = None
tree = insert(tree, 8)
tree = insert(tree, 3)
tree = insert(tree, 1)
tree = insert(tree, 6)
tree = insert(tree, 7)
tree = insert(tree, 10)
tree = insert(tree, 14)
tree = insert(tree, 4)

print(tree.data)

delete_node(tree, 1)
inorder(tree, " ", True)