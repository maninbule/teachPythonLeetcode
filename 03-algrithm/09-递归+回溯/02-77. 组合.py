'''
https://leetcode.cn/problems/combinations/description/
'''
import copy
from typing import List

class Solution:
    def dfs(self,i:int,choose:list[int],n:int,k:int):
        if len(choose) == k:
            self.ans.append(copy.copy(choose))
            return
        if i > n:
            return
        need = k - len(choose)
        left = n - i + 1
        if need > left:
            return
        # 选择i
        choose.append(i)
        self.dfs(i + 1,choose,n,k)
        choose.pop()
        # 不选择i
        self.dfs(i + 1,choose,n,k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.dfs(1,[],n,k)
        return self.ans
