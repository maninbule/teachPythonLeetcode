'''
https://leetcode.cn/problems/remove-duplicate-node-lcci/description/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        st = set()
        dummy = ListNode(0)
        tail = dummy
        curNode = head
        while curNode:
            nextNode = curNode.next
            if curNode.val not in st:
                st.add(curNode.val)
                tail.next = curNode
                tail = tail.next
                tail.next = None
            curNode = nextNode
        return dummy.next