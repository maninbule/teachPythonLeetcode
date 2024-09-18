'''
https://leetcode.cn/problems/is-graph-bipartite/description/
'''
from typing import List
class Solution:
    def dfs(self,x:int,color:str):
        for y in self.g[x]:
            if self.col[y] != 0:
                if self.col[y] == color:
                    self.ok = False
            else:
                if color == 'Black':
                    self.col[y] = 'White'
                else:
                    self.col[y] = 'Black'
                self.dfs(y,self.col[y])
    def isBipartite(self, graph: List[List[int]])->bool:
        n = len(graph)
        self.ok = True
        self.g = graph
        self.col = [0] * n
        for i in range(n):
            if self.col[i] == 0:
                self.dfs(i,"Black")
        return self.ok