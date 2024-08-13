'''
https://leetcode.cn/problems/combination-sum/description/
'''
from typing import List
import copy

class Solution:
    def dfs(self,i:int,choose:list[int],sum:int,candidates:list[int],target:int) -> None:
        if sum == target:
            self.ans.append(copy.copy(choose))
            return
        if sum > target or i == len(candidates):
            return
        # 选
        choose.append(candidates[i])
        self.dfs(i,choose,sum + candidates[i],candidates,target)
        choose.pop()
        # 不选
        self.dfs(i + 1,choose,sum,candidates,target)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        choose = []
        self.dfs(0,choose,0,candidates,target)
        return self.ans


