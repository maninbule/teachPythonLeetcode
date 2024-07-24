'''
https://leetcode.cn/problems/left-and-right-sum-differences/description/
'''
from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            leftsum = 0
            rightsum = 0
            for j in range(0,i): # i = 0
                leftsum += nums[j]
            for j in range(i + 1,n):
                rightsum += nums[j]
            ans[i] = abs(leftsum - rightsum)
        return ans
