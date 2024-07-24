# https://leetcode.cn/problems/convert-1d-array-into-2d-array/
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[i * n + j]
        return ans