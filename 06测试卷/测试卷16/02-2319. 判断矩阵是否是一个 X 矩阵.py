'''
https://leetcode.cn/problems/check-if-matrix-is-x-matrix/description/
'''
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        total = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                total += grid[i][j]
        for i in range(n):
            x = grid[i][i]
            if x == 0:
                return False
            total -= x
        for i in range(n):
            x = grid[i][n-1-i]
            if x == 0:
                return False
            total -= x
        if n % 2 == 1:
            total += grid[n//2][n//2] # 3 (0,1,2) 3//2 = 1
        return total == 0