'''
https://leetcode.cn/problems/permutations/description/
'''
import copy
from typing import List


class Solution:
    def dfs(self,cnt:int,choose:list[int]):
        if cnt == len(self.nums):
            self.ans.append(copy.copy(choose))
            return
        for x in self.nums:
            if x in self.vis and self.vis[x] == True:
                continue
            # 选择x
            self.vis[x] = True
            self.dfs(cnt + 1,choose + [x])
            # 取消选择x
            self.vis[x] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.vis = {} # vis[x] = True/False
        self.nums = nums
        self.ans = []
        self.dfs(0,[])
        return self.ans
