'''
https://leetcode.cn/problems/merge-two-sorted-lists/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curNode1 = list1
        curNode2 = list2
        while curNode1 and curNode2:
            if curNode1.val < curNode2.val:
                nextNode = curNode1.next
                tail.next = curNode1
                tail = tail.next
                tail.next = None
                curNode1 = nextNode
            else:
                nextNode = curNode2.next
                tail.next = curNode2
                tail = tail.next
                tail.next = None
                curNode2 = nextNode
        if curNode1:
            tail.next = curNode1
        if curNode2:
            tail.next = curNode2
        return dummy.next
