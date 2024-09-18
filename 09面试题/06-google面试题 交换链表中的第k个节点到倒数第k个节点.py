# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curNode = head
        while curNode is not None:
            n += 1
            curNode = curNode.next
        if k > n//2:
            k = n - k + 1
        firstk,lastK = None,None
        firstknext,lastKnext = None,None
        curNode = head
        for i in range(1,n + 1):
            if i == k:
                firstk = curNode
                firstknext = curNode.next
            if i == n - k + 1:
                lastK = curNode
                lastKnext = curNode.next
            curNode = curNode.next
        if firstk == lastK:
            return head
        dummy = ListNode()
        tail = dummy
        curNode = head
        for i in range(1,n + 1):
            if i == k:
                tail.next = lastK
                curNode = firstknext
            elif i == n - k + 1:
                tail.next = firstk
                curNode = lastKnext
            else:
                tail.next = curNode
                if curNode:
                    curNode = curNode.next
            tail = tail.next
        tail.next = None
        return dummy.next
# dummy->64->46->66->35->80