'''
https://leetcode.cn/problems/find-the-difference/description/
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import defaultdict
        counts = defaultdict(int)
        countt = defaultdict(int)
        for v in s:
            counts[v] += 1
        for v in t:
            countt[v] += 1
        for v in t:
            if countt[v] == counts[v] + 1:
                return v
