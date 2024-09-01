'''
https://leetcode.cn/problems/find-if-path-exists-in-graph/description/?envType=problem-list-v2&envId=union-find
'''
from typing import List

class Solution:
    def find(self,x:int)->int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]
        else:
            return x
    def union(self,x:int,y:int):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.fa[fy] = fx
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.fa = [0] * n
        for i in range(n):
            self.fa[i] = i
        for x,y in edges:
            self.union(x,y)
        if self.find(source) == self.find(destination):
            return True
        else:
            return False