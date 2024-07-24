'''
https://leetcode.cn/problems/number-of-changing-keys/description/
'''

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        last = s[0]
        ans = 0
        for i in range(1,len(s)):
            c = s[i]
            if last != c:
               ans += 1
            last = c
        return ans

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        ans = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                ans += 1
        return ans