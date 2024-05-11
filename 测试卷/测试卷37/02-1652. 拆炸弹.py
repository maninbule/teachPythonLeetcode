'''
https://leetcode.cn/problems/defuse-the-bomb/description/
'''
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        for i in range(n):
            if k < 0:
                cur = i - 1
                for j in range(k):
                    if cur == -1:
                        cur = n-1
                    ans[i] += code[cur]
                    cur -= 1
            else:
                cur = i + 1
                for j in range(k):
                    if cur == n:
                        cur = 0
                    ans[i] += code[cur]
                    cur += 1
        return ans



