#https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# write driver code yourself

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        container = []
        current  = ListNode() #empty node
        newHead = current

        while head != None:
            container.append(head)
            head = head.next            
            
        if len(container) % 2 != 0 :
            return container[(len(container)//2)]
        else :
            return container[(len(container) + 1) // 2]