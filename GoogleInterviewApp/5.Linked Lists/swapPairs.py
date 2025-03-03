# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes 
# (i.e., only nodes themselves may be changed.)

# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

from typing import Optional

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# https://leetcode.com/problems/swap-nodes-in-pairs/

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = head
        prev = dummy

        while first and first.next:
            second = first.next
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
            first = first.next

        return dummy.next

    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = head.next
        prev = None
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head

            next_ = head.next.next
            head.next.next = head

            head.next = next_
            head = next_

        return dummy


    def print_list(self, head: Optional[ListNode]):
        pointer = head
        while pointer:
            print(pointer.value)
            pointer = pointer.next

solution = Solution()
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list = solution.swap_pairs(list)
solution.print_list(list)