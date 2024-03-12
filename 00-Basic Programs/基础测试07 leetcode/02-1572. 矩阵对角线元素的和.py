'''
url: https://leetcode.cn/problems/matrix-diagonal-sum/description/?envType=study-plan-v2&envId=programming-skills
'''
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # n x n
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]
        j = n - 1
        for i in range(n): # i 递增
            sum += mat[i][j]
            j -= 1 # j递减
        if n % 2 == 1:
            sum -= mat[n//2][n//2]
        return sum