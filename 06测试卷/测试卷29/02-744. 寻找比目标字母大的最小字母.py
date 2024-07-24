'''
https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/
'''
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = None
        for c in letters:
            if ord(c) > ord(target):
                if ans is None or ord(c) < ord(ans):
                    ans = c
        if ans is None:
            ans = letters[0]
        return ans