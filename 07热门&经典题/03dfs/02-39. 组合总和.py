'''
https://leetcode.cn/problems/combination-sum/description/
'''
import copy
from typing import List

class Solution:
    def dfs(self,i:int,cursum:int,choose:list[int]):
        if cursum == self.target:
            self.ans.append(copy.copy(choose))
            return
        if cursum > self.target or i >= len(self.candidates):
            return
        # 不选
        self.dfs(i + 1,cursum,choose)
        # 选
        self.dfs(i,cursum + self.candidates[i],choose + [self.candidates[i]])
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.ans = []
        self.target = target
        self.dfs(0,0,[])
        return self.ans