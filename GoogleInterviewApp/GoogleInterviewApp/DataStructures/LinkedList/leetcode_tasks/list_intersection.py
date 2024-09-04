from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# HashTable
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

# 2 pointers
class Solution2Pointers:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next

        return pointerA

# Stack
class SolutionStack:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA, stackB = [], []
        while headA:
            stackA.append(headA)
            headA = headA.next
            
        while headB:
            stackB.append(headB)
            headB = headB.next
            
        intersectionNode = None
        nodeA = stackA.pop()
        nodeB = stackB.pop()
        while nodeA == nodeB:
            intersectionNode = nodeA
            nodeA = stackA.pop()
            nodeB = stackB.pop()
            
        return intersectionNode

# length difference
class SolutionLengthDifference:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA, lengthB = 0, 0
        pointA, pointB = headA, headB
        
        # 1st length
        while pointA:
            lengthA += 1
            pointA = pointA.next

        # 2nd length
        while pointB:
            lengthB += 1
            pointB = pointB.next

        # length difference
        if lengthA > lengthB:
            d = lengthA - lengthB
            pointA = headA
            pointB = headB
        else:
            d = lengthB - lengthA
            pointA = headB
            pointB = headA

        # make d steps in longer list
        for i in range(d):
            pointA = pointA.next

        # while pointA and pointB:
        #     if pointA == pointB:
        #         return pointA
        #     pointA = pointA.next
        #     pointB = pointB.next
            
        # return None

        intersectionNode = None
        # step in both lists until match node
        while pointA != pointB and pointA and pointB:
           intersectionNode = pointA
           pointA = pointA.next
           pointB = pointB.next
           
        return intersectionNode.next if intersectionNode else None

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

s1 = SolutionLengthDifference()
node = s1.getIntersectionNode(list1, list2)
print(node.val)

s2 = Solution()
node = s2.getIntersectionNode(list1, list2)
print(node.val)

s3 = Solution2Pointers()
node = s3.getIntersectionNode(list1, list2)
print(node.val)

s4 = SolutionStack()
node = s4.getIntersectionNode(list1, list2)
print(node.val)