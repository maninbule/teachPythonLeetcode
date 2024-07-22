'''
https://leetcode.cn/problems/number-of-islands/description/
'''
from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if len(grid) == 0:
            return 0
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for i in range(n)]
        dir = [[-1, 0], [+1, 0], [0, 1], [0, -1]]
        def bfs(x:int,y:int)->None:
            q = deque()
            vis[x][y] = True
            q.append((x,y))
            while len(q) > 0:
                now = q.popleft()
                x,y = now[0],now[1]
                for i in range(len(dir)):
                    dx = dir[i][0]
                    dy = dir[i][1]
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if grid[nx][ny] != '1':
                        continue
                    if vis[nx][ny] == True:
                        continue
                    vis[nx][ny] = True
                    q.append((nx,ny))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and vis[i][j] == False:
                    bfs(i,j)
                    ans += 1
        return ans