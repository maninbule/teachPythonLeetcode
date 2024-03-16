
'''
url: https://leetcode.cn/problems/contains-duplicate/description/
'''

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        count = defaultdict(int)
        for v in nums:
            count[v] += 1
        for v in nums:
            if count[v] >= 2:
                return True
        return False