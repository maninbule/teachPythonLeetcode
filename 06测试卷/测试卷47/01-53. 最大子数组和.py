'''
https://leetcode.cn/problems/maximum-subarray/description/
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1,n):
            dp[i] = max(nums[i],dp[i-1] + nums[i])
            ans = max(ans,dp[i])
        return ans

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        nums = [0] + nums
        pre = [0] * len(nums)
        min_pre = 0
        ans = nums[1]
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] + nums[i]
            ans = max(ans,pre[i] - min_pre)
            min_pre = min(min_pre,pre[i])
        return ans