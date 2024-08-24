
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,x:int): # api
        if self.root is None:
            self.root = TreeNode(x)
            return
        else:
            self.insert_dfs(self.root,x)
    def search(self,x:int)->bool: # api
        return self.search_dfs(self.root,x)
    def remove(self,x:int)->bool:
        pass
    def search_dfs(self,curNode,x:int)->bool:
        if curNode is None:
            return False
        if curNode.val == x:
            return True
        if x < curNode.val:
            return self.search_dfs(curNode.left,x)
        else:
            return self.search_dfs(curNode.right,x)

    def insert_dfs(self,curNode,x:int):
        if curNode.val == x:
            return
        if x < curNode.val:
            if curNode.left is None:
                curNode.left = TreeNode(x)
            else:
                self.insert_dfs(curNode.left,x)
        else:
            if curNode.right is None:
                curNode.right = TreeNode(x)
            else:
                self.insert_dfs(curNode.right,x)

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(7)
    bst.insert(15)
    bst.insert(6)
    bst.insert(9)
    bst.insert(9)

    print(bst.search(6))
    print(bst.search(5))
    print(bst.search(10))
    print(bst.search(9))

