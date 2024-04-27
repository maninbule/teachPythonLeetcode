'''
https://leetcode.cn/problems/count-binary-substrings/description/
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1,len(s),2): # [i,i + 1],[i,i + 3]
                t = s[i:j + 1]
                if t.count('0') != t.count('1'):
                    continue
                # 01 len = 2 [0:1] ->"0"
                if len(set(t[:len(t)//2])) != 1:
                    continue
                # [1:] ->"1"
                if len(set(t[len(t)//2:])) != 1:
                    continue
                ans += 1
        return ans




