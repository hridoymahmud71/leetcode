
#https://leetcode.com/problems/reverse-linked-list/
# write driver code yourself

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        current  = ListNode() #empty node
        newHead = current

        while head != None:
            stack.append(head.val)
            head = head.next
            
        for i in range(len(stack) - 1,-1,-1):
            current.next = ListNode(stack[i]) 
            current = current.next

        return newHead.next
