# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

# You are given a doubly linked list,
# which contains nodes that have a next pointer, 
# a previous pointer, and an additional child pointer.

# flatten the list so that all the nodes appear in a single-level, doubly linked list.

from typing import Optional

class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        pseudoHead.next.prev = None

        return pseudoHead.next

    def flatten_dfs(self, prev, curr) -> Optional[Node]:
        if not curr:
            return prev
        
        curr.prev = prev
        prev.next = curr

        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None

        return self.flatten_dfs(tail, tempNext)
    
class Solution2:
    def flatten(self, head):
        if not head:
            return None
        
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr
        pseudoHead.next.prev = None

        return pseudoHead.next