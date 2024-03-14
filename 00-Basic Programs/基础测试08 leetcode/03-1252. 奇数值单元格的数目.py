'''
url: https://leetcode.cn/problems/cells-with-odd-values-in-a-matrix/description/
'''
from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        G = [[0]*n for _ in range(m)]
        for index in indices:
            r,c = index[0],index[1]
            for j in range(n):
                G[r][j] += 1
            for i in range(m):
                G[i][c] += 1
        ans = 0
        for row in G:
            for x in row:
                if x % 2 == 1:
                    ans += 1
        return ans