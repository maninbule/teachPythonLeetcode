'''
https://leetcode.cn/problems/maximum-ascending-subarray-sum/description/
'''
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                cur += nums[i]
            else:
                ans = max(ans,cur)
                cur = nums[i]
        ans = max(ans,cur)
        return ans
