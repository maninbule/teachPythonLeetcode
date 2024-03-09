
'''
URL:https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/description/
'''
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # st = set(nums)
        # n = len(nums)
        # ans = []
        # for i in range(1,n + 1):
        #     if i not in st:
        #         ans.append(i)
        # return ans
        # 第二种做法
        n = len(nums)
        vis = [False] * (1 + n)
        for v in nums:
            vis[v] = True
        ans = []
        for i in range(1,n + 1):
            if not vis[i]:
                ans.append(i)
        return ans
