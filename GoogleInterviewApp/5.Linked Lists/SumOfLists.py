# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        cur = result
        carry = 0

        while l1 or l2 or carry != 0:
            sum = carry
            if l1: 
                sum += l1.val

            if l2:
                sum += l2.val

            carry = sum // 10

            newNode = ListNode(sum % 10)
            cur.next = newNode
            cur = newNode

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        return result.next

solution = Solution()
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution.addTwoNumbers(l1, l2)