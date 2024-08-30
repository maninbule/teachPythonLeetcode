'''
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) == 0:
            return 0
        res = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            res = max(res,prices[i] - min_price)
            min_price = min(min_price,prices[i])
        return res
