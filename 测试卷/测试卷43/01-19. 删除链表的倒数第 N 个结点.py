'''
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        cur = head
        while cur is not None:
            total += 1
            cur = cur.next
        id = total - n + 1
        cur = head
        dummy = ListNode()
        tail = dummy
        cnt = 1
        while cur is not None:
            nxt = cur.next
            if id == cnt:
                del cur
            else:
                tail.next = cur
                tail = tail.next
                tail.next = None
            cur = nxt
            cnt += 1
        return dummy.next
