'''
'''

'''
给你一个二叉树，树的边权大于0

你可以删除你想删除的边，需要保证所有的叶子节点都与root节点没有连边。
问删除的边的权值总和最小是多少 ?

'''

class TreeNode:
    def __init__(self,treenodeid:int):
        self.treenodeid = treenodeid
        self.left = None
        self.right = None
        self.leftWeight = 0
        self.rightWeight = 0

# 边权只等于等于0
def dfs(root:TreeNode,WeightFromFatherNode:int)->int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return WeightFromFatherNode
    weightOfLeftSubTree = dfs(root.left,root.leftWeight)
    weightOfRightSubTree = dfs(root.right, root.rightWeight)
    return min(WeightFromFatherNode,weightOfLeftSubTree + weightOfRightSubTree)

# 边权可以小于0，等于0，大于0
def dfs(root:TreeNode,WeightFromFatherNode:int)->int:
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return WeightFromFatherNode
    weightOfLeftSubTree = dfs(root.left,root.leftWeight)
    weightOfRightSubTree = dfs(root.right, root.rightWeight)
    # 断开WeightFromFatherNode
    cost1 =  WeightFromFatherNode + min(0,weightOfLeftSubTree) + min(0,weightOfRightSubTree)
    # 不断开WeightFromFatherNode
    cost2 = weightOfLeftSubTree + weightOfRightSubTree
    return min(cost1,cost2)

# if __name__ == '__main__':
#     node = [TreeNode(i) for i in range(8)]
#     node[1].left = node[2]
#     node[1].right = node[3]
#     node[2].left = node[4]
#     node[2].right = node[5]
#     node[3].left = node[6]
#     node[3].right = node[7]
#     node[1].leftWeight = 2
#     node[1].rightWeight = 5
#     node[2].leftWeight = 1
#     node[2].rightWeight = 1
#     node[3].leftWeight = 1
#     node[3].rightWeight = 3
#     inf = 2**30
#     res = dfs(node[1],inf)
#     print(res)

if __name__ == '__main__':
    node = [TreeNode(i) for i in range(8)]
    node[1].left = node[2]
    node[1].right = node[3]
    node[2].left = node[4]
    node[2].right = node[5]
    node[3].left = node[6]
    node[3].right = node[7]
    node[1].leftWeight = -4
    node[1].rightWeight = 5
    node[2].leftWeight = -2
    node[2].rightWeight = 5
    node[3].leftWeight = 1
    node[3].rightWeight = 3
    inf = 2**30
    res = dfs(node[1],inf)
    print(res)

# 刚才边的权值都是大于等于0的，现在要修改成边权可以是负数，0，正数
# 现在要让总和最小


