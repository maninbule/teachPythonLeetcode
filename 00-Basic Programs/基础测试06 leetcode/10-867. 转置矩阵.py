
'''
url: https://leetcode.cn/problems/transpose-matrix/description/
'''
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for j in range(len(matrix[0])): # 遍历第j列
            row = []
            for i in range(len(matrix)): # 遍历第j列的每一行
                row.append(matrix[i][j])
            ans.append(row)
        return ans

