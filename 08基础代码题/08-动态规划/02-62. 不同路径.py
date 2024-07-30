'''
https://leetcode.cn/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        # 计算第一行的方案数
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]
        # 计算第一列的方案数
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
