
'''
url: https://leetcode.cn/problems/running-sum-of-1d-array/description/
'''
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] + nums[i]
        return pre
