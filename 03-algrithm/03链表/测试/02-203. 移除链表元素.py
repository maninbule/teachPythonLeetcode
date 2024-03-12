'''
技巧1：尾插法
技巧2：辅助头节点：需要返回一个新链表的时候，我们一般会设置一个额外的辅助头节点，方便我们插入新节点。

url: https://leetcode.cn/problems/remove-linked-list-elements/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pass