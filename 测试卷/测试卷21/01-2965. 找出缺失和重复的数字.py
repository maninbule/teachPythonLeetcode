'''
https://leetcode.cn/problems/find-missing-and-repeated-values/description/
'''
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        from collections import defaultdict
        mp = defaultdict(int)
        n = len(grid)
        for i in range(n):
            for j in range(n):
                mp[grid[i][j]] += 1
        ans = [0,0]
        for x in range(1,n*n + 1):
            if mp[x] == 2:
                ans[0] = x
            if mp[x] == 0:
                ans[1] = x
        return ans