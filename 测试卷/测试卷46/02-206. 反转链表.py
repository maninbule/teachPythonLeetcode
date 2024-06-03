'''
https://leetcode.cn/problems/reverse-linked-list/description/
'''
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = nxt
        return dummy.next