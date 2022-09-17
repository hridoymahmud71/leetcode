
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# write driver code yourself

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        stack = []
        current  = ListNode() #empty node
        newHead = current

        while head != None:
            stack.append(head.val)
            head = head.next
            
        for i in range(len(stack)):
            if i  != (len(stack) - n):
                current.next = ListNode(stack[i]) 
                current = current.next

        return newHead.next
