'''
https://leetcode.cn/problems/permutations/description/
'''
import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.vis = [False] * len(nums)
        self.choose = []
        self.dfs(0,nums)
        return self.ans

    def dfs(self,count:int,nums:list[int]):
        if count == len(nums):
            self.ans.append(copy.copy(self.choose))
            return
        for i in range(len(nums)):
            if self.vis[i]:
                continue
            self.choose.append(nums[i])
            self.vis[i] = True
            self.dfs(count + 1,nums)
            self.vis[i] = False
            self.choose.pop()
