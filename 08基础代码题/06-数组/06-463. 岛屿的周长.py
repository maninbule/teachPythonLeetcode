'''
https://leetcode.cn/problems/island-perimeter/description/
'''
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        n,m = len(grid),len(grid[0])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt = 0
                    for dx,dy in dir:
                        nx = i + dx
                        ny = j + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >=m:
                            cnt += 1
                        elif grid[nx][ny] == 0:
                            cnt += 1
                    ans += cnt
        return ans