from typing import Optional
from unittest import result

class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node

# Remove Node by value from LinkedList
def remove(list: LinkedList, value):
    dummy = ListNode(0, list.head)
    pre = dummy
    cur = list.head
    while cur:
        if cur.value == value:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return dummy.next

# Remove Node By Index
def remove(list: LinkedList, index):
    dummy = ListNode(0, list.head)
    pre = dummy
    cur = list
    for _ in range(0, index):
        pre = cur
        cur = cur.next
    pre.next = cur.next
    return dummy.next

# Reverse
def reverse(head: ListNode):
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

# Palindrome
def isPalindrome(head: ListNode):
    middle = middle_second_node(head)

    pre = None
    cur = middle
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    first_half, second_half = head, pre
    while first_half and second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# Middle Node
def middle_second_node(head: ListNode):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# 1 -> 2 -> 2 -> 4
# 1 -> 2 -> 3 -> 4 -> 5
def middle_first_node(head: ListNode) -> ListNode:
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Sum of Lists
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    cur = result
    carry = 0
    while l1 and l2:
        sum = l1.value + l2.value
        cur.next = ListNode(sum % 10 + carry)
        carry = sum // 10
        cur = cur.next
        l1 = l1.next
        l2 = l2.next
    
    cur.next = l1 if l1 != None else l2
    return result.next

    # 1 -> 3 -> 7 -> 2
    # 2 -> 4 -> 8
    # 3 -> 7 -> 5 -> 

def sumList(list1: ListNode, list2: ListNode) -> ListNode:
    result = ListNode(0)
    cur = result
    carry = 0
    while list1 or list2 or carry:
        list1val = list1.value if list1 else 0
        list2val = list2.value if list2 else 0
        (sum, carry) = divmod(list1val + list2val + carry, 10)
        cur.next = ListNode(sum)
        cur = cur.next
        
    return result.next

# List Cycle
def hasCycle(head: ListNode) -> bool:
    visited = set()
    pointer = head
    while pointer:
        if pointer in visited:
            return True
        visited.add(pointer)

    return False

def detectCyclePointers(head: ListNode) -> bool:
    slow = head
    fast = head.next
    while slow != fast and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow == fast

# 1 -> 3 -> 4 -> 5 -> 6
#      ^              | 
#      | <----------- | 
#

# 2 Lists Intersection
# the same HashSet or 2 pointers for cycle
    
# Even / Odd
def oddEvenList(self, head: ListNode) -> ListNode:
    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = even.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead
    return head

# merge
def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    pre = ListNode(0)
    result = pre
    while list1 and list2:
        if list1.value < list2.value:
            pre.next = list1
            list1 = list1.next
        else:
            pre.next = list2
            list2 = list2.next
        pre = pre.next

    pre.next = list1 if list1 else list2

    return result.next

list1 = ListNode(1, ListNode(4, ListNode(8, ListNode(9))))
list2 = ListNode(2, ListNode(3, ListNode(10)))
res = merge(list1, list2)
print()