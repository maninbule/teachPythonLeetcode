
'''
url: https://leetcode.cn/problems/first-letter-to-appear-twice/description/
'''

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        from collections import defaultdict
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
            if cnt[c] == 2:
                return c
        return ""

'''
abccbaacz
1112
a : 1
b : 2
c : 2

'''