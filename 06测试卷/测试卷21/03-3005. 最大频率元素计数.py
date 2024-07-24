'''
https://leetcode.cn/problems/count-elements-with-maximum-frequency/description/
'''
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import defaultdict
        mp = defaultdict(int)
        mx_cnt = 0
        for x in nums:
            mp[x] += 1
            mx_cnt = max(mx_cnt,mp[x])
        # -------------
        st = set(nums)
        count = 0
        for x in st:
            if mp[x] == mx_cnt:
                count += 1
        return count * mx_cnt
