'''
https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        cur = head
        while cur is not None:
            nxt = cur.next
            if nxt is None or cur.val != nxt.val:
                tail.next = cur
                tail = tail.next
            cur = nxt
        return dummy.next