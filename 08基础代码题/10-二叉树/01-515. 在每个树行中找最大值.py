'''
https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/
'''
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q)
            level_max = None
            for i in range(size):
                curNode = q.popleft()
                if level_max is None:
                    level_max = curNode.val
                else:
                    level_max = max(level_max,curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            ans.append(level_max)
        return ans