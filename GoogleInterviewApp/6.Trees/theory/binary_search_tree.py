from typing import Optional


class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self._val = val
        self._left: Optional[TreeNode] = left
        self._right: Optional[TreeNode] = right
        self._parent: Optional[TreeNode] = None

    @property
    def val(self):
        return self._val

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent

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
        root._right = insert(root.right, key)
    else:
        root._left = insert(root.left, key)

    return root

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
        parent._left = new_node
    else:
        parent._right = new_node

    return root

insert(tree, 5)
insert_iterative(tree, 8)

# replace sub-tree with root of sub_tree_u by sub-tree with root sub_tree_v
def transplant(tree_node, sub_tree_u, sub_tree_v):
    if sub_tree_u.parent is None:
        tree_node.root = sub_tree_v
    elif sub_tree_u == sub_tree_u.parent.left:
        sub_tree_u.parent.left = sub_tree_v
    else:
        sub_tree_u.parent.right = sub_tree_v

    if not sub_tree_v is None:
        sub_tree_v.parent = sub_tree_u.parent

def tree_delete(root, node_delete):
    if not node_delete.left:
        transplant(root, node_delete, node_delete.right)
    elif not node_delete.right:
        transplant(root, node_delete, node_delete.left)
    else:
        y = tree_minimum(node_delete.right)
        if y.parent != node_delete:
            transplant(root, y, y.right)
            y.right = node_delete.right
            y.right.parent = y
        transplant(root, node_delete, y)
        y.left =  node_delete.left
        y.left.parent = y