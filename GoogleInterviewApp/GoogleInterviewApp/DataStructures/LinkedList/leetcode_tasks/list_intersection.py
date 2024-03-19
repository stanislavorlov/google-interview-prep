from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_A = set()
        while headA != None:
            nodes_A.add(headA)
            headA = headA.next

        while headB != None:
            if headB in nodes_A:
                return headB
            
            headB = headB.next
        
        return None
    
class Solution2Pointers:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next

        return pointerA
    

node3 = ListNode('c3')
node2 = ListNode('c2')
node2.next = node3
node1 = ListNode('c1')
node1.next = node2

list1 = ListNode('a1')
nodea2 = ListNode('a2')
list1.next = nodea2
nodea2.next = node1

list2 = ListNode('b1')
nodeb2 = ListNode('b2')
list2.next = nodeb2
nodeb3 = ListNode('b3')
nodeb2.next = nodeb3
nodeb3.next = node1

solution = Solution2Pointers()
node = solution.getIntersectionNode(list1, list2)
print(node.val)