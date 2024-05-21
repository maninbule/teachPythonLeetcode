'''
https://leetcode.cn/problems/merge-two-sorted-lists/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = list1,list2
        dummy = ListNode()
        tail = dummy
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next
            else:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
        if cur1 is not None:
            tail.next = cur1
        if cur2 is not None:
            tail.next = cur2
        return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n1.next = n2
n2.next = n3
l1 = n1

n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n4.next = n5
n5.next = n6
l2 = n4

s = Solution()
head = s.mergeTwoLists(l1,l2)

while head is not None:
    print(head.val,end=" ")
    head = head.next