'''
https://leetcode.cn/problems/check-whether-two-strings-are-almost-equivalent/description/
'''

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import defaultdict
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for c in word1:
            cnt1[c] += 1
        for c in word2:
            cnt2[c] += 1
        for ascii in range(ord('a'),ord('z') + 1):
            c = chr(ascii)
            if abs(cnt1[c] - cnt2[c]) > 3:
                return False
        return True