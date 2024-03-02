
'''
url: https://leetcode.cn/problems/valid-parentheses/description/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                left = stack[-1]
                if left != '(' and  c == ')':
                    return False
                if left != '[' and  c == ']':
                    return False
                if left != '{' and  c == '}':
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True