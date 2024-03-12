
'''
url: https://leetcode.cn/problems/robot-return-to-origin/description/
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import defaultdict
        cnt = defaultdict(int)
        for c in moves:
            cnt[c] += 1
        return cnt['U'] == cnt['D'] and cnt['L'] == cnt['R']