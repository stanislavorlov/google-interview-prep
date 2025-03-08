# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return dummy.next

    def print(self, head: Optional[ListNode]):
        while head is not None:
            print(head.val)
            head = head.next

head = ListNode(1, ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))
solution = Solution()
solution.deleteDuplicates(head)
solution.print(head)