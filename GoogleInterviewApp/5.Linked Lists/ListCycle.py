from typing import Optional

from DataStructures.LinkedList.LeetcodeList import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
    
    def hasCycleSet(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head
        while cur != None:
            if cur in visited:
                return True
            
            visited.add(cur)
            cur = cur.next

        return False
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        cur = head
        while cur != None:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next

        return None