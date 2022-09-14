# Definition for singly-linked list.

# https://leetcode.com/problems/rotate-list/submissions/
# write driver code yourself

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        
        curr  = ListNode()
        newHead = curr
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        
        print(nums)
        if len(nums) == 0:
            return head
        k = k % len(nums)

        def reverseArray(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverseArray(nums, 0, len(nums) - 1)    
        reverseArray(nums, 0, k - 1)
        reverseArray(nums, k, len(nums) - 1)

        for i in range(len(nums)):
            curr.next = ListNode(nums[i])
            curr = curr.next
            
        return newHead.next

        for i in range(len(nums)):
            curr.next = ListNode(nums[i])
            curr = curr.next
            
        return newHead.next