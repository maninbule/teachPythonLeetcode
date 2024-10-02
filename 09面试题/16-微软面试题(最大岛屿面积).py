'''
岗位：前端
微软面试题
'''
from typing import List

'''
https://leetcode.cn/problems/ZL6zAn/description/
'''

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        max_size = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == False:
                    max_size = max(max_size, self.bfs(i, j, grid, visited))
        return max_size

    def bfs(self, x: int, y: int, grid: List[List[int]], visited: List[List[bool]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[x][y] == 0:
            return 0
        q = deque([[x, y]])
        visited[x][y] = True
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        size = 0
        while len(q) > 0:
            x, y = q.popleft()
            size += 1
            for i in range(4):
                nx = x + dir[i][0]
                ny = y + dir[i][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if grid[nx][ny] == 0:
                    continue
                if visited[nx][ny] == True:
                    continue
                visited[nx][ny] = True
                q.append([nx, ny])
        return size
# dfs版本

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        max_size = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == False:
                    visited[i][j] = True
                    max_size = max(max_size, self.dfs(i, j, grid, visited))
        return max_size

    def dfs(self,x: int, y: int, grid: List[List[int]], visited: List[List[bool]])->int:
        n, m = len(grid), len(grid[0])
        size = 1
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if grid[nx][ny] == 0:
                continue
            if visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            size += self.dfs(nx,ny,grid,visited)
        return size