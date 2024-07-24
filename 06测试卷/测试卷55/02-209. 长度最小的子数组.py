'''
https://leetcode.cn/problems/minimum-size-subarray-sum/description/
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            sumofSubarr = 0
            for j in range(i,n):
                sumofSubarr += nums[j]
                if sumofSubarr >= target:
                    length = j - i + 1
                    if res == 0:
                        res = length
                    else:
                        res = min(res,length)
                    break
        return res