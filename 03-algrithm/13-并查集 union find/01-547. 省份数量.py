'''
https://leetcode.cn/problems/number-of-provinces/description/?envType=problem-list-v2&envId=union-find
'''
from typing import List


class Solution:
    # 第2步：写find函数，find函数是递归的
    def find(self,x:int)->int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        else:
            return x
    # 第3步：写union函数，表示要让x和y所在的集合进行合并，也就是x和y要在同一个集合
    def union(self,x:int,y:int):
        fx = self.find(x) # x所在集合的祖先
        fy = self.find(y) # y所在集合的祖先
        if fx != fy:   # 如果两个祖先不是同一个，就让其中一个祖先认另一个是自己的祖先
            self.fa[fx] = fy
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # 第1步：初始化，让fa[i] = i ,各自为一个集合
        self.fa = [0] * n
        for i in range(n):
            self.fa[i] = i
        for i in range(n):
            for j in range(i + 1,n): # i < j
                if isConnected[i][j] == 1:
                    self.union(i,j)
        res = 0
        for i in range(n):
            if self.find(i) == i:
                res += 1
        return res

