'''
https://leetcode.cn/problems/subsets/
'''
import copy
from typing import List


class Solution:
    def dfs(self,i:int,choose:list[int],nums:list[int],res:list[list]):
        if i >= len(nums):
            res.append(copy.copy(choose))
            return
        # 选择nums[i]
        choose.append(nums[i])
        self.dfs(i + 1,choose,nums,res)
        choose.pop()
        # 不选
        self.dfs(i + 1,choose,nums,res)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        choose = []
        res = []
        self.dfs(0,choose,nums,res)
        return res