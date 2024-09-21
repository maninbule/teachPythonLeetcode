'''
https://leetcode.cn/problems/subsets/
'''
import copy
from typing import List


class Solution:
    def dfs(self,i:int,choose:list[int],nums:list[int]):
        if i == len(nums):
            self.res.append(copy.copy(choose))
            return
        # 对于第i个nums[i]：选与不选
        # 选
        choose.append(nums[i])
        self.dfs(i + 1,choose,nums)
        choose.pop()
        # 不选
        self.dfs(i + 1,choose,nums)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        choose = []
        self.dfs(0,choose,nums)
        return self.res

# 加一个限制，选择的子集不能超过x
class Solution:
    def dfs(self,i:int,choose:list[int],nums:list[int],x):
        if sum(choose) > x:
            return
        if i == len(nums):
            self.res.append(copy.copy(choose))
            return
        # 对于第i个nums[i]：选与不选
        # 选
        choose.append(nums[i])
        self.dfs(i + 1,choose,nums,x)
        choose.pop()
        # 不选
        self.dfs(i + 1,choose,nums,x)
    def subsets(self, nums: List[int],x) -> List[List[int]]:
        self.res = []
        choose = []
        self.dfs(0,choose,nums,x)
        return self.res