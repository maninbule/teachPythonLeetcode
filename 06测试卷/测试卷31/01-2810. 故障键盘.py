'''
https://leetcode.cn/problems/faulty-keyboard/description/
'''

from collections import deque
class Solution:
    def finalString(self, s: str) -> str:
        dir = 0
        q = deque()
        for c in s:
            if c != 'i':
                if dir == 0:
                    q.append(c)
                else:
                    q.appendleft(c)
            else:
                dir ^= 1
        ans = ""
        while len(q) > 0:
            ans += q.popleft()
        if dir == 1:
            ans = ans[::-1]
        return ans


