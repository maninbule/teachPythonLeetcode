'''

技巧：链表的遍历
url: https://leetcode.cn/problems/middle-of-the-linked-list/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur is not None:
            cnt += 1
            cur = cur.next
        middle = cnt//2
        cur = head      # 0 -> middle
        for _ in range(middle):
            cur = cur.next
        return cur





