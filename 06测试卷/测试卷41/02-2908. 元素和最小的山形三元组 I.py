'''
https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/description/
'''
from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min,right_min = [0] * n,[0] * n
        left_min[0] = nums[0]
        right_min[n-1] = nums[n-1]
        for i in range(1,n):
            left_min[i] = min(left_min[i-1],nums[i])
        for i in range(n-2,-1,-1):
            right_min[i] = min(right_min[i+1],nums[i])
        ans = -1
        for i in range(1,n-1):
            lmin,rmin = left_min[i-1],right_min[i+1]
            total = lmin + rmin + nums[i]
            if lmin < nums[i] and nums[i] > rmin:
                if ans == -1:
                    ans = total
                else:
                    ans = min(ans,total)
        return ans

nums = [8,6,1,5,3]
s = Solution()
print(s.minimumSum(nums))
