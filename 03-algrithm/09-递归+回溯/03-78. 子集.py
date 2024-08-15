'''
https://leetcode.cn/problems/subsets/description/
'''
from typing import List
import copy

class Solution:
    def dfs(self,i:int,choose:list[int],nums:list[int]):
        if i == len(nums):
            self.ans.append(copy.copy(choose))
            return
        # choose nums[i]
        choose.append(nums[i])
        self.dfs(i + 1,choose,nums)
        choose.pop()
        # not choose
        self.dfs(i + 1,choose,nums)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        choose = []
        self.dfs(0,choose,nums)
        return self.ans