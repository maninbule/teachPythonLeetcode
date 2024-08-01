'''
https://leetcode.cn/problems/subsets/description/
'''
from typing import List
import copy

class Solution:
    def dfs(self,i:int,choose:list[int]):
        if i == len(self.nums):
            # 选完了，把选择的方案choose拷贝一下，并放到答案中
            self.ans.append(copy.copy(choose))
            return
        # 不选第i个元素
        self.dfs(i + 1,choose)
        # 选第i个元素
        self.dfs(i + 1,choose + [self.nums[i]])
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = []
        self.dfs(0,[])
        return self.ans
