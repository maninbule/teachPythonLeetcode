'''
https://leetcode.cn/problems/rotate-string/
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        s += s
        for i in range(n):#
            if s[i:i + n] == goal:
                return True
        return False
