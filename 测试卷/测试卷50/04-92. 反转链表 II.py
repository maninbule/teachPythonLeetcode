'''
https://leetcode.cn/problems/reverse-linked-list-ii/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        head1,head2,head3 = ListNode(),ListNode(),ListNode()
        tail1,tail2,tail3 = head1,head2,head3
        cur = head
        for i in range(1,length + 1):
            nxt = cur.next
            if i < left:
                tail1.next = cur
                tail1 = tail1.next
            elif left <= i <= right:
                cur.next = head2.next
                head2.next = cur
                if i == left:
                    tail2 = cur
            else:
                tail3.next = cur
                tail3 = tail3.next
            cur = nxt
        tail1.next = head2.next
        tail2.next = head3.next
        return head1.next