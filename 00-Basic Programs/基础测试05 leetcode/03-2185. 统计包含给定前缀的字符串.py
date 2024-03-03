
'''
url: https://leetcode.cn/problems/counting-words-with-a-given-prefix/description/
'''
from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)
        for w in words:
            if len(w) < n:
                continue
            if w[:n] == pref:
                count += 1
        return count
