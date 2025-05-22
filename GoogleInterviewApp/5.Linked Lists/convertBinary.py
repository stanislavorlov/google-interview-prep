# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description

# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.

# Input: head = [1,0,1]
# Output: 5

class ListNode:

    def __init__(self, value, next = None):
        self.val = value
        self.next = next

def getDecimalValue(head: ListNode) -> int:

    sum = 0
    while head:
        sum += head.val * pow(2, pow_val)
        pow_val += 1
        head = head.next

    return sum

def getDecimalValue2(head: ListNode) -> int:
    sum = 0
    while head:
        sum = sum << 1 | head.val
        head = head.next

    return sum

list = ListNode(1, ListNode(0, ListNode(1)))                    # 5
print(getDecimalValue2(list))

list = ListNode(1, ListNode(0, ListNode(0, ListNode(0))))       # 8
print(getDecimalValue2(list))