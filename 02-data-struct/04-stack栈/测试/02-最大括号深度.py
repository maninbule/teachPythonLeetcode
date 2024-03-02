
'''
url:https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/description/
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        length = 0
        ans = 0
        for c in s:
            if c == '(':
                length += 1
            elif c == ')':
                length -= 1
            ans = max(ans,length)
        return ans
