from linkedList import ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list1Head = list1
        list2Head = list2

        newHead = None
        currentHead = None


        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1Head.val <= list2Head.val:
                currentHead = list1Head
                newHead = list1Head
                list1Head = list1Head.next
            else:
                currentHead = list2Head
                newHead = list2Head
                list2Head = list2Head.next

        while list1Head != None and list2Head != None:
            if list1Head.val <= list2Head.val:
                currentHead.next = list1Head
                list1Head = list1Head.next
                currentHead = currentHead.next
            else:
                currentHead.next = list2Head
                list2Head = list2Head.next
                currentHead = currentHead.next
        
        if list1Head != None:
            currentHead.next = list1Head
        else:
            currentHead.next = list2Head

        return newHead

