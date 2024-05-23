'''
https://leetcode.cn/problems/kth-node-from-end-of-list-lcci/description/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        cur = head
        for i in range(n-k):
            cur = cur.next
        return cur