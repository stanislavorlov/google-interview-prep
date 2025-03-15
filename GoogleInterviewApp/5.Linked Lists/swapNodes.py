# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
from typing import Optional


# Return the head of the linked list after swapping the values of the kth node from the beginning
# and the kth node from the end (the list is 1-indexed).

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        front = end = None
        current = head
        while current:
            length += 1
            if end:
                end = end.next
            if length == k:
                front = current
                end = head
            current = current.next

        temp = front.val
        front.val = end.val
        end.val = temp

        return head

    def print(self, head: Optional[ListNode]):
        output = ''
        while head is not None:
            output += f" {head.val}"
            head = head.next
        print(output)

solution = Solution()
head_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution.swapNodes(head_node, 2)
solution.print(head_node)       # 1 -> 4 -> 3 -> 2 -> 5

head_node = ListNode(7,ListNode(9,ListNode(6,ListNode(6,ListNode(7,
       ListNode(8,ListNode(3,ListNode(0,ListNode(9,ListNode(5))))))))))

solution.swapNodes(head_node, 5)
solution.print(head_node)       # [7,9,6,6,8,7,3,0,9,5]