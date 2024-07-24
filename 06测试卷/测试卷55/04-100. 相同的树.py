'''
https://leetcode.cn/problems/same-tree/description/
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
        if not curNode1 and curNode2:
            return False
        if curNode1 and not curNode2:
            return False
        # 两个节点都是空
        if not curNode1 and not curNode2:
            return True
        # 两个节点都不为空，就判断值是否相同
        if curNode1.val != curNode2.val:
            return False
        # 还需要判断curNode1下面的节点结构和curNode2下面的结构是否完全一样
        ans_left = self.dfs(curNode1.left,curNode2.left)
        ans_right = self.dfs(curNode1.right,curNode2.right)
        return ans_left and ans_right
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p,q)
