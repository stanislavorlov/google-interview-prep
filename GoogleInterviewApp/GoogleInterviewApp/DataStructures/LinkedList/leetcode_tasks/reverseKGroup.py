# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointer = head
        kTail = None
        
        new_head = None
        while pointer:
            count = 0
            
            pointer = head
            while count < k and pointer:
                pointer = pointer.next
                count += 1
                
            if count == k:
                reversedHead = self.reverseList(head, k)
                
                if not new_head:
                    new_head = reversedHead
                    
                if kTail:
                    kTail.next = reversedHead
                    
                kTail = head
                head = pointer
                
        if kTail:
            kTail.next = head
            
        return new_head if new_head else head

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    root = ListNode(0, head)
    prev, cur = root, head
    
    while cur:
        listIndex = 0
        tail = cur
        while cur and listIndex < k:
            cur = cur.next
            listIndex += 1
            
        if listIndex < k:
            prev.next = tail
        else:
            prev.next = reverse(tail, k)
            prev = tail
            
    return root.next

def reverse(head: ListNode, k):
    prev, ptr = None, head
    
    while ptr and k:
        next = ptr.next
        ptr.next = prev
        prev = ptr
        ptr = next
        k -= 1

    return prev

list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
solution = Solution()
result = reverseKGroup(list, 4)

p = result
while p:
    print(p.val)
    p = p.next