
'''
url: https://leetcode.cn/problems/sum-of-unique-elements/description/
'''
from typing import List
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import defaultdict
        mp = defaultdict(int)
        for v in nums:
            mp[v] += 1
        ans = 0
        for v in nums:
            if mp[v] == 1:
                ans += v
        return ans