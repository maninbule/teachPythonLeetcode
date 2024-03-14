'''
url: https://leetcode.cn/problems/find-words-that-can-be-formed-by-characters/description/
'''
from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import defaultdict
        have = defaultdict(int)
        for c in chars:
            have[c] += 1
        ans = 0
        for w in words:
            can = True
            cnt = defaultdict(int)
            for c in w:
                cnt[c] += 1
            for c,need in cnt.items():
                if need > have[c]:
                    can = False
                    break
            if can:
                ans += len(w)
        return ans


