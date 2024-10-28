'''
题意
given a binary tree and output from top to bottom which nodes can be seen from the right side of the binary tree
The input is the root node of a binary tree, the output is an array, and the elements of the array are ints.


思路：
Algorithm used: bfs
steps:
1. We can use bfs to access the binary tree layer by layer
2. For each layer of nodes, we can record the value of its last node and put this value into the answer array
3. How to determine the current traversal layer, we can dequeue all the nodes of the previous layer, and then enqueue all the nodes of the next layer
4. Return the answer array


'''

# 代码
# Import the queue package
from collections import deque


# Define the node class of the binary tree
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def solution(root: TreeNode) -> list[int]:
    if root is None:  # Handle special cases, root is empty
        return []
    q = deque()  # Create a queue
    q.append(root)  # Put root in the queue
    res = []  # store the result
    while len(q) > 0:
        size = len(q)  # The number of nodes in the current layer
        for i in range(size):
            curNode = q.popleft()
            if i == size - 1:  # If it is the last node of the current layer
                res.append(curNode.val)
            if curNode.left:  # Put the left child of the current node into the queue
                q.append(curNode.left)
            if curNode.right:  # Put the right child of the current node into the queue
                q.append(curNode.right)
    return res  # return the result


'''
            1
        /       \
       2         3
        \         \
        5          4

layer 1 : q = [1]  result = []
layer 2 : get all nodes from layer1, node(1) is the  rightmost node,so result =[1]
            Then all the nodes of the next layer will be queued
            so q = [2,3]
layer 3: get all nodes from layer2, node(3) is the  rightmost node, so result = [1,3]
        Then all the nodes of the next layer will be queued
        so q = [5,4]
finally,  get all nodes from layer3, node(4) is the  rightmost node, so result = [1,3,4]
        There is no next layer of nodes, and the queue will not queue new elements
return [1,3,4]

Time complexity: O(n) because each node only needs to be queued once and then dequeued once
Space complexity: O(n) because a queue needs to be opened, and this queue can hold at most n elements
'''


