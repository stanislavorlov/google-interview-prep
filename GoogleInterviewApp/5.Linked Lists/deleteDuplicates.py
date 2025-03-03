# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4597/
from typing import Optional


# Given the head of a sorted linked list, delete all duplicates

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

    def print(self, head: Optional[ListNode]):
        while head:
            print(head.val)
            head = head.next

solution = Solution()
head = ListNode(1, ListNode(1, ListNode(2)))
solution.deleteDuplicates(head)
print('first')
solution.print(head)

head = ListNode(1,ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
solution.deleteDuplicates(head)
print('second')
solution.print(head)

head = ListNode(1, ListNode(1, ListNode(1)))
solution.deleteDuplicates(head)
print('third')
solution.print(head)