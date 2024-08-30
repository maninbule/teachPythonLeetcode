'''
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        分析：
        状态： dp[i][0] = profit 经历过前i天了并且手上没有股票，能获得的最大利润是profit
              dp[i][1] = profit 经历过前i天了并且手上有一支股票，能获得的最大利润是profit
        答案： max(dp[n-1][0],dp[n-1][1])
        转移： dp[0][0] = 0 第0天没有股票，收益是0
               dp[0][1] = -prices[0] 手上有一只股票，收益-prices[0]
               dp[i][0] = max(dp[i-1][0] + 0,dp[i-1][1] + prices[i])
                            (1)一种是前1天没有股票，第i天也不买, 收益为0
                            (2)前1天有一只股票，第i天卖出，获得收益prices[i]
                dp[i][1] = max(dp[i-1][1] + 0,dp[i-1][0] - prices[i])
                            (1)前1天有一只股票，但是第i天不卖出，收益为0
                            (2)前1天没有股票，第i天去购买一支股票，收益为-prices[i]
        '''
        if prices is None or len(prices) == 0:
            return 0
        n = len(prices)
        dp = [[0,0] for i in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] - prices[i])
        return max(dp[n-1][0],dp[n-1][1])