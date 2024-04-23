'''
https://leetcode.cn/problems/ant-on-the-boundary/description/
'''
from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cur = 0
        ans = 0
        for v in nums:
            cur += v
            if cur == 0:
                ans += 1
        return ans