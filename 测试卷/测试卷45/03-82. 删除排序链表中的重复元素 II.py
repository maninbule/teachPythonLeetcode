'''
https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None
        tail = None
        cur = head
        last = None
        while cur is not None:
            nxt = cur.next
            if last and last.val == cur.val:
                pass
            elif cur.next and cur.next.val == cur.val:
                pass
            else:
                if newhead is None:
                    newhead = cur
                    tail = cur
                    tail.next = None
                else:
                    tail.next = cur
                    tail = tail.next
                    tail.next = None
            last = cur
            cur = nxt
        return newhead

'''
https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
'''
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        tail = newhead
        cur = head
        last = None
        while cur is not None:
            nxt = cur.next
            if last and last.val == cur.val:
                pass
            elif cur.next and cur.next.val == cur.val:
                pass
            else:
                tail.next = cur
                tail = tail.next
                tail.next = None
            last = cur
            cur = nxt
        return newhead.next