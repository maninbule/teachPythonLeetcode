'''
https://leetcode.cn/problems/add-two-numbers/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        cur1,cur2 = l1,l2
        add = 0
        while cur1 or cur2:
            val1,val2 = 0,0
            if cur1:
                val1 = cur1.val
            if cur2:
                val2 = cur2.val
            curSum = add + val1 + val2
            add = curSum//10
            curSum = curSum % 10
            tail.next = ListNode(curSum)
            tail = tail.next
            tail.next = None
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        if add > 0:
            tail.next = ListNode(add)
            tail = tail.next
            tail.next = None
        return dummy.next