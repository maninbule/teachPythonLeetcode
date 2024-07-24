# https://leetcode.cn/problems/modify-the-matrix/description/
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n,m = len(matrix),len(matrix[0])
        for j in range(m):
            mx = -1
            for i in range(n):
                mx = max(matrix[i][j],mx)
            for i in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = mx
        return matrix