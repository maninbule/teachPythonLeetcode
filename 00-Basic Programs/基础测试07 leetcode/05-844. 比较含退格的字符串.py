
'''
url: https://leetcode.cn/problems/backspace-string-compare/description/

'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for c in s:
            if c == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        s = "".join(stack)

        stack = []
        for c in t:
            if c == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        t = "".join(stack)
        return s == t


