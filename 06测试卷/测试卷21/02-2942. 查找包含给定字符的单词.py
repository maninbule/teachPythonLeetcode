'''
https://leetcode.cn/problems/find-words-containing-character/description/
'''
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if words[i].find(x) != -1:
                ans.append(i)
        return ans