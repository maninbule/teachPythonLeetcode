
'''
url: https://leetcode.cn/problems/sum-of-unique-elements/description/
'''
from typing import List
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        for v in nums:
            count[v] += 1
        ans = 0
        for v in nums:
            if count[v] == 1:
               ans += v
        return ans