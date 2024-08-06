'''
https://leetcode.cn/problems/shortest-distance-to-a-character/description/
'''
from typing import List

# O(n^2)
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n
        for i in range(n):
            for j in range(n):
                if s[j] == c:
                    ans[i] = min(ans[i],abs(i - j))
        return ans

# O(n)
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n
        last = -1
        for i in range(n):
            if s[i] == c:
                last = i
            if last != -1:
                ans[i] = min(ans[i], i - last)
        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last = i
            if last != -1:
                ans[i] = min(ans[i], last - i)
        "abc".startswith()
        return ans
