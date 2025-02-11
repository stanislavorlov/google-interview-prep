# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

#Input:  l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807

from typing import Optional

class ListNode:

    def __init__(self, value, next = None):
        self.val = value
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy = ListNode(0)
    res = dummy
    while l1 or l2 or carry:
        l1val = l1.val if l1 else 0
        l2val = l2.val if l2 else 0
        carry, out = divmod(l1val + l2val + carry, 10)
        dummy.next = ListNode(out)
        dummy = dummy.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return res.next

def print_list(head: Optional[ListNode]):
    point = head
    while point:
        print(point.val)
        point = point.next

# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# res = addTwoNumbers(l1, l2)

# print_list(res)

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

res = addTwoNumbers(l1, l2)

print("First sum")
print_list(res)

l1 = ListNode(3, ListNode(7))
l2 = ListNode(9, ListNode(2))
res = addTwoNumbers(l1, l2)

print("Second sum")
print_list(res)

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print("Third sum")
res = addTwoNumbers(l1, l2)
print_list(res)