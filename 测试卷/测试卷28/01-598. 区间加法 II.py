'''
https://leetcode.cn/problems/range-addition-ii/description/
'''
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        max_m,max_n = m,n
        for op in ops:
            x,y = op
            max_m = min(max_m,x)
            max_n = min(max_n,y)
        return max_n * max_m