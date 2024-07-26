'''
中国字节
https://leetcode.cn/problems/symmetric-tree/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self,curNode1:TreeNode,curNode2:TreeNode)->bool:
        if not curNode1 and not curNode2:
            return True
        if not curNode1 and curNode2:
            return False
        if curNode1 and not curNode2:
            return False
        if curNode1.val != curNode2.val:
            return False
        # 两个节点都有，值也一样
        # 就需要判断他们下面是否对称了
        return self.dfs(curNode1.left,curNode2.right) and self.dfs(curNode1.right,curNode2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root,root)