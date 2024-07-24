'''
https://leetcode.cn/problems/increasing-triplet-subsequence/description/
'''

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)
        pre_min = [0] * n
        suf_max = [0] * n
        pre_min[0] = nums[0]
        for i in range(1,n):
            pre_min[i] = min(pre_min[i-1],nums[i])
        suf_max[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suf_max[i] = max(suf_max[i+1],nums[i])
        for i in range(1,n-1):
            if pre_min[i-1] < nums[i] < suf_max[i+1]:
                return True
        return False