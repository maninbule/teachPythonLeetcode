'''
https://leetcode.cn/problems/reverse-linked-list/
'''
# 头插法
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curNode = head
        while curNode:
            nextNode = curNode.next
            curNode.next = dummy.next
            dummy.next = curNode
            curNode = nextNode
        return dummy.next
