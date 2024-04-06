'''
https://leetcode.cn/problems/maximum-number-of-words-found-in-sentences/description/
'''
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            ans = max(ans,len(s.split()))
        return ans