from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head
        even = head.next
        evenHead = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
     
     def print(self, head: Optional[ListNode]):
        while head != None:
            print(head.val)
            head = head.next
        
solution = Solution()
list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
solution.oddEvenList(list)
solution.print(list)