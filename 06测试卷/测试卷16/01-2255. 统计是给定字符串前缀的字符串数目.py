
'''
https://leetcode.cn/problems/count-prefixes-of-a-given-string/description/
'''
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        st = set()
        ans = 0
        for i in range(1,len(s) + 1):
            st.add(s[:i])
        for w in words:
            if w in st: # O(1)
                ans += 1
        return ans


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for w in words:
            if len(w) > len(s):
                continue
            eq = True
            for i in range(len(w)):
                if w[i] != s[i]:
                    eq = False
                    break
            if eq:
                ans += 1
        return ans


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for w in words:
            if s.find(w) == 0:
                ans += 1
        return ans