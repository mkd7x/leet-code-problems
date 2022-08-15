from linkedList import ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum = 0

        if l1.val == 0 and l1.next == None:
            return l2
        elif l2.val == 0 and l2.next == None:
            return l1

        depth = 0
        while (l1 != None or l2 != None):
            if l1 != None:
                sum += l1.val * (10 ** depth)
                l1 = l1.next
            
            if l2 != None:
                sum += l2.val * (10 ** depth)
                l2 = l2.next

            depth += 1
        
        headNode = ListNode(sum % 10)
        currentNode = headNode

        sum = sum // 10

        while (sum != 0):
            newNode = ListNode(sum % 10)
            currentNode.next = newNode
            currentNode = newNode

            sum = sum // 10
        
        return headNode