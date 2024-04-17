'''
https://leetcode.cn/problems/dKk3P7/description/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if s == t:
            return False
        mps = defaultdict(int)
        mpt = defaultdict(int)
        for c in s:
            mps[c] += 1
        for c in t:
            mpt[c] += 1
        for ascii in range(ord('a'),ord('z') + 1):
            c = chr(ascii)
            if mps[c] != mpt[c]:
                return False
        return True


