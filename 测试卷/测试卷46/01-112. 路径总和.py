'''
https://leetcode.cn/problems/path-sum/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        ok = [False] # ok[0] = True
        def dfs(cur_node,prefixsum:int):
            if cur_node.left is None and cur_node.right is None:
                if prefixsum == targetSum:
                    ok[0] = True
                return
            if cur_node.left is not None:
                dfs(cur_node.left,prefixsum + cur_node.left.val)
            if cur_node.right is not None:
                dfs(cur_node.right,prefixsum + cur_node.right.val)
        dfs(root,root.val)
        return ok[0]

