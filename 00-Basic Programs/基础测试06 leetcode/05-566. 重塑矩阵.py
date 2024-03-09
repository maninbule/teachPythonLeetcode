
'''
url: https://leetcode.cn/problems/reshape-the-matrix/description/
'''
from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        if n * m != r * c:
            return mat
        rows = []
        for i in range(n):
            rows += mat[i]
        index = 0
        ans = [[0] * c for _ in range(r)] # r x c
        for i in range(r):
            for j in range(c):
                ans[i][j] = rows[index]
                index += 1
        return ans
