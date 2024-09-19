'''
https://leetcode.cn/problems/binary-tree-right-side-view/description/
'''
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self,root,level):
        if len(self.ans) < level:
            self.ans.append(root.val)
        if root.right:
            self.dfs(root.right,level + 1)
        if root.left:
            self.dfs(root.left, level + 1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.ans = []
        self.dfs(root,1)
        return self.ans