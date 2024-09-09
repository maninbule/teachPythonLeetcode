'''
https://leetcode.cn/problems/min-cost-climbing-stairs/description/
'''
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        n = len(cost)
        # 创建dp数组
        dp = [0] * (n + 1)
        # 初始值
        dp[0] = 0
        dp[1] = 0
        # 计算所有的dp[i]
        for i in range(2,n + 1):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
        # 返回答案
        return dp[n]
