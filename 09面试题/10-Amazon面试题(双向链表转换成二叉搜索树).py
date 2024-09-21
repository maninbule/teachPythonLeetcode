'''
给你一个双向链表，将这个双向链表转换成一个二叉搜索树

双向链表：2<->8<->16<->20<->24

转换成BST：
         16
       /    \
    8       20
   /  \     / \
  2   null null 24
[2,8,16,20,24]
输出就是这个BST的root节点
'''

class ListNode:
    def __init__(self,val,pre = None,next = None):
        self.val = val
        self.pre = pre
        self.next = next
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # [head,tail) [head,None)
    def getMiddleListNode(self,head:ListNode,tail:ListNode):
        length = 0
        curNode = head
        while curNode != tail:
            length += 1
            curNode = curNode.next
        curNode = head
        for i in range(length//2):
            curNode = curNode.next
        return curNode
    def buildBST(self,head:ListNode)->TreeNode:
        return self.buildBSTByDFS(head,None)
    def buildBSTByDFS(self,head:ListNode,tail:ListNode):
        # [head,tail)
        if head == tail:
            return None
        # 节点个数大于等于1
        midNode = self.getMiddleListNode(head,tail)
        leftChild = self.getMiddleListNode(head,midNode)
        rightChild = self.getMiddleListNode(midNode.next,tail)
        midNode = TreeNode(midNode.val)
        midNode.left = leftChild
        midNode.right = rightChild
        return midNode

class Test:
    def __init__(self):
        self.inorderOfBST = []
        self.orderOfList = []
    def dfs(self,root:TreeNode):
        if root == None:
            return
        if root.left:
            self.dfs(root.left)
        self.inorderOfBST.append(root.val)
        if root.right:
            self.dfs(root.right)
    def getorderOfList(self,head:ListNode):
        curNode = head
        while curNode:
            self.orderOfList.append(curNode.val)
            curNode = curNode.next
    def test(self,head:ListNode,root:TreeNode)->bool:
        self.dfs(root)
        self.getorderOfList(head)
        return self.inorderOfBST == self.orderOfList


if __name__ == '__main__':
    # 2<->8<->16<->20<->24
    val = [2,8,16,20,24]
    arr = [ListNode(val[i]) for i in range(len(val))]
    for i in range(len(val)-1):
        arr[i].next = arr[i + 1]
    head = arr[0]
    root = Solution().buildBST(head)
    print(Test().test(head,root))