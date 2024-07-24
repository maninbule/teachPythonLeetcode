'''
https://leetcode.cn/problems/remove-linked-list-elements/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curNode = head
        while curNode:
            nextNode = curNode.next
            if curNode.val != val:
                tail.next = curNode
                tail = tail.next
                tail.next = None
            curNode = nextNode
        return dummy.next


