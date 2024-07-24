'''
https://leetcode.cn/problems/most-frequent-even-element/description/
'''
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        mx_cnt = 0
        for x in nums:
            if x % 2 == 0:
                cnt[x] += 1
                mx_cnt = max(cnt[x],mx_cnt)
        ans = -1
        for x in nums:
            if x % 2 == 0 and cnt[x] == mx_cnt:
                if ans == -1:
                    ans = x
                else:
                    ans = min(ans,x)
        return ans
