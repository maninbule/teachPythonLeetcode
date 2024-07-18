'''
https://leetcode.cn/problems/binary-tree-paths/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if root is None:
            return []
        ans = []
        def dfs(curNode,curPath):
            if not curNode.left and not curNode.right:
                ans.append(curPath)
            if curNode.left:
                dfs(curNode.left,curPath + "->" + str(curNode.left.val))
            if curNode.right:
                dfs(curNode.right,curPath + "->" + str(curNode.right.val))
        dfs(root,str(root.val))
        return ans
