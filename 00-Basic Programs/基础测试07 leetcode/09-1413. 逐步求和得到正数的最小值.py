
'''
url: https://leetcode.cn/problems/minimum-value-to-get-positive-step-by-step-sum/description/
'''
from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        presum = nums[0]
        minpre = presum
        for i in range(1,len(nums)):
            presum += nums[i]
            minpre = min(minpre,presum)
        if minpre >= 1:
            return 1
        else:
            return 1 - minpre
