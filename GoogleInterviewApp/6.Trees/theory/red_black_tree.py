import sys
from enum import Enum

class Color(Enum):
    RED = 1
    BLACK = 2

class RedBlackNode:
    def __init__(self, val):
        self._color = Color.BLACK
        self._parent = None
        self._val = val
        self._left = None
        self._right = None

    @property
    def color(self):
        return self._color

    @property
    def is_red(self):
        return self._color == Color.RED

    @property
    def parent(self):
        return self._parent

    @property
    def val(self):
        return self._val

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def print_color(self):
        if self.color == Color.BLACK:
            return '(b)'
        return '(r)'

class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode(0)
        self.nil._color = Color.BLACK
        self.nil._left = None
        self.nil._right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RedBlackNode(val)
        new_node._parent = None
        new_node._left = self.nil
        new_node._right = self.nil
        new_node._color = Color.RED

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right

        new_node._parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent._left = new_node
        else:
            parent._right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node: RedBlackNode):
        while node.parent and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == Color.RED:
                    node.parent._color = Color.BLACK
                    y._color = Color.BLACK
                    node.parent.parent._color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent._color = Color.BLACK
                    node.parent.parent._color = Color.RED
                    self.rotate_right(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == Color.RED:
                    node.parent._color = Color.BLACK
                    y._color = Color.BLACK
                    node.parent.parent._color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent._color = Color.BLACK
                    node.parent.parent._color = Color.RED
                    self.rotate_left(node.parent.parent)

            if node == self.root:
                break

        self.root._color = Color.BLACK

    def rotate_left(self, node):
        y = node.right
        node._right = y.left
        if y.left != self.nil:
            y._left._parent = node

        y._parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node._parent._left = y
        else:
            node._parent._right = y
        y._left = node
        node._parent = y

    def rotate_right(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y._right._parent = node

        y._parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node._parent._right = y
        else:
            node._parent._left = y
        y._right = node
        node._parent = y

    def print_helper(self, root: RedBlackNode, indent: str, last: bool):
        if root is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(root.val)
            self.print_helper(root.left, indent, False)
            self.print_helper(root.right, indent, True)

tree = RedBlackTree()
nums = [33, 13, 52, 9, 21, 61, 8, 11]
nums.sort()
for num in nums:
    tree.insert(num)

tree.print_helper(tree.root, " ", True)