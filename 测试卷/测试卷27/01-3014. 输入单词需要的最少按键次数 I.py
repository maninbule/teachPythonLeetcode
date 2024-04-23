'''
https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-i/description/
'''

class Solution:
    def minimumPushes(self, word: str) -> int:
        # 8次1 8次2，8次3，2个4
        from collections import defaultdict
        mp = defaultdict(int)
        for c in word:
            mp[c] += 1
        times = []
        for key,value in mp.items():
            times.append(value)
        times.sort(key=lambda x:-x)
        push_times = [1]*8 + [2] * 8 + [3]*8 + [4] * 2
        ans = 0
        for i in range(len(times)):
            ans += times[i] * push_times[i]
        return ans