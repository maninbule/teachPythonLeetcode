'''
https://leetcode.cn/problems/longest-harmonious-subsequence/description/
'''
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        for v in nums:
            cnt[v] += 1
        ans = 0
        keys = list(cnt.keys())
        for key in keys:
            if cnt[key + 1] > 0:
                ans = max(ans, cnt[key] + cnt[key + 1])
        return ans