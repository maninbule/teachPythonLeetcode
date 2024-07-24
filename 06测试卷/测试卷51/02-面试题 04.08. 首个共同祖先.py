'''
https://leetcode.cn/problems/first-common-ancestor-lcci/description
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 可以不去记忆 这种方法
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pathq = []
        pathp = []

        def dfs(curnode: TreeNode, path: list[TreeNode]):
            if curnode == p:
                for x in path:
                    pathp.append(x)
            if curnode == q:
                for x in path:
                    pathq.append(x)
            if curnode.left:
                dfs(curnode.left, path + [curnode.left])
            if curnode.right:
                dfs(curnode.right, path + [curnode.right])

        dfs(root, [root])
        res = root
        for i in range(min(len(pathp), len(pathq))):
            if pathp[i] == pathq[i]:
                res = pathq[i]
        return res


# 理解这个，面试的时候，用这个写法 ， (递归 + 回溯)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = []
        def dfs(curnode:TreeNode)->int:
            sum = 0
            if curnode == p or curnode == q:
                sum += 1
            if curnode.left:
                sum += dfs(curnode.left)
            if curnode.right:
                sum += dfs(curnode.right)
            if sum == 2 and res == []:
                res.append(curnode)
            return sum
        dfs(root)
        return res[0]