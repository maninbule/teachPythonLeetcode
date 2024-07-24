'''
https://leetcode.cn/problems/balanced-binary-tree/description/
'''
from idlelib.tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = True
    def dfs(self, curNode: TreeNode) -> int:
        if curNode is None:
            return 0
        height_left = self.dfs(curNode.left)
        height_right = self.dfs(curNode.right)
        if abs(height_left - height_right) > 1:
            self.ans = False
        return 1 + max(height_left, height_right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.dfs(root)
        return self.ans
