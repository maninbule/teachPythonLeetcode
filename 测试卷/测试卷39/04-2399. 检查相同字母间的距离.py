'''
https://leetcode.cn/problems/check-distances-between-same-letters/description/
'''
from typing import List
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        from collections import defaultdict
        last = defaultdict(int)
        for i in range(1,len(s) + 1):
            c = s[i-1]
            if last[c] != 0 and i - last[c] - 1 != distance[ord(c) - ord('a')]:
                return False
            last[c] = i
        return True

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        last = dict()
        for i in range(len(s)):
            c = s[i]
            if c in last and i - last[c] - 1 != distance[ord(c) - ord('a')]:
                return False
            last[c] = i
        return True