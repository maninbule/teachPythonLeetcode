'''
https://leetcode.cn/problems/linked-list-cycle/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has_visited = set()
        cur = head
        while cur is not None:
            if cur in has_visited:
                return True
            has_visited.add(cur)
            cur = cur.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow is not None and fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return False



