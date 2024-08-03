'''
https://leetcode.cn/problems/maximum-number-of-balloons/description/
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import defaultdict
        table = defaultdict(int)
        balloon = defaultdict(int)
        for c in "balloon":
            balloon[c] += 1
        for c in text:
            table[c] += 1
        ans = len(text)
        for c,count in balloon.items(): # a b l o n
            cur = table[c] // count
            ans = min(ans,cur)
        return ans

