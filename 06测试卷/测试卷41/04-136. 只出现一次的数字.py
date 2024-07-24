'''
https://leetcode.cn/problems/single-number/description/
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for v in nums:
            ans ^= v
        return ans