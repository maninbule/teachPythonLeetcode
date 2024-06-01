'''
https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# maxDepth(root)->计算root节点二叉树的高度

# 1 + max(root左子树的高度，root右子树的高度)
