'''
https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        from collections import deque
        q = deque()
        res = []
        q.append(root)
        while len(q) > 0:
            size = len(q)
            cur_level = []
            for i in range(size):
                cur = q.popleft()
                cur_level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(cur_level)
        return res[::-1]