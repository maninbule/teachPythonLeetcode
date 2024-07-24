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
        for i in range(n):# ans[i]
            if k > 0:
                pos = i + 1 # start index = i + 1
                sum = 0
                for j in range(k):
                    if pos == n:
                        pos = 0
                    sum += code[pos]
                    pos += 1
                ans[i] = sum
            else: #
                pos = i - 1  # start index = i - 1
                sum = 0
                for j in range(-k):
                    if pos == -1:
                        pos = n-1
                    sum += code[pos]
                    pos -= 1
                ans[i] = sum
        return ans

s = Solution()
s.decrypt([2,4,9,3],-2)
