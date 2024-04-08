'''
https://leetcode.cn/problems/number-of-arithmetic-triplets/description/
'''
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1,n):
                    if nums[j] - nums[i] == diff == nums[k] - nums[j]:
                        ans += 1
        return ans