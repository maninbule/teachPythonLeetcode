'''
url: https://leetcode.cn/problems/find-pivot-index/description/
'''
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        pre[0] = nums[0]
        suf[n-1] = nums[n-1]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1] + nums[i]
        for i in range(n):
            left,right = 0,0
            if i > 0:
                left = pre[i-1]
            if i < n-1:
                right = suf[i+1]
            if left == right:
                return i
        return -1
'''
pre[i] 
suf[i]

pre[i-1] i suf[i+1]
'''