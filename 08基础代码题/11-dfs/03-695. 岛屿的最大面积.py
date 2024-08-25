'''
https://leetcode.cn/problems/max-area-of-island/description/
'''
from typing import List
class Solution:
    def dfs(self,i:int,j:int,vis:list[list[bool]],grid:list[list[int]])->int:
        cnt = 1
        for dx,dy in [[-1,0],[1,0],[0,1],[0,-1]]:
            nx,ny = i + dx,j + dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                continue
            if vis[nx][ny] == True:
                continue
            if grid[nx][ny] == 0:
                continue
            # gird[nx][ny] = 1
            vis[nx][ny] = True
            cnt += self.dfs(nx,ny,vis,grid)
        return cnt
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        ans = 0
        n,m = len(grid),len(grid[0])
        vis = [[False] * m for i in range(n)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and vis[i][j] == False:
                    vis[i][j] = True
                    ans = max(ans,self.dfs(i,j,vis,grid))
        return ans