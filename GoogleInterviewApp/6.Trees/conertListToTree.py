# Convert a linked list to height-balanced binary search tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/editorial/

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self, space = 0, level_space = 5):
        space += level_space
        if self.right:
            self.right.print_tree(space)
        for i in range(level_space, space):
            print(end= " ")
        print("|" + str(self.val) + "|<")

        if self.left:
            self.left.print_tree(space)
    
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        middle = self.find_middle(head)

        node = TreeNode(middle.val)

        if head == middle:
            return node
        
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(middle.next)

        return node


    def find_middle(self, head: Optional[ListNode]):
        # the pointer to disconnect the left half from the mid node
        prev = None
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # case when slow pointer equals to head
        if prev:
            prev.next = None

        return slow
    
solution = Solution()
list = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
tree = solution.sortedListToBST(list)

tree.print_tree()