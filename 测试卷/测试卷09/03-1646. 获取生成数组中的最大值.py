'''
https://leetcode.cn/problems/get-maximum-in-generated-array/description/
'''

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        ans = [0] * (n + 1)
        ans[0] = 0
        ans[1] = 1
        max_value = 1
        for i in range(1,n+1):
            if 2 <= 2*i <= n:
                ans[2*i] = ans[i]
            if 2 <= 2*i + 1 <= n:
                ans[2 * i + 1] = ans[i] + ans[i+1]
            max_value = max(max_value,ans[i])
        return max_value
