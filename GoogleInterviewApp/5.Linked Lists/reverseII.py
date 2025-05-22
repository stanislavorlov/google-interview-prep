# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional


# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Input: head = [5], left = 1, right = 1
# Output: [5]

# 1 <= left <= right <= n

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left-1, right-1

        tail, con = cur, prev
        while right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur

        return head


    def print_list(self, head: Optional[ListNode]):
        pointer = head
        while pointer:
            print(pointer.val)
            pointer = pointer.next

sol = Solution()
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list = sol.reverseBetween(list, 2, 4)
sol.print_list(list)        # [1,4,3,2,5]