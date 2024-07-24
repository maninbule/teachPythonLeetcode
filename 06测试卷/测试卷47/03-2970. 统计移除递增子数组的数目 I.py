'''
https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/description/
'''

class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        n = len(nums)
        m = n + 2
        nums = [-1] + nums + [100]
        left,right = [0] * m,[0] * m
        left[0] = 1
        right[m-1] = 1
        for i in range(1,m):
            if nums[i-1] < nums[i]:
                left[i] = 1
            else:
                break
        for i in range(m-2,-1,-1):
            if nums[i] < nums[i+1]:
                right[i] = 1
            else:
                break
        ans = 0
        for i in range(0,m):
            for j in range(i + 2,m):
                if left[i] == 1 and right[j] == 1 and nums[i] < nums[j]:
                    ans += 1
        return ans
