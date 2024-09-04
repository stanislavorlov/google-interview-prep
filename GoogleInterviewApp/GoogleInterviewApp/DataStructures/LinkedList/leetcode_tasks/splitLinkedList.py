# https://leetcode.com/problems/split-a-circular-linked-list/

import math
from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def splitCircularLinkedList2(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        pointer, size = list, 0

        while pointer:
            size += 1
            pointer = pointer.next
            if pointer == list:
                break
        
        import math
        firstHalfLength = math.ceil(size / 2)
        prev, pointer = None, list
        while firstHalfLength:
            prev = pointer
            pointer = pointer.next
            firstHalfLength -= 1
            
        prev.next = None

        p = pointer
        while p.next != list:
            p = p.next
        p.next = None

        return [list, pointer]

    def splitCircularLinkedList(self, list: Optional[ListNode]) -> list[Optional[ListNode]]:
        slow, fast = list, list.next
        
        while fast != list and fast.next != list:
            slow = slow.next
            fast = fast.next.next
            
        head1 = list
        head2 = slow.next
        slow.next = head1
        cur = head2
        while cur.next != list:
            cur = cur.next
        cur.next = head2
        
        return [head1, head2]

sol = Solution()
node1 = ListNode(7)
list1 = ListNode(1, ListNode(5, node1))
node1.next = list1
print("list 1")
sol.splitCircularLinkedList(list1)          # [1,5] [7]

node2 = ListNode(5)
list2 = ListNode(2, ListNode(6, ListNode(1, node2)))
node2.next = list2
print("list 2")
sol.splitCircularLinkedList(list2)          # [2,6] [1,5]