'''
https://leetcode.cn/problems/permutations-ii/description/
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.choose = []
        self.vis = [False] * len(nums)
        self.dfs(0,nums)
        return self.ans

    def dfs(self,count:int,nums:list[int]):
        if count == len(nums):
            self.ans.append(copy.copy(self.choose))
            return
        for i in range(len(nums)):
            if self.vis[i]:
                continue
            if i - 1>=0 and nums[i-1] == nums[i] and self.vis[i-1] == False:
                continue
            self.choose.append(nums[i])
            self.vis[i] = True
            self.dfs(count + 1,nums)
            self.choose.pop()
            self.vis[i] = False
