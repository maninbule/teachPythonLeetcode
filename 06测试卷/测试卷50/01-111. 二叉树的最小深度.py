'''
https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode],a,b,c) -> int:
        if root is None:
            return 0
        def dfs(root)->int:
            if root.left is None and root.right is None:
                return 1
            if root.left and root.right:
                return 1 + min(dfs(root.left),dfs(root.right))
            elif root.left:
                return 1 + dfs(root.left)
            else:
                return 1 + dfs(root.right)
        return dfs(root)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque()
        level = 0
        if root is None:
            return 0
        q.append(root)
        level += 1
        while len(q) > 0:
            # 上一层取出来，下一层进入
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return level
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if len(q) > 0:
                level += 1
        return level