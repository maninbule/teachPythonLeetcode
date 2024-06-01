'''
https://leetcode.cn/problems/binary-tree-right-side-view/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        vis = dict()
        def dfs(root, level):  # 1
            if root is None:
                return
            if level not in vis:
                ans.append(root.val)
                vis[level] = True
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        dfs(root, 1)
        return ans
