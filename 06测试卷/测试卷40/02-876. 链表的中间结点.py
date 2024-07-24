'''
https://leetcode.cn/problems/middle-of-the-linked-list/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        cur = head
        for _ in range(n//2):
            cur = cur.next
        return cur

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
head = n1

s = Solution()
middleNode = s.middleNode(head)
print(middleNode.val)