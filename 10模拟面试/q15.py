'''
题意：
 Given a binary tree, find the lowest common ancestor
 题意没有什么好说的
可以这样来说这个题的意思：
It probably gives you two nodes. Go up these two nodes and ask which is the nearest point where they can meet.

思路：
Approach: Algorithm: Recursion
1. If the current node is null, return None.
2. If the current node is either p or q, return the current node.
3. Recursively search for LCA in the left and right subtrees.
4. If both left and right calls return non-null, the current node is the LCA; if only one side is non-null, return that side.

'''

# 代码
# First define the node class of the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root: # If the current node is empty, return None
        return None
    # If the current node is p or q, we can return directly
    if root == p or root == q:
        return root
    # Go to the left subtree to see if the p or q node can be found
    left = lowest_common_ancestor(root.left, p, q)
    # Go to the right subtree to see if the p or q node can be found
    right = lowest_common_ancestor(root.right, p, q)

    # If node p or q can be found to the left of the current node, and p or q can also be found to the right of the current node, then the current node is the answer.
    if left and right:
        return root
    # Returns left or right. One of the current left or right must be non-empty.
    return left if left else right

'''
Time complexity: O(n) because each node is only visited once
Space complexity: O(h) Because recursion is used, recursion will use a stack space by default. The maximum number of elements stored in the stack space is the height h of the binary tree.
'''
