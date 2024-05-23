'''
https://leetcode.cn/problems/is-subsequence/description/
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s):
            if j == len(t):
                return False
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == s[j]:
                i += 1
        return i == len(s)

s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s,t))
