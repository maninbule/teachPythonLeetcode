''''''


'''
给定一个公司，公司的组织结构是一个树形结构(非二叉树)，最顶层是CEO，现在CEO要传递一个消息给所有员工

每一个员工(包括CEO)都要花费一定的阅读时间，自己阅读完后，才能传递给自己的下属

问题1： 问所有员工阅读完消息，至少需要多长时间?
问题2： 问至少50%最底层员工阅读完消息，至少需要多长时间?
问题3： 全公司50%员工阅读完消息，至少需要多长时间?
'''

class TreeNode:
    def __init__(self,time):
        self.time = time
        self.left = None
        self.right = None

def solution(root:TreeNode)->int:
    if root is None:
        return 0
    return dfs(root)

def dfs(curNode:TreeNode)->int:
    # 空节点
    if curNode is None:
        return 0
    # 叶子节点
    if curNode.left is None or curNode.right is None:
        return curNode.time
    # 非叶子节点 = 当前节点阅读的时间 + max(左子树阅读完的时间，右子树阅读完的时间)
    return curNode.time + max(dfs(curNode.left),dfs(curNode.right))

def solution2(root:TreeNode)->int:
    if root is None:
        return 0
    times = []
    dfs2(root,0,times)
    times.sort()
    # [0,1,2,3]  len = 4 (len-1)//2 = 2 [0,1,2,3,4] len = 5 (len-1)//2
    return times[(len(times) - 1)//2]
def dfs2(curNode:TreeNode,curTime:int,times:list[int]):
    curTime += curNode.time # 当前节点阅读完之后的时间
    # 叶子节点
    if curNode.left is None and curNode.right is None:
        times.append(curTime)
        return
    if curNode.left:
        dfs2(curNode.left,curTime,times)
    if curNode.right:
        dfs2(curNode.right,curTime,times)

def solution3(root:TreeNode)->int:
    if root is None:
        return 0
    times = []
    dfs3(root,0,times)
    times.sort()
    # [0,1,2,3]  len = 4 (len-1)//2 = 2 [0,1,2,3,4] len = 5 (len-1)//2
    return times[(len(times) - 1)//2]
def dfs3(curNode:TreeNode,curTime:int,times:list[int]):
    curTime += curNode.time # 当前节点阅读完之后的时间
    times.append(curTime) # 不管是不是叶子节点，都记录一下时间
    # 叶子节点
    if curNode.left is None and curNode.right is None:
        return
    if curNode.left:
        dfs3(curNode.left,curTime,times)
    if curNode.right:
        dfs3(curNode.right,curTime,times)


# 测试
times = [1,5,10,6,7,2,8]
nodes = [TreeNode(times[i]) for i in range(len(times))]
for i in range(3):
    nodes[i].left = nodes[i*2 + 1]
    nodes[i].right = nodes[i*2 + 2]

print(solution(nodes[0]))
print(solution2(nodes[0]))
print(solution3(nodes[0]))