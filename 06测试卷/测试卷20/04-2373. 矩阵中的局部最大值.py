'''
https://leetcode.cn/problems/largest-local-values-in-a-matrix/description/
'''
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for i in range(n-2)]
        for i in range(n):
            for j in range(n):
                if not (i + 2 < n and j + 2 < n):
                    continue
                # i,j 就是3x3矩阵的左上角
                mx = grid[i][j]
                for x in range(i,i + 3): # [i,i+1,i+2]
                    for y in range(j,j + 3): # [j,j + 1,j + 2]
                        mx = max(mx,grid[x][y])
                ans[i][j] = mx
        return ans