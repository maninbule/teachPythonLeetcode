'''
https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/description/
'''
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        Lmin,Rmin = [0] * n,[0] * n
        Lmin[0] = nums[0]
        for i in range(1,n):
            Lmin[i] = min(Lmin[i-1],nums[i])
        Rmin[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            Rmin[i] = min(Rmin[i + 1],nums[i])
        ans = -1
        for i in range(1,n-1):
            s = Lmin[i-1] + nums[i] + Rmin[i+1]
            if Lmin[i-1] < nums[i] > Rmin[i+1]:
                if ans == -1:
                    ans = s
                else:
                    ans = min(ans,s)
        return ans
