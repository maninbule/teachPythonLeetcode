'''
https://leetcode.cn/problems/string-compression/description/
'''
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = ""
        cnt = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                cnt += 1
            else:
                ans += chars[i-1]
                if cnt > 1: #a2b2
                    ans += str(cnt)
                cnt = 1
        ans += chars[-1] # a2b2c3
        if cnt > 1:
            ans += str(cnt)
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)