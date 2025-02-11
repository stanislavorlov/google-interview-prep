#Input: head = [1,2,6,3,4,5,6], val = 6
#Output: [1,2,3,4,5]

#Input: head = [7,7,7,7], val = 7
#Output: []

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        cur = head
        prev = dummyHead
        while cur != None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        
        return dummyHead.next
    
    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
    
    def print(self, head: Optional[ListNode]):
        while head != None:
            print(head.val)
            head = head.next
    
solution = Solution()
list = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
list = solution.removeElements2(list, 1)
solution.print(list)