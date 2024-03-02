'''
url:https://leetcode.cn/problems/first-unique-character-in-a-string/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        for i in range(len(s)):
            c = s[i]
            if mp[c] == 1:
                return i
        return -1