'''
https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/
'''

class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        ans = nums[0]
        nums = nums[1:]
        nums.sort()
        return ans + nums[0] + nums[1]