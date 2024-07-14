'''
https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
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
        for i in range(0,len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        return res
