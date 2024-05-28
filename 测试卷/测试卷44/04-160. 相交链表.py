'''
https://leetcode.cn/problems/intersection-of-two-linked-lists/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def savetolistFromLinkList(self,head:ListNode)->list[ListNode]:
        ans = []
        cur = head
        while cur is not None:
            ans.append(cur)
            cur = cur.next
        return ans
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1 = self.savetolistFromLinkList(headA)
        list2 = self.savetolistFromLinkList(headB)
        pos = -1
        ans = None
        while abs(pos) <= len(list1) and abs(pos) <= len(list2):
            if list1[pos] == list2[pos]:
                ans = list1[pos]
            else:
                break
            pos -= 1
        return ans

class Solution:
    def getLastOfLinkList(self,head:ListNode)->ListNode:
        while head.next is not None:
            head = head.next
        return head
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        if self.getLastOfLinkList(headA) != self.getLastOfLinkList(headB):
            return None
        A = headA
        B = headB
        D = self.getLastOfLinkList(headA)
        while A != B:
            if A == D:
                A = headB
            else:
                A = A.next
            if B == D:
                B = headA
            else:
                B = B.next
        return A

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B:
            if A == None:
                A = headB
            else:
                A = A.next
            if B == None:
                B = headA
            else:
                B = B.next
        return A